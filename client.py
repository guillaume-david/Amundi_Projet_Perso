# client_test.py
import requests

BASE = "http://127.0.0.1:8000/analytics"

def get_overview():
    r = requests.get(f"{BASE}/portfolio-kpi")
    print("Status:", r.status_code)
    print("Overview JSON:")
    print(r.json())

def get_performance():
    params = {
        "contract": "SamplePortfolio0001",
        "begin": "2023-01-01",
        "end": "2023-08-28"
    }
    r = requests.get(f"{BASE}/portfolio-kpi/performance", params=params)
    print("\nPerformance JSON:")
    print(r.json())

def get_risk():
    params = {
        "contract": "SamplePortfolio0001",
        "begin": "2023-01-01",
        "end": "2023-08-28"
    }
    r = requests.get(f"{BASE}/portfolio-kpi/risk-characteristics", params=params)
    print("\nRisk JSON:")
    print(r.json())


def get_values():
    params = {"contract": "SamplePortfolio0001", "when": "2023-08-28"}
    r = requests.get(f"http://127.0.0.1:8000/portfolio/values", params=params)
    print("\nValues JSON:")
    print(r.json())

if __name__ == "__main__":
    get_overview()
    get_performance()
    get_risk()
    get_values()