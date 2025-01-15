from environs import Env

env = Env()
env.read_env()

# telegram bot token
TOKEN = env.str("7628087790:AAEk1UPEaEWl7sshWhhDNeZI4BcwH0XyS_4")

# postgres connection
USER_POSTGRES = env.str("USER_POSTGRES")
PASSWORD_POSTGRES = env.str("PASSWORD_POSTGRES")
HOST_POSTGRES = env.str("HOST_POSTGRES")
PORT_POSTGRES = env.str("PORT_POSTGRES")
DATABASE_POSTGRES = env.str("DATABASE_POSTGRES")

# file with command /start
START_FILE_ID = env.str("START_FILE_ID")

# chat to forward photo user
FORWARD_CHAT_ID = None

# admin list
ADMINS = [813415126, 5773913054]
