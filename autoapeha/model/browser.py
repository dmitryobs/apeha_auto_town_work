from dataclasses import dataclass

@dataclass
class BrowserConfig:
    base_url: str
    driver_timeout: int
    user_agent: str
    headless: bool
    proxy: str
    disable_notifications: bool
    disable_automatic_updates: bool
