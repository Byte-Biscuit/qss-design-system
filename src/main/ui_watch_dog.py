# -*- coding: utf-8 -*-

import time
import subprocess
from pathlib import Path
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from main.logger_config import log


work_dir = Path(__file__).resolve().parent


class UiFileHandler(FileSystemEventHandler):
    """
    Event handler for monitoring .ui files
    """

    def __init__(self, ui_dir: Path):
        super().__init__()
        self.ui_dir = ui_dir
        log.info(f"Initialized UiFileHandler for directory: {ui_dir}")

    def on_modified(self, event):
        """
        Triggered when a file is modified
        """
        if event.is_directory:
            log.info(f"Directory modified: {event.src_path}")
            return
        if event.src_path.endswith(".ui"):
            log.info(f"File modified: {event.src_path}")
            self.generate_py_file(event.src_path)

    def on_created(self, event):
        """
        Triggered when a file is created
        """
        if event.is_directory:
            log.info(f"Directory created: {event.src_path}")
            return
        if event.src_path.endswith(".ui"):
            self.generate_py_file(event.src_path)

    def on_moved(self, event):
        """
        Triggered when a file is moved or renamed
        """
        if event.is_directory:
            log.info(f"Directory moved: {event.src_path}")
            return
        if event.src_path.endswith(".ui"):
            self.generate_py_file(event.src_path)

    def dispatch(self, event):
        """
        Unified handler for all event types.
        """
        if event.is_directory:
            return

        if event.src_path.endswith(".ui") and Path(event.src_path).exists():
            log.info(f"[{event.event_type}] Detected UI file event: {event.src_path}")
            self.generate_py_file(event.src_path)

    def generate_py_file(self, ui_file_path: str):
        """
        Use pyside6-uic to convert .ui files to .py files
        """
        ui_file = Path(ui_file_path)
        py_file_name = ui_file.stem.replace("-", "_") + ".py"
        py_file_path = ui_file.parent / py_file_name

        try:
            # Execute the pyside6-uic command
            subprocess.run(
                ["pyside6-uic", str(ui_file), "-o", str(py_file_path)],
                check=True,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
            )
            log.info(f"Generated: {py_file_path}")
        except subprocess.CalledProcessError as e:
            log.error(f"Error generating {py_file_path}: {e.stderr.decode()}")


def monitor_ui_directory(ui_dir: Path):
    """
    Monitor the ui directory
    """
    event_handler = UiFileHandler(ui_dir)
    observer = Observer()
    observer.schedule(event_handler, str(ui_dir), recursive=True)
    observer.start()
    log.info(f"Monitoring directory: {ui_dir}")

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
        log.info("Stopped monitoring.")
    observer.join()


if __name__ == "__main__":
    # Set the ui directory path
    ui_directory = Path(work_dir, "ui")
    if not ui_directory.exists():
        log.error(f"Directory does not exist: {ui_directory}")
    else:
        monitor_ui_directory(ui_directory)
