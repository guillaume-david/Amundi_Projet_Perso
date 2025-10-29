# Amundi_Projet_Perso
Travail personnel sur le projet industriel

# Premières commandes:
uv init
uv venv
source .venv/bin/activate
uv add fastapi
uv add requests
uv add uvicorn
uv add "mcp[cli]" 
uv add httpx
uv add anthropic


# https://portal.aixigo.com/docs/analytics-api#sampledata
L’Analytics API est une API REST conçue pour l’analyse rapide et fiable de produits financiers et de portefeuilles, en utilisant des données de marché actuelles et historiques.
Elle permet aussi d’intégrer des valeurs de comparaison (benchmarks, indices) et sert principalement aux présentations d’évaluations et aux rapports internes ou externes des institutions financières.

Les calculs peuvent porter sur un ou plusieurs portefeuilles, y compris ceux contenant des ordres ouverts (ordres non encore exécutés).
Il est également possible d’analyser des portefeuilles virtuels, constitués de combinaisons ad hoc de produits.

L’API offre une grande flexibilité d’analyse, grâce à :
la sélection libre de la période d’étude,
le choix de la méthode de calcul,
la prise en compte de devises, taxes, frais, ou crédits selon le besoin,
et diverses options d’agrégation (par portefeuille, instrument, classe d’actifs, région, pays, ou secteur).

Elle propose deux modes de calcul :
Synchronous resources → résultats immédiats via HTTP (pour petits volumes).
Asynchronous resources → résultats progressifs via Kafka (pour gros volumes, dans la section “report”).

# Récupérer un token...
https://portal.aixigo.com/docs/perform-authenticated-bloxx-requests
    Formulate a POST request to the OpenID Connect server of a BLOXX instance.
    Include user credentials (name and password), client ID, and client password.
    Once authenticated, use the obtained access token for REST requests.
Bon a priori on ne peut pas faire des requêtes sans récupérer des authentifiants disponibles ici
script get_token.py prêt mais il me manque mes identifiants sandbox (client ID et client Secret...)

# Du coup on va récupérer la forme des données envoyées quand ça marche (toutes accessibles ici):
https://portal.aixigo.com/docs/analytics-api#
    et ensuite, on crée un serveur simulé (mock)
        il simule les vraies API Aixigo (ex : /portfolio/contracts, /portfolio/transactions, etc.)
        pour chaque endpoint, on les met en forme selon les exemples du site
        python -m uvicorn usecase1_mockserver:app --reload --port 8000
    ainsi qu'un client correspondant (REST sans MCP)
        uv run client.py

# Amélioration avec serveur MCP:
    rajout de usecase1_mcpserver.py (il expose des outils MCP (list_contracts, get_transactions, etc.) qui, eux, appellent les endpoints REST du mock.)
    rajout de mcp_client.py (attention la clé Anthopic dans .env n'est pas valide donc ne fonctionne pas)


# Séquence pour que ça fonctionne:
uvicorn usecase1_mockserver:app --port 8000
uv run usecase1_mcpserver.py
uv run mcp_client.py usecase1_mcpserver.py
    