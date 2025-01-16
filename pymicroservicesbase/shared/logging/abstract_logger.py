from abc import ABC, abstractmethod


class AbstractLogger(ABC):
    def __init__(self):
        super().__init__()

    @abstractmethod
    def info(self, msg, *args, **kwargs):
        """Info ..."""
        raise NotImplementedError

    @abstractmethod
    def warning(self, msg, *args, **kwargs):
        raise NotImplementedError

    @abstractmethod
    def error(self, msg, *args, **kwargs):
        raise NotImplementedError

    @abstractmethod
    def debug(self, msg, *args, **kwargs):
        raise NotImplementedError

    @abstractmethod
    def critical(self, msg, *args, **kwargs):
        raise NotImplementedError

    @abstractmethod
    def log(self, level, msg, *args, **kwargs):
        raise NotImplementedError

    def trace(self, level, msg, stack_level, *args, **kwargs):
        raise NotImplementedError

    def verbose(self, level, msg, stack_level, *args, **kwargs):
        raise NotImplementedError

    # @abstractmethod
    # def fatal(self, msg, *args, **kwargs):
    #     pass

    # @abstractmethod
    # def warn(self, msg, *args, **kwargs):
    #     pass

    # @abstractmethod
    # def exception(self, exception,*args, **kwargs):
    #     pass
