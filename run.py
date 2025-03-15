from app import create_app
from app.config import Config

app = create_app()

if __name__ == "__main__":
    if Config.SSL_ENABLED and Config.SSL_CERT_PATH and Config.SSL_KEY_PATH:
        app.run(
            host='0.0.0.0',
            port=5000,  # Keep using port 5000 or change to 443 if preferred
            ssl_context=(Config.SSL_CERT_PATH, Config.SSL_KEY_PATH)
        )
    else:
        app.run(host='0.0.0.0', port=5000)

