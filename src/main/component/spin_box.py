# -*- coding: utf-8 -*-
from PySide6.QtWidgets import QMainWindow, QLabel, QSpinBox, QDoubleSpinBox
from main.i18n import get_text
from main.logger_config import log


def apply_spin_box_style(window: QMainWindow):
    log.info("Apply spin box style")
    # 状态样式
    success_spin_box: QSpinBox = window.success_spin_box
    success_spin_box.setProperty("class", "success")
    warning_spin_box: QSpinBox = window.warning_spin_box
    warning_spin_box.setProperty("class", "warning")
    error_spin_box: QSpinBox = window.error_spin_box
    error_spin_box.setProperty("class", "error")

    # 尺寸样式
    small_spin_box: QSpinBox = window.small_spin_box
    small_spin_box.setProperty("class", "small")
    large_spin_box: QSpinBox = window.large_spin_box
    large_spin_box.setProperty("class", "large")

    # 帮助标签
    spin_box_help_label: QLabel = window.spin_box_help_label
    spin_box_help_label.setProperty("class", "help")
    spin_box_help_label.setText(get_text("spin_box_style"))
