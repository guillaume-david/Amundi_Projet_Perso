import requests

# ============================================================
# CONFIGURATION GLOBALE
# ============================================================

# Deux tokens différents selon les routes
TOKEN_ASSET = "eyJhbGciOiJSUzI1NiIsInR5cCIgOiAiSldUIiwia2lkIiA6ICI4ZksxTW95NkVidjktcjNEQ3IwMXJtemVsY3FkMUpUbVJDaGh6YkxRblpnIn0.eyJleHAiOjE3NjI0Mzk4NzMsImlhdCI6MTc2MjQzNjI3MywiYXV0aF90aW1lIjoxNzYyNDMyNzMwLCJqdGkiOiJhYTlmMTY1My05YWE4LTQ2ZWUtOTkxYS0wZTgzY2VjY2Y2OWYiLCJpc3MiOiJodHRwczovL2xvZ2luLnBvcnRhbC5haXhpZ28uY2xvdWQvcmVhbG1zL2FwcHMiLCJhdWQiOlsid2Vic2l0ZSIsImRlbW8iXSwic3ViIjoiZ3VpbGxhdW1lLmRhdmlkQHN0dWRlbnQtY3MuZnIiLCJ0eXAiOiJJRCIsImF6cCI6IndlYnNpdGUiLCJzaWQiOiI4ZjU3OWI3Yi03OTRiLTRhMzAtYmNmMS02YzRhM2RmNWUxMjAiLCJhdF9oYXNoIjoiTWViRkxpVDAzU0EwVnBUU0R3UlA0USIsImFjciI6IjAiLCJlbWFpbF92ZXJpZmllZCI6dHJ1ZSwicm9sZXMiOlsiR1VFU1QiXSwibmFtZSI6IkRhdmlkIEd1aWxsYXVtZSIsInByZWZlcnJlZF91c2VybmFtZSI6Imd1aWxsYXVtZS5kYXZpZEBzdHVkZW50LWNzLmZyIiwiZ2l2ZW5fbmFtZSI6IkRhdmlkIiwiZmFtaWx5X25hbWUiOiJHdWlsbGF1bWUiLCJ0ZW5hbnQiOiJndWVzdCIsImVtYWlsIjoiZ3VpbGxhdW1lLmRhdmlkQHN0dWRlbnQtY3MuZnIifQ.SVaiurzUz8iqRm-vNCbiKMN1tOLVWRkbUj7wMXYMWIMiSQ-NBFBRZyMMPN6kl9xTSqYcqxKlWXz7qHF7N9bC9kbhpUanm5Xv5HV8ZAlVBZhnPW9p6JvUWTkFF6GRh9p1RbLGrYxJ9UN9sXfRvhAjbLnXtoDC_YMNTWMgehhLJASY9cBKqxKv-wU9a_CEI6B1fvtB6U7E5SvhGcSJSmhcPCSKWofKqHWCH3XrvccybkGv85jcVg_hvE61A5pf2zRljEV6L-gR4Q2jg5aX6Ljv6ssJn890cV4ScQIilYF1d99NPxVFSsjWHkyIBK2LMbd4upyHB1FJa4KChuHBdjyITw" 
TOKEN_PORTFOLIO = "eyJhbGciOiJSUzI1NiIsInR5cCIgOiAiSldUIiwia2lkIiA6ICI4ZksxTW95NkVidjktcjNEQ3IwMXJtemVsY3FkMUpUbVJDaGh6YkxRblpnIn0.eyJleHAiOjE3NjI0NDM0MTQsImlhdCI6MTc2MjQzOTgxNCwiYXV0aF90aW1lIjoxNzYyNDMyNzMwLCJqdGkiOiIyMWM4MzBlMC0yOTk2LTQwNjEtYmI4OS1kMDY2ODc5ODQzZWYiLCJpc3MiOiJodHRwczovL2xvZ2luLnBvcnRhbC5haXhpZ28uY2xvdWQvcmVhbG1zL2FwcHMiLCJhdWQiOlsid2Vic2l0ZSIsImRlbW8iXSwic3ViIjoiZ3VpbGxhdW1lLmRhdmlkQHN0dWRlbnQtY3MuZnIiLCJ0eXAiOiJJRCIsImF6cCI6IndlYnNpdGUiLCJzaWQiOiI4ZjU3OWI3Yi03OTRiLTRhMzAtYmNmMS02YzRhM2RmNWUxMjAiLCJhdF9oYXNoIjoicDkxVDlQT0lfanJVTV9uR01ScHp0QSIsImFjciI6IjAiLCJlbWFpbF92ZXJpZmllZCI6dHJ1ZSwicm9sZXMiOlsiR1VFU1QiXSwibmFtZSI6IkRhdmlkIEd1aWxsYXVtZSIsInByZWZlcnJlZF91c2VybmFtZSI6Imd1aWxsYXVtZS5kYXZpZEBzdHVkZW50LWNzLmZyIiwiZ2l2ZW5fbmFtZSI6IkRhdmlkIiwiZmFtaWx5X25hbWUiOiJHdWlsbGF1bWUiLCJ0ZW5hbnQiOiJndWVzdCIsImVtYWlsIjoiZ3VpbGxhdW1lLmRhdmlkQHN0dWRlbnQtY3MuZnIifQ.kDHU7WKBEeNSszHlCjzdjUMFhI0i0r7FvKzz0EYzIGrT8WBqdLswtq3qOu4gYRHpwkjkFuaU4i9sTaVvPzzIxJpcxlNsKHG_Wj7n7gm1fnQZfP6JKXOH6R8O1QaNHWa3_EaX7ohTjeBgwwu1vtm088T0xXRdcQQ9ZWAjgJfUXX-zPN9yVwsf4kIYjUsmifN5WUDVC_Tj7MaZKWZqkmQlqau-MZdUDJ_QrcIoHgDv95JxhvEqXcncEYUJO37tAFiyr1vUDUZt8JuTdOoSKM3ayRJ4HP6I1Rf3TUw55-MUVWrkxS8HNYwwU-18K8Xsqk-cZG2pKG1oIhw1x1ELY88QTQ"

