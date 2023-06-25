import pytest

from toga_winforms.libs import WinIcon

from .probe import BaseProbe


class IconProbe(BaseProbe):
    alternate_resource = "resources/icons/blue"

    def __init__(self, app, icon):
        super().__init__()
        self.app = app
        self.icon = icon
        assert isinstance(self.icon._impl.native, WinIcon)

    def assert_icon_content(self, path):
        if path == "resources/icons/green":
            assert (
                self.icon._impl.path
                == self.app.paths.app / "resources" / "icons" / "green.ico"
            )
        elif path == "resources/icons/blue":
            assert (
                self.icon._impl.path
                == self.app.paths.app / "resources" / "icons" / "blue.png"
            )
        else:
            pytest.fail("Unkonwn icon resouce")

    def assert_default_icon_content(self):
        assert self.icon._impl.path == self.app.paths.toga / "resources" / "toga.ico"
