#!/usr/bin/env python3
"""Get Google OAuth2 access token from Service Account key (Finansy agent)."""
import json, time, base64, sys
import urllib.request, urllib.parse

SA_KEY_PATH = "/var/lib/private/teamon-clean/co_demo/users/usr_tg_6674981864/personal-agent/workspace/inbox/sheetsms-470810-6e08611f9f12.json"
SCOPE = "https://www.googleapis.com/auth/spreadsheets"

def b64url(data):
    if isinstance(data, str):
        data = data.encode()
    return base64.urlsafe_b64encode(data).rstrip(b"=").decode()

def get_token():
    with open(SA_KEY_PATH) as f:
        sa = json.load(f)

    now = int(time.time())
    header = b64url(json.dumps({"alg": "RS256", "typ": "JWT"}))
    payload = b64url(json.dumps({
        "iss": sa["client_email"],
        "scope": SCOPE,
        "aud": sa["token_uri"],
        "iat": now,
        "exp": now + 3600,
    }))
    signing_input = f"{header}.{payload}".encode()

    from cryptography.hazmat.primitives import hashes, serialization
    from cryptography.hazmat.primitives.asymmetric import padding

    private_key = serialization.load_pem_private_key(
        sa["private_key"].encode(), password=None
    )
    signature = private_key.sign(signing_input, padding.PKCS1v15(), hashes.SHA256())
    jwt_token = f"{header}.{payload}.{b64url(signature)}"

    data = urllib.parse.urlencode({
        "grant_type": "urn:ietf:params:oauth:grant-type:jwt-bearer",
        "assertion": jwt_token,
    }).encode()

    req = urllib.request.Request(sa["token_uri"], data=data,
                                  headers={"Content-Type": "application/x-www-form-urlencoded"})
    with urllib.request.urlopen(req, timeout=15) as resp:
        result = json.load(resp)

    print(result["access_token"])

if __name__ == "__main__":
    get_token()
