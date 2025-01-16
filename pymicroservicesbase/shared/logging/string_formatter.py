# from .log_level import LogLevel
import inspect
import logging
import traceback
from typing import Any, Literal, Mapping, Optional

# from utils.datetime.formats import DateTimeFormat
logging_colors = {
    "levelname": {
        "DEBUG": "\033[94m",  # Blue
        "INFO": "\033[92m",  # Green
        "WARNING": "\033[93m",  # Yellow
        "ERROR": "\033[91m",  # Red
        "CRITICAL": "\033[95m",  # Magenta
    },
    "timestamp": {
        "DEBUG": "\033[37m",  # Light gray for timestamp
        "INFO": "\033[32m",  # Green
        "WARNING": "\033[33m",  # Yellow
        "ERROR": "\033[31m",  # Red
        "CRITICAL": "\033[35m",  # Magenta
    },
    "process": {
        "DEBUG": "\033[36m",  # Cyan for process
        "INFO": "\033[92m",  # Green
        "WARNING": "\033[33m",  # Yellow
        "ERROR": "\033[31m",  # Red
        "CRITICAL": "\033[35m",  # Magenta
    },
    "thread": {
        "DEBUG": "\033[34m",  # Blue for thread
        "INFO": "\033[92m",  # Green
        "WARNING": "\033[33m",  # Yellow
        "ERROR": "\033[31m",  # Red
        "CRITICAL": "\033[35m",  # Magenta
    },
    "name": {
        "DEBUG": "\033[96m",  # Cyan for logger name
        "INFO": "\033[94m",  # Blue
        "WARNING": "\033[93m",  # Yellow
        "ERROR": "\033[91m",  # Red
        "CRITICAL": "\033[95m",  # Magenta
    },
    "message": {
        "DEBUG": "\033[37m",  # Light gray for message
        "INFO": "\033[32m",  # Green
        "WARNING": "\033[33m",  # Yellow
        "ERROR": "\033[31m",  # Red
        "CRITICAL": "\033[35m",  # Magenta
    },
    "pathname": {
        "DEBUG": "\033[90m",  # Dark gray for pathname
        "INFO": "\033[36m",  # Cyan
        "WARNING": "\033[93m",  # Yellow
        "ERROR": "\033[91m",  # Red
        "CRITICAL": "\033[35m",  # Magenta
    },
    "filename": {
        "DEBUG": "\033[90m",  # Dark gray for filename
        "INFO": "\033[36m",  # Cyan
        "WARNING": "\033[93m",  # Yellow
        "ERROR": "\033[91m",  # Red
        "CRITICAL": "\033[35m",  # Magenta
    },
    "module": {
        "DEBUG": "\033[90m",  # Dark gray for module
        "INFO": "\033[36m",  # Cyan
        "WARNING": "\033[93m",  # Yellow
        "ERROR": "\033[91m",  # Red
        "CRITICAL": "\033[95m",  # Magenta
    },
    "funcname": {
        "DEBUG": "\033[95m",  # Magenta for function name
        "INFO": "\033[34m",  # Blue
        "WARNING": "\033[93m",  # Yellow
        "ERROR": "\033[91m",  # Red
        "CRITICAL": "\033[33m",  # Orange
    },
    "lineno": {
        "DEBUG": "\033[96m",  # Cyan for line number
        "INFO": "\033[92m",  # Green
        "WARNING": "\033[93m",  # Yellow
        "ERROR": "\033[91m",  # Red
        "CRITICAL": "\033[95m",  # Magenta
    },
    "created": {
        "DEBUG": "\033[37m",  # Light gray for created timestamp
        "INFO": "\033[32m",  # Green
        "WARNING": "\033[33m",  # Yellow
        "ERROR": "\033[31m",  # Red
        "CRITICAL": "\033[35m",  # Magenta
    },
    "msecs": {
        "DEBUG": "\033[37m",  # Light gray for msecs
        "INFO": "\033[32m",  # Green
        "WARNING": "\033[33m",  # Yellow
        "ERROR": "\033[31m",  # Red
        "CRITICAL": "\033[35m",  # Magenta
    },
    "relativeCreated": {
        "DEBUG": "\033[37m",  # Light gray for relativeCreated
        "INFO": "\033[32m",  # Green
        "WARNING": "\033[33m",  # Yellow
        "ERROR": "\033[31m",  # Red
        "CRITICAL": "\033[35m",  # Magenta
    },
    "stacktrace": {
        "DEBUG": "\033[37m",  # Light gray for stack trace
        "INFO": "\033[32m",  # Green
        "WARNING": "\033[33m",  # Yellow
        "ERROR": "\033[91m",  # Red (to emphasize errors)
        "CRITICAL": "\033[35m",  # Magenta (for critical errors)
    },
    "exception": {
        "DEBUG": "\033[37m",  # Light gray for stack trace
        "INFO": "\033[32m",  # Green
        "WARNING": "\033[33m",  # Yellow
        "ERROR": "\033[91m",  # Red (to emphasize errors)
        "CRITICAL": "\033[35m",  # Magenta (for critical errors)
    },
    "extra": {
        "DEBUG": "\033[37m",  # Light gray for stack trace
        "INFO": "\033[32m",  # Green
        "WARNING": "\033[33m",  # Yellow
        "ERROR": "\033[91m",  # Red (to emphasize errors)
        "CRITICAL": "\033[35m",  # Magenta (for critical errors)
    },
}


