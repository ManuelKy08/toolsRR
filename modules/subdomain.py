from colorama import Fore, init
import requests
from concurrent.futures import ThreadPoolExecutor, as_completed

init(autoreset=True)

# List of common subdomains
subdomains = [
    'www', 'mail', 'ftp', 'localhost', 'webmail', 'smtp', 'webdisk', 'cpanel', 'whm', 
    'autodiscover', 'autoconfig', 'admin', 'test', 'blog', 'shop', 'api', 'dev', 'staging'
]

# Function to check each subdomain
def check_subdomain(domain, subdomain):
    url = f"http://{subdomain}.{domain}"
    try:
        response = requests.get(url, timeout=3)
        if response.status_code == 200:
            return url
    except requests.RequestException:
        return None

# Main function to find valid subdomains
def find_subdomains(domain):
    valid_subdomains = []
    with ThreadPoolExecutor(max_workers=10) as executor:
        future_to_subdomain = {executor.submit(check_subdomain, domain, subdomain): subdomain for subdomain in subdomains}
        for future in as_completed(future_to_subdomain):
            subdomain = future_to_subdomain[future]
            try:
                result = future.result()
                if result:
                    print(f"Valid subdomain found: {result}")
                    valid_subdomains.append(result)
            except Exception as exc:
                print(f"{subdomain}.{domain} generated an exception: {exc}")
    return valid_subdomains

def __start__():
    try:
        print(Fore.RED + " [!] Enter Target Domain\n")
        domain = input(Fore.RED + " ┌─[" + Fore.LIGHTGREEN_EX + "RRSEC" + Fore.BLUE + "~" + Fore.WHITE + "@ROOT" + Fore.RED + "/" + Fore.CYAN + "RR" + Fore.RED + "/" + Fore.LIGHTYELLOW_EX + "Subdomain-Finder" + Fore.RED + """]\n └──╼ """ + Fore.WHITE + "# ")
        print(f"Scanning {domain} for subdomains...\n")
        found_subdomains = find_subdomains(domain)
        print("\nScan complete. Found the following valid subdomains:")
        for subdomain in found_subdomains:
            print(subdomain)
    except KeyboardInterrupt:
        print("\nExiting...")

if __name__ == "__main__":
    __start__()
