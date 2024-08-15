from prompt_toolkit.completion import Completer, Completion
from prompt_toolkit import PromptSession

class CustomCompleter(Completer):
    """
    Custom CLI completter
    """

    def __init__(self, commands: list, all_commands: bool = False) -> None:
        super().__init__()
        self.commands = commands
        self.all_commands = all_commands

    def get_completions(self, document, complete_event):
        for command in self.commands:
            if command[: len(document.current_line)] != document.current_line and not self.all_commands:
                continue
            yield Completion(
                command,
                start_position=-len(document.current_line),
                style="bg:green fg:ansiblack",
                selected_style="fg:lightcyan bg:ansiblack",
            )

class Prompt():
    """
    Custom prompt
    """
    def __init__(self, mouse_support=True) -> None:
        self.session = PromptSession()
        self.mouse_support = mouse_support

    def prompt(self, message: str, commands: list, all_commands: bool = False) -> str:
        """
        Provide CLI promt and return enterd data
        """
        return self.session.prompt(
                    message,
                    completer=CustomCompleter(commands, all_commands),
                    mouse_support=self.mouse_support
                )
