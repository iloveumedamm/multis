from os import getenv
from dotenv import load_dotenv

load_dotenv("config.env")


class Telegram:
    API_ID = int(getenv("API_ID", "19117812"))
    API_HASH = getenv("API_HASH", "9253698d3f30a0bd779ba321744a6076")
    BOT_TOKEN = getenv("BOT_TOKEN", "7113839904:AAHPLKgjlgEeM5ho0LN0IdFBqgAJr436D0I")
    PORT = int(getenv("PORT", 6762))
    BASE_URL = getenv("BASE_URL", "https://cinemanearme.online").rstrip('/')
    SESSION_STRING = getenv("SESSION_STRING", "BQEjtvQAcGecG8xv4vKw5k8q7sHMBo_ST_lWlyKBA1PTCWDPrCGcpUEdXBo4w1oN7Tdq-cbL8mdvuY80A4kQgxy8_rqCRAWBfSGXglxikoZVgwdK8DeRlfOFjrvTQmumgGWHd33cS-6OLWjuwL3F5nK0gr6FrcMxdb74O7t-RM7fo11th1-V30iGxudWDHSH-VnF_dxARGZnTHpRfMc1p9jhZ3VmjyfmxIXKG9g8W_qawo9s0P_fe6P19HfFeUXjqTzAsCyRshljIcvPnOC4kNUW0_wz7jLm58cA8fRxesOi-Oyqgo3Y6MOVXCvOoISvuyoNy7b7ufe36cqQQOcEUuPuPIJRlwAAAAGJPQdCAA")
    DATABASE_URL = getenv("DATABASE_URL", "mongodb+srv://lajihi2115:lgAEiuZHs917nZgy@cluster0.lx88eg8.mongodb.net/?retryWrites=true&w=majority")
    AUTH_CHANNEL = [channel.strip()
                    for channel in getenv("AUTH_CHANNEL", "-1002040445051").split(",")]
    THEME = getenv("THEME", "quartz").lower()
    USERNAME = getenv("USERNAME", "admin")
    PASSWORD = getenv("PASSWORD", "admin")
    ADMIN_USERNAME = getenv("ADMIN_USERNAME", "surfTG")
    ADMIN_PASSWORD = getenv("ADMIN_PASSWORD", "surfTG")
    SLEEP_THRESHOLD = int(getenv("SLEEP_THRESHOLD", "60"))
    WORKERS = int(getenv("WORKERS", "10"))
    MULTI_CLIENT = bool(getenv("MULTI_CLIENT", "True"))
    USE_CACHE = bool(getenv("USE_CACHE", "True"))
    HIDE_CHANNEL = bool(getenv("HIDE_CHANNEL", ""))
