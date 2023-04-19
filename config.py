from dataclasses import dataclass
from environs import Env


@dataclass
class Api:
    api_token: str


@dataclass
class TgBot:
    token: str
    use_redis: bool


@dataclass
class Db:
    host: str
    password: str
    user: str
    database: str
    port: str


@dataclass
class CypherKey:
    key: str


@dataclass
class Config:
    api: Api
    bot: TgBot
    db: Db
    key: CypherKey


def load_config(path: str = None):
    env = Env()
    env.read_env(path)

    return Config(
        api=Api(
            api_token=env.str("TOKEN")
        ),
        bot=TgBot(
            token=env.str("BOT_TOKEN"),
            use_redis=env.bool("USE_REDIS")
        ),
        db=Db(
            host=env.str("DATABASE_HOST"),
            password=env.str("DATABASE_PASSWORD"),
            user=env.str("DATABASE_USER"),
            database=env.str("DATABASE_NAME"),
            port=env.str("DATABASE_PORT"),
        ),
        key=CypherKey(
            key=env.str("CIPHER_KEY")
        )
    )
