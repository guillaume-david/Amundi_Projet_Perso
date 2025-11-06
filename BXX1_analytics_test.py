import requests

# Deux tokens différents selon le type d’API
TOKEN_ASSET = "eyJhbGciOiJSUzI1NiIsInR5cCIgOiAiSldUIiwia2lkIiA6ICI4ZksxTW95NkVidjktcjNEQ3IwMXJtemVsY3FkMUpUbVJDaGh6YkxRblpnIn0.eyJleHAiOjE3NjI0Mzk4NzMsImlhdCI6MTc2MjQzNjI3MywiYXV0aF90aW1lIjoxNzYyNDMyNzMwLCJqdGkiOiJhYTlmMTY1My05YWE4LTQ2ZWUtOTkxYS0wZTgzY2VjY2Y2OWYiLCJpc3MiOiJodHRwczovL2xvZ2luLnBvcnRhbC5haXhpZ28uY2xvdWQvcmVhbG1zL2FwcHMiLCJhdWQiOlsid2Vic2l0ZSIsImRlbW8iXSwic3ViIjoiZ3VpbGxhdW1lLmRhdmlkQHN0dWRlbnQtY3MuZnIiLCJ0eXAiOiJJRCIsImF6cCI6IndlYnNpdGUiLCJzaWQiOiI4ZjU3OWI3Yi03OTRiLTRhMzAtYmNmMS02YzRhM2RmNWUxMjAiLCJhdF9oYXNoIjoiTWViRkxpVDAzU0EwVnBUU0R3UlA0USIsImFjciI6IjAiLCJlbWFpbF92ZXJpZmllZCI6dHJ1ZSwicm9sZXMiOlsiR1VFU1QiXSwibmFtZSI6IkRhdmlkIEd1aWxsYXVtZSIsInByZWZlcnJlZF91c2VybmFtZSI6Imd1aWxsYXVtZS5kYXZpZEBzdHVkZW50LWNzLmZyIiwiZ2l2ZW5fbmFtZSI6IkRhdmlkIiwiZmFtaWx5X25hbWUiOiJHdWlsbGF1bWUiLCJ0ZW5hbnQiOiJndWVzdCIsImVtYWlsIjoiZ3VpbGxhdW1lLmRhdmlkQHN0dWRlbnQtY3MuZnIifQ.SVaiurzUz8iqRm-vNCbiKMN1tOLVWRkbUj7wMXYMWIMiSQ-NBFBRZyMMPN6kl9xTSqYcqxKlWXz7qHF7N9bC9kbhpUanm5Xv5HV8ZAlVBZhnPW9p6JvUWTkFF6GRh9p1RbLGrYxJ9UN9sXfRvhAjbLnXtoDC_YMNTWMgehhLJASY9cBKqxKv-wU9a_CEI6B1fvtB6U7E5SvhGcSJSmhcPCSKWofKqHWCH3XrvccybkGv85jcVg_hvE61A5pf2zRljEV6L-gR4Q2jg5aX6Ljv6ssJn890cV4ScQIilYF1d99NPxVFSsjWHkyIBK2LMbd4upyHB1FJa4KChuHBdjyITw" 
TOKEN_PORTFOLIO = "eyJhbGciOiJSUzI1NiIsInR5cCIgOiAiSldUIiwia2lkIiA6ICI4ZksxTW95NkVidjktcjNEQ3IwMXJtemVsY3FkMUpUbVJDaGh6YkxRblpnIn0.eyJleHAiOjE3NjI0Mzk4NzMsImlhdCI6MTc2MjQzNjI3MywiYXV0aF90aW1lIjoxNzYyNDMyNzMwLCJqdGkiOiJhYTlmMTY1My05YWE4LTQ2ZWUtOTkxYS0wZTgzY2VjY2Y2OWYiLCJpc3MiOiJodHRwczovL2xvZ2luLnBvcnRhbC5haXhpZ28uY2xvdWQvcmVhbG1zL2FwcHMiLCJhdWQiOlsid2Vic2l0ZSIsImRlbW8iXSwic3ViIjoiZ3VpbGxhdW1lLmRhdmlkQHN0dWRlbnQtY3MuZnIiLCJ0eXAiOiJJRCIsImF6cCI6IndlYnNpdGUiLCJzaWQiOiI4ZjU3OWI3Yi03OTRiLTRhMzAtYmNmMS02YzRhM2RmNWUxMjAiLCJhdF9oYXNoIjoiTWViRkxpVDAzU0EwVnBUU0R3UlA0USIsImFjciI6IjAiLCJlbWFpbF92ZXJpZmllZCI6dHJ1ZSwicm9sZXMiOlsiR1VFU1QiXSwibmFtZSI6IkRhdmlkIEd1aWxsYXVtZSIsInByZWZlcnJlZF91c2VybmFtZSI6Imd1aWxsYXVtZS5kYXZpZEBzdHVkZW50LWNzLmZyIiwiZ2l2ZW5fbmFtZSI6IkRhdmlkIiwiZmFtaWx5X25hbWUiOiJHdWlsbGF1bWUiLCJ0ZW5hbnQiOiJndWVzdCIsImVtYWlsIjoiZ3VpbGxhdW1lLmRhdmlkQHN0dWRlbnQtY3MuZnIifQ.SVaiurzUz8iqRm-vNCbiKMN1tOLVWRkbUj7wMXYMWIMiSQ-NBFBRZyMMPN6kl9xTSqYcqxKlWXz7qHF7N9bC9kbhpUanm5Xv5HV8ZAlVBZhnPW9p6JvUWTkFF6GRh9p1RbLGrYxJ9UN9sXfRvhAjbLnXtoDC_YMNTWMgehhLJASY9cBKqxKv-wU9a_CEI6B1fvtB6U7E5SvhGcSJSmhcPCSKWofKqHWCH3XrvccybkGv85jcVg_hvE61A5pf2zRljEV6L-gR4Q2jg5aX6Ljv6ssJn890cV4ScQIilYF1d99NPxVFSsjWHkyIBK2LMbd4upyHB1FJa4KChuHBdjyITw"

