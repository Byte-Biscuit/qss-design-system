# -*- coding: utf-8 -*-
from PySide6.QtCore import QDir
from PySide6.QtWidgets import (
    QMainWindow,
    QApplication,
)
from PySide6.QtGui import QIcon
from pathlib import Path
import sys
from main.component.menu import apply_menu_style
from main.component.push_button import apply_push_button_style
from main.component.line_edit import apply_line_edit_style
from main.component.tree_view import apply_tree_view_style
from main.component.label import apply_label_style
from main.component.plain_text_edit import apply_plain_text_edit_style
from main.component.splitter import apply_splitter_style
from main.component.check_box import apply_check_box_style
from main.component.combo_box import apply_combo_box_style
from main.component.status_bar import apply_status_bar_style
from main.component.spin_box import apply_spin_box_style
from main.logger_config import log
from main.ui.main_window import Ui_main_window as UiMainWindow
from main.image_view_dialog import ImageViewDialog


work_dir = Path(__file__).resolve().parent
ui_path = work_dir / "ui"
qss_file = ui_path / "qss_desigin_system.qss"


class MainWindow(QMainWindow, UiMainWindow):
    def __init__(self):
        super().__init__()
        # Initialize main window
        self.setupUi(self)
        self.screen_size = QApplication.primaryScreen().geometry()
        # Initialize image view dialog
        self.image_view_dialog = ImageViewDialog(self)
        self.apply_style()

    def apply_style(self):
        # QPushButton
        apply_push_button_style(window=self)
        # QLineEdit
        apply_line_edit_style(window=self)
        # QTreeView
        apply_tree_view_style(window=self)
        # QLabel
        apply_label_style(window=self, image_view_dialog=self.image_view_dialog)
        # QMenu
        apply_menu_style(window=self)
        # QPlainTextEdit
        apply_plain_text_edit_style(window=self)
        # QSplitter
        apply_splitter_style(window=self)
        # QCheckBox
        apply_check_box_style(window=self)
        # QComboBox
        apply_combo_box_style(window=self)
        # QStatusBar
        apply_status_bar_style(window=self)
        # QSpinBox
        apply_spin_box_style(window=self)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.setWindowIcon(QIcon(Path(ui_path / "logo_512.png").as_posix()))
    window.show()
    with open(file=qss_file, mode="r", encoding="utf-8") as fp:
        QDir.setCurrent(qss_file.parent.as_posix())
        style_sheet = fp.read()
        style_sheet = style_sheet.replace(
            "url(icons/", f"url({qss_file.parent.as_posix()}/icons/"
        )
        # self.image_view_dialog.setStyleSheet(style_sheet)
        window.setStyleSheet(style_sheet)
    sys.exit(app.exec())
