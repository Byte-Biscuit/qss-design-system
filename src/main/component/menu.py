# -*- coding: utf-8 -*-
from os import path
from pathlib import Path
from PySide6.QtCore import Qt
from PySide6.QtGui import QIcon, QActionGroup
from PySide6.QtWidgets import QMainWindow, QLabel, QMenu
from main.logger_config import log

work_dir = Path(__file__).resolve().parent
assets_path = Path(work_dir, "..", "ui", "assets")


def apply_menu_style(window: QMainWindow):
    log.info("Apply menu style")
    click_to_view_context_menu_label: QLabel = window.click_to_view_context_menu_label
    click_to_view_context_menu_label.setProperty("class", "large info")
    # Enable context menu for the label
    click_to_view_context_menu_label.setContextMenuPolicy(Qt.CustomContextMenu)
    # Create a context menu
    context_menu = QMenu(click_to_view_context_menu_label)
    # Add actions to the context menu
    action1 = context_menu.addAction("Option1")
    action1.setIcon(
        QIcon(path.join(assets_path.as_posix(), "demo_context_menu_option1.svg"))
    )
    action2 = context_menu.addAction("Option2")
    action2.setIcon(
        QIcon(path.join(assets_path.as_posix(), "demo_context_menu_option2.svg"))
    )
    action3 = context_menu.addAction("Option3")
    action3.setIcon(
        QIcon(path.join(assets_path.as_posix(), "demo_context_menu_option3.svg"))
    )
    # Connect the actions to slots
    action1.triggered.connect(lambda: log.info("Option1 selected"))
    action2.triggered.connect(lambda: log.info("Option2 selected"))
    action3.triggered.connect(lambda: log.info("Option3 selected"))

    # Show the context menu when the label is clicked
    click_to_view_context_menu_label.customContextMenuRequested.connect(
        lambda pos: context_menu.exec_(
            click_to_view_context_menu_label.mapToGlobal(pos)
        )
    )
    radio_action_group = QActionGroup(window)
    radio_action_group.setExclusive(True)
    radio1_menu_action = window.radio1_menu_action
    radio2_menu_action = window.radio2_menu_action
    radio2_menu_action.setActionGroup(radio_action_group)
    radio1_menu_action.setActionGroup(radio_action_group)
