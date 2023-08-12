import os

from PySide6.QtGui import QDragEnterEvent, QDropEvent
from PySide6.QtWidgets import QWidget, QLabel, QVBoxLayout, QHBoxLayout, QPushButton, QFileDialog, QListWidget

from GlobalSettings import global_settings


class InputFolderPathsWidget(QWidget):
    def __init__(self):
        super(InputFolderPathsWidget, self).__init__()
        self.setup_ui()

    def setup_ui(self):
        layout_main = QVBoxLayout()
        layout_main.setContentsMargins(0, 0, 0, 0)
        layout_main.setSpacing(0)
        layout_title = QHBoxLayout()
        layout_title.setContentsMargins(0, 0, 0, 0)
        layout_title.setSpacing(0)
        title_label = QLabel("需要处理的合集文件夹")
        title_label.setStyleSheet("font-size: 15px; color: #000000;")
        layout_title.addWidget(title_label)
        layout_title.addStretch(1)
        self.add_folder_button = QPushButton("添加")
        self.add_folder_button.setStyleSheet(f"""
        QPushButton {{
            font-size: 14px;
            color: #000000;
            background-color: #FFFFFF;
            border: 1px solid #000000;
            border-radius: 5px;
            }}""")
        self.add_folder_button.setFixedSize(60, 30)
        self.add_folder_button.clicked.connect(self.add_folder_button_clicked)
        layout_title.addWidget(self.add_folder_button)
        layout_title.addSpacing(5)
        self.delete_folder_button = QPushButton("删除")
        self.delete_folder_button.setStyleSheet(f"""
        QPushButton {{
            font-size: 14px;
            color: #000000;
            background-color: #FFFFFF;
            border: 1px solid #000000;
            border-radius: 5px;
            }}""")
        self.delete_folder_button.setFixedSize(60, 30)
        self.delete_folder_button.clicked.connect(self.delete_folder_button_clicked)
        layout_title.addWidget(self.delete_folder_button)
        layout_main.addLayout(layout_title)
        layout_main.addSpacing(5)
        self.show_list = QListWidget()
        self.show_list.setStyleSheet("""
        QListWidget {
            font-size: 12px;
            color: #000000;
            background-color: #7f7f7f;
            border: 2px solid #000000;
            border-radius: 5px;
            outline: none;
            }
        QListWidget::item {
            height: 30px;
            padding: 5px;
            background-color: #aaaaaa;
            }
        QListWidget::item:selected {
            background-color: #dddddd;
            color: #000000;
            }""")
        layout_main.addWidget(self.show_list)
        self.setLayout(layout_main)
        self.setAcceptDrops(True)

    def add_folder_button_clicked(self):
        new_path = QFileDialog.getExistingDirectory(self, "请选择需要处理的合集文件夹")
        if new_path:
            for path in global_settings.choose_folder_paths:
                if path == new_path:
                    return
            global_settings.choose_folder_paths.append(new_path)
            self.show_list.clear()
            for path in global_settings.choose_folder_paths:
                self.show_list.addItem(path)

    def delete_folder_button_clicked(self):
        if self.show_list.currentItem() is None:
            return
        global_settings.choose_folder_paths.remove(self.show_list.currentItem().text())
        self.show_list.clear()
        for path in global_settings.choose_folder_paths:
            self.show_list.addItem(path)

    def dragEnterEvent(self, event: QDragEnterEvent) -> None:
        if event.mimeData().hasFormat("text/uri-list"):
            event.acceptProposedAction()

    def dropEvent(self, event: QDropEvent) -> None:
        urls = event.mimeData().urls()
        if urls is []:
            return
        for url in urls:
            real_url = url.toLocalFile()
            if os.path.isdir(real_url):
                for path in global_settings.choose_folder_paths:
                    if path == real_url:
                        return
                global_settings.choose_folder_paths.append(real_url)
        self.show_list.clear()
        for path in global_settings.choose_folder_paths:
            self.show_list.addItem(path)
