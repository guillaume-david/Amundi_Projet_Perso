import asyncio #Importe le module asyncio, utilisé pour exécuter du code asynchrone (fonctions async / await).
from typing import Optional
from contextlib import AsyncExitStack

from mcp import ClientSession, StdioServerParameters # Importe les classes nécessaires à la gestion de sessions client MCP.
from mcp.client.stdio import stdio_client # Importe la fonction pour établir une connexion via les flux standard (stdin/stdout).

from anthropic import Anthropic # Importe la classe principale pour interagir avec l’API Claude (Anthropic).
from dotenv import load_dotenv # Importe la fonction permettant de charger les variables d’environnement depuis un fichier .env.

load_dotenv()  # load environment variables from .env

class MCPClient:
    def __init__(self):
        # Initialize session and client objects
        self.session: Optional[ClientSession] = None
        self.exit_stack = AsyncExitStack()

        # Vérifie la présence d'une clé Anthropic
        import os
        api_key = os.getenv("ANTHROPIC_API_KEY")
        if not api_key:
            print("⚠️  No ANTHROPIC_API_KEY found — running in offline mode (MCP only).")
            self.anthropic = None
        else:
            try:
                self.anthropic = Anthropic(api_key=api_key)
                print("✅ Anthropic client initialized.")
            except Exception as e:
                print(f"⚠️  Failed to initialize Anthropic client: {e}")
                self.anthropic = None


    async def connect_to_server(self, server_script_path: str): #Méthode asynchrone pour lancer et établir la connexion avec un serveur MCP local (Python ou Node.js).
        """Connect to an MCP server
        
        Args:
            server_script_path: Path to the server script (.py or .js)
        """
        is_python = server_script_path.endswith('.py')
        is_js = server_script_path.endswith('.js')
        if not (is_python or is_js):
            raise ValueError("Server script must be a .py or .js file")
            
        command = "python" if is_python else "node"
        server_params = StdioServerParameters(
            command=command, # Commande à exécuter (python ou node)
            args=[server_script_path], # Fichier du serveur MCP à lancer
            env=None # Pas de variables d’environnement spécifiques
        )
        
        stdio_transport = await self.exit_stack.enter_async_context(stdio_client(server_params)) #Établit une connexion asynchrone avec le serveur via les flux standard
        self.stdio, self.write = stdio_transport ## Stocke les objets de lecture et d’écriture du flux MCP.
        self.session = await self.exit_stack.enter_async_context(ClientSession(self.stdio, self.write)) #Crée la session client MCP, qui gérera les requêtes, les réponses et les appels d’outils.
        
        await self.session.initialize() ## Initialise la session (handshake MCP, découverte des outils disponibles, etc.).
        
        # List available tools
        response = await self.session.list_tools()
        tools = response.tools
        print("\nConnected to server with tools:", [tool.name for tool in tools])

    async def process_query(self, query: str) -> str: #Fonction qui envoie une question à Claude, lui fournit les outils MCP disponibles et traite ses réponses (texte et appels d’outils).
        """Process a query using Claude and available tools"""
        messages = [
            {
                "role": "user",
                "content": query
            }
        ]
        
        if not self.anthropic:
            # Mode sans Claude : exécute simplement la commande comme un outil MCP
            if query.startswith("tool "):
                parts = query.split(" ", 2)
                tool_name = parts[1]
                tool_args = {}
                if len(parts) == 3:
                    import json
                    try:
                        tool_args = json.loads(parts[2])
                    except json.JSONDecodeError:
                        return "❌ Invalid JSON arguments."

                result = await self.session.call_tool(tool_name, tool_args)
                return f"🛠️  Tool '{tool_name}' executed:\n{result.content}"

            return "🤖 Anthropic (Claude) is not configured. Use 'tool <name> {json_args}' to call MCP tools directly."
    
        response = await self.session.list_tools()
        available_tools = [{ 
            "name": tool.name,
            "description": tool.description,
            "input_schema": tool.inputSchema
        } for tool in response.tools]

        # Initial Claude API call
        response = self.anthropic.messages.create(
            model="claude-sonnet-4-5",
            max_tokens=1000,
            messages=messages,
            tools=available_tools
        )

        # Process response and handle tool calls
        final_text = [] ## Liste des morceaux de texte qui formeront la réponse finale.

        for content in response.content: #Parcourt les différents éléments de la réponse (Claude peut renvoyer plusieurs objets : texte, appels d’outils, etc.).
            if content.type == 'text':
                final_text.append(content.text)
            elif content.type == 'tool_use':
                tool_name = content.name ## Nom de l’outil que Claude veut utiliser.
                tool_args = content.input ## Arguments à passer à cet outil.
                
                # Execute tool call
                result = await self.session.call_tool(tool_name, tool_args)  ## Appelle l’outil côté serveur MCP et récupère son résultat.
                final_text.append(f"[Calling tool {tool_name} with args {tool_args}]") ## Ajoute une trace lisible dans la réponse.

                # Continue conversation with tool results / Si Claude avait ajouté du texte explicatif en plus de la requête d’outil, on le garde dans la conversation.
                if hasattr(content, 'text') and content.text:
                    messages.append({
                      "role": "assistant",
                      "content": content.text
                    })
                messages.append({
                    "role": "user", 
                    "content": result.content
                })

                # Get next response from Claude / Relance un nouvel appel à Claude pour qu’il poursuive la discussion avec le résultat de l’outil.
                response = self.anthropic.messages.create(
                    model="claude-sonnet-4-5",
                    max_tokens=1000,
                    messages=messages,
                )

                final_text.append(response.content[0].text) 

        return "\n".join(final_text) ## Renvoie la réponse complète sous forme de texte continu.





    async def chat_loop(self): #Fonction asynchrone qui crée une boucle interactive dans le terminal pour dialoguer avec Claude et les outils MCP.
        """Run an interactive chat loop"""
        print("\nMCP Client Started!")
        print("Type your queries or 'quit' to exit.")
        
        while True:
            try:
                query = input("\nQuery: ").strip() ## Attend la saisie d’une requête utilisateur.
                
                if query.lower() == 'quit':
                    break
                    
                response = await self.process_query(query) ## Envoie la requête à la méthode process_query().
                print("\n" + response) ## Affiche la réponse de Claude.
                    
            except Exception as e:
                print(f"\nError: {str(e)}")
    
    async def cleanup(self):
        """Clean up resources"""
        await self.exit_stack.aclose() ## Ferme proprement toutes les ressources ouvertes (connexion, session, etc.).

async def main():
    if len(sys.argv) < 2: #Vérifie qu’un argument (chemin vers le serveur MCP) a été passé au script.
        print("Usage: python client.py <path_to_server_script>") 
        sys.exit(1)
        
    client = MCPClient()
    try:
        await client.connect_to_server(sys.argv[1])
        await client.chat_loop()
    finally:
        await client.cleanup()

if __name__ == "__main__":
    import sys
    asyncio.run(main())