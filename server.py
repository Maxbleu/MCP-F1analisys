import uvicorn
from mcp_f1analisys.server.mcp_server import create_mcp_server

mcp = create_mcp_server()

http_app = mcp.http_app(path="/sse", transport="sse")

if __name__ == "__main__":
    uvicorn.run(http_app, host="::", port=8000)