BASE_URL = "https://demo.portal.aixigo.cloud/analytics"


def get_headers(token: str, hal: bool = False):
    """
    Construit les en-têtes standard pour une requête Aixigo.
    Les endpoints 'catalogues' nécessitent souvent 'application/hal+json'.
    """
    return {
        "accept": "application/hal+json" if hal else "application/json",
        "Authorization": f"Bearer {token}"
    }

def safe_print_json(resp: requests.Response):
    """
    Affiche proprement le JSON ou le texte brut de la réponse.
    """
    print(f"Status: {resp.status_code}")
    try:
        print(resp.json())
    except Exception:
        print(resp.text)
    print("-" * 80)


# ============================================================
# TESTS DES ENDPOINTS ASSET
# ============================================================

def test_asset_endpoints():
    """Teste les endpoints de la section /asset de l'API Aixigo."""
    print("********************* TEST DES ENDPOINTS /ASSET ***************************************")

    # /asset
    print("➡️  /asset")
    url = f"{BASE_URL}/asset"
    resp = requests.get(url, headers=get_headers(TOKEN_ASSET, hal=True))
    safe_print_json(resp)

    # /asset/assets
    print("➡️  /asset/assets")
    url = f"{BASE_URL}/asset/assets"
    params = {
        "asset": "850403",
        "when": "2024-01-01"
    }
    resp = requests.get(url, headers=get_headers(TOKEN_ASSET), params=params)
    safe_print_json(resp)

    # /asset/quotes
    print("➡️  /asset/quotes")
    url = f"{BASE_URL}/asset/quotes"
    params = {
        "asset": "850403",
        "when": "2024-01-01"
    }
    resp = requests.get(url, headers=get_headers(TOKEN_ASSET), params=params)
    safe_print_json(resp)

    # /asset/exchange-rates
    print("➡️  /asset/exchange-rates")
    url = f"{BASE_URL}/asset/exchange-rates"
    params = {
        "sourceCurrency": "EUR",
        "targetCurrency": "CHF",
        "when": "2024-01-01"
    }
    resp = requests.get(url, headers=get_headers(TOKEN_ASSET), params=params)
    safe_print_json(resp)

    # /asset/benchmark-performance
    print("➡️  /asset/benchmark-performance")
    url = f"{BASE_URL}/asset/benchmark-performance"
    params = {
        "begin": "2024-01-01",
        "end": "2025-01-01",
        "benchmark": "benchmark_INDEX_SP500"
    }
    resp = requests.get(url, headers=get_headers(TOKEN_ASSET), params=params)
    safe_print_json(resp)

    # /asset/benchmarks
    print("➡️  /asset/benchmarks")
    url = f"{BASE_URL}/asset/benchmarks"
    resp = requests.get(url, headers=get_headers(TOKEN_ASSET))
    safe_print_json(resp)

    # /asset/benchmark-quote-series
    print("➡️  /asset/benchmark-quote-series")
    url = f"{BASE_URL}/asset/benchmark-quote-series"
    params = {
        "begin": "2024-01-01",
        "end": "2025-01-01",
        "benchmark": "benchmark_INDEX_SP500"
    }
    resp = requests.get(url, headers=get_headers(TOKEN_ASSET), params=params)
    safe_print_json(resp)

    # /asset/benchmark-risk-characteristics
    print("➡️  /asset/benchmark-risk-characteristics")
    url = f"{BASE_URL}/asset/benchmark-risk-characteristics"
    params = {
        "begin": "2024-01-01",
        "end": "2025-01-01",
        "benchmark": "benchmark_INDEX_SP500"
    }
    resp = requests.get(url, headers=get_headers(TOKEN_ASSET), params=params)
    safe_print_json(resp)

    print("✅ Tests des endpoints /asset terminés.\n")


