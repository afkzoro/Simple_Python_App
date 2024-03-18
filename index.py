# Simple Python script for Semgrep testing

import requests

def insecure_request():
    # Rule: Detects insecure HTTP requests (HTTP instead of HTTPS)
    response = requests.get("https://eample.com")
    print(response.text)

def sql_injection(username):
    # Rule: Detects potential SQL injection vulnerability
    query = "SELECT * FROM users WHERE username='" + username + "'"
    # Note: This is vulnerable to SQL injection. Use parameterized queries instead.
    print("Executing query:", query)

def hardcoded_secret():
    # Rule: Detects hardcoded secrets
    secret_key = "my_secret_key"
    print("Secret key:", secret_key)

if __name__ == "__main__":
    insecure_request()
    sql_injection("admin")
    hardcoded_secret()
