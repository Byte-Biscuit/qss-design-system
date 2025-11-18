# -*- coding: utf-8 -*-
from PySide6.QtWidgets import QMainWindow, QTreeView, QLabel, QHeaderView
from main.i18n import get_text
from main.logger_config import log
from PySide6.QtGui import QStandardItemModel, QStandardItem


def apply_tree_view_style(window: QMainWindow):
    log.info("Apply tree view style")
    # Base style
    tree_view: QTreeView = window.tree_view
    # Create a model for the tree view
    model = QStandardItemModel()
    model.setHorizontalHeaderLabels(["Region Information"])
    default_style_tree_view_label: QLabel = window.default_style_tree_view_label
    default_style_tree_view_label.setProperty("class", "help")
    default_style_tree_view_label.setText(get_text("default_style_tree_view"))
    # Define hierarchical data with more entries
    data = {
        "Asia": {
            "China": [
                "Beijing - Capital City of China with Ancient History and Modern Development",
                "Shanghai - The Largest Commercial and Financial Center in Eastern China",
                "Guangzhou - Historical Trading Port and Modern Manufacturing Hub",
                "Shenzhen - Special Economic Zone and Technology Innovation Center",
                "Chengdu - Home of Giant Pandas and Sichuan Cuisine Culture Center",
                "Wuhan - Major Transportation Hub and Educational Center of Central China",
            ],
            "Japan": [
                "Tokyo - The World's Largest Metropolitan Area and Japan's Capital",
                "Osaka - Major Economic Center and Historical Merchant City",
                "Kyoto - Ancient Capital with Over a Thousand Buddhist Temples",
                "Nagoya - Industrial Hub and Home to Toyota Motor Corporation" * 10,
                "Sapporo - Largest City in Hokkaido Famous for Snow Festival",
                "Fukuoka - Gateway to Asia and Major Port City of Western Japan",
            ],
        },
        # Rest of the data structure remains the same
        "Europe": {"Germany": [], "France": [], "Italy": []},
        "North America": {"USA": [], "Canada": [], "Mexico": []},
        "South America": {"Brazil": [], "Argentina": [], "Colombia": []},
        "Africa": {"South Africa": [], "Nigeria": [], "Egypt": []},
        "Oceania": {"Australia": [], "New Zealand": [], "Fiji": []},
    }

    # Populate the model with data
    for continent, countries in data.items():
        continent_item = QStandardItem(continent)
        for country, cities in countries.items():
            country_item = QStandardItem(country)
            for city in cities:
                city_item = QStandardItem(city)
                country_item.appendRow(city_item)
            continent_item.appendRow(country_item)
        model.appendRow(continent_item)

    # Set the model to the tree view
    tree_view.setModel(model)
