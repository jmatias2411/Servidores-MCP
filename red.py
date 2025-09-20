import requests, socket
from fastmcp import FastMCP

mcp = FastMCP("NetCheckMCP")

@mcp.tool
def conexion_red() -> dict:
    """
    Diagnóstico rápido de red: DNS y salida HTTPS.
    - dns_ok: True si se resuelve api.coindesk.com
    - https_ok: True si se puede acceder a https://example.com
    - detalle: info extra de IP, status o errores
    """
    out = {"dns_ok": False, "https_ok": False, "detalle": {}}

    # Comprobación DNS
    try:
        ip = socket.gethostbyname("api.coindesk.com")
        out["dns_ok"] = True
        out["detalle"]["coindesk_ip"] = ip
    except Exception as e:
        out["detalle"]["dns_error"] = str(e)

    # Comprobación HTTPS
    try:
        r = requests.get("https://example.com", timeout=5)
        out["https_ok"] = (200 <= r.status_code < 400)
        out["detalle"]["https_status"] = r.status_code
    except Exception as e:
        out["detalle"]["https_error"] = str(e)

    return out

if __name__ == "__main__":
    mcp.run()
