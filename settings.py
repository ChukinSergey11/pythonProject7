from dataclasses import dataclass
from environs import Env
@dataclass()
class Bots:
    not_token:str
    admin_id:str
    post_channel:str
    you_kassa_token:str

@dataclass()
class Db:
    redis:str
    user:str
    host:str
    password:str
    db:str

@dataclass()
class Settings:
    bots:Bots
    db:Db


def get_settings(path:str):
    env=Env()
    env.read.env(path)

    return Settings(
        bots=Bots(
            bot_token=env.str("BOT_TOKEN"),
            admin_id=env.str("ADMIN_ID"),
            post_channel=env.str("POSTING_CHANNEL"),
            you_kassa_token=env.str("YOUKASSA_TOKEN")
        ),
        db=Db(
            redis=env.str("DB_REDIS_DNS"),
            user=env.str("DB_USER"),
            host=env.str("DB_HOST"),
            password=env.str("DB_PASSWORD"),
            db=env.str("DB_DATABASE")
        )
    )

settings=get_settings('input')
print(settings)

