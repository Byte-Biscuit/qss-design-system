# -*- coding: utf-8 -*-
from PySide6.QtWidgets import QMainWindow, QLabel, QTextBrowser
from main.i18n import get_text
from main.logger_config import log


def apply_text_browser_style(window: QMainWindow):
    log.info("Apply text browser style")
    # 基础样式
    default_text_browser: QTextBrowser = window.default_text_browser
    default_text_browser.setHtml(
        "<h2>QTextBrowser Example</h2>"
        "<p>This is a <b>QTextBrowser</b> widget that supports rich text formatting.</p>"
        "<ul>"
        "<li>Supports <span style='color: #1677ff;'>HTML</span> content</li>"
        "<li>Displays <i>formatted text</i></li>"
        "<li>Read-only by default</li>"
        "</ul>"
        "<p>It can display links: <a href='https://www.qt.io'>Qt Official Website</a></p>"
    )
    default_text_browser.setOpenExternalLinks(True)
    
    # 帮助标签
    text_browser_help_label: QLabel = window.text_browser_help_label
    text_browser_help_label.setProperty("class", "help")
    text_browser_help_label.setText(get_text("text_browser_style"))