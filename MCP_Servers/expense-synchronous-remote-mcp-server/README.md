python -m venv venv
venv\Scripts\activate
uv run --active python main.py
npx @modelcontextprotocol/inspector http://127.0.0.1:8000/mcp
Transport Type : Streamable HTTP
URL : http://127.0.0.1:8000/mcp