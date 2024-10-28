import urllib.request
import json
from typing import Optional

class Brewery:
    def __init__(self, id: str, name: str, brewery_type: str, city: str, state: Optional[str], country: str,
                 website_url: Optional[str]):
        self.id = id
        self.name = name
        self.brewery_type = brewery_type
        self.city = city
        self.state = state
        self.country = country
        self.website_url = website_url

    def __str__(self):
        return (f"id: {self.id}\n"
                f"nazwa: {self.name}\n"
                f"typ: {self.brewery_type}\n"
                f"miejsce: {self.city}, {self.state if self.state else ''}, {self.country}\n"
                f"url: {self.website_url if self.website_url else 'brak'}\n")


def fetch_breweries():
    url = "https://api.openbrewerydb.org/v1/breweries?per_page=20"

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
    }

    req = urllib.request.Request(url, headers=headers)

    try:
        with urllib.request.urlopen(req) as response:
            data = response.read().decode('utf-8')
            return json.loads(data)
    except urllib.error.URLError as e:
        print(f"Błąd podczas pobierania danych: {e}")
        return []


def main():
    breweries_data = fetch_breweries()

    breweries = [Brewery(brewery['id'],
                         brewery['name'],
                         brewery['brewery_type'],
                         brewery['city'],
                         brewery.get('state'),
                         brewery['country'],
                         brewery.get('website_url')) for brewery in breweries_data]

    for brewery in breweries:
        print(brewery)

if __name__ == "__main__":
    main()
