import requests

# === Configuration ===
BASE_URL = "https://demo.portal.aixigo.cloud"

# Deux tokens différents selon le type d’API
TOKEN_ASSET = "eyJhbGciOiJSUzI1NiIsInR5cCIgOiAiSldUIiwia2lkIiA6ICI4ZksxTW95NkVidjktcjNEQ3IwMXJtemVsY3FkMUpUbVJDaGh6YkxRblpnIn0.eyJleHAiOjE3NjE5MTEzOTcsImlhdCI6MTc2MTkwNzc5NywiYXV0aF90aW1lIjoxNzYxOTA3Nzk2LCJqdGkiOiIxYzM4ZWM4My0xMDc2LTRiM2UtOGNkZi04OTg2NDNjNTQ4ZDgiLCJpc3MiOiJodHRwczovL2xvZ2luLnBvcnRhbC5haXhpZ28uY2xvdWQvcmVhbG1zL2FwcHMiLCJhdWQiOlsid2Vic2l0ZSIsImRlbW8iXSwic3ViIjoiZ3VpbGxhdW1lLmRhdmlkQHN0dWRlbnQtY3MuZnIiLCJ0eXAiOiJJRCIsImF6cCI6IndlYnNpdGUiLCJzaWQiOiIzMDYwZWZjOC0yYjcxLTQ2OGYtODBhMS04MjczMTEzZjZjZDciLCJhdF9oYXNoIjoic19GNWdjc28yRm44WjNSbV93UzNCUSIsImFjciI6IjEiLCJlbWFpbF92ZXJpZmllZCI6dHJ1ZSwicm9sZXMiOlsiR1VFU1QiXSwibmFtZSI6IkRhdmlkIEd1aWxsYXVtZSIsInByZWZlcnJlZF91c2VybmFtZSI6Imd1aWxsYXVtZS5kYXZpZEBzdHVkZW50LWNzLmZyIiwiZ2l2ZW5fbmFtZSI6IkRhdmlkIiwiZmFtaWx5X25hbWUiOiJHdWlsbGF1bWUiLCJ0ZW5hbnQiOiJndWVzdCIsImVtYWlsIjoiZ3VpbGxhdW1lLmRhdmlkQHN0dWRlbnQtY3MuZnIifQ.aD005OlPBKwkmPYfwchOUB-cFADLuGT1R8wna20EteKUDSv3EfpOu3R9piTqvmmQGZRJLNhtxRe2X1X7jJV39-Kwc3tix5cKjiIpV8F5CXZxEOAYP_IysSHHJJBfLSnj7h759qORtvlKn8nu44vQpEEhMTGvBcgafdn-QtkWHKov8wGSOrQRrycdf6JAi8oMINeIz-U2tklQXKqUliFa3NueO28KX9vjTFLDMmHbU3eN5jIXVxbKfve25He6KbqIq8o183EZ8h4sNHOukFx4HvxySgwiQ58KPoY3UUO-PUgBrcIzQt0bigzp16ioIyMjg2pT_pi5fKWCb4VAt9LNmw"
TOKEN_PORTFOLIO = "eyJhbGciOiJSUzI1NiIsInR5cCIgOiAiSldUIiwia2lkIiA6ICI4ZksxTW95NkVidjktcjNEQ3IwMXJtemVsY3FkMUpUbVJDaGh6YkxRblpnIn0.eyJleHAiOjE3NjE5MTEzOTcsImlhdCI6MTc2MTkwNzc5NywiYXV0aF90aW1lIjoxNzYxOTA3Nzk2LCJqdGkiOiIxYzM4ZWM4My0xMDc2LTRiM2UtOGNkZi04OTg2NDNjNTQ4ZDgiLCJpc3MiOiJodHRwczovL2xvZ2luLnBvcnRhbC5haXhpZ28uY2xvdWQvcmVhbG1zL2FwcHMiLCJhdWQiOlsid2Vic2l0ZSIsImRlbW8iXSwic3ViIjoiZ3VpbGxhdW1lLmRhdmlkQHN0dWRlbnQtY3MuZnIiLCJ0eXAiOiJJRCIsImF6cCI6IndlYnNpdGUiLCJzaWQiOiIzMDYwZWZjOC0yYjcxLTQ2OGYtODBhMS04MjczMTEzZjZjZDciLCJhdF9oYXNoIjoic19GNWdjc28yRm44WjNSbV93UzNCUSIsImFjciI6IjEiLCJlbWFpbF92ZXJpZmllZCI6dHJ1ZSwicm9sZXMiOlsiR1VFU1QiXSwibmFtZSI6IkRhdmlkIEd1aWxsYXVtZSIsInByZWZlcnJlZF91c2VybmFtZSI6Imd1aWxsYXVtZS5kYXZpZEBzdHVkZW50LWNzLmZyIiwiZ2l2ZW5fbmFtZSI6IkRhdmlkIiwiZmFtaWx5X25hbWUiOiJHdWlsbGF1bWUiLCJ0ZW5hbnQiOiJndWVzdCIsImVtYWlsIjoiZ3VpbGxhdW1lLmRhdmlkQHN0dWRlbnQtY3MuZnIifQ.aD005OlPBKwkmPYfwchOUB-cFADLuGT1R8wna20EteKUDSv3EfpOu3R9piTqvmmQGZRJLNhtxRe2X1X7jJV39-Kwc3tix5cKjiIpV8F5CXZxEOAYP_IysSHHJJBfLSnj7h759qORtvlKn8nu44vQpEEhMTGvBcgafdn-QtkWHKov8wGSOrQRrycdf6JAi8oMINeIz-U2tklQXKqUliFa3NueO28KX9vjTFLDMmHbU3eN5jIXVxbKfve25He6KbqIq8o183EZ8h4sNHOukFx4HvxySgwiQ58KPoY3UUO-PUgBrcIzQt0bigzp16ioIyMjg2pT_pi5fKWCb4VAt9LNmw"

