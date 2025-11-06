""" Script inutile, il s'agissait de simuler un serveur AIXIGO
l'objectif était de répondre au fait qu'on arrivait pas à requêter les endpoints de l'API analytics (il nous fallait un token)
"""


# mock_aixigo.py
from fastapi import FastAPI
from fastapi import Query
from fastapi.responses import JSONResponse
from datetime import date

app = FastAPI(title="Mock Aixigo Use Case 1")
""" USE CASE : quel client dois-je appeler prochainement:
GET /portfolio/contracts
GET /portfolio/persons-of-contract/{contractId}
GET /portfolio/transactions
GET /portfolio-kpi/performance
"""

# identifiants
@app.get("/portfolio/contracts")
async def get_contracts():
    contracts = [
        {
            "id": "Contract001",
            "contract": {
                "id": "SamplePortfolio0001",
                "detailedType": "DISCRETIONARY",
                "contractNumber": "0001-ACC",
                "openingDate": "2020-05-01",
                "closingDate": None,
                "currency": "EUR",
                "state": "ACTIVE",
                "purpose": "Investment management",
                "annotation": "Simulated contract for POC",
                "accounts": [
                    {
                        "id": "Account-001",
                        "openingDate": "2020-05-01",
                        "closingDate": None,
                        "type": "PORTFOLIO",
                        "detailedType": "STANDARD",
                        "accountNumber": "FR7612345678900001",
                        "currency": "EUR",
                        "iban": "FR7612345678900001",
                        "bic": "AGRIFRPP",
                        "positions": [
                            {"id": "Pos-906866", "depositoryId": "Depot-A", "assetId": "906866"}
                        ],
                    }
                ],
            },
            "restrictions": [],
            "paymentPlans": [],
        },
        {
            "id": "Contract002",
            "contract": {
                "id": "SamplePortfolio0002",
                "detailedType": "ADVISORY",
                "contractNumber": "0002-ACC",
                "openingDate": "2021-03-10",
                "closingDate": None,
                "currency": "EUR",
                "state": "ACTIVE",
                "purpose": "Private banking",
                "annotation": "Simulated contract",
                "accounts": [
                    {
                        "id": "Account-002",
                        "openingDate": "2021-03-10",
                        "closingDate": None,
                        "type": "PORTFOLIO",
                        "detailedType": "STANDARD",
                        "accountNumber": "FR7612345678900002",
                        "currency": "EUR",
                        "iban": "FR7612345678900002",
                        "bic": "AGRIFRPP",
                        "positions": [
                            {"id": "Pos-A0M7P5", "depositoryId": "Depot-B", "assetId": "A0M7P5"}
                        ],
                    }
                ],
            },
            "restrictions": [],
            "paymentPlans": [],
        },
        {
            "id": "Contract003",
            "contract": {
                "id": "SamplePortfolio0003",
                "detailedType": "DISCRETIONARY",
                "contractNumber": "0003-ACC",
                "openingDate": "2019-11-20",
                "closingDate": None,
                "currency": "USD",
                "state": "ACTIVE",
                "purpose": "Investment",
                "annotation": "Simulated USD portfolio",
                "accounts": [
                    {
                        "id": "Account-003",
                        "openingDate": "2019-11-20",
                        "closingDate": None,
                        "type": "PORTFOLIO",
                        "detailedType": "STANDARD",
                        "accountNumber": "US998877665544333",
                        "currency": "USD",
                        "iban": None,
                        "bic": None,
                        "positions": [
                            {"id": "Pos-A112ZR", "depositoryId": "Depot-C", "assetId": "A112ZR"}
                        ],
                    }
                ],
            },
            "restrictions": [],
            "paymentPlans": [],
        },
        {
            "id": "Contract004",
            "contract": {
                "id": "SamplePortfolio0004",
                "detailedType": "DISCRETIONARY",
                "contractNumber": "0004-ACC",
                "openingDate": "2022-07-01",
                "closingDate": None,
                "currency": "CHF",
                "state": "ACTIVE",
                "purpose": "Wealth management",
                "annotation": "Swiss client portfolio",
                "accounts": [
                    {
                        "id": "Account-004",
                        "openingDate": "2022-07-01",
                        "closingDate": None,
                        "type": "PORTFOLIO",
                        "detailedType": "STANDARD",
                        "accountNumber": "CH9300762011623852957",
                        "currency": "CHF",
                        "iban": "CH9300762011623852957",
                        "bic": "POFICHBEXXX",
                        "positions": [
                            {"id": "Pos-A12DFH", "depositoryId": "Depot-D", "assetId": "A12DFH"}
                        ],
                    }
                ],
            },
            "restrictions": [],
            "paymentPlans": [],
        },
        {
            "id": "Contract005",
            "contract": {
                "id": "SamplePortfolio0005",
                "detailedType": "DISCRETIONARY",
                "contractNumber": "0005-ACC",
                "openingDate": "2023-02-14",
                "closingDate": None,
                "currency": "EUR",
                "state": "ACTIVE",
                "purpose": "Sustainable investment",
                "annotation": "New ESG-focused portfolio",
                "accounts": [
                    {
                        "id": "Account-005",
                        "openingDate": "2023-02-14",
                        "closingDate": None,
                        "type": "PORTFOLIO",
                        "detailedType": "STANDARD",
                        "accountNumber": "FR7612345678900005",
                        "currency": "EUR",
                        "iban": "FR7612345678900005",
                        "bic": "AGRIFRPP",
                        "positions": [
                            {"id": "Pos-A0HHKV", "depositoryId": "Depot-E", "assetId": "A0HHKV"}
                        ],
                    }
                ],
            },
            "restrictions": [],
            "paymentPlans": [],
        },
    ]
    return JSONResponse(contracts)


