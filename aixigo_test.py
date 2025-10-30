import requests

# === Configuration ===
BASE_URL = "https://demo.portal.aixigo.cloud/analytics"
TOKEN = "eyJhbGciOiJSUzI1NiIsInR5cCIgOiAiSldUIiwia2lkIiA6ICI4ZksxTW95NkVidjktcjNEQ3IwMXJtemVsY3FkMUpUbVJDaGh6YkxRblpnIn0.eyJleHAiOjE3NjE4MzIzNTMsImlhdCI6MTc2MTgyODc1MywiYXV0aF90aW1lIjoxNzYxODI4NzQxLCJqdGkiOiI2ZWY1NDlmMy1lOTdkLTRhNTEtODYwYy0xNDcyN2I3YWI0NjIiLCJpc3MiOiJodHRwczovL2xvZ2luLnBvcnRhbC5haXhpZ28uY2xvdWQvcmVhbG1zL2FwcHMiLCJhdWQiOlsid2Vic2l0ZSIsImRlbW8iXSwic3ViIjoiZ3VpbGxhdW1lLmRhdmlkQHN0dWRlbnQtY3MuZnIiLCJ0eXAiOiJJRCIsImF6cCI6IndlYnNpdGUiLCJzaWQiOiJhODRmNTEyYi1lMjFhLTQ0MDUtODQ0Zi04YzI5NGQwMWI1MmIiLCJhdF9oYXNoIjoibld3NWhKdTl1WmZSYXhzU1RZLVUyZyIsImFjciI6IjAiLCJlbWFpbF92ZXJpZmllZCI6dHJ1ZSwicm9sZXMiOlsiR1VFU1QiXSwibmFtZSI6IkRhdmlkIEd1aWxsYXVtZSIsInByZWZlcnJlZF91c2VybmFtZSI6Imd1aWxsYXVtZS5kYXZpZEBzdHVkZW50LWNzLmZyIiwiZ2l2ZW5fbmFtZSI6IkRhdmlkIiwiZmFtaWx5X25hbWUiOiJHdWlsbGF1bWUiLCJ0ZW5hbnQiOiJndWVzdCIsImVtYWlsIjoiZ3VpbGxhdW1lLmRhdmlkQHN0dWRlbnQtY3MuZnIifQ.MrmxUdd0lTHxkXDJ0reuzEXh4yScQZzj68897SySnvkJF6EbJSiJB0_DWeUdoPzpy0_7WeNe61EALGSKpnG_jSUVzGEdcCy09HdnA0fwprY8sNWPeaS_O3XtSkoAh-J49oUjQiVG5f84aRQCFxYskAPjooCmOzPpEekk_b7EKedJ3fzo-huSA43t80PV8dOH3uaqnQhgh-aBmJQyaUMqRrl5hVtGb6j81Lbxg5PueBSDhzAvqwt5eqxNs_YoRtzWIe7F3wnhCxBns2qPy4VlB5o4lJnOcVFYfpdoHEL65aukmSc0mLdkoT6T8t2VLQu-R-RQJpmPnIB9BS6vfGUpiQ"

HEADERS = {
    "accept": "application/hal+json",
    "x-id-token": TOKEN
}

# === Exemple de requête 1 : Liste des endpoints portfolio-kpi ===
print("➡️ Test : /portfolio-kpi")
resp = requests.get(f"{BASE_URL}/portfolio-kpi", headers=HEADERS)
print("Status:", resp.status_code)
print("Response: (non développée)")
#print(resp.json())


# === Exemple de requête 2 : Performance d’un portefeuille ===
print("\n➡️ Test : /portfolio-kpi/performance")
params = {
    "begin": "2024-01-01",
    "end": "2025-01-01",
    "restriction": "NONE",
    "contractSet": "NONE",
    "contract": "SamplePortfolio0001",
    "algorithm": "MODIFIED_DIETZ",
    "aggregation": "ALL",
    "currencySelection": "CONTRACT"
}
resp = requests.get(f"{BASE_URL}/portfolio-kpi/performance", headers=HEADERS, params=params)
print("Status:", resp.status_code)
try:
    print(resp.json())
except Exception:
    print(resp.text)
