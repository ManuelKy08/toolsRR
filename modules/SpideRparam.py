import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse, parse_qs
from collections import defaultdict
from colorama import Fore

def __start__():
    try:
        print(Fore.RED + " [!] Enter Target URL\n")
        target_url = input(Fore.RED + " ┌─[" + Fore.LIGHTGREEN_EX + "RRSEC" + Fore.BLUE + "~" + Fore.WHITE + "@ROOT" + Fore.RED + "/" + Fore.CYAN + "RR" + Fore.RED + "/" + Fore.LIGHTYELLOW_EX + "URL-Parameter-Scanner" + Fore.RED + """]\n └──╼ """ + Fore.WHITE + "# ")
        main(target_url)
    except KeyboardInterrupt:
        print("\nExiting...")

def get_urls_from_page(url):
    try:
        response = requests.get(url, timeout=5)
        soup = BeautifulSoup(response.content, "html.parser")
        return [urljoin(url, link.get('href')) for link in soup.find_all('a', href=True)]
    except requests.RequestException as e:
        print(f"Failed to retrieve URLs from {url}: {e}")
        return []

def find_url_parameters(urls):
    params = defaultdict(list)
    for url in urls:
        parsed_url = urlparse(url)
        query_params = parse_qs(parsed_url.query)
        for param, value in query_params.items():
            params[param].extend(value)
    return params

def main(target_url):
    try:
        print(f"Scanning {target_url} for URL parameters...\n")
        
        urls_to_scan = [target_url]
        seen_urls = set()

        while urls_to_scan:
            current_url = urls_to_scan.pop(0)
            if current_url in seen_urls:
                continue
            seen_urls.add(current_url)
            print(f"Scanning {current_url}...")
            urls_on_page = get_urls_from_page(current_url)
            urls_to_scan.extend(urls_on_page)
        
        url_parameters = find_url_parameters(seen_urls)
        
        print("\nScan complete. Found the following URL parameters:")
        for param, values in url_parameters.items():
            print(f"{param}: {values}")

    except requests.RequestException as e:
        print(f"Failed to connect to {target_url}: {e}")
    except Exception as ex:
        print(f"An error occurred: {ex}")

if __name__ == "__main__":
    __start__()
