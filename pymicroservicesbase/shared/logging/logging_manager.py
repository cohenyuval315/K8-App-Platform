import logging


class LoggingManager:
    """LoggingManager"""

    loggers = {}

    def __new__(cls):
        cls.get_loggers()
        return super().__new__(cls)

    @classmethod
    def get_loggers(cls):
        """
        get all loggers
        """
        cls.loggers = {
            name: logging.getLogger(name)
            for name in logging.root.manager.loggerDict
        }

    @classmethod
    def add_logger(
        cls, name: str, level=logging.DEBUG, handler=logging.StreamHandler()
    ):
        """
        Add a logger with the specified name, logging level, and handler.
        """
        if name not in cls.loggers:
            logger = logging.getLogger(name)
            logger.setLevel(level)
            logger.addHandler(handler)
            cls.loggers[name] = logger

    @classmethod
    def remove_logger(cls, name: str):
        """
        Remove a logger from the system if it exists.
        """
        if name in cls.loggers:
            logger = cls.loggers.pop(name)
            for handler in logger.handlers:
                handler.close()
                logger.removeHandler(handler)

    @classmethod
    def list_loggers(cls):
        """
        List all active loggers and their levels.
        """
        return cls.loggers

    @classmethod
    def change_logger_level(cls, name: str, level: int):
        """
        Change the logging level of an existing logger.
        """
        if name in cls.loggers:
            logger = cls.loggers[name]
            logger.setLevel(level)


# Usage Example:
if __name__ == "__main__":
    # Create a LoggingManager instance
    lg_manager = LoggingManager()

    # List existing loggers
    print("Existing loggers:", lg_manager.list_loggers())

    # Add a new logger
    lg_manager.add_logger("customLogger1")
    lg_manager.add_logger("customLogger2")

    # List loggers after adding new ones
    print("Loggers after addition:", lg_manager.list_loggers())

    # Remove a logger
    lg_manager.remove_logger("customLogger1")

    # List loggers after removal
    print("Loggers after removal:", lg_manager.list_loggers())