def get_headers(token: str, hal: bool = False): #on met en hal ou en json en fonction (les endpoints "catalogues" sont en hal)
    """Construit les en-têtes standard pour une requête Aixigo."""
    return {
        "accept": "application/hal+json" if hal else "application/json",
        "Authorization": f"Bearer {token}"
    }

def safe_print_json(resp):
    """Affiche proprement le JSON ou le texte brut."""
    print(f"Status: {resp.status_code}")
    try:
        print(resp.json())
    except Exception:
        print(resp.text)
    print("-" * 80)


# === 1️⃣ Test de l’endpoint /asset ===
print("➡️ Test : /asset")
asset_url = f"{BASE_URL}/analytics/asset"
r_asset = requests.get(asset_url, headers=get_headers(TOKEN_ASSET, hal=True))
safe_print_json(r_asset)


# === 2️⃣ Test de l’endpoint /portfolio ===
print("➡️ Test : /portfolio")
portfolio_url = f"{BASE_URL}/analytics/portfolio"
r_portfolio = requests.get(portfolio_url, headers=get_headers(TOKEN_PORTFOLIO, hal=True))
safe_print_json(r_portfolio)


# === 3️⃣ Test : /portfolio-kpi/performance ===
print("➡️ Test : /portfolio-kpi/performance")
performance_url = f"{BASE_URL}/analytics/portfolio-kpi/performance"
params = [
    ("begin", "2024-01-01"),
    ("end", "2025-01-01"),
    ("restriction", "NONE"),
    ("aggregation", "ALL"),                     # obligatoire
    ("contractSet", "NONE"),                    # obligatoire si "contract" utilisé
    ("contract", "SamplePortfolio0001"),        # tableau (explode)
    ("algorithm", "MODIFIED_DIETZ"),            # tableau (explode)
    ("currencySelection", "CONTRACT"),          # recommandé
    ("paymentCalculation", "ALL_PAYMENTS")      # souvent requis
]
r_perf = requests.get(performance_url, headers=get_headers(TOKEN_PORTFOLIO), params=params)
safe_print_json(r_perf)
