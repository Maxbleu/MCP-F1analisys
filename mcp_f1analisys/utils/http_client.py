import httpx, os

class F1AnalysisClient:
    def __init__(self):
        self.client = httpx.AsyncClient(
            base_url=f"http://f1analisys.railway.internal:8000/api/analisys",
            timeout=httpx.Timeout(30.0, connect=10.0),
            limits=httpx.Limits(max_keepalive_connections=5, max_connections=10),
            follow_redirects=True
        )
    
    async def get_image(self, path: str) -> bytes:
        """Get image data from the F1 analysis API"""
        response = await self.client.get(path)
        response.raise_for_status()
        data = response.json()
        return data["url"]
    
    async def close(self):
        """Close the HTTP client"""
        await self.client.aclose()