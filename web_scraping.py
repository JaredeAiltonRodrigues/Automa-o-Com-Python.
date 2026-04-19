import httpx
from bs4 import BeautifulSoup

def scrape_vagas(url: str) -> list[dict]:
    resp = httpx.get(url, headers={"User-Agent": "Mozilla/5.0"})
    soup = BeautifulSoup(resp.text, "html.parser")

    return [
        {
            "titulo": vaga.select_one(".title").text.strip(),
            "empresa": vaga.select_one(".company").text.strip(),
        }
        for vaga in soup.select(".job-card")
    ]
