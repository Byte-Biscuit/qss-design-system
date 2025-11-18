# -*- coding: utf-8 -*-
from PySide6.QtWidgets import QMainWindow, QLabel
from main.i18n import get_text
from main.logger_config import log


def apply_check_box_style(window: QMainWindow):
    log.info("Apply checkbox style")
    default_check_box = window.default_check_box
    small_check_box = window.small_check_box
    small_check_box.setProperty("class", "small")
    large_check_box = window.large_check_box
    large_check_box.setProperty("class", "large")
    check_box_help_label: QLabel = window.check_box_help_label
    check_box_help_label.setProperty("class", "help")
    check_box_help_label.setText(get_text("check_box_style"))
