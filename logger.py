from typing import Literal
from rich.console import Console
from datetime import datetime

color_map = {
    'INFO': 'green',
    'WARN': 'yellow',
    'KILL': 'red'
}

class BaseConsole(Console):
    """
    Base console class that extends the Rich Console.
    This can be used to add custom logging or output formatting.
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fmt = "[bold green]{loglevel}[/]:     {message}"

    def logger(self, loglevel: Literal['INFO', 'WARN'] = 'INFO', *, message: str | None = None, color: str = 'green', bold: bool = True, bold_level: bool = True) -> None:
        """
        Log a message with the specified log level, color, and bold formatting.
        """
        if not message:
            return self.print()
        if bold:
            message = f"[bold {color}]{message}[/]"
        else:
            message = f"[{color}]{message}[/]"
        loglevel = f"[{color_map.get(loglevel, 'green')}]{loglevel}"
        return self.print(self.fmt.format(loglevel=loglevel, message=message))

    def info(self, message: str | None = None, color: str = 'green', bold: bool = True, bold_level: bool = True):
        """
        Log an info message.
        """
        return self.logger('INFO', message=message, color=color, bold=bold, bold_level=bold_level)

    def warn(self, message: str | None = None, color: str = 'yellow', bold: bool = True):
        """
        Log a warning message.
        """
        return self.logger('WARN', message=message, color=color, bold=bold)

    def kill(self, message: str | None = None, color: str = 'red', bold: bool = True):
        """
        Placeholder for a method to kill the console.
        This can be overridden in subclasses if needed.
        """
        return self.logger('KILL', message=message, color=color, bold=bold)

class VenusConsole(BaseConsole):
    """
    Custom console for Venus that extends the Rich Console.
    This can be used to add custom logging or output formatting.
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.venus_fmt = "[green]{time}[green] {message}"

    def log(self, message: str, bold: bool = False, color: str = 'green'):
        """
        Log a message with the current time.
        """
        if bold:
            message = f"[bold {color}]{message}[/]"
        else:
            message = f"[{color}]{message}[/]"
        self.print(self.venus_fmt.format(time=datetime.now().strftime('%H:%M:%S.%f')[:-3], message=message))