# === Configuration ===
BASE_URL = "https://demo.portal.aixigo.cloud"

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



def test_endpoints_asset():
    # === 1️e Test de l’endpoint /asset ===
    print("********************* TEST DE /ASSET ***************************************")
    print("➡️ Test : /asset")
    asset_url = f"{BASE_URL}/analytics/asset"
    r_asset = requests.get(asset_url, headers=get_headers(TOKEN_ASSET, hal=True))
    safe_print_json(r_asset)

    print("➡️ Test : /asset/assets")
    asset_assets_url = f"{BASE_URL}/analytics/asset/assets"
    params = [
        ("asset",850403), # ou 850403 - 884437 - 865985 - 870747 - 906866 - A0HHKV - A0M7P5 - A0M7P6 - A117ME - A1CX3T - A112JK - A112ZR - A12DFH - A1XCLR - HYXU00 - A0Q4FW
        ("when",'2024-01-01')
    ]
    r_asset_assets = requests.get(asset_assets_url, headers=get_headers(TOKEN_ASSET), params=params)
    safe_print_json(r_asset_assets)

    print("➡️ Test : /asset/quotes")
    asset_quotes_url = f"{BASE_URL}/analytics/asset/quotes"
    params = [
        ("asset",850403), # ou 850403 - 884437 - 865985 - 870747 - 906866 - A0HHKV - A0M7P5 - A0M7P6 - A117ME - A1CX3T - A112JK - A112ZR - A12DFH - A1XCLR - HYXU00 - A0Q4FW
        ("when",'2024-01-01')
    ]
    r_asset_quotes = requests.get(asset_quotes_url, headers=get_headers(TOKEN_ASSET), params=params)
    safe_print_json(r_asset_quotes)


    print("➡️ Test : /asset/exchange-rates")
    asset_exchange_rates_url = f"{BASE_URL}/analytics/asset/exchange-rates"
    params = [
        ("sourceCurrency",'EUR'),
        ("targetCurrency",'CHF'),
        ("when",'2024-01-01')
    ]
    r_asset_exchange_rates = requests.get(asset_exchange_rates_url, headers=get_headers(TOKEN_ASSET), params=params)
    safe_print_json(r_asset_exchange_rates)

    print("➡️ Test : /asset/benchmark-performance")
    asset_benchmark_performance_url = f"{BASE_URL}/analytics/asset/benchmark-performance"
    params = [
        ("begin",'2024-01-01'),
        ("end",'2025-01-01'),
        ("benchmark",'benchmark_INDEX_SP500') #ou benchmark_INDEX_DAX / benchmark_INDEX_STOXX50 / benchmark_INDEX_DOWJONES / benchmark_INDEX_NASDAQ / benchmark_INDEX_SP500 / benchmark_INDEX_MSCIWORLD / benchmark_INDEX_RUSSELL2000 / benchmark_INDEX_VIX
    ]
    r_asset_benchmark_performance = requests.get(asset_benchmark_performance_url, headers=get_headers(TOKEN_ASSET), params=params)
    safe_print_json(r_asset_benchmark_performance)

    print("➡️ Test : /asset/benchmarks")
    asset_benchmarks_url = f"{BASE_URL}/analytics/asset/benchmarks"
    r_asset_benchmarks = requests.get(asset_benchmarks_url, headers=get_headers(TOKEN_ASSET))
    safe_print_json(r_asset_benchmarks)

    print("➡️ Test : /asset/benchmark-quote-series")
    asset_benchmark_quote_series_url = f"{BASE_URL}/analytics/asset/benchmark-quote-series"
    params = [
        ("begin",'2024-01-01'),
        ("end",'2025-01-01'),
        ("benchmark",'benchmark_INDEX_SP500') #ou benchmark_INDEX_DAX / benchmark_INDEX_STOXX50 / benchmark_INDEX_DOWJONES / benchmark_INDEX_NASDAQ / benchmark_INDEX_SP500 / benchmark_INDEX_MSCIWORLD / benchmark_INDEX_RUSSELL2000 / benchmark_INDEX_VIX
    ]
    r_asset_benchmark_quote_series = requests.get(asset_benchmark_quote_series_url, headers=get_headers(TOKEN_ASSET), params=params)
    safe_print_json(r_asset_benchmark_quote_series)

    print("➡️ Test : /asset/benchmark-risk-characteristics")
    asset_benchmark_risk_characteristics_url = f"{BASE_URL}/analytics/asset/benchmark-risk-characteristics"
    params = [
        ("begin",'2024-01-01'),
        ("end",'2025-01-01'),
        ("benchmark",'benchmark_INDEX_SP500') #ou benchmark_INDEX_DAX / benchmark_INDEX_STOXX50 / benchmark_INDEX_DOWJONES / benchmark_INDEX_NASDAQ / benchmark_INDEX_SP500 / benchmark_INDEX_MSCIWORLD / benchmark_INDEX_RUSSELL2000 / benchmark_INDEX_VIX
    ]
    r_asset_benchmark_risk_characteristics = requests.get(asset_benchmark_risk_characteristics_url, headers=get_headers(TOKEN_ASSET), params=params)
    safe_print_json(r_asset_benchmark_risk_characteristics)
    
    
    return None
