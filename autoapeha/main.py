from autoapeha.app.app import start_app
from autoapeha.app.config import Config
from autoapeha.logger.logger import create_logger

if __name__ == "__main__":

    config = Config()

    logger = create_logger("app", config.logger_config)

    logger.info("Starting app")

    start_app(logger,config)

