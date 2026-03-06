from dataclasses import dataclass


@dataclass(frozen=True)
class Settings:
    base_url: str = "https://dummyjson.com"
    timeout_seconds: float = 10.0


def get_settings() -> Settings:
    return Settings()
