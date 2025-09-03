from dotenv import load_dotenv
import os

load_dotenv()  # lee el archivo .env

client_id = os.getenv("SPOTIFY_CLIENT_ID")
secret_id = os.getenv("SPOTIFY_SECRET_ID")
refresh_token = os.getenv("SPOTIFY_REFRESH_TOKEN")

print(client_id, secret_id, refresh_token)