# NAME = "name"  # Logger name
# ASCTIME = "asctime"  # Timestamp
# LEVELNAME = "levelname"  # Log level (e.g., DEBUG, INFO)
# MESSAGE = "message"  # Log message content
# MODULE = "module"  # Module name
# FUNCNAME = "funcName"  # Function name
# LINENO = "lineno"  # Line number

#     # Extended options
# PATHNAME = "pathname"  # Full path of the source file
# FILENAME = "filename"  # File name from path
# THREAD = "thread"  # Thread ID
# THREADNAME = "threadName"  # Thread name
# PROCESS = "process"  # Process ID
# CREATED = "created"  # Time when the LogRecord was created (time.time())
# MILLISECONDS = "msecs"  # Millisecond part of time
# RELATIVE_CREATED = "relativeCreated"  # Relative creation time (ms)


class StringFormatter(logging.Formatter):
    def __init__(
        self,
        fmt: str | None = None,
        datefmt: str | None = None,
        style: Literal["%", "{", "$"] = "{",
        validate: bool = True,
        default_color: str = "\033[0m",
        include_thread: bool = True,
        include_thread_id: bool = True,
        include_process_id: bool = True,
        include_name: bool = True,
        include_module: bool = True,
        include_funcname: bool = False,
        include_lineno: bool = True,
        include_pathname: bool = True,
        include_process: bool = False,
        include_force_traceback: bool = False,
        include_extra: bool = False,
        defaults: Mapping[str, Any] | None = None,
        **kwargs,
    ):
        super().__init__(fmt, datefmt, style, validate, defaults=defaults)
        self.default_color = default_color
        self.logging_colors = logging_colors
        self.include_thread = include_thread
        self.include_module = include_module
        self.include_funcname = include_funcname
        self.include_lineno = include_lineno
        self.include_pathname = include_pathname
        self.include_process = include_process
        self.include_name = include_name
        self.include_process_id = include_process_id
        self.include_thread_id = include_thread_id
        self.include_force_traceback = include_force_traceback
        self.include_extra = include_extra

    def color_log(self, levelname: str, key: str, value: str):
        if self.logging_colors is None:
            return value
        coloring = self.logging_colors.get(key)
        if not isinstance(coloring, dict):
            raise ValueError(f"invalid logging color value for {key}")
        color = coloring.get(levelname, self.default_color)
        return f"{color}{value}{self.default_color}"

    def format(self, record: logging.LogRecord):
        log_entry_parts = []
        levelname = f"{record.levelname}"
        timestamp = self.formatTime(record, "%Y-%m-%d | %H:%M:%S.%f")[
            :-3
        ]  # 19 chars (e.g., 2018-07-29 | 21:10:29.178)
        timestamp = self.color_log(levelname, "timestamp", timestamp)
        log_entry_parts.append(f"{timestamp:<23}")

        if self.include_name:
            name = f"{record.name:<10}"
            name = self.color_log(levelname, "name", name)
            log_entry_parts.append(f"{name}")

        if self.include_process:
            process = f"{record.processName:<10}"
            if self.include_process_id:
                process_id = f"{record.process}"
                process = process + f"({process_id})"
            process = self.color_log(levelname, "process", process)
            log_entry_parts.append(f"{process}")

        if self.include_thread:
            thread = f"{record.threadName:<10}"
            if self.include_thread_id:
                thread_id = f"{record.thread}"
                thread = thread + f"({thread_id})"
            thread = self.color_log(levelname, "thread", thread)
            log_entry_parts.append(f"{thread}")

        _levelname = self.color_log(levelname, "levelname", levelname)
        log_entry_parts.append(f"{_levelname}")

        if self.include_pathname:
            pathname = f"{record.pathname}"
            pathname = self.color_log(levelname, "pathname", pathname)
            log_entry_parts.append(f"{pathname}")

        elif self.include_module:
            module = f"{record.module}"
            module = self.color_log(levelname, "module", module)
            log_entry_parts.append(f"{module}")

        if self.include_funcname and record.funcName != "<module>":
            funcname = f"{record.funcName}"
            funcname = self.color_log(levelname, "funcname", funcname)
            log_entry_parts.append(f"{funcname}")

        if self.include_lineno:
            lineno = f"{record.lineno}"
            lineno = self.color_log(levelname, "lineno", lineno)
            log_entry_parts.append(f"{lineno}")

        message = record.getMessage()
        message = self.color_log(levelname, "message", message)
        log_entry_parts.append(f"{message}")

        log_entry = " | ".join(log_entry_parts)

        stack_info = self.formatStack(record.stack_info)
        if stack_info:
            stacktrace_info = self.color_log(
                levelname, "stacktrace", stack_info
            )
            log_entry += f"\n{stacktrace_info}"

        if record.exc_info:
            if (
                isinstance(record.exc_info, tuple)
                and len(record.exc_info) == 3
            ):
                exception_info = self.formatException(record.exc_info)
                exception_info = self.color_log(
                    levelname, "exception", exception_info
                )
                log_entry += f"\n{exception_info}"

        return log_entry

    def formatStack(self, stack_info: Optional[str]):  # type: ignore
        if stack_info is None:
            return None
        format_stack_string = ""
        stacktrace_header = "\n=== STACK TRACE ===\n"
        stacktrace_footer = "\n=== END STACK TRACE ===\n"

        # exception_details = stack_info.exc_type if stack_info.exc_type else "UnknownException"
        # exception_message = str(stack_info.exc_value) if stack_info.exc_value else "No message"

        stack_text = super().formatStack(stack_info)

        stack = inspect.stack()[::-1]

        stack_names = (
            inspect.getmodulename(stack[0].filename),  # Top level file name
            *(
                frame.function for frame in stack[1:]
            ),  # Function names in the stack
        )
        stack_names_str = "\n   ".join(
            f"Function: {str(item) if item is not None else 'None'}"
            for item in stack_names
        )

        error_location = f"\n   *** ERROR OCCURRED IN: {stack_names[-1]} ***"

        traceback_stack = traceback.format_stack()
        traceback_str = "\n   ".join(traceback_stack)

        format_stack_string += (
            stacktrace_header
            # + f"Exception: {exception_details} - {exception_message}\n"
            + "\nFormatted Stack Trace:\n"
            + f"   {stack_text}"
            + "\n\nFunction Call Stack:\n"
            + f"   {stack_names_str}"
            + f"{error_location}"
            + "\n\nRaw Traceback:\n"
            + f"   {traceback_str}"
            + stacktrace_footer
        )
        return format_stack_string

    def formatException(self, ei):
        format_exception_string = ""
        exception_header = "\n=== EXCEPTION ===\n"
        exception_footer = "\n=== END EXCEPTION ===\n"
        # exception_header = " \n --- Exception ---\n"
        # exception_footer = "\n ------------------ \n"
        exec_text = super().formatException(ei)
        format_exception_string += (
            exception_header + exec_text + exception_footer
        )
        return format_exception_string


if __name__ == "__main__":
    logger = logging.getLogger("TestLogger")
    logger.setLevel(logging.DEBUG)
    console_handler = logging.StreamHandler()
    formatter = StringFormatter(
        fmt="{levelname} - {message}",
        include_thread=True,
        include_process=True,
    )
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)
    logger.debug("This is a debug message.")
    logger.info("This is an info message.")
    logger.warning("This is a warning message.")
    logger.error("This is an error message.")
    logger.critical("This is a critical message.")

    try:
        # This will raise a ZeroDivisionError
        1 / 0  # type: ignore
    except ZeroDivisionError as e:
        # Log the exception using the 'exc_info' argument
        logger.error("An error occurred", exc_info=e, stack_info=True)
