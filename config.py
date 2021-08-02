from dotenv import dotenv_values


def env_get(key: str):
    env = dotenv_values(".env")
    if not env:
        raise ValueError("No .env file found")
    return env.get(key)


class Config(object):
    SECRET_KEY = env_get("SECRET_KEY")
    MONGODB_HOST = env_get("MONGODB_HOST")
    MONGODB_PORT = int(env_get("MONGODB_PORT"))
    MONGODB_DB = env_get("MONGODB_DB")
    if not SECRET_KEY:
        raise ValueError("No SECRET_KEY set for Flask application")


class DevelopmentConfig(Config):
    DEBUG = True
    TESTING = True


class ProductionConfig(Config):
    DEBUG = False
    TESTING = False
    env_prod = dotenv_values(".env.prod")
    if env_prod:
        SECRET_KEY = env_prod["SECRET_KEY"] if env_prod.get("SECRET_KEY") else Config.SECRET_KEY
        DEBUG = env_prod["DEBUG"] if env_prod.get("DEBUG") else DEBUG
        TESTING = env_prod["TESTING"] if env_prod.get("TESTING") else TESTING
