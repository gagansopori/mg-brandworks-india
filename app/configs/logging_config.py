import logging, sys

class LoggerConfig:
    """
    A unified logging provider that configures the root logger.
    This ensures Services, Utils, and Blueprints all share the same format.
    """
    @staticmethod
    def setup(log_level="INFO"):
        # 1. format: Timestamp | Level | Module | Message
        log_format = "[%(asctime)s] %(levelname)-8s [%(name)s.%(funcName)s:%(lineno)d] %(message)s"
        date_format = "%Y-%m-%d %H:%M:%S"
        # 2. Root Logger: directing to sys.stdout for K8s compatibility
        logging.basicConfig(
            level=getattr(logging, log_level.upper(), logging.INFO),
            format=log_format,
            datefmt=date_format,
            handlers=[
                logging.StreamHandler(sys.stdout)
            ]
        )
        # 3. Suppress noisy 3rd party logs (e.g., werkzeug, urllib3)
        logging.getLogger("werkzeug").setLevel(logging.WARNING)
        logging.getLogger("urllib3").setLevel(logging.WARNING)

        root_logger = logging.getLogger()
        root_logger.info(f"Global logger initialized at {log_level} level")

    @staticmethod
    def get_logger(name):
        return logging.getLogger(name)