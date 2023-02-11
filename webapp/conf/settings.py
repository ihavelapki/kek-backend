from pydantic import BaseSettings


class Settings(BaseSettings):
    server_host: str = '127.0.0.1'
    server_port: int = 5000
    database_url: str = 'sqlite:///./database_2.sqlite3'


settings = Settings(_env_file=r"etc/.env", _env_file_encoding='utf-8')
