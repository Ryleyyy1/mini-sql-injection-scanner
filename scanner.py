import requests

def load_payloads(file_path):
    with open(file_path, "r") as file:
        return file.read().splitlines()

def scan_url(url, param, payloads):
    print(f"[+] Scanning: {url}")
    for payload in payloads:
        test_payload = payload
        params = {param: test_payload}

        try:
            response = requests.get(url, params=params, timeout=5)

            if "syntax" in response.text.lower() or "mysql" in response.text.lower():
                print(f"[!!!] Possible SQL Injection Found!")
                print(f"Payload: {payload}\n")
            else:
                print(f"[-] Tested payload: {payload}")

        except requests.exceptions.RequestException as e:
            print(f"[ERROR] {e}")

if __name__ == "__main__":
    target_url = input("Target URL (without params): ")
    parameter = input("Parameter name (e.g. id): ")
    payload_file = "payloads.txt"

    payloads = load_payloads(payload_file)
    scan_url(target_url, parameter, payloads)