#test_endpoints_asset()

def test_endpoints_portfolio():
    # === 2️e Test de l’endpoint /portfolio ===
    print("********************* TEST DE /PORTFOLIO ***************************************")
    """
    print("➡️ Test : /portfolio")
    portfolio_url = f"{BASE_URL}/analytics/portfolio"
    r_portfolio = requests.get(portfolio_url, headers=get_headers(TOKEN_PORTFOLIO, hal=True))
    safe_print_json(r_portfolio)

    print("➡️ Test : /portfolio/pending-orders")
    portfolio_pending_orders_url = f"{BASE_URL}/analytics/portfolio/pending-orders"
    params = [
        ("when", "2025-01-01"),
        ("contract", "SamplePortfolio0001"),        # jusqu'à SamplePortfolio0010
    ]
    r_portfolio_pending_orders = requests.get(portfolio_pending_orders_url, headers=get_headers(TOKEN_PORTFOLIO), params=params)
    safe_print_json(r_portfolio_pending_orders)

    print("➡️ Test : /portfolio/assets-period")
    portfolio_assets_period_url = f"{BASE_URL}/analytics/portfolio/assets-period"
    params = [
        ("begin", "2024-01-01"),
        ("end", "2025-01-01"),
        ("contract", "SamplePortfolio0001"),        # jusqu'à SamplePortfolio0010
    ]
    r_portfolio_assets_period = requests.get(portfolio_assets_period_url, headers=get_headers(TOKEN_PORTFOLIO), params=params)
    safe_print_json(r_portfolio_assets_period)
    
    
    print("➡️ Test : /portfolio/assets-snapshot")
    portfolio_assets_snapshot_url = f"{BASE_URL}/analytics/portfolio/assets-snapshot"
    params = [
        ("when", "2025-01-01"),
        ("contract", "SamplePortfolio0001"),        # jusqu'à SamplePortfolio0010
    ]
    r_portfolio_assets_snapshot = requests.get(portfolio_assets_snapshot_url, headers=get_headers(TOKEN_PORTFOLIO), params=params)
    safe_print_json(r_portfolio_assets_snapshot)

    print("➡️ Test : /portfolio/cash-flows")
    portfolio_cash_flows_url = f"{BASE_URL}/analytics/portfolio/cash-flows"
    params = [
        ("begin", "2024-01-01"),
        ("end", "2025-01-01"),
        ("contract", "SamplePortfolio0001"),        # jusqu'à SamplePortfolio0010
    ]
    r_portfolio_cash_flows = requests.get(portfolio_cash_flows_url, headers=get_headers(TOKEN_PORTFOLIO), params=params)
    safe_print_json(r_portfolio_cash_flows)

    print("➡️ Test : /portfolio/contracts-of-person/{personId}")
    person_id = "customer_001"  # par exemple de customer_001 à customer010
    url = f"{BASE_URL}/analytics/portfolio/contracts-of-person/{person_id}"

    response = requests.get(url, headers=get_headers(TOKEN_PORTFOLIO))
    safe_print_json(response)
"""

    

    return None

/initial-values (params : when / contract)
/interest-data (params: aggregation = ALL / contract)
/partial-holdings (params: begin / end / contract)
/persons-of-contract/{contractId} (params: contract)
/contracts (params: begin / end / contract)
/positions-period (params: begin / end / contract)
/positions-snapshot - (params : when / contract)
/transactions - (params: begin / end / contract)
/transaction-statistics - (params: begin / end / contract)
/transaction-series - (params: begin / end / contract)
/values - (params : when / contract)
/value-series - (params: begin / end / contract)
/value-statistics (params: begin / end / contract)
/contract-sets/{contractSetId} - je n'arrive pas à trouver le paramètre à entrer ici
/contract-sets - j'obtiens une réponse 403 ici (forbidden)

test_endpoints_portfolio()

def test_endpoints_portfolio_kpi():
    # === 3️e Test : /portfolio-kpi/performance ===
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
    
    return None