import socket
from concurrent.futures import ThreadPoolExecutor
from colorama import Fore

def __start__():
    try:
        print(Fore.RED + " [!] Enter Website Address\n")
        target = input(Fore.RED + " ┌─[" + Fore.LIGHTGREEN_EX + "RRSEC" + Fore.BLUE + "~" + Fore.WHITE + "@ROOT" + Fore.RED + "/" + Fore.CYAN + "RR" + Fore.RED + "/" + Fore.LIGHTYELLOW_EX + "BertubiTubi" + Fore.RED + """]\n └──╼ """ + Fore.WHITE + "# ")
        main(target)
    except KeyboardInterrupt:
        print("\nExiting...")

def scan_port(ip, port):
    """Scan a single port on a given IP address."""
    scanner = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    scanner.settimeout(1)  # Timeout of 1 second for each port scan
    try:
        scanner.connect((ip, port))
        return port, True  # Port is open
    except:
        return port, False  # Port is closed
    finally:
        scanner.close()

def scan_ports(ip, ports, num_threads=100):
    """Scan multiple ports on a given IP address."""
    open_ports = []
    with ThreadPoolExecutor(max_workers=num_threads) as executor:
        results = executor.map(lambda p: scan_port(ip, p), ports)
        for port, is_open in results:
            if is_open:
                open_ports.append(port)
    return open_ports

def main(target):
    try:
        ports_to_scan = range(1, 1025)  # Example range of ports to scan (1-1024)
        
        ip = socket.gethostbyname(target)
        print(f"Scanning {target} ({ip})...")
        
        open_ports = scan_ports(ip, ports_to_scan)
        
        if open_ports:
            print(f"Open ports on {target} ({ip}):")
            for port in open_ports:
                print(f"Port {port} is open")
        else:
            print(f"No open ports found on {target} ({ip}) in the specified range.")
    except socket.gaierror:
        print("Invalid hostname. Please try again.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    __start__()
