import requests
from datetime import datetime
from fastmcp import FastMCP

mcp = FastMCP("CryptoMCP")

def _get(url: str, timeout: int = 5):
    return requests.get(url, timeout=timeout, headers={"User-Agent": "CryptoMCP/1.0"})

@mcp.tool
def precio_bitcoin() -> str:
    """
    Devuelve el precio actual de BTC en USD.
    Intenta varias fuentes y devuelve 'fuente: precio (ISO8601)'.
    """
    # 1) CoinDesk
    try:
        r = _get("https://api.coindesk.com/v1/bpi/currentprice.json")
        d = r.json()
        price = d["bpi"]["USD"].get("rate_float") or float(d["bpi"]["USD"]["rate"].replace(",", ""))
        return f"CoinDesk: {price:.2f} USD ({datetime.utcnow().isoformat()}Z)"
    except Exception:
        pass

    # 2) CoinGecko
    try:
        r = _get("https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd")
        price = float(r.json()["bitcoin"]["usd"])
        return f"CoinGecko: {price:.2f} USD ({datetime.utcnow().isoformat()}Z)"
    except Exception:
        pass

    # 3) Blockchain.info
    try:
        r = _get("https://blockchain.info/ticker")
        price = float(r.json()["USD"]["last"])
        return f"Blockchain.info: {price:.2f} USD ({datetime.utcnow().isoformat()}Z)"
    except Exception as e:
        return f"[ERROR] No se pudo obtener el precio desde ninguna fuente: {e}"

if __name__ == "__main__":
    mcp.run()
