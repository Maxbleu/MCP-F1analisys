import requests, os

async def get_image(path: str) -> str:
    """Get image data from the F1 analysis API"""

    headers = {
        "Authorization": f"Bearer {os.getenv("JWT_TOKEN")}",
        "Content-Type": "application/json",
        "Accept": "application/json"
    }
    session = requests.Session()
    session.headers.update(headers)
    try:
        url = f"http://{os.getenv("F1ANALISYS_PRIVATE_NETWORK")}/api/analisys{path}"
        timeout = 10
        allow_redirects = True
        response = requests.get(
            url=url,
            headers=headers,
            timeout=timeout,
            allow_redirects=allow_redirects
        )
        response.raise_for_status()
        return response.json()["url"]
    except requests.exceptions.HTTPError as http_err:
        raise
    except requests.exceptions.RequestException as req_err:
        raise
    except ValueError as json_err:
        raise