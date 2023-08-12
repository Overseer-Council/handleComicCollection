import json
import os
import sys

from PySide6.QtWidgets import QMainWindow, QApplication, QVBoxLayout, QHBoxLayout, QLabel, QWidget

from GlobalSettings import global_settings
from Widgets.CheckBoxWidget import CheckBoxWidget
from Widgets.ChineseHintWordsWidget import ChineseHintWordsWidget
from Widgets.ChooseSavePathWidget import ChooseSavePathWidget
from Widgets.DenyWordsWidget import DenyWordsWidget
from Widgets.InputFolderPathsWidget import InputFolderPathsWidget
from Widgets.ProcessWidget import ProcessWidget
from Widgets.SecondaryFolderChoose import SecondaryFolderChooseWidget


class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.widget = QWidget()
        self.load_global_settings()
        self.setup_ui()
        self.setWindowTitle("南+合集处理器")
        self.setMinimumSize(1600, 900)

    def load_global_settings(self):
        settings_save_path = os.path.join(os.getcwd(), "settings.json")
        if os.path.exists(settings_save_path):
            setting_json = json.load(open(settings_save_path, "r", encoding="utf-8"))
            global_settings.set_settings(setting_json)

    def setup_ui(self):
        layout_main = QVBoxLayout()
        layout_main.setContentsMargins(5, 5, 5, 5)
        layout_main.setSpacing(10)
        layout_up = QHBoxLayout()
        layout_up.setContentsMargins(0, 0, 0, 0)
        layout_up.setSpacing(5)
        layout_part_one = QVBoxLayout()
        layout_part_one.setContentsMargins(0, 0, 0, 0)
        layout_part_one.setSpacing(0)
        self.input_folder_paths_widget = InputFolderPathsWidget()
        layout_part_one.addWidget(self.input_folder_paths_widget)
        layout_up.addLayout(layout_part_one)
        layout_part_two = QVBoxLayout()
        layout_part_two.setContentsMargins(0, 0, 0, 0)
        layout_part_two.setSpacing(0)
        self.secondary_folder_choose_widget = SecondaryFolderChooseWidget()
        layout_part_two.addWidget(self.secondary_folder_choose_widget)
        layout_up.addLayout(layout_part_two)
        layout_part_three = QVBoxLayout()
        layout_part_three.setContentsMargins(0, 0, 0, 0)
        layout_part_three.setSpacing(0)
        self.chinese_hint_words_widget = ChineseHintWordsWidget()
        layout_part_three.addWidget(self.chinese_hint_words_widget)
        layout_up.addLayout(layout_part_three)
        layout_part_four = QVBoxLayout()
        layout_part_four.setContentsMargins(0, 0, 0, 0)
        layout_part_four.setSpacing(0)
        self.deny_words_widget = DenyWordsWidget()
        layout_part_four.addWidget(self.deny_words_widget)
        layout_up.addLayout(layout_part_four)
        layout_main.addLayout(layout_up)
        layout_down = QVBoxLayout()
        layout_down.setContentsMargins(0, 0, 0, 0)
        layout_down.setSpacing(5)
        settings_label = QLabel("设置")
        settings_label.setStyleSheet("font-size: 15px; color: #000000;")
        layout_down.addWidget(settings_label)
        self.setting_checkboxs = CheckBoxWidget()
        layout_down.addWidget(self.setting_checkboxs)
        self.save_path_widget = ChooseSavePathWidget()
        layout_down.addWidget(self.save_path_widget)
        self.process_widget = ProcessWidget()
        layout_down.addWidget(self.process_widget)
        layout_main.addLayout(layout_down)
        self.widget.setLayout(layout_main)
        self.setCentralWidget(self.widget)
        self.widget.show()
        self.setStyleSheet("""
        QMainWindow {
            background-color: #ffffff;
            }""")

    def closeEvent(self, event):
        self.save_global_settings()
        event.accept()

    def save_global_settings(self):
        settings_save_path = os.path.join(os.getcwd(), "settings.json")
        with open(settings_save_path, "w", encoding="utf-8") as f:
            json.dump(global_settings.get_settings(), f, ensure_ascii=False, indent=4)


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
