"""
Google Sheets OAuth2 token refresh for agt_zavod.
Uses SA key from GOOGLE_SHEETS_SA env var (base64-encoded JSON).
Caches token for 55 minutes in workspace/runtime/gsheets_zavod_token.json
"""
import base64, json, time, os, sys

CACHE_PATH = os.path.join(os.path.dirname(__file__), '..', 'runtime', 'gsheets_zavod_token.json')
CACHE_PATH = os.path.normpath(CACHE_PATH)
TTL = 55 * 60


def load_cache():
    try:
        d = json.load(open(CACHE_PATH))
        if time.time() - d.get('ts', 0) < TTL:
            return d.get('tok')
    except Exception:
        pass
    return None


def save_cache(tok):
    os.makedirs(os.path.dirname(CACHE_PATH), exist_ok=True)
    json.dump({'tok': tok, 'ts': time.time()}, open(CACHE_PATH, 'w'))


def fetch_token():
    import requests
    from cryptography.hazmat.primitives import hashes, serialization
    from cryptography.hazmat.primitives.asymmetric import padding as apad

    raw = os.environ.get('GOOGLE_SHEETS_SA', '')
    if not raw:
        print('ERROR: GOOGLE_SHEETS_SA env not set', file=sys.stderr)
        sys.exit(1)

    padding = '=' * (-len(raw) % 4)
    sa = json.loads(base64.urlsafe_b64decode(raw + padding))

    now = int(time.time())

    def enc(obj):
        return base64.urlsafe_b64encode(
            json.dumps(obj, separators=(',', ':')).encode()
        ).rstrip(b'=').decode()

    header_b64 = enc({'alg': 'RS256', 'typ': 'JWT'})
    payload_b64 = enc({
        'iss': sa['client_email'],
        'scope': 'https://www.googleapis.com/auth/spreadsheets',
        'aud': sa['token_uri'],
        'iat': now,
        'exp': now + 3600,
    })
    to_sign = f'{header_b64}.{payload_b64}'

    pk = serialization.load_pem_private_key(sa['private_key'].encode(), password=None)
    sig_bytes = pk.sign(to_sign.encode(), apad.PKCS1v15(), hashes.SHA256())
    sig_b64 = base64.urlsafe_b64encode(sig_bytes).rstrip(b'=').decode()
    grant = f'{to_sign}.{sig_b64}'

    r = requests.post(sa['token_uri'],
                      data={'grant_type': 'urn:ietf:params:oauth:grant-type:jwt-bearer',
                            'assertion': grant},
                      timeout=15)
    data = r.json()
    tok = data.get('access_token')
    if not tok:
        print(f'ERROR from token endpoint: {data}', file=sys.stderr)
        sys.exit(1)
    return tok


cached = load_cache()
if cached:
    print('STATUS:cached')
    print(f'TOKEN:{cached}')
else:
    tok = fetch_token()
    save_cache(tok)
    print('STATUS:refreshed')
    print(f'TOKEN:{tok}')
