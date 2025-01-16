import asyncio
from typing import List, Callable, Any
from ..web_service import WebService
from abc import ABC, abstractmethod


class AbstractLifeSpan(ABC):
    def __init__(self, app: WebService):
        self.app = app

    async def run_hooks(
        self, app: WebService, hooks: List[Callable[WebService, Any]]
    ):
        tasks = [func(app) for func in hooks]
        try:
            results = await asyncio.gather(*tasks)
        except* ExceptionGroup as eg:
            raise eg
        return results

    @abstractmethod
    async def initialize_resources(self):
        pass

    @abstractmethod
    async def on_startup(self):
        pass

    @abstractmethod
    async def on_shutdown(self):
        pass

    @abstractmethod
    async def finalize_resources(self):
        pass

    async def lifespan(self):
        await self.run_hooks(self.app, self.initialize_resources)
        await self.run_hooks(self.app, self.on_startup)
        yield
        await self.run_hooks(self.app, self.on_shutdown)
        await self.run_hooks(self.app, self.finalize_resources)
