# -*- coding: utf-8 -*-
from webbrowser import get
from PySide6.QtWidgets import QMainWindow, QPushButton, QLabel
from main.i18n import get_text
from main.logger_config import log


def apply_push_button_style(window: QMainWindow):
    log.info("Apply button style")
    # Base styles
    primary_button: QPushButton = window.primary_button
    primary_button.setProperty("class", "primary")
    dashed_button: QPushButton = window.dashed_button
    dashed_button.setProperty("class", "dashed")
    text_button: QPushButton = window.text_button
    text_button.setProperty("class", "text")
    link_button: QPushButton = window.link_button
    link_button.setProperty("class", "link")
    base_style_label: QLabel = window.base_style_label
    base_style_label.setProperty("class", "help")
    base_style_label.setText(get_text("base_style_button"))
    # Size styles
    large_button: QPushButton = window.large_button
    large_button.setProperty("class", "primary large")
    small_button: QPushButton = window.small_button
    small_button.setProperty("class", "primary small")
    size_style_label: QLabel = window.size_style_label
    size_style_label.setProperty("class", "help")
    size_style_label.setText(get_text("size_style_button"))
    # Danger
    primary_danager_button: QPushButton = window.primary_danger_button
    primary_danager_button.setProperty("class", "primary danger")
    default_danger_button: QPushButton = window.default_danger_button
    default_danger_button.setProperty("class", "danger")
    dashed_danger_button: QPushButton = window.dashed_danger_button
    dashed_danger_button.setProperty("class", "dashed danger")
    text_danger_button: QPushButton = window.text_danger_button
    text_danger_button.setProperty("class", "text danger")
    link_danger_button: QPushButton = window.link_danger_button
    link_danger_button.setProperty("class", "link danger")
    danger_style_label: QLabel = window.danger_style_label
    danger_style_label.setProperty("class", "help")
    danger_style_label.setText(get_text("danger_style_button"))
