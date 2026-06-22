from flask import Flask, redirect, request, jsonify
from urllib.parse import urlencode
import requests

# SETUP CHECKLIST:
# [ ] Register app in Zid Partner Dashboard
# [ ] Copy Client ID and Secret into this file
# [ ] Start ngrok: ngrok http 5000
# [ ] Paste the HTTPS ngrok URL into NGROK_URL below (no trailing slash!)
# [ ] In Partner Dashboard, 
# [ ] set Callback URL to: {NGROK_URL}/zid/callback -> https://unemotive-susanne-unscanned.ngrok-free.dev/zid/callback
# [ ] set Redirection URL to: {NGROK_URL}/zid/redirect -> https://unemotive-susanne-unscanned.ngrok-free.dev/zid/redirect
# [ ] Run: python app.py



app = Flask(__name__)

# === Zid OAuth Config ===
# IMPORTANT: redirect_uri must match the callback URL in Partner Dashboard EXACTLY 
# (including protocol, domain, path, and trailing slashes)


# Configruable
NGROK_URL = 'ADD_HERE' # Example https://unemotive-susanne-unscanned.ngrok-free.dev
CLIENT_ID = 0000
CLIENT_SECRET = 'YOUR_CLIENT_Secret'



# Keep without changing
REDIRECT_URI = f'{NGROK_URL}/zid/callback'
AUTH_URL = 'https://oauth.zid.sa/oauth/authorize'
TOKEN_URL = 'https://oauth.zid.sa/oauth/token'

# Temporary token storage (replace with DB in production)
tokens = {}


@app.route('/')
def home():
    return {
        'redirect_url': f'https://{request.host}/zid/redirect',
        'callback_url': f'https://{request.host}/zid/callback'
    }


@app.route('/zid/redirect')
def zid_auth():
    """Step 1: Redirect merchant to Zid authorization page"""
    return redirect(f"{AUTH_URL}?{urlencode({
        'client_id': CLIENT_ID,
        'redirect_uri': REDIRECT_URI,
        'response_type': 'code'
    })}")


@app.route('/zid/callback')
def zid_callback():
    """Step 2: Exchange authorization code for access token"""
    code = request.args.get('code')
    if not code:
        return jsonify(error='Authorization code missing'), 400

    resp = requests.post(TOKEN_URL, data={
        'grant_type': 'authorization_code',
        'client_id': CLIENT_ID,
        'client_secret': CLIENT_SECRET,
        'redirect_uri': REDIRECT_URI,
        'code': code
    })

    if not resp.ok:
        return jsonify(error='Token request failed', details=resp.text), resp.status_code

    tokens['data'] = resp.json()
    return jsonify(tokens['data'])


if __name__ == '__main__':
    app.run(debug=True)