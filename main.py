from textual.app import App, ComposeResult
from textual.widgets import Header, Footer, DirectoryTree
from textual.containers import Container
import asyncio


class OpenTorah(App):
    BINDINGS = [("e", "toggle_filetree", "Toggle File Explorer")]

    CSS = """
    DirectoryTree {
        width: 30;
        height: 100%;
        dock: left;
    }
    
    DirectoryTree.-hidden {
        display: none;
    }
    """

    async def on_mount(self) -> None:
        self.title = "openTorah"

    def compose(self) -> ComposeResult:
        yield Header()
        yield DirectoryTree("./data/sefarim", classes="-hidden")
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
