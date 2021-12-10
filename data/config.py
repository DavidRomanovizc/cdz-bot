from environs import Env

# Теперь используем вместо библиотеки python-dotenv библиотеку environs
env = Env()
env.read_env()

BOT_TOKEN = env.str("BOT_TOKEN")  # Забираем значение типа str
ADMINS = env.list("ADMINS")  # Тут у нас будет список из админов
IP = env.str("ip")  # Тоже str, но для айпи адреса хоста

DB_USER = env.str('DB_USER')
DB_PASS = env.str('DB_PASS')
DB_HOST = env.str('DB_HOST')
DB_NAME = env.str('DB_NAME')


API_ACCESS_TOKEN = env.str("api_access_token")
PHONE_NUMBER = env.str("phone_number")
SecretP2 = env.str("secret_p2p")

UTOKEN = env.str("yootoken")