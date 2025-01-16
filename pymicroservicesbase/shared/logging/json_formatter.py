import json
import logging
import traceback
from typing import Any


class JsonFormatter(logging.Formatter):
    def format(self, record: logging.LogRecord):
        # Initialize the log message dictionary
        log_message = {}

        # Add timestamp to the log message
        log_message["timestamp"] = self.formatTime(record, self.datefmt)

        # Add log level and message
        log_message["level"] = record.levelname
        log_message["message"] = record.getMessage()

        # Include the logger name and any other details
        log_message["logger"] = record.name
        log_message["module"] = record.module
        log_message["function"] = record.funcName
        log_message["line"] = record.lineno

        # Handle 'exc_info' (exception details)
        if record.exc_info:
            log_message["exception"] = self.formatException(record.exc_info)

        # Handle 'stack_info' (stack trace information)
        if record.stack_info:
            log_message["stack_info"] = self.formatStack(record.stack_info)

        # Convert the log message dictionary to JSON
        return json.dumps(log_message, indent=2)

    def formatException(self, ei):
        """
        Format the exception into a string (this will typically include traceback information).
        """
        if ei:
            return "".join(traceback.format_exception(*ei))
        return None

    def formatStack(self, stack_info: Any | str | None = None):
        """
        Format the stack info (if any) into a string.
        """
        if stack_info:
            # Check if the stack_info is a list (i.e., FrameSummary objects)
            if isinstance(stack_info, list):
                # If it is a list, use traceback.format_list
                # return "".join(traceback.format_list(stack_info))
                try:
                    # traceback.extract_stack()
                    # traceback.extract_tb()
                    return "".join(traceback.format_list(stack_info))  # type: ignore TODO
                except TypeError as e:
                    return f"Error formatting stack: {str(e)}"
            else:
                # If it's not a list, treat it as a string (default behavior)
                return str(stack_info)
        return None


# Usage Example:
if __name__ == "__main__":
    logger = logging.getLogger("my_logger")
    logger.setLevel(logging.DEBUG)

    # Create a JSON formatter and handler
    json_formatter = JsonFormatter()

    # Add console handler with the formatter
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(json_formatter)
    logger.addHandler(console_handler)

    # Test the logger with an exception
    try:
        1 / 0  # type: ignore
    except ZeroDivisionError as e:
        logger.error("An error occurred", exc_info=e, stack_info=True)
