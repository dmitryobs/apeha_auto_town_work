from dataclasses import dataclass


@dataclass
class UserConfig:
    login: str
    password: str
