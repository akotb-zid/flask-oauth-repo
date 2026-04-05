# Flask OAuth Example

<div align="center">

![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-2.x-000000?style=for-the-badge&logo=flask&logoColor=white)
![OAuth 2.0](https://img.shields.io/badge/OAuth-2.0-EB5424?style=for-the-badge&logo=auth0&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

A minimal Flask application demonstrating the **Zid OAuth 2.0** authorization flow.  
Users are redirected to Zid for authorization, and the resulting access token is displayed upon return.

> ⚠️ **Demo purposes only.** Tokens are stored in memory. For production, use a database and environment variables.

</div>

---

## 📋 Table of Contents

- [Features](#-features)
- [Prerequisites](#-prerequisites)
- [Quick Start](#-quick-start)
- [Configuration](#-configuration)
- [Usage](#-usage)
- [Routes](#-routes)
- [Project Structure](#-project-structure)
- [Security Notes](#-security-notes)
- [License](#-license)

---

## ✨ Features

- Simple OAuth 2.0 authorization code flow with Zid
- Minimal dependencies — just Flask and Requests
- Easy local testing via Ngrok
- Clean callback handling and token display

---

## 🔧 Prerequisites

- Python 3.8+
- [Ngrok](https://ngrok.com/) (for exposing your local server)
- A registered Zid app with a valid `client_id` and `client_secret`

---

## 🚀 Quick Start

### 1. Clone the repository

```bash
git clone https://github.com/akotb-zid/flask-oauth-repo.git
cd flask-oauth-repo
```

### 2. Install dependencies

```bash
pip install Flask requests
```

### 3. Configure your credentials

Open `app.py` and replace the placeholder values with your actual Zid app credentials and your Ngrok URL:

```python
CLIENT_ID     = 12345                                         # Your Zid app client ID
CLIENT_SECRET = 'mySecretKey'                                 # Your Zid app client secret
REDIRECT_URI  = 'https://abcd1234.ngrok.io/zid/callback'     # Your Ngrok callback URL
```

> **Example:** If your Ngrok URL is `https://abcd1234.ngrok.io`, your redirect URI becomes:  
> `https://abcd1234.ngrok.io/zid/callback`

---

## ⚙️ Configuration

Before you run anything, make sure the redirect and callback URLs are registered in your **Zid Partner Dashboard**.

| Setting | Value |
|---|---|
| Redirect URL | `https://<your-ngrok-url>/zid/redirect` |
| Callback URL | `https://<your-ngrok-url>/zid/callback` |

---

## 🏃 Usage

### Step 1 — Expose your local server with Ngrok

```bash
ngrok http 5000
```

Copy the generated `https://` URL (e.g., `https://abcd1234.ngrok.io`).

### Step 2 — Run the Flask app

```bash
python app.py
```

### Step 3 — Start the OAuth flow

Open your browser and navigate to:

```
https://<your-ngrok-url>/zid/redirect
```

After authorizing on Zid, you'll be redirected to the callback URL and your access token will be displayed.

---

## 🗺️ Routes

| Route | Method | Description |
|---|---|---|
| `/` | `GET` | Displays token data if available, or a welcome message |
| `/zid/redirect` | `GET` | Initiates the OAuth 2.0 authorization flow |
| `/zid/callback` | `GET` | Receives the authorization code and exchanges it for a token |

---

## 📁 Project Structure

```
flask-oauth-repo/
├── app.py          # Main Flask application
└── README.md       # This file
```

---

## 🔒 Security Notes

- **Never commit secrets to GitHub.** Use environment variables or a `.env` file (with [`python-dotenv`](https://pypi.org/project/python-dotenv/)) and add `.env` to your `.gitignore`.
- **In-memory token storage** is suitable for demos only. Use a proper database (e.g., PostgreSQL, Redis) in production.
- **Rotate your credentials** immediately if they are ever accidentally exposed.

---

## 📄 License

This project is licensed under the [MIT License](LICENSE) — free to use and modify.
