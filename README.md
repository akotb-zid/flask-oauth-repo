````markdown
# Flask OAuth Example

## Description
A simple Flask app demonstrating Zid OAuth 2.0.  
It redirects users to Zid for authorization and displays the access token.

⚠️ **Demo only** — tokens are stored in memory. For production, use a database and environment variables.

---

## Quick Start

### Clone the repository
```bash
git clone https://github.com/akotb-zid/flask-oauth-repo.git
cd flask-oauth-repo
````

### Install dependencies

```bash
pip install Flask requests
```

### Edit `app.py`

Replace with your Zid credentials and Ngrok URL:

```python
CLIENT_ID = 12345                # Your Zid app client ID
CLIENT_SECRET = 'mySecretKey'    # Your Zid app client secret
REDIRECT_URI = 'https://abcd1234.ngrok.io/zid/callback'  # Ngrok callback URL
```

**Example:**
If your Ngrok URL is `https://abcd1234.ngrok.io`, your redirect URL becomes:
`https://abcd1234.ngrok.io/zid/callback`

---

## Usage

### Start Ngrok to expose your local server

```bash
ngrok http 5000
```

### Create the OAuth URLs using your Ngrok URL

```
YOUR_NGROK_URL/zid/redirect
YOUR_NGROK_URL/zid/callback
```

**Example with Ngrok URL `https://abcd1234.ngrok.io`:**

```
https://abcd1234.ngrok.io/zid/redirect
https://abcd1234.ngrok.io/zid/callback
```

### Add these URLs in the partner dashboard when installing the app

* `/zid/redirect` → starts the OAuth flow
* `/zid/callback` → receives the authorization code and exchanges it for a token

### Run the Flask app

```bash
python app.py
```

### Start the OAuth flow in your browser

```
YOUR_NGROK_URL/zid/redirect
```

After authorization, you’ll be redirected to the callback URL and see your token.

---

## Notes

* Tokens are stored in memory — use a database in production.
* Never commit your secrets to github.

---

## Routes

| Route           | Description                               |
| --------------- | ----------------------------------------- |
| `/`             | Shows token data or a welcome message     |
| `/zid/redirect` | Starts the OAuth authorization flow       |
| `/zid/callback` | Receives the authorization code and token |

---

## License

MIT License — free to use and modify.

```
```
