from app.config_loader import load_config
from app import start_app

if __name__ == "__main__":
    config = load_config()
    start_app(config)

