from environs import Env
import base64
env = Env()
env.read_env()

API_TOKEN = env.str("API_TOKEN")
WEBAPP_HOST = '0.0.0.0'
WEBAPP_PORT = env.int("PORT", 5000)
WEBHOOK_HOST = env.str("WEBHOOK_HOST", None)
WEBHOOK_PATH = f"/webhook/{API_TOKEN}"
WEBHOOK_URL = f"{WEBHOOK_HOST}{WEBHOOK_PATH}"
ADMINS = env.list("ADMINS", [])

