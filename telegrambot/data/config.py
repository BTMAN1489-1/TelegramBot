from environs import Env
import base64
env = Env()
env.read_env()

API_TOKEN = env.str("API_TOKEN")
WEBAPP_HOST = '0.0.0.0'
WEBAPP_PORT = env.int("PORT", 5000)
WEBHOOK_HOST = env.str("WEBHOOK_HOST", None)
URL_SAFE_TOKEN = base64.standard_b64encode(API_TOKEN.encode("utf-8")).decode("utf-8")
WEBHOOK_PATH = f"/webhook/{URL_SAFE_TOKEN}"
WEBHOOK_URL = f"https://{WEBHOOK_HOST}{WEBHOOK_PATH}"
ADMINS = env.list("ADMINS", [])

