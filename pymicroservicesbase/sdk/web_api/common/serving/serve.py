from fastapi.staticfiles import StaticFiles
import pathlib
import os
from ...core_api.web_service import WebService


def setup_static_files(
    app: WebService, path: pathlib.Path, name: str = "static"
) -> WebService:
    normal_path = path.resolve().absolute()
    if not normal_path.exists():
        os.makedirs(normal_path.as_posix(), exist_ok=True)
    app.mount(f"/{name}", StaticFiles(directory=name), name=name)
    return app
