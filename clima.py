import requests
from fastmcp import FastMCP

mcp = FastMCP("WeatherMCP")

@mcp.tool
def clima(ciudad: str) -> str:
    """
    Devuelve el clima actual en una ciudad (formato breve).
    Ejemplo: clima("Madrid") -> "Madrid: ☀️ +25°C"
    """
    try:
        url = f"http://wttr.in/{ciudad}?format=3"
        resp = requests.get(url, timeout=5)
        return resp.text.strip()
    except Exception as e:
        return f"[ERROR] No se pudo obtener el clima: {e}"

if __name__ == "__main__":
    mcp.run()
    