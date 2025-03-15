from app import create_app
from app.config import Config

key_file = Config.SSL_KEY_PATH
cert_file = Config.SSL_CERT_PATH

app = create_app()

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True, ssl_context=(cert_file, key_file))

