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

# token générique pour les endpoints:
BASE_URL = "https://demo.portal.aixigo.cloud/analytics"
TOKEN = "eyJhbGciOiJSUzI1NiIsInR5cCIgOiAiSldUIiwia2lkIiA6ICI4ZksxTW95NkVidjktcjNEQ3IwMXJtemVsY3FkMUpUbVJDaGh6YkxRblpnIn0.eyJleHAiOjE3NjE4MzIzNTMsImlhdCI6MTc2MTgyODc1MywiYXV0aF90aW1lIjoxNzYxODI4NzQxLCJqdGkiOiI2ZWY1NDlmMy1lOTdkLTRhNTEtODYwYy0xNDcyN2I3YWI0NjIiLCJpc3MiOiJodHRwczovL2xvZ2luLnBvcnRhbC5haXhpZ28uY2xvdWQvcmVhbG1zL2FwcHMiLCJhdWQiOlsid2Vic2l0ZSIsImRlbW8iXSwic3ViIjoiZ3VpbGxhdW1lLmRhdmlkQHN0dWRlbnQtY3MuZnIiLCJ0eXAiOiJJRCIsImF6cCI6IndlYnNpdGUiLCJzaWQiOiJhODRmNTEyYi1lMjFhLTQ0MDUtODQ0Zi04YzI5NGQwMWI1MmIiLCJhdF9oYXNoIjoibld3NWhKdTl1WmZSYXhzU1RZLVUyZyIsImFjciI6IjAiLCJlbWFpbF92ZXJpZmllZCI6dHJ1ZSwicm9sZXMiOlsiR1VFU1QiXSwibmFtZSI6IkRhdmlkIEd1aWxsYXVtZSIsInByZWZlcnJlZF91c2VybmFtZSI6Imd1aWxsYXVtZS5kYXZpZEBzdHVkZW50LWNzLmZyIiwiZ2l2ZW5fbmFtZSI6IkRhdmlkIiwiZmFtaWx5X25hbWUiOiJHdWlsbGF1bWUiLCJ0ZW5hbnQiOiJndWVzdCIsImVtYWlsIjoiZ3VpbGxhdW1lLmRhdmlkQHN0dWRlbnQtY3MuZnIifQ.MrmxUdd0lTHxkXDJ0reuzEXh4yScQZzj68897SySnvkJF6EbJSiJB0_DWeUdoPzpy0_7WeNe61EALGSKpnG_jSUVzGEdcCy09HdnA0fwprY8sNWPeaS_O3XtSkoAh-J49oUjQiVG5f84aRQCFxYskAPjooCmOzPpEekk_b7EKedJ3fzo-huSA43t80PV8dOH3uaqnQhgh-aBmJQyaUMqRrl5hVtGb6j81Lbxg5PueBSDhzAvqwt5eqxNs_YoRtzWIe7F3wnhCxBns2qPy4VlB5o4lJnOcVFYfpdoHEL65aukmSc0mLdkoT6T8t2VLQu-R-RQJpmPnIB9BS6vfGUpiQ"

HEADERS = {
    "accept": "application/hal+json",
    "x-id-token": TOKEN
}

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

# Liste des endpoints de AnalyticsAPI : https://portal.aixigo.com/docs/analytics-api
/asset - liste les endpoints qui appartiennenent à asset
    /asset - toutes les données de référence et de marché pertinentes
        asset=850403&when=YYYY-MM-DD
    /quotes - toutes les données de marché pour un asset à une date précise
        asset=850403&when=YYYY-MM-DD
    /exchange-rates
        sourceCurrency=EUR&targetCurrency=CHF&when=2025-01-01
    /benchmark-performance
        begin=2024-01-01&end=2025-01-01&benchmark=benchmark_INDEX_SP500"
    /benchmarks - retourne la liste des benchmarks disponible
    /benchmarks-quotes-series - performance journalière d'un benchmark entre deux dates
        begin=2024-01-01&end=2025-01-01&benchmark=benchmark_INDEX_SP500
    /benchmark-risk-characteristics - risque journalier d'un benchmark entre deux dates
        begin=2024-01-01&end=2025-01-01&benchmark=benchmark_INDEX_SP500

/portfolio - liste les endpoints qui appartiennenent à portfolio
    /pending-orders - NOK
    /assets-period - NOK
    /assets-snapshot - NOK
    /cash-flows - NOK
    /contracts-of-person/{personId} - donne tous les contrats associés à une personne
        /customer_001
    /initial-values - NOK
    /interest-data - NOK
    /partial-holdings - NOK
    /persons-of-contract/{contractId} - infos sur toutes les personnes associées à un contrat
        /SamplePortfolio0001
    /contracts - info sur un contrat donné
        begin=2024-01-01&end=2025-01-01&contract=SamplePortfolio0001
    /positions-period - NOK
    /positions-snapshot - NOK
    /transactions - NOK
    /transaction-statistics - NOK
    /transaction-series - NOK
    /values - NOK
    /value-series - NOK
    /contract-sets/{contractSetId} - NOK
    /contract-sets - NOK

/portfolio-kpi - liste les endpoints qui appartiennenent à portfolio-kpi
    NOK

/report - liste les endpoints qui appartiennent à /report
    NOK

/data - liste les endpoints de /data
    NOK

/data-provisioning -
    NOK

/health/info - état de l'API
/health/check - idem
/license
/version


