from textual.app import App, ComposeResult
from textual.widgets import Header, Footer


class OpenTorah(App):
    def compose(self) -> ComposeResult:
        yield Header()
        yield Footer()


if __name__ == "__main__":
    app = OpenTorah()
    app.run()
