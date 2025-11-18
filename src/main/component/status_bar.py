# -*- coding: utf-8 -*-
from PySide6.QtWidgets import QMainWindow, QLabel, QStatusBar, QPushButton
from main.i18n import get_text
from main.logger_config import log


def apply_status_bar_style(window: QMainWindow):
    log.info("Apply status_bar style")
    status_bar: QStatusBar = window.status_bar
    status_bar_default_push_button: QPushButton = window.status_bar_default_push_button
    status_bar_info_push_button: QPushButton = window.status_bar_info_push_button
    status_bar_warning_push_button: QPushButton = window.status_bar_warning_push_button
    status_bar_error_push_button: QPushButton = window.status_bar_error_push_button
    status_bar_info_push_button.setProperty("class", "primary")
    status_bar_warning_push_button.setProperty("class", "danger")
    status_bar_error_push_button.setProperty("class", "primary danger")

    # 绑定按钮点击事件，切换status_bar的class属性并设置对应文字
    status_bar_default_push_button.clicked.connect(
        lambda: (
            status_bar.setProperty("class", ""),
            status_bar.showMessage("默认状态"),
            status_bar.style().unpolish(status_bar),
            status_bar.style().polish(status_bar),
        )
    )
    status_bar_info_push_button.clicked.connect(
        lambda: (
            status_bar.setProperty("class", "info"),
            status_bar.showMessage("信息提示"),
            status_bar.style().unpolish(status_bar),
            status_bar.style().polish(status_bar),
        )
    )
    status_bar_warning_push_button.clicked.connect(
        lambda: (
            status_bar.setProperty("class", "warning"),
            status_bar.showMessage("警告状态"),
            status_bar.style().unpolish(status_bar),
            status_bar.style().polish(status_bar),
        )
    )
    status_bar_error_push_button.clicked.connect(
        lambda: (
            status_bar.setProperty("class", "error"),
            status_bar.showMessage("错误状态"),
            status_bar.style().unpolish(status_bar),
            status_bar.style().polish(status_bar),
        )
    )

    status_bar_help_label: QLabel = window.status_bar_help_label
    status_bar_help_label.setProperty("class", "help")
    status_bar_help_label.setText(get_text("status_bar_style"))
