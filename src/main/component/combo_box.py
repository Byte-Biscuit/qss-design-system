# -*- coding: utf-8 -*-
from PySide6.QtWidgets import QMainWindow, QLabel, QComboBox
from main.i18n import get_text
from main.logger_config import log


def apply_combo_box_style(window: QMainWindow):
    log.info("Apply combo_box style")
    default_combo_box: QComboBox = window.default_combo_box
    small_combo_box: QComboBox = window.small_combo_box
    large_combo_box: QComboBox = window.large_combo_box

    # Add sample data: Top 10 tourist attractions (default_combo_box)
    attractions = [
        "Great Wall of China",
        "Eiffel Tower",
        "Machu Picchu",
        "Statue of Liberty",
        "Colosseum",
        "Taj Mahal",
        "Grand Canyon",
        "Christ the Redeemer",
        "Pyramids of Giza",
        "Sydney Opera House",
    ]
    default_combo_box.addItems(attractions)

    # Add sample data: Top 10 classic novels (small_combo_box)
    novels = [
        "Pride and Prejudice",
        "Moby-Dick",
        "War and Peace",
        "The Great Gatsby",
        "1984",
        "To Kill a Mockingbird",
        "Crime and Punishment",
        "The Catcher in the Rye",
        "Jane Eyre",
        "The Odyssey",
    ]
    small_combo_box.addItems(novels)
    small_combo_box.setProperty("class", "small")

    # Add sample data: Top 10 movies (large_combo_box)
    movies = [
        "The Godfather",
        "The Shawshank Redemption",
        "Schindler's List",
        "Pulp Fiction",
        "The Dark Knight",
        "Forrest Gump",
        "Inception",
        "Fight Club",
        "The Lord of the Rings",
        "Star Wars",
    ]
    large_combo_box.addItems(movies)
    large_combo_box.setProperty("class", "large")
    combo_box_help_label: QLabel = window.combo_box_help_label
    combo_box_help_label.setProperty("class", "help")
    combo_box_help_label.setText(get_text("combo_box_style"))
