# Servidores-MCP  
Servidores MCP creados con [FastMCP](https://pypi.org/project/fastmcp/) en el taller **"Crea tu primer servidor MCP con Python y FastMCP"**.  

Este repo incluye ejemplos de servidores MCP que exponen funciones como herramientas (`tools`) accesibles desde clientes MCP (ej. Claude Desktop, Open WebUI).  

- 📈 **BitcoinMCP** → devuelve el precio actual de BTC en USD.  
- 🌦 **ClimaMCP** → consulta el clima en tiempo real de una ciudad.  
- 🖥 **RedMCP** → utilidades básicas del sistema (procesos, logs, etc.).  

---

## 🚀 Requisitos
- Python 3.10+  
- `pip` actualizado  
- (Opcional) `node` / `npm` si quieres usar [MCP Inspector](https://www.npmjs.com/package/@modelcontextprotocol/inspector)  

---

## 📂 Estructura del proyecto
```

Servidores-MCP/
├─ bitcoin.py
├─ clima.py
├─ red.py
├─ requirements.txt
└─ README.md

````

---

## ⚙️ Instalación
1. Clona el repositorio:
   ```bash
   git clone https://github.com/jmatias2411/Servidores-MCP.git
   cd Servidores-MCP
    ````

2. Crea un entorno virtual e instala dependencias:

   ```bash
   python -m venv .venv
   source .venv/bin/activate   # Linux/macOS
   .\.venv\Scripts\Activate.ps1 # Windows PowerShell

   pip install --upgrade pip
   pip install -r requirements.txt
   ```

El `requirements.txt` contiene:

```
fastmcp
requests
pandas
```

---

## ▶️ Ejecutar los servidores

Cada archivo levanta un servidor MCP distinto.

### BitcoinMCP

```bash
python bitcoin.py
```

### ClimaMCP

```bash
python clima.py
```

### RedMCP

```bash
python red.py
```

Cuando un servidor corre, verás logs tipo:

```
FastMCP Starting server: BitcoinMCP
Tools: ['precio_bitcoin']
```

---

## 🔍 Probar con MCP Inspector

[MCP Inspector](https://www.npmjs.com/package/@modelcontextprotocol/inspector) es como el Postman de MCP: permite ver y ejecutar tus tools antes de conectarlas a un LLM.

Instalación:

```bash
npm install -g @modelcontextprotocol/inspector
```

Ejemplo:

```bash
mcp-inspector python bitcoin.py
```

Se abrirá una UI en tu navegador con:

* Lista de tools
* Formularios para enviar parámetros
* Respuestas JSON en tiempo real

---

## 🤖 Conectar con un cliente MCP

Ejemplo de configuración (`mcp_servers.json`) para Claude Desktop u Open WebUI:

```json
{
  "servers": {
    "BitcoinMCP": {
      "command": "python",
      "args": ["bitcoin.py"]
    },
    "ClimaMCP": {
      "command": "python",
      "args": ["clima.py"]
    },
    "RedMCP": {
      "command": "python",
      "args": ["red.py"]
    }
  }
}
```

Coloca este archivo en la carpeta de configuración del cliente y reinicia.

---

## ✅ Buenas prácticas

* Añade **type hints** a tus tools → FastMCP genera automáticamente validación con JSON Schema.
* No expongas comandos de sistema sin validación (`shell=True` es peligroso).
* Limita tamaños de respuesta (ej. logs grandes).
* Usa `mcp-inspector` para probar antes de conectar a un LLM real.

---

## 🛠 Troubleshooting rápido

* **No aparecen tools en Inspector** → revisa que la función tenga `@tool` y type hints.
* **`python: command not found`** → usa la ruta absoluta al ejecutable del venv.
* **Error de permisos en RedMCP** → asegúrate de tener permisos adecuados en tu sistema.

---

## 📜 Licencia

Uso libre con fines educativos. 🚀

