# -*- coding: utf-8 -*-
from PySide6.QtWidgets import QMainWindow, QLabel, QDialog, QHBoxLayout
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt, QSize
from main.i18n import get_text
from main.logger_config import log
from pathlib import Path
from main.util import assets_path


class ImageLabel(QLabel):
    def __init__(self, image_view_dialog: QDialog, parent=None):
        super().__init__(parent)
        self.image_path = None
        self.image_view_dialog = image_view_dialog
        self.setFixedSize(QSize(200, 200))
        self.setAlignment(Qt.AlignCenter)

    def mousePressEvent(self, event):
        if self.image_path:
            click_handler(self.image_view_dialog, self.image_path)

    def set_image(self, image_path: Path):
        self.image_path = image_path
        self.setCursor(Qt.PointingHandCursor)
        self.setProperty("class", "image")
        load_image_into_container(self, image_path)


def show_full_image(image_view_dialog: QDialog, image_path: Path):
    image_view_dialog.show()
    image_view_label: QLabel = image_view_dialog.image_view_label
    image_size = image_view_label.size()
    image_pixmap = QPixmap(image_path.as_posix())
    if image_pixmap.isNull():
        log.error(f"Failed to load image: {image_path}")
        return
    # Scale the image to fit the label while maintaining aspect ratio
    scaled_pixmap = image_pixmap.scaled(
        image_size, Qt.KeepAspectRatio, Qt.SmoothTransformation
    )
    # Set the scaled pixmap to the label
    image_view_label.setPixmap(scaled_pixmap)
    image_view_dialog.setWindowTitle(
        f"Image: {image_path.name}"
    )  # Set the window title to the image name


def click_handler(image_view_dialog: QDialog, image_path: Path):
    show_full_image(image_view_dialog, image_path)


def load_image_into_container(label: QLabel, image_path: Path):
    pixmap = QPixmap(image_path.as_posix())
    if not pixmap.isNull():
        scaled_pixmap = pixmap.scaled(
            label.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation
        )
        label.setPixmap(scaled_pixmap)
        label.setAlignment(Qt.AlignCenter)


def apply_label_style(window: QMainWindow, image_view_dialog: QDialog):
    log.info("Apply label style")
    # Infor style
    info_label: QLabel = window.info_label
    info_label.setProperty("class", "info")
    # Success style
    success_label: QLabel = window.success_label
    success_label.setProperty("class", "success")
    # Warning style
    warning_label: QLabel = window.warning_label
    warning_label.setProperty("class", "warning")
    # Error style
    error_label: QLabel = window.error_label
    error_label.setProperty("class", "error")
    # Small style
    small_label: QLabel = window.small_label
    small_label.setProperty("class", "success small")
    # Large style
    large_label: QLabel = window.large_label
    large_label.setProperty("class", "success large")

    # Image style,
    image_layout: QHBoxLayout = window.image_layout

    image_1_label: ImageLabel = ImageLabel(image_view_dialog, window)
    image_1_label.setProperty("class", "image")
    image_1 = assets_path / "andrei-r-popescu-HBsmzKuGyuI-unsplash.jpg"
    image_1_label.set_image(image_1)
    image_1_label.setCursor(Qt.PointingHandCursor)
    image_layout.addWidget(image_1_label)

    image_2_label: ImageLabel = ImageLabel(image_view_dialog, window)
    image_2_label.setProperty("class", "image")
    image_2 = assets_path / "ivo-sousa-martins-4s8kbW2GkfU-unsplash.jpg"
    image_2_label.set_image(image_2)
    image_2_label.setCursor(Qt.PointingHandCursor)
    image_layout.addWidget(image_2_label)

    image_3 = assets_path / "sumup-X9ONq8pARiU-unsplash.jpg"
    image_3_label: ImageLabel = ImageLabel(image_view_dialog, window)
    image_3_label.set_image(image_3)
    image_3_label.setProperty("class", "image")
    image_3_label.setCursor(Qt.PointingHandCursor)
    image_layout.addWidget(image_3_label)

    image_4 = assets_path / "toni-tan-y28C0M9Mabg-unsplash.jpg"
    image_4_label: ImageLabel = ImageLabel(image_view_dialog, window)
    image_4_label.setProperty("class", "image")
    image_4_label.set_image(image_4)
    image_4_label.setCursor(Qt.PointingHandCursor)
    image_layout.addWidget(image_4_label)

    # Help content
    label_help_label: QLabel = window.label_help_label
    label_help_label.setProperty("class", "help")
    label_help_label.setText(get_text("full_style_label"))