def test_portfolio_endpoints():
    """Teste les endpoints de la section /portfolio de l'API Aixigo."""
    print("********************* TEST DES ENDPOINTS /PORTFOLIO ***************************************")

    # /portfolio
    print("➡️  /portfolio")
    url = f"{BASE_URL}/portfolio"
    resp = requests.get(url, headers=get_headers(TOKEN_PORTFOLIO, hal=True))
    safe_print_json(resp)

    # /portfolio/pending-orders
    print("➡️  /portfolio/pending-orders")
    url = f"{BASE_URL}/portfolio/pending-orders"
    params = {
        "when": "2025-01-01",
        "contract": "SamplePortfolio0001"
    }
    resp = requests.get(url, headers=get_headers(TOKEN_PORTFOLIO), params=params)
    safe_print_json(resp)

    # /portfolio/assets-period
    print("➡️  /portfolio/assets-period")
    url = f"{BASE_URL}/portfolio/assets-period"
    params = {
        "begin": "2024-01-01",
        "end": "2025-01-01",
        "contract": "SamplePortfolio0001"
    }
    resp = requests.get(url, headers=get_headers(TOKEN_PORTFOLIO), params=params)
    safe_print_json(resp)

    # /portfolio/assets-snapshot
    print("➡️  /portfolio/assets-snapshot")
    url = f"{BASE_URL}/portfolio/assets-snapshot"
    params = {
        "when": "2025-01-01",
        "contract": "SamplePortfolio0001"
    }
    resp = requests.get(url, headers=get_headers(TOKEN_PORTFOLIO), params=params)
    safe_print_json(resp)

    # /portfolio/cash-flows
    print("➡️  /portfolio/cash-flows")
    url = f"{BASE_URL}/portfolio/cash-flows"
    params = {
        "begin": "2024-01-01",
        "end": "2025-01-01",
        "contract": "SamplePortfolio0001"
    }
    resp = requests.get(url, headers=get_headers(TOKEN_PORTFOLIO), params=params)
    safe_print_json(resp)

    # /portfolio/contracts-of-person/{personId}
    print("➡️  /portfolio/contracts-of-person/{personId}")
    for i in range(1, 11):  # customer001 → customer010
        person_id = f"customer_{i:03}"
        url = f"{BASE_URL}/portfolio/contracts-of-person/{person_id}"
        print(f"➡️  Test : {url}")
        resp = requests.get(url, headers=get_headers(TOKEN_PORTFOLIO))
        safe_print_json(resp)


    # /portfolio/initial-values
    print("➡️  /portfolio/initial-values")
    url = f"{BASE_URL}/portfolio/initial-values"
    params = {
        "when": "2025-01-01",
        "contract": "SamplePortfolio0001"
    }
    resp = requests.get(url, headers=get_headers(TOKEN_PORTFOLIO), params=params)
    safe_print_json(resp)

    # /portfolio/interest-data
    print("➡️  /portfolio/interest-data")
    url = f"{BASE_URL}/portfolio/interest-data"
    params = {
        "aggregation": "ALL",
        "contract": "SamplePortfolio0001"
    }
    resp = requests.get(url, headers=get_headers(TOKEN_PORTFOLIO), params=params)
    safe_print_json(resp)

    # /portfolio/partial-holdings
    print("➡️  /portfolio/partial-holdings")
    url = f"{BASE_URL}/portfolio/partial-holdings"
    params = {
        "begin": "2024-01-01",
        "end": "2025-01-01",
        "contract": "SamplePortfolio0001"
    }
    resp = requests.get(url, headers=get_headers(TOKEN_PORTFOLIO), params=params)
    safe_print_json(resp)

    # /portfolio/persons-of-contract/{contractId}
    print("➡️  /portfolio/persons-of-contract/{contractId}")
    contract_id = "SamplePortfolio0001"
    url = f"{BASE_URL}/portfolio/persons-of-contract/{contract_id}"
    resp = requests.get(url, headers=get_headers(TOKEN_PORTFOLIO))
    safe_print_json(resp)

    # /portfolio/contracts
    print("➡️  /portfolio/contracts")
    url = f"{BASE_URL}/portfolio/contracts"
    params = {
        "begin": "2024-01-01",
        "end": "2025-01-01",
        "contract": "SamplePortfolio0001"
    }
    resp = requests.get(url, headers=get_headers(TOKEN_PORTFOLIO), params=params)
    safe_print_json(resp)

    # /portfolio/positions-period
    print("➡️  /portfolio/positions-period")
    url = f"{BASE_URL}/portfolio/positions-period"
    params = {
        "begin": "2024-01-01",
        "end": "2025-01-01",
        "contract": "SamplePortfolio0001"
    }
    resp = requests.get(url, headers=get_headers(TOKEN_PORTFOLIO), params=params)
    safe_print_json(resp)

    # /portfolio/positions-snapshot
    print("➡️  /portfolio/positions-snapshot")
    url = f"{BASE_URL}/portfolio/positions-snapshot"
    params = {
        "when": "2025-01-01",
        "contract": "SamplePortfolio0001"
    }
    resp = requests.get(url, headers=get_headers(TOKEN_PORTFOLIO), params=params)
    safe_print_json(resp)

    # /portfolio/transactions
    print("➡️  /portfolio/transactions")
    url = f"{BASE_URL}/portfolio/transactions"
    params = {
        "begin": "2024-01-01",
        "end": "2025-01-01",
        "contract": "SamplePortfolio0001"
    }
    resp = requests.get(url, headers=get_headers(TOKEN_PORTFOLIO), params=params)
    safe_print_json(resp)

    # /portfolio/transaction-statistics
    print("➡️  /portfolio/transaction-statistics")
    url = f"{BASE_URL}/portfolio/transaction-statistics"
    params = {
        "begin": "2024-01-01",
        "end": "2025-01-01",
        "contract": "SamplePortfolio0001"
    }
    resp = requests.get(url, headers=get_headers(TOKEN_PORTFOLIO), params=params)
    safe_print_json(resp)

    # /portfolio/transaction-series
    print("➡️  /portfolio/transaction-series")
    url = f"{BASE_URL}/portfolio/transaction-series"
    params = {
        "begin": "2024-01-01",
        "end": "2025-01-01",
        "contract": "SamplePortfolio0001"
    }
    resp = requests.get(url, headers=get_headers(TOKEN_PORTFOLIO), params=params)
    safe_print_json(resp)

    # /portfolio/values
    print("➡️  /portfolio/values")
    url = f"{BASE_URL}/portfolio/values"
    params = {
        "when": "2025-01-01",
        "contract": "SamplePortfolio0001"
    }
    resp = requests.get(url, headers=get_headers(TOKEN_PORTFOLIO), params=params)
    safe_print_json(resp)

    # /portfolio/value-series
    print("➡️  /portfolio/value-series")
    url = f"{BASE_URL}/portfolio/value-series"
    params = {
        "begin": "2024-01-01",
        "end": "2025-01-01",
        "contract": "SamplePortfolio0001"
    }
    resp = requests.get(url, headers=get_headers(TOKEN_PORTFOLIO), params=params)
    safe_print_json(resp)

    # /portfolio/value-statistics
    print("➡️  /portfolio/value-statistics")
    url = f"{BASE_URL}/portfolio/value-statistics"
    params = {
        "begin": "2024-01-01",
        "end": "2025-01-01",
        "contract": "SamplePortfolio0001"
    }
    resp = requests.get(url, headers=get_headers(TOKEN_PORTFOLIO), params=params)
    safe_print_json(resp)

    # /portfolio/contract-sets/{contractSetId}
    print("➡️  /portfolio/contract-sets/{contractSetId}")
    contract_set_id = "SampleContractSet0001"  # hypothétique ID de set
    url = f"{BASE_URL}/portfolio/contract-sets/{contract_set_id}"
    resp = requests.get(url, headers=get_headers(TOKEN_PORTFOLIO))
    safe_print_json(resp)

    # /portfolio/contract-sets
    print("➡️  /portfolio/contract-sets")
    url = f"{BASE_URL}/portfolio/contract-sets"
    resp = requests.get(url, headers=get_headers(TOKEN_PORTFOLIO))
    safe_print_json(resp)

    print("Tests des endpoints /portfolio terminés.\n")



# ============================================================
# LANCEMENT
# ============================================================


#test_asset_endpoints()
test_portfolio_endpoints()
