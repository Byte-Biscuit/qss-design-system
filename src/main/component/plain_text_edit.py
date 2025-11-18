# -*- coding: utf-8 -*-
from PySide6.QtCore import QTimer
from PySide6.QtWidgets import QMainWindow, QLabel, QPlainTextEdit
from main.i18n import get_text
from main.logger_config import log
import random

log_levels = {
    "INFO": "#1677ff",  # $colorInfo
    "SUCCESS": "#52c41a",  # $colorSuccess
    "WARNING": "#faad14",  # $colorWarning
    "ERROR": "#ff4d4f",  # $colorError
}


def append_random_log(plain_text_edit: QPlainTextEdit):
    level = random.choice(list(log_levels.keys()))
    color = log_levels[level]
    message = f"[{level}] This is a sample log message."
    plain_text_edit.appendPlainText(message)
    scrollbar = plain_text_edit.verticalScrollBar()
    scrollbar.setValue(scrollbar.maximum())


def apply_plain_text_edit_style(window: QMainWindow):
    log.info("Apply plain text edit style")
    plain_text_edit: QPlainTextEdit = window.plain_text_edit
    plain_text_edit_style_label: QLabel = window.plain_text_edit_style_label
    plain_text_edit_style_label.setProperty("class", "help")
    plain_text_edit_style_label.setText(get_text("plain_text_edit_style"))
    timer = QTimer(parent=window)
    timer.timeout.connect(lambda: append_random_log(plain_text_edit))
    timer.start(1000)
