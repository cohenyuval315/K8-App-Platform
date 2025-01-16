import asyncio
import debugpy


def connect_debugger(host: str, port: int):
    """connect debugpy debugger

    Args:
        host (str): host
        port (int): port
    """
    debugpy.listen((host, port))
    debugpy.wait_for_client()


async def is_debugger_online(
    debugger_port: int, debugger_host: str = ".*"
) -> bool:
    """checks if debug server is online

    Args:
        debugger_port (int): port of debug server
        debugger_host (str, optional): debug server host. Defaults to ".*" (any).

    Returns:
        bool: true if debuger server is online
    """
    command = (
        f'lsof -i -P -n | grep "TCP {debugger_host}:{debugger_port} (LISTEN)"'
    )
    proc = await asyncio.subprocess.create_subprocess_shell(
        command,
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE,
    )
    stdout, _ = await proc.communicate()
    return bool(stdout)


async def get_stdout_from_command(command: str) -> bytes:
    """ """
    proc = await asyncio.subprocess.create_subprocess_shell(
        command,
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE,
    )
    stdout, stderr = await proc.communicate()
    return stdout


if __name__ == "__main__":
    _port = 5678
    result = asyncio.run(is_debugger_online(_port))
    print(result)
