# mock_aixigo.py
from fastapi import FastAPI
from fastapi.responses import JSONResponse

app = FastAPI(title="Mock Aixigo Analytics API")

# Overview: /portfolio-kpi
@app.get("/analytics/portfolio-kpi")
async def portfolio_kpi_overview():
    return JSONResponse({
        "_links": {
            "self": {"href": "https://demo.portal.aixigo.cloud/analytics/portfolio-kpi"},
            "performance": [{"href": "/analytics/portfolio-kpi/performance"}],
            "risk-characteristics": [{"href": "/analytics/portfolio-kpi/risk-characteristics"}],
            "return": [{"href": "/analytics/portfolio-kpi/return"}]
        }
    })

# Performance endpoint (simulé)
@app.get("/analytics/portfolio-kpi/performance")
async def portfolio_performance(contract: str = "SamplePortfolio0001",
                                begin: str = "2023-01-01",
                                end: str = "2023-08-28",
                                aggregation: str | None = None):
    simulated_response = {
        "contract": contract,
        "currency": "EUR",
        "period": {"begin": begin, "end": end},
        "performance": {
            "timeWeightedReturn": 0.064,   # 6.4%
            "moneyWeightedReturn": 0.061,  # 6.1%
            "modifiedDietz": 0.062
        },
        "aggregations": aggregation
    }
    return JSONResponse(simulated_response)




# Values endpoint (extrait simplifié)
@app.get("/portfolio/values")
async def portfolio_values(contract: str = "SamplePortfolio0001", when: str = "2023-08-28", aggregation: str = "CONTRACT"):
    response = {
        "contract": contract,
        "when": when,
        "aggregation": aggregation,
        "values": {
            "marketValue": 1234567.89,
            "cash": 23456.78,
            "positions": [
                {"assetId": "850403", "quantity": 100, "marketValue": 500000},
                {"assetId": "906866", "quantity": 50, "marketValue": 300000}
            ]
        }
    }
    return JSONResponse(response)



@app.get("/analytics/portfolio-kpi/risk-characteristics")
async def portfolio_risk_characteristics(contract: str = "SamplePortfolio0001",
                                         begin: str = "2023-01-01",
                                         end: str = "2023-08-28"):
    simulated_risk = {
        "contract": contract,
        "currency": "EUR",
        "period": {"begin": begin, "end": end},
        "risk": {
            "volatility": 0.081,             # 8.1 %
            "valueAtRisk": -0.045,           # -4.5 % (à 95 % de confiance)
            "maxDrawdown": -0.072,           # -7.2 %
            "sharpeRatio": 0.78
        },
        "comments": "Volatility and VaR computed on daily returns for YTD period."
    }
    return JSONResponse(simulated_risk)