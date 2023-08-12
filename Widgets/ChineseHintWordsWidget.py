from PySide6.QtWidgets import QWidget, QLabel, QVBoxLayout, QHBoxLayout, QPushButton, QListWidget, \
    QInputDialog, QLineEdit

from GlobalSettings import global_settings


class ChineseHintWordsWidget(QWidget):
    def __init__(self):
        super(ChineseHintWordsWidget, self).__init__()
        self.setup_ui()

    def setup_ui(self):
        layout_main = QVBoxLayout()
        layout_main.setContentsMargins(0, 0, 0, 0)
        layout_main.setSpacing(0)
        layout_title = QHBoxLayout()
        layout_title.setContentsMargins(0, 0, 0, 0)
        layout_title.setSpacing(0)
        title_label = QLabel("保留内容标识词")
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
        layout_hint = QHBoxLayout()
        layout_hint.setContentsMargins(0, 0, 0, 0)
        layout_hint.setSpacing(0)
        hint_label = QLabel("如输入”汉化“，则所有名称中含有”汉化“的文件夹均会被保留。\n如果此处不输入任何内容，则默认保留所有文件夹。")
        hint_label.setStyleSheet("font-size: 12px; color: #000000;")
        layout_hint.addWidget(hint_label)
        layout_main.addLayout(layout_hint)
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
        for word in global_settings.hint_words:
            self.show_list.addItem(word)
        layout_main.addWidget(self.show_list)
        self.setLayout(layout_main)

    def add_folder_button_clicked(self):
        new_path = QInputDialog.getText(self, "标识词设置", "请输入新的汉化标识词", QLineEdit.Normal)
        if new_path[0] and new_path[1]:
            for word in global_settings.hint_words:
                if word == new_path[0]:
                    return
            global_settings.hint_words.append(new_path[0])
            self.show_list.clear()
            for word in global_settings.hint_words:
                self.show_list.addItem(word)

    def delete_folder_button_clicked(self):
        if self.show_list.currentItem() is None:
            return
        global_settings.hint_words.remove(self.show_list.currentItem().text())
        self.show_list.clear()
        for word in global_settings.hint_words:
            self.show_list.addItem(word)
