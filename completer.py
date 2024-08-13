from prompt_toolkit.completion import Completer, Completion

class CustomCompleter(Completer):
    """
    Custom CLI completter
    """
    def __init__(self, commands: list) -> None:
        super().__init__()
        self.commands = commands

    def get_completions(self, document, complete_event):
        # print(complete_event)
        for command in self.commands:
            if command[:len(document.current_line)] != document.current_line:
                continue
            yield Completion(command,
                            start_position=-len(document.current_line),
                            style='bg:green fg:ansiblack',
                            selected_style='fg:lightcyan bg:ansiblack')
