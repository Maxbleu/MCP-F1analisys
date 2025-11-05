import httpx, os

class F1AnalysisClient:
    def __init__(self):
        self._client = None
        self._base_url = None
    
    @property
    def client(self):
        if self._client is None:
            private_network = os.getenv("PRIVATE_NETWORK")
            self._base_url = f"http://{private_network}/api/analisys"
            self._client = httpx.AsyncClient(
                base_url=self._base_url,
                timeout=httpx.Timeout(30.0, connect=10.0),
                limits=httpx.Limits(max_keepalive_connections=5, max_connections=10),
                follow_redirects=True
            )
        return self._client
    
    async def get_image(self, path: str) -> bytes:
        """Get image data from the F1 analysis API"""
        client = self.client
        response = await client.get(path)
        response.raise_for_status()
        data = response.json()
        return data["url"]
    
    async def close(self):
        """Close the HTTP client"""
        if self._client:
            await self._client.aclose()