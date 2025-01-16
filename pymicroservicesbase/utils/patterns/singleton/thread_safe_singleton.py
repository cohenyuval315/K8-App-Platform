import threading
from .base_singleton import BaseSingleton

# class ThreadSingleton:
#     _instance = None
#     _lock = threading.Lock()

#     def __new__(cls, *args, **kwargs):
#         if cls._instance is None:
#             with cls._lock:
#                 if cls._instance is None:
#                     cls._instance = super(ThreadSingleton, cls).__new__(cls, *args, **kwargs)
#         return cls._instance


class ThreadSafeSingleton(BaseSingleton):
    _lock = threading.Lock()

    @classmethod
    def get_instance(cls, *args, **kwargs):
        with cls._lock:
            return super().get_instance(*args, **kwargs)
