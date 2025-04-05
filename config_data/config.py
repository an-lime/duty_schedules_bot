from dataclasses import dataclass
from environs import Env


@dataclass
class DataBase:
    LOGIN: str
    PASSWORD: str
    HOST: str
    PORT: str
    DATABASE: str

    def __post_init__(self):
        self.url = f'postgresql+asyncpg://{self.LOGIN}:{self.PASSWORD}@{self.HOST}:{self.PORT}/{self.DATABASE}'


@dataclass
class TgBot:
    BOT_TOKEN: str


@dataclass
class BotConfig:
    Bot: TgBot
    Database: DataBase


def load_config(path: str | None = None) -> BotConfig:
    env = Env()
    env.read_env(path)
    bot = TgBot(BOT_TOKEN=env('BOT_TOKEN'))
    database = DataBase(
        LOGIN=env('DB_LOGIN'),
        PASSWORD=env('DB_PASSWORD'),
        HOST=env('DB_HOST'),
        PORT=env('DB_PORT'),
        DATABASE=env('DATABASE'),
    )
    return BotConfig(Bot=bot, Database=database)
