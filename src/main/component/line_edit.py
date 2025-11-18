# -*- coding: utf-8 -*-
from webbrowser import get
from PySide6.QtWidgets import QMainWindow, QLabel, QLineEdit
from main.i18n import get_text
from main.logger_config import log


def apply_line_edit_style(window: QMainWindow):
    log.info("Apply line edit style")
    # Base style
    sucess_line_edit: QLineEdit = window.sucess_line_edit
    sucess_line_edit.setProperty("class", "success")
    warning_line_edit: QLineEdit = window.warning_line_edit
    warning_line_edit.setProperty("class", "warning")
    error_line_edit: QLineEdit = window.error_line_edit
    error_line_edit.setProperty("class", "error")
    base_style_line_edit_label: QLabel = window.base_style_line_edit_label
    base_style_line_edit_label.setProperty("class", "help")
    base_style_line_edit_label.setText(get_text("base_style_line_edit"))
    # Disabled style
    disabled_line_edit: QLineEdit = window.disabled_line_edit
    disabled_line_edit.setProperty("class", "disabled")
    disable_line_edit_label: QLabel = window.disable_line_edit_label
    disable_line_edit_label.setProperty("class", "help")
    disable_line_edit_label.setText(get_text("disabled_style_line_edit"))
    # Size style
    large_line_edit: QLineEdit = window.large_line_edit
    large_line_edit.setProperty("class", "large")
    small_line_edit: QLineEdit = window.small_line_edit
    small_line_edit.setProperty("class", "small")
    size_line_edit_label: QLabel = window.size_line_edit_label
    size_line_edit_label.setProperty("class", "help")
    size_line_edit_label.setText(get_text("size_style_line_edit"))
