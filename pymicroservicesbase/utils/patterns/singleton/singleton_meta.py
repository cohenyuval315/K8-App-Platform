import asyncio
import threading


class SingletonMeta(type):
    """A metaclass for creating thread-safe and async-safe singleton classes."""

    _instances = {}
    _thread_lock = threading.Lock()

    def __call__(cls, *args, **kwargs):
        # Thread-safe instance creation
        with cls._thread_lock:
            if cls not in cls._instances:
                # Create a new instance if it doesn't already exist
                instance = super().__call__(*args, **kwargs)
                cls._instances[cls] = instance
        return cls._instances[cls]

    async def ainstance(cls, *args, **kwargs):
        """Async-safe method for getting the singleton instance."""
        if cls not in cls._instances:
            # Use an asyncio lock to ensure only one coroutine creates the instance
            async with asyncio.Lock():
                if cls not in cls._instances:
                    instance = cls(*args, **kwargs)
                    cls._instances[cls] = instance
        return cls._instances[cls]
