# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 6.9.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QFormLayout,
    QHBoxLayout, QHeaderView, QLabel, QLayout,
    QLineEdit, QMainWindow, QMenu, QMenuBar,
    QPlainTextEdit, QPushButton, QSizePolicy, QSpacerItem,
    QSpinBox, QSplitter, QStatusBar, QTabWidget,
    QTextBrowser, QTreeView, QVBoxLayout, QWidget)

class Ui_main_window(object):
    def setupUi(self, main_window):
        if not main_window.objectName():
            main_window.setObjectName(u"main_window")
        main_window.resize(893, 617)
        self.actionOption1 = QAction(main_window)
        self.actionOption1.setObjectName(u"actionOption1")
        self.actionOption3 = QAction(main_window)
        self.actionOption3.setObjectName(u"actionOption3")
        self.actionOption4 = QAction(main_window)
        self.actionOption4.setObjectName(u"actionOption4")
        self.actionSuboption1 = QAction(main_window)
        self.actionSuboption1.setObjectName(u"actionSuboption1")
        self.actionSuboption2 = QAction(main_window)
        self.actionSuboption2.setObjectName(u"actionSuboption2")
        self.actionSuboption3 = QAction(main_window)
        self.actionSuboption3.setObjectName(u"actionSuboption3")
        self.actionManual = QAction(main_window)
        self.actionManual.setObjectName(u"actionManual")
        self.actionAbout = QAction(main_window)
        self.actionAbout.setObjectName(u"actionAbout")
        self.actionContact = QAction(main_window)
        self.actionContact.setObjectName(u"actionContact")
        self.actionChecked = QAction(main_window)
        self.actionChecked.setObjectName(u"actionChecked")
        self.actionChecked.setCheckable(True)
        self.actionUnchecked = QAction(main_window)
        self.actionUnchecked.setObjectName(u"actionUnchecked")
        self.actionUnchecked.setCheckable(True)
        self.radio1_menu_action = QAction(main_window)
        self.radio1_menu_action.setObjectName(u"radio1_menu_action")
        self.radio1_menu_action.setCheckable(True)
        self.radio2_menu_action = QAction(main_window)
        self.radio2_menu_action.setObjectName(u"radio2_menu_action")
        self.radio2_menu_action.setCheckable(True)
        self.centralwidget = QWidget(main_window)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_4 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.example_tab = QTabWidget(self.centralwidget)
        self.example_tab.setObjectName(u"example_tab")
        self.tab_button = QWidget()
        self.tab_button.setObjectName(u"tab_button")
        self.verticalLayout_2 = QVBoxLayout(self.tab_button)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self._2 = QVBoxLayout()
        self._2.setObjectName(u"_2")
        self._2.setContentsMargins(-1, 1, 1, 1)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.primary_button = QPushButton(self.tab_button)
        self.primary_button.setObjectName(u"primary_button")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.primary_button.sizePolicy().hasHeightForWidth())
        self.primary_button.setSizePolicy(sizePolicy)

        self.horizontalLayout.addWidget(self.primary_button)

        self.default_button = QPushButton(self.tab_button)
        self.default_button.setObjectName(u"default_button")
        sizePolicy.setHeightForWidth(self.default_button.sizePolicy().hasHeightForWidth())
        self.default_button.setSizePolicy(sizePolicy)

        self.horizontalLayout.addWidget(self.default_button)

        self.dashed_button = QPushButton(self.tab_button)
        self.dashed_button.setObjectName(u"dashed_button")
        sizePolicy.setHeightForWidth(self.dashed_button.sizePolicy().hasHeightForWidth())
        self.dashed_button.setSizePolicy(sizePolicy)

        self.horizontalLayout.addWidget(self.dashed_button)

        self.text_button = QPushButton(self.tab_button)
        self.text_button.setObjectName(u"text_button")
        sizePolicy.setHeightForWidth(self.text_button.sizePolicy().hasHeightForWidth())
        self.text_button.setSizePolicy(sizePolicy)

        self.horizontalLayout.addWidget(self.text_button)

        self.link_button = QPushButton(self.tab_button)
        self.link_button.setObjectName(u"link_button")
        sizePolicy.setHeightForWidth(self.link_button.sizePolicy().hasHeightForWidth())
        self.link_button.setSizePolicy(sizePolicy)

        self.horizontalLayout.addWidget(self.link_button)


        self._2.addLayout(self.horizontalLayout)

        self.base_style_label = QLabel(self.tab_button)
        self.base_style_label.setObjectName(u"base_style_label")
        self.base_style_label.setTextInteractionFlags(Qt.TextInteractionFlag.LinksAccessibleByMouse|Qt.TextInteractionFlag.TextSelectableByMouse)

        self._2.addWidget(self.base_style_label)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.large_button = QPushButton(self.tab_button)
        self.large_button.setObjectName(u"large_button")
        sizePolicy.setHeightForWidth(self.large_button.sizePolicy().hasHeightForWidth())
        self.large_button.setSizePolicy(sizePolicy)

        self.horizontalLayout_2.addWidget(self.large_button)

        self.small_button = QPushButton(self.tab_button)
        self.small_button.setObjectName(u"small_button")
        sizePolicy.setHeightForWidth(self.small_button.sizePolicy().hasHeightForWidth())
        self.small_button.setSizePolicy(sizePolicy)

        self.horizontalLayout_2.addWidget(self.small_button)

        self.disable_push_button = QPushButton(self.tab_button)
        self.disable_push_button.setObjectName(u"disable_push_button")
        self.disable_push_button.setEnabled(False)

        self.horizontalLayout_2.addWidget(self.disable_push_button)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.horizontalLayout_2.setStretch(0, 2)
        self.horizontalLayout_2.setStretch(1, 2)
        self.horizontalLayout_2.setStretch(3, 6)

        self._2.addLayout(self.horizontalLayout_2)

        self.size_style_label = QLabel(self.tab_button)
        self.size_style_label.setObjectName(u"size_style_label")
        self.size_style_label.setTextInteractionFlags(Qt.TextInteractionFlag.LinksAccessibleByMouse|Qt.TextInteractionFlag.TextSelectableByMouse)

        self._2.addWidget(self.size_style_label)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.primary_danger_button = QPushButton(self.tab_button)
        self.primary_danger_button.setObjectName(u"primary_danger_button")
        sizePolicy.setHeightForWidth(self.primary_danger_button.sizePolicy().hasHeightForWidth())
        self.primary_danger_button.setSizePolicy(sizePolicy)

        self.horizontalLayout_3.addWidget(self.primary_danger_button)

        self.default_danger_button = QPushButton(self.tab_button)
        self.default_danger_button.setObjectName(u"default_danger_button")
        sizePolicy.setHeightForWidth(self.default_danger_button.sizePolicy().hasHeightForWidth())
        self.default_danger_button.setSizePolicy(sizePolicy)

        self.horizontalLayout_3.addWidget(self.default_danger_button)

        self.dashed_danger_button = QPushButton(self.tab_button)
        self.dashed_danger_button.setObjectName(u"dashed_danger_button")
        sizePolicy.setHeightForWidth(self.dashed_danger_button.sizePolicy().hasHeightForWidth())
        self.dashed_danger_button.setSizePolicy(sizePolicy)

        self.horizontalLayout_3.addWidget(self.dashed_danger_button)

        self.text_danger_button = QPushButton(self.tab_button)
        self.text_danger_button.setObjectName(u"text_danger_button")
        sizePolicy.setHeightForWidth(self.text_danger_button.sizePolicy().hasHeightForWidth())
        self.text_danger_button.setSizePolicy(sizePolicy)

        self.horizontalLayout_3.addWidget(self.text_danger_button)

        self.link_danger_button = QPushButton(self.tab_button)
        self.link_danger_button.setObjectName(u"link_danger_button")
        sizePolicy.setHeightForWidth(self.link_danger_button.sizePolicy().hasHeightForWidth())
        self.link_danger_button.setSizePolicy(sizePolicy)

        self.horizontalLayout_3.addWidget(self.link_danger_button)


        self._2.addLayout(self.horizontalLayout_3)

        self.danger_style_label = QLabel(self.tab_button)
        self.danger_style_label.setObjectName(u"danger_style_label")
        self.danger_style_label.setTextInteractionFlags(Qt.TextInteractionFlag.LinksAccessibleByMouse|Qt.TextInteractionFlag.TextSelectableByMouse)

        self._2.addWidget(self.danger_style_label)


        self.verticalLayout_2.addLayout(self._2)

        self.example_tab.addTab(self.tab_button, "")
        self.tab_treeview = QWidget()
        self.tab_treeview.setObjectName(u"tab_treeview")
        self.verticalLayout = QVBoxLayout(self.tab_treeview)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.tree_view = QTreeView(self.tab_treeview)
        self.tree_view.setObjectName(u"tree_view")

        self.verticalLayout.addWidget(self.tree_view)

        self.default_style_tree_view_label = QLabel(self.tab_treeview)
        self.default_style_tree_view_label.setObjectName(u"default_style_tree_view_label")
        self.default_style_tree_view_label.setTextInteractionFlags(Qt.TextInteractionFlag.LinksAccessibleByMouse|Qt.TextInteractionFlag.TextSelectableByKeyboard|Qt.TextInteractionFlag.TextSelectableByMouse)

        self.verticalLayout.addWidget(self.default_style_tree_view_label)

        self.verticalLayout.setStretch(0, 7)
        self.verticalLayout.setStretch(1, 3)
        self.example_tab.addTab(self.tab_treeview, "")
        self.tab_line_edit = QWidget()
        self.tab_line_edit.setObjectName(u"tab_line_edit")
        self.verticalLayout_3 = QVBoxLayout(self.tab_line_edit)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.normal_line_edit = QLineEdit(self.tab_line_edit)
        self.normal_line_edit.setObjectName(u"normal_line_edit")

        self.horizontalLayout_4.addWidget(self.normal_line_edit)

        self.sucess_line_edit = QLineEdit(self.tab_line_edit)
        self.sucess_line_edit.setObjectName(u"sucess_line_edit")

        self.horizontalLayout_4.addWidget(self.sucess_line_edit)

        self.warning_line_edit = QLineEdit(self.tab_line_edit)
        self.warning_line_edit.setObjectName(u"warning_line_edit")

        self.horizontalLayout_4.addWidget(self.warning_line_edit)

        self.error_line_edit = QLineEdit(self.tab_line_edit)
        self.error_line_edit.setObjectName(u"error_line_edit")

        self.horizontalLayout_4.addWidget(self.error_line_edit)


        self.verticalLayout_3.addLayout(self.horizontalLayout_4)

        self.base_style_line_edit_label = QLabel(self.tab_line_edit)
        self.base_style_line_edit_label.setObjectName(u"base_style_line_edit_label")
        self.base_style_line_edit_label.setTextInteractionFlags(Qt.TextInteractionFlag.LinksAccessibleByMouse|Qt.TextInteractionFlag.TextSelectableByKeyboard|Qt.TextInteractionFlag.TextSelectableByMouse)

        self.verticalLayout_3.addWidget(self.base_style_line_edit_label)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.disabled_line_edit = QLineEdit(self.tab_line_edit)
        self.disabled_line_edit.setObjectName(u"disabled_line_edit")
        self.disabled_line_edit.setEnabled(False)

        self.horizontalLayout_6.addWidget(self.disabled_line_edit)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_2)

        self.horizontalLayout_6.setStretch(1, 3)

        self.verticalLayout_3.addLayout(self.horizontalLayout_6)

        self.disable_line_edit_label = QLabel(self.tab_line_edit)
        self.disable_line_edit_label.setObjectName(u"disable_line_edit_label")
        self.disable_line_edit_label.setTextInteractionFlags(Qt.TextInteractionFlag.LinksAccessibleByMouse|Qt.TextInteractionFlag.TextSelectableByKeyboard|Qt.TextInteractionFlag.TextSelectableByMouse)

        self.verticalLayout_3.addWidget(self.disable_line_edit_label)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.large_line_edit = QLineEdit(self.tab_line_edit)
        self.large_line_edit.setObjectName(u"large_line_edit")

        self.horizontalLayout_5.addWidget(self.large_line_edit)

        self.small_line_edit = QLineEdit(self.tab_line_edit)
        self.small_line_edit.setObjectName(u"small_line_edit")

        self.horizontalLayout_5.addWidget(self.small_line_edit)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_3)

        self.horizontalLayout_5.setStretch(2, 3)

        self.verticalLayout_3.addLayout(self.horizontalLayout_5)

        self.size_line_edit_label = QLabel(self.tab_line_edit)
        self.size_line_edit_label.setObjectName(u"size_line_edit_label")
        self.size_line_edit_label.setTextInteractionFlags(Qt.TextInteractionFlag.LinksAccessibleByMouse|Qt.TextInteractionFlag.TextSelectableByKeyboard|Qt.TextInteractionFlag.TextSelectableByMouse)

        self.verticalLayout_3.addWidget(self.size_line_edit_label)

        self.example_tab.addTab(self.tab_line_edit, "")
        self.tab_label = QWidget()
        self.tab_label.setObjectName(u"tab_label")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.tab_label.sizePolicy().hasHeightForWidth())
        self.tab_label.setSizePolicy(sizePolicy1)
        self.verticalLayout_5 = QVBoxLayout(self.tab_label)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.default_label = QLabel(self.tab_label)
        self.default_label.setObjectName(u"default_label")
        sizePolicy1.setHeightForWidth(self.default_label.sizePolicy().hasHeightForWidth())
        self.default_label.setSizePolicy(sizePolicy1)
        self.default_label.setTextInteractionFlags(Qt.TextInteractionFlag.LinksAccessibleByMouse|Qt.TextInteractionFlag.TextSelectableByKeyboard|Qt.TextInteractionFlag.TextSelectableByMouse)

        self.horizontalLayout_7.addWidget(self.default_label)

        self.info_label = QLabel(self.tab_label)
        self.info_label.setObjectName(u"info_label")
        sizePolicy1.setHeightForWidth(self.info_label.sizePolicy().hasHeightForWidth())
        self.info_label.setSizePolicy(sizePolicy1)
        self.info_label.setTextInteractionFlags(Qt.TextInteractionFlag.LinksAccessibleByMouse|Qt.TextInteractionFlag.TextSelectableByKeyboard|Qt.TextInteractionFlag.TextSelectableByMouse)

        self.horizontalLayout_7.addWidget(self.info_label)

        self.success_label = QLabel(self.tab_label)
        self.success_label.setObjectName(u"success_label")
        sizePolicy1.setHeightForWidth(self.success_label.sizePolicy().hasHeightForWidth())
        self.success_label.setSizePolicy(sizePolicy1)
        self.success_label.setTextInteractionFlags(Qt.TextInteractionFlag.LinksAccessibleByMouse|Qt.TextInteractionFlag.TextSelectableByKeyboard|Qt.TextInteractionFlag.TextSelectableByMouse)

        self.horizontalLayout_7.addWidget(self.success_label)

        self.warning_label = QLabel(self.tab_label)
        self.warning_label.setObjectName(u"warning_label")
        sizePolicy1.setHeightForWidth(self.warning_label.sizePolicy().hasHeightForWidth())
        self.warning_label.setSizePolicy(sizePolicy1)
        self.warning_label.setTextInteractionFlags(Qt.TextInteractionFlag.LinksAccessibleByMouse|Qt.TextInteractionFlag.TextSelectableByKeyboard|Qt.TextInteractionFlag.TextSelectableByMouse)

        self.horizontalLayout_7.addWidget(self.warning_label)

        self.error_label = QLabel(self.tab_label)
        self.error_label.setObjectName(u"error_label")
        sizePolicy1.setHeightForWidth(self.error_label.sizePolicy().hasHeightForWidth())
        self.error_label.setSizePolicy(sizePolicy1)
        self.error_label.setTextInteractionFlags(Qt.TextInteractionFlag.LinksAccessibleByMouse|Qt.TextInteractionFlag.TextSelectableByKeyboard|Qt.TextInteractionFlag.TextSelectableByMouse)

        self.horizontalLayout_7.addWidget(self.error_label)


        self.verticalLayout_5.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.large_label = QLabel(self.tab_label)
        self.large_label.setObjectName(u"large_label")
        sizePolicy1.setHeightForWidth(self.large_label.sizePolicy().hasHeightForWidth())
        self.large_label.setSizePolicy(sizePolicy1)
        self.large_label.setTextInteractionFlags(Qt.TextInteractionFlag.LinksAccessibleByMouse|Qt.TextInteractionFlag.TextSelectableByKeyboard|Qt.TextInteractionFlag.TextSelectableByMouse)

        self.horizontalLayout_8.addWidget(self.large_label)

        self.small_label = QLabel(self.tab_label)
        self.small_label.setObjectName(u"small_label")
        sizePolicy1.setHeightForWidth(self.small_label.sizePolicy().hasHeightForWidth())
        self.small_label.setSizePolicy(sizePolicy1)
        self.small_label.setTextInteractionFlags(Qt.TextInteractionFlag.LinksAccessibleByMouse|Qt.TextInteractionFlag.TextSelectableByKeyboard|Qt.TextInteractionFlag.TextSelectableByMouse)

        self.horizontalLayout_8.addWidget(self.small_label)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_4)

        self.horizontalLayout_8.setStretch(0, 3)
        self.horizontalLayout_8.setStretch(1, 3)
        self.horizontalLayout_8.setStretch(2, 4)

        self.verticalLayout_5.addLayout(self.horizontalLayout_8)

        self.image_layout = QHBoxLayout()
        self.image_layout.setObjectName(u"image_layout")
        self.image_layout.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.image_layout.setContentsMargins(-1, -1, -1, 10)

        self.verticalLayout_5.addLayout(self.image_layout)

        self.label_help_label = QLabel(self.tab_label)
        self.label_help_label.setObjectName(u"label_help_label")
        self.label_help_label.setTextInteractionFlags(Qt.TextInteractionFlag.LinksAccessibleByMouse|Qt.TextInteractionFlag.TextSelectableByKeyboard|Qt.TextInteractionFlag.TextSelectableByMouse)

        self.verticalLayout_5.addWidget(self.label_help_label)

        self.verticalLayout_5.setStretch(2, 2)
        self.example_tab.addTab(self.tab_label, "")
        self.tab_menu = QWidget()
        self.tab_menu.setObjectName(u"tab_menu")
        self._3 = QHBoxLayout(self.tab_menu)
        self._3.setObjectName(u"_3")
        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self._3.addItem(self.horizontalSpacer_5)

        self.click_to_view_context_menu_label = QLabel(self.tab_menu)
        self.click_to_view_context_menu_label.setObjectName(u"click_to_view_context_menu_label")
        self.click_to_view_context_menu_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.click_to_view_context_menu_label.setTextInteractionFlags(Qt.TextInteractionFlag.LinksAccessibleByMouse|Qt.TextInteractionFlag.TextSelectableByKeyboard|Qt.TextInteractionFlag.TextSelectableByMouse)

        self._3.addWidget(self.click_to_view_context_menu_label)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self._3.addItem(self.horizontalSpacer_6)

        self.example_tab.addTab(self.tab_menu, "")
        self.tab_splitter = QWidget()
        self.tab_splitter.setObjectName(u"tab_splitter")
        self.horizontalLayout_9 = QHBoxLayout(self.tab_splitter)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.splitter_2 = QSplitter(self.tab_splitter)
        self.splitter_2.setObjectName(u"splitter_2")
        self.splitter_2.setOrientation(Qt.Orientation.Horizontal)
        self.label = QLabel(self.splitter_2)
        self.label.setObjectName(u"label")
        self.label.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.label.setAutoFillBackground(False)
        self.label.setStyleSheet(u"background-color: rgb(0, 170, 0);")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.splitter_2.addWidget(self.label)
        self.splitter = QSplitter(self.splitter_2)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setOrientation(Qt.Orientation.Vertical)
        self.splitter_help_label = QLabel(self.splitter)
        self.splitter_help_label.setObjectName(u"splitter_help_label")
        self.splitter_help_label.setStyleSheet(u"")
        self.splitter_help_label.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.splitter.addWidget(self.splitter_help_label)
        self.label_3 = QLabel(self.splitter)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setStyleSheet(u"background-color: rgb(255, 170, 255);")
        self.label_3.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.splitter.addWidget(self.label_3)
        self.splitter_2.addWidget(self.splitter)

        self.horizontalLayout_9.addWidget(self.splitter_2)

        self.example_tab.addTab(self.tab_splitter, "")
        self.tab_plain_text_edit = QWidget()
        self.tab_plain_text_edit.setObjectName(u"tab_plain_text_edit")
        self.verticalLayout_6 = QVBoxLayout(self.tab_plain_text_edit)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.plain_text_edit = QPlainTextEdit(self.tab_plain_text_edit)
        self.plain_text_edit.setObjectName(u"plain_text_edit")

        self.verticalLayout_6.addWidget(self.plain_text_edit)

        self.plain_text_edit_style_label = QLabel(self.tab_plain_text_edit)
        self.plain_text_edit_style_label.setObjectName(u"plain_text_edit_style_label")
        self.plain_text_edit_style_label.setTextInteractionFlags(Qt.TextInteractionFlag.LinksAccessibleByMouse|Qt.TextInteractionFlag.TextSelectableByKeyboard|Qt.TextInteractionFlag.TextSelectableByMouse)

        self.verticalLayout_6.addWidget(self.plain_text_edit_style_label)

        self.verticalLayout_6.setStretch(0, 2)
        self.verticalLayout_6.setStretch(1, 1)
        self.example_tab.addTab(self.tab_plain_text_edit, "")
        self.tab_text_browser = QWidget()
        self.tab_text_browser.setObjectName(u"tab_text_browser")
        self.text_browser_layout = QVBoxLayout(self.tab_text_browser)
        self.text_browser_layout.setSpacing(15)
        self.text_browser_layout.setObjectName(u"text_browser_layout")
        self.text_browser_layout.setContentsMargins(20, 20, 20, 20)
        self.text_browser_row1 = QHBoxLayout()
        self.text_browser_row1.setObjectName(u"text_browser_row1")
        self.default_text_browser = QTextBrowser(self.tab_text_browser)
        self.default_text_browser.setObjectName(u"default_text_browser")
        self.default_text_browser.setMinimumSize(QSize(0, 100))

        self.text_browser_row1.addWidget(self.default_text_browser)


        self.text_browser_layout.addLayout(self.text_browser_row1)

        self.text_browser_help_label = QLabel(self.tab_text_browser)
        self.text_browser_help_label.setObjectName(u"text_browser_help_label")
        self.text_browser_help_label.setTextInteractionFlags(Qt.TextInteractionFlag.LinksAccessibleByMouse|Qt.TextInteractionFlag.TextSelectableByKeyboard|Qt.TextInteractionFlag.TextSelectableByMouse)

        self.text_browser_layout.addWidget(self.text_browser_help_label)

        self.example_tab.addTab(self.tab_text_browser, "")
        self.check_box_tab = QWidget()
        self.check_box_tab.setObjectName(u"check_box_tab")
        self.verticalLayout_7 = QVBoxLayout(self.check_box_tab)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.default_check_box = QCheckBox(self.check_box_tab)
        self.default_check_box.setObjectName(u"default_check_box")

        self.verticalLayout_7.addWidget(self.default_check_box)

        self.small_check_box = QCheckBox(self.check_box_tab)
        self.small_check_box.setObjectName(u"small_check_box")

        self.verticalLayout_7.addWidget(self.small_check_box)

        self.large_check_box = QCheckBox(self.check_box_tab)
        self.large_check_box.setObjectName(u"large_check_box")

        self.verticalLayout_7.addWidget(self.large_check_box)

        self.disabled_uncheck_box = QCheckBox(self.check_box_tab)
        self.disabled_uncheck_box.setObjectName(u"disabled_uncheck_box")
        self.disabled_uncheck_box.setEnabled(False)

        self.verticalLayout_7.addWidget(self.disabled_uncheck_box)

        self.disable_checked_box = QCheckBox(self.check_box_tab)
        self.disable_checked_box.setObjectName(u"disable_checked_box")
        self.disable_checked_box.setEnabled(False)
        self.disable_checked_box.setChecked(True)

        self.verticalLayout_7.addWidget(self.disable_checked_box)

        self.check_box_help_label = QLabel(self.check_box_tab)
        self.check_box_help_label.setObjectName(u"check_box_help_label")
        self.check_box_help_label.setTextInteractionFlags(Qt.TextInteractionFlag.LinksAccessibleByKeyboard|Qt.TextInteractionFlag.LinksAccessibleByMouse|Qt.TextInteractionFlag.TextBrowserInteraction|Qt.TextInteractionFlag.TextSelectableByKeyboard|Qt.TextInteractionFlag.TextSelectableByMouse)

        self.verticalLayout_7.addWidget(self.check_box_help_label)

        self.example_tab.addTab(self.check_box_tab, "")
        self.combo_box_tab = QWidget()
        self.combo_box_tab.setObjectName(u"combo_box_tab")
        self.verticalLayout_8 = QVBoxLayout(self.combo_box_tab)
        self.verticalLayout_8.setSpacing(20)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(20, 20, 20, 20)
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.large_combo_box = QComboBox(self.combo_box_tab)
        self.large_combo_box.setObjectName(u"large_combo_box")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.FieldRole, self.large_combo_box)

        self.small_combo_box = QComboBox(self.combo_box_tab)
        self.small_combo_box.setObjectName(u"small_combo_box")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.FieldRole, self.small_combo_box)

        self.label_4 = QLabel(self.combo_box_tab)
        self.label_4.setObjectName(u"label_4")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.label_4)

        self.label_5 = QLabel(self.combo_box_tab)
        self.label_5.setObjectName(u"label_5")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.label_5)

        self.label_2 = QLabel(self.combo_box_tab)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.LabelRole, self.label_2)

        self.default_combo_box = QComboBox(self.combo_box_tab)
        self.default_combo_box.setObjectName(u"default_combo_box")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.default_combo_box)


        self.verticalLayout_8.addLayout(self.formLayout)

        self.combo_box_help_label = QLabel(self.combo_box_tab)
        self.combo_box_help_label.setObjectName(u"combo_box_help_label")
        self.combo_box_help_label.setTextInteractionFlags(Qt.TextInteractionFlag.LinksAccessibleByMouse|Qt.TextInteractionFlag.TextSelectableByKeyboard|Qt.TextInteractionFlag.TextSelectableByMouse)

        self.verticalLayout_8.addWidget(self.combo_box_help_label)

        self.example_tab.addTab(self.combo_box_tab, "")
        self.status_bar_tab = QWidget()
        self.status_bar_tab.setObjectName(u"status_bar_tab")
        self.verticalLayout_10 = QVBoxLayout(self.status_bar_tab)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_7)

        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setSpacing(20)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(-1, 30, -1, -1)
        self.status_bar_default_push_button = QPushButton(self.status_bar_tab)
        self.status_bar_default_push_button.setObjectName(u"status_bar_default_push_button")

        self.verticalLayout_9.addWidget(self.status_bar_default_push_button)

        self.status_bar_info_push_button = QPushButton(self.status_bar_tab)
        self.status_bar_info_push_button.setObjectName(u"status_bar_info_push_button")

        self.verticalLayout_9.addWidget(self.status_bar_info_push_button)

        self.status_bar_warning_push_button = QPushButton(self.status_bar_tab)
        self.status_bar_warning_push_button.setObjectName(u"status_bar_warning_push_button")

        self.verticalLayout_9.addWidget(self.status_bar_warning_push_button)

        self.status_bar_error_push_button = QPushButton(self.status_bar_tab)
        self.status_bar_error_push_button.setObjectName(u"status_bar_error_push_button")

        self.verticalLayout_9.addWidget(self.status_bar_error_push_button)


        self.horizontalLayout_10.addLayout(self.verticalLayout_9)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_8)

        self.horizontalLayout_10.setStretch(0, 3)
        self.horizontalLayout_10.setStretch(1, 1)
        self.horizontalLayout_10.setStretch(2, 3)

        self.verticalLayout_10.addLayout(self.horizontalLayout_10)

        self.status_bar_help_label = QLabel(self.status_bar_tab)
        self.status_bar_help_label.setObjectName(u"status_bar_help_label")
        self.status_bar_help_label.setTextInteractionFlags(Qt.TextInteractionFlag.LinksAccessibleByMouse|Qt.TextInteractionFlag.TextSelectableByKeyboard|Qt.TextInteractionFlag.TextSelectableByMouse)

        self.verticalLayout_10.addWidget(self.status_bar_help_label)

        self.verticalLayout_10.setStretch(0, 4)
        self.verticalLayout_10.setStretch(1, 2)
        self.example_tab.addTab(self.status_bar_tab, "")
        self.spin_box_tab = QWidget()
        self.spin_box_tab.setObjectName(u"spin_box_tab")
        self.verticalLayout_11 = QVBoxLayout(self.spin_box_tab)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.formLayout_2 = QFormLayout()
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.formLayout_2.setContentsMargins(20, 20, 20, 20)
        self.spin_box_small_label = QLabel(self.spin_box_tab)
        self.spin_box_small_label.setObjectName(u"spin_box_small_label")

        self.formLayout_2.setWidget(0, QFormLayout.ItemRole.LabelRole, self.spin_box_small_label)

        self.spin_box_default_label = QLabel(self.spin_box_tab)
        self.spin_box_default_label.setObjectName(u"spin_box_default_label")

        self.formLayout_2.setWidget(1, QFormLayout.ItemRole.LabelRole, self.spin_box_default_label)

        self.spin_box_large_label = QLabel(self.spin_box_tab)
        self.spin_box_large_label.setObjectName(u"spin_box_large_label")

        self.formLayout_2.setWidget(2, QFormLayout.ItemRole.LabelRole, self.spin_box_large_label)

        self.small_spin_box = QSpinBox(self.spin_box_tab)
        self.small_spin_box.setObjectName(u"small_spin_box")

        self.formLayout_2.setWidget(0, QFormLayout.ItemRole.FieldRole, self.small_spin_box)

        self.default_spin_box = QSpinBox(self.spin_box_tab)
        self.default_spin_box.setObjectName(u"default_spin_box")

        self.formLayout_2.setWidget(1, QFormLayout.ItemRole.FieldRole, self.default_spin_box)

        self.large_spin_box = QSpinBox(self.spin_box_tab)
        self.large_spin_box.setObjectName(u"large_spin_box")

        self.formLayout_2.setWidget(2, QFormLayout.ItemRole.FieldRole, self.large_spin_box)

        self.spin_box_success_label = QLabel(self.spin_box_tab)
        self.spin_box_success_label.setObjectName(u"spin_box_success_label")

        self.formLayout_2.setWidget(3, QFormLayout.ItemRole.LabelRole, self.spin_box_success_label)

        self.spin_box_warning_label = QLabel(self.spin_box_tab)
        self.spin_box_warning_label.setObjectName(u"spin_box_warning_label")

        self.formLayout_2.setWidget(4, QFormLayout.ItemRole.LabelRole, self.spin_box_warning_label)

        self.spin_box_error_label = QLabel(self.spin_box_tab)
        self.spin_box_error_label.setObjectName(u"spin_box_error_label")

        self.formLayout_2.setWidget(5, QFormLayout.ItemRole.LabelRole, self.spin_box_error_label)

        self.success_spin_box = QSpinBox(self.spin_box_tab)
        self.success_spin_box.setObjectName(u"success_spin_box")

        self.formLayout_2.setWidget(3, QFormLayout.ItemRole.FieldRole, self.success_spin_box)

        self.warning_spin_box = QSpinBox(self.spin_box_tab)
        self.warning_spin_box.setObjectName(u"warning_spin_box")

        self.formLayout_2.setWidget(4, QFormLayout.ItemRole.FieldRole, self.warning_spin_box)

        self.error_spin_box = QSpinBox(self.spin_box_tab)
        self.error_spin_box.setObjectName(u"error_spin_box")

        self.formLayout_2.setWidget(5, QFormLayout.ItemRole.FieldRole, self.error_spin_box)


        self.verticalLayout_11.addLayout(self.formLayout_2)

        self.spin_box_help_label = QLabel(self.spin_box_tab)
        self.spin_box_help_label.setObjectName(u"spin_box_help_label")
        self.spin_box_help_label.setTextInteractionFlags(Qt.TextInteractionFlag.LinksAccessibleByMouse|Qt.TextInteractionFlag.TextSelectableByKeyboard|Qt.TextInteractionFlag.TextSelectableByMouse)

        self.verticalLayout_11.addWidget(self.spin_box_help_label)

        self.verticalLayout_11.setStretch(0, 1)
        self.verticalLayout_11.setStretch(1, 1)
        self.example_tab.addTab(self.spin_box_tab, "")

        self.verticalLayout_4.addWidget(self.example_tab)

        main_window.setCentralWidget(self.centralwidget)
        self.menu_bar = QMenuBar(main_window)
        self.menu_bar.setObjectName(u"menu_bar")
        self.menu_bar.setGeometry(QRect(0, 0, 893, 33))
        self.menuFile = QMenu(self.menu_bar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuOption2 = QMenu(self.menuFile)
        self.menuOption2.setObjectName(u"menuOption2")
        self.menuHelp = QMenu(self.menu_bar)
        self.menuHelp.setObjectName(u"menuHelp")
        self.menuMenu = QMenu(self.menu_bar)
        self.menuMenu.setObjectName(u"menuMenu")
        self.menuCheck_Status = QMenu(self.menuMenu)
        self.menuCheck_Status.setObjectName(u"menuCheck_Status")
        self.menuRadio_Status = QMenu(self.menuMenu)
        self.menuRadio_Status.setObjectName(u"menuRadio_Status")
        main_window.setMenuBar(self.menu_bar)
        self.status_bar = QStatusBar(main_window)
        self.status_bar.setObjectName(u"status_bar")
        main_window.setStatusBar(self.status_bar)

        self.menu_bar.addAction(self.menuFile.menuAction())
        self.menu_bar.addAction(self.menuMenu.menuAction())
        self.menu_bar.addAction(self.menuHelp.menuAction())
        self.menuFile.addAction(self.actionOption1)
        self.menuFile.addAction(self.menuOption2.menuAction())
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionOption3)
        self.menuFile.addAction(self.actionOption4)
        self.menuOption2.addAction(self.actionSuboption1)
        self.menuOption2.addAction(self.actionSuboption2)
        self.menuOption2.addAction(self.actionSuboption3)
        self.menuHelp.addAction(self.actionManual)
        self.menuHelp.addAction(self.actionContact)
        self.menuHelp.addAction(self.actionAbout)
        self.menuMenu.addAction(self.menuCheck_Status.menuAction())
        self.menuMenu.addAction(self.menuRadio_Status.menuAction())
        self.menuCheck_Status.addAction(self.actionChecked)
        self.menuCheck_Status.addAction(self.actionUnchecked)
        self.menuRadio_Status.addAction(self.radio1_menu_action)
        self.menuRadio_Status.addAction(self.radio2_menu_action)

        self.retranslateUi(main_window)

        self.example_tab.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(main_window)
    # setupUi

    def retranslateUi(self, main_window):
        main_window.setWindowTitle(QCoreApplication.translate("main_window", u"QSS Design System", None))
        self.actionOption1.setText(QCoreApplication.translate("main_window", u"Option1", None))
        self.actionOption3.setText(QCoreApplication.translate("main_window", u"Option3", None))
        self.actionOption4.setText(QCoreApplication.translate("main_window", u"Option4", None))
        self.actionSuboption1.setText(QCoreApplication.translate("main_window", u"Suboption1", None))
        self.actionSuboption2.setText(QCoreApplication.translate("main_window", u"Suboption2", None))
        self.actionSuboption3.setText(QCoreApplication.translate("main_window", u"Suboption3", None))
        self.actionManual.setText(QCoreApplication.translate("main_window", u"Manual", None))
        self.actionAbout.setText(QCoreApplication.translate("main_window", u"About", None))
        self.actionContact.setText(QCoreApplication.translate("main_window", u"Contact", None))
        self.actionChecked.setText(QCoreApplication.translate("main_window", u"Checked", None))
        self.actionUnchecked.setText(QCoreApplication.translate("main_window", u"Unchecked", None))
        self.radio1_menu_action.setText(QCoreApplication.translate("main_window", u"Radio1", None))
        self.radio2_menu_action.setText(QCoreApplication.translate("main_window", u"Radio2", None))
        self.primary_button.setText(QCoreApplication.translate("main_window", u"Primary Button", None))
        self.default_button.setText(QCoreApplication.translate("main_window", u"Default Button", None))
        self.dashed_button.setText(QCoreApplication.translate("main_window", u"Dashed Button", None))
        self.text_button.setText(QCoreApplication.translate("main_window", u"Text Button", None))
        self.link_button.setText(QCoreApplication.translate("main_window", u"Link Button", None))
        self.base_style_label.setText(QCoreApplication.translate("main_window", u"TextLabel", None))
        self.large_button.setText(QCoreApplication.translate("main_window", u"Large Button", None))
        self.small_button.setText(QCoreApplication.translate("main_window", u"Small Button", None))
        self.disable_push_button.setText(QCoreApplication.translate("main_window", u"Disable Button", None))
        self.size_style_label.setText(QCoreApplication.translate("main_window", u"TextLabel", None))
        self.primary_danger_button.setText(QCoreApplication.translate("main_window", u"Danger", None))
        self.default_danger_button.setText(QCoreApplication.translate("main_window", u"Danger", None))
        self.dashed_danger_button.setText(QCoreApplication.translate("main_window", u"Danger", None))
        self.text_danger_button.setText(QCoreApplication.translate("main_window", u"Danger", None))
        self.link_danger_button.setText(QCoreApplication.translate("main_window", u"Danger", None))
        self.danger_style_label.setText(QCoreApplication.translate("main_window", u"TextLabel", None))
        self.example_tab.setTabText(self.example_tab.indexOf(self.tab_button), QCoreApplication.translate("main_window", u"QPushButton", None))
        self.default_style_tree_view_label.setText(QCoreApplication.translate("main_window", u"TextLabel", None))
        self.example_tab.setTabText(self.example_tab.indexOf(self.tab_treeview), QCoreApplication.translate("main_window", u"QTreeView", None))
        self.normal_line_edit.setPlaceholderText(QCoreApplication.translate("main_window", u"Normal LineEdit", None))
        self.sucess_line_edit.setPlaceholderText(QCoreApplication.translate("main_window", u"Suceess LineEdit", None))
        self.warning_line_edit.setPlaceholderText(QCoreApplication.translate("main_window", u"Warning LineEdit", None))
        self.error_line_edit.setPlaceholderText(QCoreApplication.translate("main_window", u"Error LineEdit", None))
        self.base_style_line_edit_label.setText(QCoreApplication.translate("main_window", u"TextLabel", None))
        self.disabled_line_edit.setPlaceholderText(QCoreApplication.translate("main_window", u"Disabled LineEdit", None))
        self.disable_line_edit_label.setText(QCoreApplication.translate("main_window", u"TextLabel", None))
        self.large_line_edit.setPlaceholderText(QCoreApplication.translate("main_window", u"Large Line Edit", None))
        self.small_line_edit.setPlaceholderText(QCoreApplication.translate("main_window", u"Small Line Edit", None))
        self.size_line_edit_label.setText(QCoreApplication.translate("main_window", u"TextLabel", None))
        self.example_tab.setTabText(self.example_tab.indexOf(self.tab_line_edit), QCoreApplication.translate("main_window", u"QLineEdit", None))
        self.default_label.setText(QCoreApplication.translate("main_window", u"Default Label", None))
        self.info_label.setText(QCoreApplication.translate("main_window", u"Info Label", None))
        self.success_label.setText(QCoreApplication.translate("main_window", u"Success Label", None))
        self.warning_label.setText(QCoreApplication.translate("main_window", u"Warning Label", None))
        self.error_label.setText(QCoreApplication.translate("main_window", u"Error Label", None))
        self.large_label.setText(QCoreApplication.translate("main_window", u"Large Label", None))
        self.small_label.setText(QCoreApplication.translate("main_window", u"Small Label", None))
        self.label_help_label.setText(QCoreApplication.translate("main_window", u"TextLabel", None))
        self.example_tab.setTabText(self.example_tab.indexOf(self.tab_label), QCoreApplication.translate("main_window", u"QLabel", None))
        self.click_to_view_context_menu_label.setText(QCoreApplication.translate("main_window", u"Right-click me", None))
        self.example_tab.setTabText(self.example_tab.indexOf(self.tab_menu), QCoreApplication.translate("main_window", u"QMenu", None))
        self.label.setText(QCoreApplication.translate("main_window", u"Left Panel", None))
        self.splitter_help_label.setText(QCoreApplication.translate("main_window", u"Top Panel", None))
        self.label_3.setText(QCoreApplication.translate("main_window", u"Bottom Panel", None))
        self.example_tab.setTabText(self.example_tab.indexOf(self.tab_splitter), QCoreApplication.translate("main_window", u"QSplitter", None))
        self.plain_text_edit_style_label.setText(QCoreApplication.translate("main_window", u"TextLabel", None))
        self.example_tab.setTabText(self.example_tab.indexOf(self.tab_plain_text_edit), QCoreApplication.translate("main_window", u"QPlainTextEdit", None))
        self.text_browser_help_label.setText(QCoreApplication.translate("main_window", u"TextLabel", None))
        self.example_tab.setTabText(self.example_tab.indexOf(self.tab_text_browser), QCoreApplication.translate("main_window", u"QTextBrowser", None))
        self.default_check_box.setText(QCoreApplication.translate("main_window", u"Default CheckBox", None))
        self.small_check_box.setText(QCoreApplication.translate("main_window", u"Small CheckBox", None))
        self.large_check_box.setText(QCoreApplication.translate("main_window", u"Large CheckBox", None))
        self.disabled_uncheck_box.setText(QCoreApplication.translate("main_window", u"Unchecked CheckBox", None))
        self.disable_checked_box.setText(QCoreApplication.translate("main_window", u"Checked CheckBox", None))
        self.check_box_help_label.setText(QCoreApplication.translate("main_window", u"TextLabel", None))
        self.example_tab.setTabText(self.example_tab.indexOf(self.check_box_tab), QCoreApplication.translate("main_window", u"QCheckBox", None))
        self.label_4.setText(QCoreApplication.translate("main_window", u"Default", None))
        self.label_5.setText(QCoreApplication.translate("main_window", u"Small", None))
        self.label_2.setText(QCoreApplication.translate("main_window", u"Large", None))
        self.combo_box_help_label.setText(QCoreApplication.translate("main_window", u"TextLabel", None))
        self.example_tab.setTabText(self.example_tab.indexOf(self.combo_box_tab), QCoreApplication.translate("main_window", u"QComboBox", None))
        self.status_bar_default_push_button.setText(QCoreApplication.translate("main_window", u"Default Status", None))
        self.status_bar_info_push_button.setText(QCoreApplication.translate("main_window", u"Info Status", None))
        self.status_bar_warning_push_button.setText(QCoreApplication.translate("main_window", u"Warning", None))
        self.status_bar_error_push_button.setText(QCoreApplication.translate("main_window", u"Error Status", None))
        self.status_bar_help_label.setText(QCoreApplication.translate("main_window", u"TextLabel", None))
        self.example_tab.setTabText(self.example_tab.indexOf(self.status_bar_tab), QCoreApplication.translate("main_window", u"QStatusBar", None))
        self.spin_box_small_label.setText(QCoreApplication.translate("main_window", u"Small", None))
        self.spin_box_default_label.setText(QCoreApplication.translate("main_window", u"Default", None))
        self.spin_box_large_label.setText(QCoreApplication.translate("main_window", u"Large", None))
        self.spin_box_success_label.setText(QCoreApplication.translate("main_window", u"Success", None))
        self.spin_box_warning_label.setText(QCoreApplication.translate("main_window", u"Warning", None))
        self.spin_box_error_label.setText(QCoreApplication.translate("main_window", u"Error", None))
        self.spin_box_help_label.setText(QCoreApplication.translate("main_window", u"TextLabel", None))
        self.example_tab.setTabText(self.example_tab.indexOf(self.spin_box_tab), QCoreApplication.translate("main_window", u"QSpinBox", None))
        self.menuFile.setTitle(QCoreApplication.translate("main_window", u"File", None))
        self.menuOption2.setTitle(QCoreApplication.translate("main_window", u"Option2", None))
        self.menuHelp.setTitle(QCoreApplication.translate("main_window", u"Help", None))
        self.menuMenu.setTitle(QCoreApplication.translate("main_window", u"Menu", None))
        self.menuCheck_Status.setTitle(QCoreApplication.translate("main_window", u"Check Status", None))
        self.menuRadio_Status.setTitle(QCoreApplication.translate("main_window", u"Radio Status", None))
    # retranslateUi

