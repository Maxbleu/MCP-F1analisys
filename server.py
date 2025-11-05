import uvicorn, os
from mcp_f1analisys.server.mcp_server import create_mcp_server

mcp = create_mcp_server()

http_app = mcp.http_app(path="/sse", transport="sse")

if __name__ == "__main__":
    host = os.getenv("HOST", "::")
    port = int(os.getenv("PORT", "8000"))
    uvicorn.run(http_app, host=host, port=port)
