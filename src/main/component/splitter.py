# -*- coding: utf-8 -*-
from webbrowser import get
from PySide6.QtWidgets import QMainWindow, QLabel
from main.i18n import get_text
from main.logger_config import log


def apply_splitter_style(window: QMainWindow):
    log.info("Applying splitter style")
    splitter_help_label: QLabel = window.splitter_help_label
    splitter_help_label.setProperty("class", "help")
    splitter_help_label.setText(get_text("splitter_style"))
