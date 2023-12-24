from textual.app import App, ComposeResult
from textual.widgets import Header, Footer, DirectoryTree, Static, Button
from textual.containers import Container, Grid
import asyncio
from config.keybinds import keys


class Welcome(Container):
    def compose(self) -> ComposeResult:
        yield Static("Welcome to openTorah", classes="h1")
        yield Grid(
            Button("Torah", classes=""),
            Button("Talmud", classes=""),
            Button("Halacha", classes=""),
            Button("Siddur", classes=""),
        )
        yield Static("a project of ShtenderOS", classes="h3")


class OpenTorah(App):
    CSS_PATH = "./main.tcss"

    BINDINGS = keys

    async def on_mount(self) -> None:
        self.title = "openTorah"

    def compose(self) -> ComposeResult:
        # yield Header()
        yield DirectoryTree("../data/sefarim", classes="-hidden sidebar")
        yield Welcome(classes="splash")
        # yield Header()
        yield Footer()

        # dashy
        # search box / command pallete
        # whichkey/footer
        # file viewer

    def action_toggle_filetree(self) -> None:
        directory_tree = self.query_one(DirectoryTree)
        directory_tree.toggle_class("-hidden")
        if not directory_tree.has_class("-hidden"):
            self.set_focus(directory_tree)


if __name__ == "__main__":
    app = OpenTorah()
    app.run()