# identifiants par contrat (conforme à la doc Aixigo)
@app.get("/portfolio/persons-of-contract/{contractId}")
async def get_persons_of_contract(contractId: str):
    mapping = {
        "SamplePortfolio0001": [
            {"personId": "P001", "relationshipType": "PRIMARY_OWNER"}
        ],
        "SamplePortfolio0002": [
            {"personId": "P002", "relationshipType": "PRIMARY_OWNER"}
        ],
        "SamplePortfolio0003": [
            {"personId": "P003", "relationshipType": "JOINT_OWNER"}
        ],
        "SamplePortfolio0004": [
            {"personId": "P004", "relationshipType": "PRIMARY_OWNER"}
        ],
        "SamplePortfolio0005": [
            {"personId": "P005", "relationshipType": "PRIMARY_OWNER"}
        ],
    }

    response = {
        "relatedPersons": mapping.get(contractId, [])
    }

    return JSONResponse(response)


@app.get("/portfolio/transactions")
async def get_transactions(contract: str = None):
    """Mock conforme à la structure Aixigo mais simplifié."""

    sample_transactions = {
        "SamplePortfolio0001": [
            {
                "transactionId": "TXN-0001-A",
                "transactionType": "BUY",
                "impactDate": "2025-03-15",
                "contractId": "SamplePortfolio0001",
                "accountId": "Account-001",
                "assetId": "906866",
                "quantity": 120,
                "totalAmount": {"currencyId": "EUR", "amount": 10000},
                "taxes": {"currencyId": "EUR", "amount": 120},
                "fees": {"currencyId": "EUR", "amount": 15},
                "tradingDate": "2025-03-14",
                "valutaDate": "2025-03-17",
                "annotation": "Regular portfolio buy operation",
            }
        ],
        "SamplePortfolio0002": [
            {
                "transactionId": "TXN-0002-A",
                "transactionType": "SELL",
                "impactDate": "2024-12-01",
                "contractId": "SamplePortfolio0002",
                "accountId": "Account-002",
                "assetId": "A0M7P5",
                "quantity": 80,
                "totalAmount": {"currencyId": "EUR", "amount": 7500},
                "taxes": {"currencyId": "EUR", "amount": 95},
                "fees": {"currencyId": "EUR", "amount": 10},
                "tradingDate": "2024-11-30",
                "valutaDate": "2024-12-02",
                "annotation": "Profit taking",
            }
        ],
        "SamplePortfolio0003": [
            {
                "transactionId": "TXN-0003-A",
                "transactionType": "BUY",
                "impactDate": "2025-09-10",
                "contractId": "SamplePortfolio0003",
                "accountId": "Account-003",
                "assetId": "A112ZR",
                "quantity": 50,
                "totalAmount": {"currencyId": "USD", "amount": 4000},
                "taxes": {"currencyId": "USD", "amount": 40},
                "fees": {"currencyId": "USD", "amount": 8},
                "tradingDate": "2025-09-09",
                "valutaDate": "2025-09-11",
                "annotation": "Client initiated buy",
            }
        ],
        "SamplePortfolio0004": [
            {
                "transactionId": "TXN-0004-A",
                "transactionType": "DIVIDEND",
                "impactDate": "2024-10-20",
                "contractId": "SamplePortfolio0004",
                "accountId": "Account-004",
                "assetId": "A12DFH",
                "quantity": 0,
                "totalAmount": {"currencyId": "CHF", "amount": 250},
                "taxes": {"currencyId": "CHF", "amount": 0},
                "fees": {"currencyId": "CHF", "amount": 0},
                "tradingDate": "2024-10-19",
                "valutaDate": "2024-10-21",
                "annotation": "Dividend payment received",
            }
        ],
        "SamplePortfolio0005": [
            {
                "transactionId": "TXN-0005-A",
                "transactionType": "BUY",
                "impactDate": "2025-01-05",
                "contractId": "SamplePortfolio0005",
                "accountId": "Account-005",
                "assetId": "A0HHKV",
                "quantity": 90,
                "totalAmount": {"currencyId": "EUR", "amount": 8200},
                "taxes": {"currencyId": "EUR", "amount": 100},
                "fees": {"currencyId": "EUR", "amount": 12},
                "tradingDate": "2025-01-04",
                "valutaDate": "2025-01-06",
                "annotation": "Reinvestment order",
            }
        ],
    }

    # Structure conforme à la doc Aixigo : holdings -> transactions
    def format_transactions(contract_id):
        return {
            "holdings": [
                {
                    "holdingId": {"contractId": contract_id},
                    "transactions": sample_transactions.get(contract_id, []),
                    "unvaluedPositions": [],
                }
            ]
        }

    # Si un contrat spécifique est demandé
    if contract:
        return JSONResponse(format_transactions(contract))

    # Sinon renvoyer toutes les transactions
    return JSONResponse({cid: format_transactions(cid) for cid in sample_transactions})


# Performance avec valeurs simulées
@app.get("/portfolio-kpi/performance")
async def portfolio_performance(contract: str = "SamplePortfolio0001",
                                begin: str = "2025-01-01",
                                end: str = "2025-10-29"):
    """Mock conforme au format Aixigo pour le KPI Performance."""

    performances = {
        "SamplePortfolio0001": 0.062,
        "SamplePortfolio0002": 0.041,
        "SamplePortfolio0003": -0.008,
        "SamplePortfolio0004": 0.027,
        "SamplePortfolio0005": 0.073,
    }

    perf = performances.get(contract, 0.0)

    simulated_response = {
        "holdings": [
            {
                "modifiedDietzPerformance": {
                    "totalPerformance": perf,
                    "yearlyPerformance": perf * 1.05  # légère variation arbitraire
                },
                "moneyWeightedPerformance": {
                    "totalPerformance": perf * 0.98,
                    "yearlyPerformance": perf
                },
                "timeWeightedPerformance": {
                    "totalPerformance": perf,
                    "yearlyPerformance": perf * 1.02
                },
                "holdingId": {"contractId": contract},
                "unvaluedPositions": []
            }
        ]
    }

    return JSONResponse(simulated_response)

