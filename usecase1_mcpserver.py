# mcp_aixigo_server.py
"""
MCP Server – Wrapper autour du mock Aixigo FastAPI local.
Expose les endpoints REST du mock comme des outils MCP.
"""

import logging
logging.basicConfig(level=logging.DEBUG)

from typing import Any
import httpx
from mcp.server.fastmcp import FastMCP

# On crée un serveur MCP nommé “aixigo_mock”
mcp = FastMCP("aixigo_mock")

# Adresse locale du mock FastAPI (il faut le lancer séparément avec uvicorn)
AIXIGO_BASE = "http://127.0.0.1:8000"


# 🔹 Outil 1 : Lister les contrats disponibles
@mcp.tool()
async def list_contracts() -> str:
    """List all simulated contracts from the local Aixigo mock server."""
    async with httpx.AsyncClient() as client:
        resp = await client.get(f"{AIXIGO_BASE}/portfolio/contracts")
        if resp.status_code != 200:
            return f"Error {resp.status_code} fetching contracts."
        contracts = resp.json()

        formatted = []
        for c in contracts:
            cid = c["contract"]["id"]
            purpose = c["contract"]["purpose"]
            currency = c["contract"]["currency"]
            formatted.append(f"{cid} — {purpose} ({currency})")

        return "\n".join(formatted)


# 🔹 Outil 2 : Récupérer les transactions d’un contrat
@mcp.tool()
async def get_transactions(contract_id: str) -> str:
    """Get last transactions for a given contract ID."""
    async with httpx.AsyncClient() as client:
        resp = await client.get(f"{AIXIGO_BASE}/portfolio/transactions", params={"contract": contract_id})
        if resp.status_code != 200:
            return f"Error {resp.status_code} fetching transactions for {contract_id}."
        data = resp.json()

        transactions = data["holdings"][0]["transactions"]
        if not transactions:
            return f"No transactions found for {contract_id}."

        formatted = []
        for tx in transactions:
            formatted.append(
                f"• {tx['transactionType']} on {tx['impactDate']} — {tx['totalAmount']['amount']} {tx['totalAmount']['currencyId']} ({tx['annotation']})"
            )
        return "\n".join(formatted)


# 🔹 Outil 3 : Récupérer la performance d’un contrat
@mcp.tool()
async def get_performance(contract_id: str) -> str:
    """Get portfolio performance for a given contract ID."""
    async with httpx.AsyncClient() as client:
        resp = await client.get(f"{AIXIGO_BASE}/portfolio-kpi/performance", params={"contract": contract_id})
        if resp.status_code != 200:
            return f"Error {resp.status_code} fetching performance for {contract_id}."
        data = resp.json()
        holdings = data["holdings"][0]
        twr = holdings["timeWeightedPerformance"]["totalPerformance"]
        mwr = holdings["moneyWeightedPerformance"]["totalPerformance"]
        md = holdings["modifiedDietzPerformance"]["totalPerformance"]

        return (
            f"Performance for {contract_id}:\n"
            f"• Time-Weighted: {twr*100:.2f}%\n"
            f"• Money-Weighted: {mwr*100:.2f}%\n"
            f"• Modified Dietz: {md*100:.2f}%"
        )


# 🔹 Outil 4 : Identifier les clients inactifs
@mcp.tool()
async def list_inactive_clients(threshold_days: int = 90) -> str:
    """List clients whose last transaction was older than threshold_days."""
    from datetime import date, datetime

    async with httpx.AsyncClient() as client:
        resp = await client.get(f"{AIXIGO_BASE}/portfolio/contracts")
        contracts = resp.json()

        inactive = []
        today = date.today()

        for c in contracts:
            cid = c["contract"]["id"]
            tx_resp = await client.get(f"{AIXIGO_BASE}/portfolio/transactions", params={"contract": cid})
            txs = tx_resp.json()["holdings"][0]["transactions"]
            if not txs:
                continue
            last_date = datetime.strptime(txs[0]["impactDate"], "%Y-%m-%d").date()
            delta = (today - last_date).days
            if delta > threshold_days:
                inactive.append(f"{cid} — last activity {delta} days ago")

        if not inactive:
            return "All clients have recent activity."

        return "\n".join(inactive)


def main():
    """Run the MCP Aixigo mock server."""
    mcp.run(transport="stdio")

if __name__ == "__main__":
    main()
