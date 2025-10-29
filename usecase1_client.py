import requests
from datetime import datetime

BASE = "http://127.0.0.1:8000"

def days_since(date_str: str) -> int:
    """Renvoie le nombre de jours écoulés depuis une date (YYYY-MM-DD)."""
    try:
        d = datetime.strptime(date_str, "%Y-%m-%d")
        return (datetime.now() - d).days
    except Exception:
        return 9999  # valeur par défaut si date invalide

def get_performance(contract_id: str) -> float | None:
    params = {
        "contract": contract_id,
        "begin": "2025-01-01",
        "end": "2025-10-29"
    }
    r = requests.get(f"{BASE}/portfolio-kpi/performance", params=params)
    if r.status_code == 200:
        data = r.json()
        holdings = data.get("holdings", [])
        if holdings:
            return holdings[0]["timeWeightedPerformance"]["totalPerformance"]
    return None


def find_inactive_clients_with_perf():
    contracts = requests.get(f"{BASE}/portfolio/contracts").json()
    print("📊 Clients inactifs avec leur performance de portefeuille :\n")

    for c in contracts:
        cid = c["contract"]["id"]

        # Récupération des personnes liées
        related = requests.get(f"{BASE}/portfolio/persons-of-contract/{cid}").json()["relatedPersons"]
        person = related[0] if related else {"personId": "Unknown", "relationshipType": "Unknown"}

        # ✅ Nouvelle logique pour récupérer la dernière transaction
        tx = requests.get(f"{BASE}/portfolio/transactions", params={"contract": cid}).json()
        holdings = tx.get("holdings", [])
        if holdings and holdings[0].get("transactions"):
            last_date = holdings[0]["transactions"][0]["impactDate"]
            days_inactive = days_since(last_date)
        else:
            last_date = "N/A"
            days_inactive = 9999

        perf = get_performance(cid)
        perf_pct = f"{perf*100:.2f} %" if perf is not None else "N/A"

        if days_inactive > 90:
            print(f"⚠️  {person['personId']} ({cid}) — {days_inactive} jours sans activité — Performance YTD : {perf_pct}")
        else:
            print(f"✅  {person['personId']} ({cid}) — contact récent ({days_inactive} jours) — Performance YTD : {perf_pct}")

if __name__ == "__main__":
    find_inactive_clients_with_perf()
