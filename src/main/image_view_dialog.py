from PySide6.QtWidgets import QDialog, QApplication
from PySide6.QtCore import Qt
from main.ui.image_view_dialog import Ui_image_view_dialog

from main.logger_config import log


class ImageViewDialog(QDialog, Ui_image_view_dialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.setParent(parent)
        self.setWindowTitle("Image Full View")
        self.setWindowFlags(self.windowFlags() | Qt.WindowStaysOnTopHint)
        # Get screen size
        screen = QApplication.primaryScreen().geometry()
        log.info(f"Screen size: {screen.width()}x{screen.height()}")
        # Set dialog size to 80% of screen
        dialog_width = int(screen.width() * 0.8)
        dialog_height = int(screen.height() * 0.8)
        self.resize(dialog_width, dialog_height)
        # Center dialog and move it slightly up
        x = (screen.width() - dialog_width) // 2
        y = (screen.height() - dialog_height) // 2 - 50
        self.move(x, y)
