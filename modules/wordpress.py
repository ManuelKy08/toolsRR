import requests
from bs4 import BeautifulSoup

# Function to scan a URL
def scan_url(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            print(f"Scanning {url}...")
            # Example: Retrieve server headers
            print("\nServer headers:")
            print("----------------")
            for header, value in response.headers.items():
                print(f"{header}: {value}")

            # Example: Analyze text content in HTML
            soup = BeautifulSoup(response.text, 'html.parser')
            # Example: Find <form> tags to look for potential security issues
            forms = soup.find_all('form')
            if forms:
                print("\nForms found:")
                for form in forms:
                    print(form)

            # Implement more relevant security checks here
        else:
            print(f"Failed to retrieve {url}: Status code {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Error scanning {url}: {str(e)}")

# Main program
if __name__ == "__main__":
    target_url = input("Enter the target URL (e.g., https://example.com): ").strip()
    scan_url(target_url)
