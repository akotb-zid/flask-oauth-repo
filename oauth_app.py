# app.py
from flask import Flask, redirect, request, jsonify, render_template_string, session
import requests
from urllib.parse import urlencode
import json  # <- needed for json.dumps

app = Flask(__name__)
app.secret_key = 'supersecretkey'

# === Zid OAuth Configuration ===
CLIENT_ID = 00000  # Add your actual client ID as INTEGER
CLIENT_SECRET = 'CLIENT_SECRET'  # Add your actual client secret as STRING
REDIRECT_URI = 'NGROK_URL/zid/callback' # Callback url from the ngrok
AUTH_URL = 'https://oauth.zid.sa/oauth/authorize'
TOKEN_URL = 'https://oauth.zid.sa/oauth/token'

# Temporary storage for token (for demo; use DB in production)
store_tokens = {}


@app.route('/')
def home():
    token_data = store_tokens.get('token_data')
    if token_data:
        return jsonify(token_data)
    return jsonify({'message': 'Welcome!'})


# Redirect route
@app.route('/zid/redirect')
def zid_oauth_redirect():
    """Redirect merchant to Zid OAuth authorization page"""
    params = {
        'client_id': CLIENT_ID,
        'redirect_uri': REDIRECT_URI,
        'response_type': 'code',
    }
    url = f"{AUTH_URL}?{urlencode(params)}"
    print("Redirecting to Zid OAuth URL:", url)
    return redirect(url)

# Callback route
@app.route('/zid/callback')
def zid_oauth_callback():
    """Receive authorization code and exchange it for tokens"""
    code = request.args.get('code')
    if not code:
        return "Authorization code not found", 400

    payload = {
        'grant_type': 'authorization_code',
        'client_id': CLIENT_ID,
        'client_secret': CLIENT_SECRET,
        'redirect_uri': REDIRECT_URI,
        'code': code,
    }

    response = requests.post(TOKEN_URL, data=payload)
    if not response.ok:
        return jsonify({
            'error': 'Token request failed',
            'status_code': response.status_code,
            'response': response.text
        }), 400

    token_data = response.json()  # <- this is inside the function
    store_tokens['token_data'] = token_data  # Save to temp storage
    session['token_data'] = token_data       # Save to user session

    # Pretty print JSON for display
    pretty_json = json.dumps(token_data, indent=4)

    html_content = f"""
    <html>
        <head><title>Zid OAuth Success</title></head>
        <body>
            <h2>Zid OAuth Authorized Successfully!</h2>
            <pre>{pretty_json}</pre>
            <a href="/">Go Home</a>
        </body>
    </html>
    """
    return render_template_string(html_content)

if __name__ == '__main__':
    app.run(debug=True)
