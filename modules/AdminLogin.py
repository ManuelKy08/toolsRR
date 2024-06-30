import sys
import requests
from colorama import Fore
import sys
def __start__():
    print(""" [!] Welcome To The Admin Login Asshole

[!] Please Enter The Target Website Address\n""")
    site = input(Fore.RED+" ┌─["+Fore.LIGHTGREEN_EX+"RRSEC"+Fore.BLUE+"~"+Fore.WHITE+"@ROOT"+Fore.RED+"/"+Fore.CYAN+"RR"+Fore.RED+"/"+Fore.LIGHTYELLOW_EX+"Admin-Login"+Fore.RED+"""]
 └──╼ """+Fore.WHITE+"# ")
    if site == "":
        try:
            target_url = input("Enter the target URL (e.g., https://example.com): ").strip()
        except Exception as e:
            print(f"Error occurred: {e}")
            sys.exit(1)

        # Data jalur admin yang umum digunakan
        admin_paths = [
            'admin/', 'administrator/', 'login.php', 'administration/', 'admin1/', 'admin2/', 'admin3/', 'admin4/', 'admin5/',
            'moderator/', 'webadmin/', 'adminarea/', 'bb-admin/', 'adminLogin/', 'admin_area/', 'panel-administracion/',
            'instadmin/', 'memberadmin/', 'administratorlogin/', 'adm/', 'account.asp', 'admin/account.asp', 'admin/index.asp',
            'admin/login.asp', 'admin/admin.asp', '/login.aspx', 'admin_area/admin.asp', 'admin_area/login.asp',
            'admin/account.html', 'admin/index.html', 'admin/login.html', 'admin/admin.html', 'admin_area/admin.html',
            'admin_area/login.html', 'admin_area/index.html', 'admin_area/index.asp', 'bb-admin/index.asp', 'bb-admin/login.asp',
            'bb-admin/admin.asp', 'bb-admin/index.html', 'bb-admin/login.html', 'bb-admin/admin.html', 'admin/home.html',
            'admin/controlpanel.html', 'admin.html', 'admin/cp.html', 'cp.html', 'administrator/index.html', 'administrator/login.html',
            'administrator/account.html', 'administrator.html', 'login.html', 'modelsearch/login.html', 'moderator.html',
            'moderator/login.html', 'moderator/admin.html', 'account.html', 'controlpanel.html', 'admincontrol.html', 'admin_login.html',
            'panel-administracion/login.html', 'admin/home.asp', 'admin/controlpanel.asp', 'admin.asp', 'pages/admin/admin-login.asp',
            'admin/admin-login.asp', 'admin-login.asp', 'admin/cp.asp', 'cp.asp', 'administrator/account.asp', 'administrator.asp',
            'acceso.asp', 'login.asp', 'modelsearch/login.asp', 'moderator.asp', 'moderator/login.asp', 'administrator/login.asp',
            'moderator/admin.asp', 'controlpanel.asp', 'admin/account.html', 'adminpanel.html', 'webadmin.html', 'administration',
            'pages/admin/admin-login.html', 'admin/admin-login.html', 'webadmin/index.html', 'webadmin/admin.html', 'webadmin/login.html',
            'user.asp', 'user.html', 'admincp/index.asp', 'admincp/login.asp', 'admincp/index.html', 'admin/adminLogin.html',
            'adminLogin.html', 'admin/adminLogin.html', 'home.html', 'adminarea/index.html', 'adminarea/admin.html', 'adminarea/login.html',
            'panel-administracion/index.html', 'panel-administracion/admin.html', 'modelsearch/index.html', 'modelsearch/admin.html',
            'admin/admin_login.html', 'admincontrol/login.html', 'adm/index.html', 'adm.html', 'admincontrol.asp', 'admin/account.asp',
            'adminpanel.asp', 'webadmin.asp', 'webadmin/index.asp', 'webadmin/admin.asp', 'webadmin/login.asp', 'admin/admin_login.asp',
            'admin_login.asp', 'panel-administracion/login.asp', 'adminLogin.asp', 'admin/adminLogin.asp', 'home.asp', 'admin.asp',
            'adminarea/index.asp', 'adminarea/admin.asp', 'adminarea/login.asp', 'admin-login.html', 'panel-administracion/index.asp',
            'panel-administracion/admin.asp', 'modelsearch/index.asp', 'modelsearch/admin.asp', 'administrator/index.asp',
            'admincontrol/login.asp', 'adm/admloginuser.asp', 'admloginuser.asp', 'admin2.asp', 'admin2/login.asp', 'admin2/index.asp',
            'adm/index.asp', 'adm.asp', 'affiliate.asp', 'adm_auth.asp', 'memberadmin.asp', 'administratorlogin.asp', 'siteadmin/login.asp',
            'siteadmin/index.asp', 'siteadmin/login.html', 'memberadmin/', 'administratorlogin/', 'adm/', 'admin/account.php', 'admin/index.php',
            'admin/login.php', 'admin/admin.php', 'admin/account.php', 'admin_area/admin.php', 'admin_area/login.php', 'siteadmin/login.php',
            'siteadmin/index.php'
        ]

        # Meminta input URL target dari pengguna
        target_url = input("Enter the target URL (e.g., https://example.com): ").strip()

        # Memastikan URL memiliki skema
        if not target_url.startswith("http://") and not target_url.startswith("https://"):
            target_url = "http://" + target_url

        print(f"Scanning {target_url} for admin login pages...\n")

        # Fungsi untuk memeriksa apakah halaman admin ada
        def check_admin_path(url, paths):
            for path in paths:
                full_url = f"{url.rstrip('/')}/{path}"
                try:
                    response = requests.get(full_url)
                    if response.status_code == 200:
                        print(f"Found admin login page: {full_url}")
                    else:
                        print(f"Checked: {full_url} (Status code: {response.status_code})")
                except requests.RequestException as e:
                    print(f"Failed to access {full_url}: {e}")

        # Memanggil fungsi untuk memeriksa halaman admin
        check_admin_path(target_url, admin_paths)

        print("\nScan complete.")

if __name__ == "__main__":
    __start__()
