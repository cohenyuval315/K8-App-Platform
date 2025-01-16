from pymicroservicesbase.sdk.web_api.core_api.web_router import WebRouter
from fastapi import WebSocket

profiling_router = WebRouter(prefix="/profiling", tags=["profiling"])


@profiling_router.post("/start")
async def start_profiling(profiler: str):
    pass


@profiling_router.get("/stop")
async def stop_profiling():
    pass


@profiling_router.get("/report/{type}")
async def get_profiling_report(type):
    pass


@profiling_router.websocket(
    "/ws/",
)
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    is_profiling = True
    while is_profiling:
        line = ""
        await websocket.send_text(line)
        is_profiling = False
