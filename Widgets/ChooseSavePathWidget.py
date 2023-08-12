from PySide6.QtWidgets import QWidget, QHBoxLayout, QLabel, QPushButton, QFileDialog

from GlobalSettings import global_settings


class ChooseSavePathWidget(QWidget):
    def __init__(self):
        super(ChooseSavePathWidget, self).__init__()
        self.setup_ui()

    def setup_ui(self):
        layout_main = QHBoxLayout()
        layout_main.setContentsMargins(0, 0, 0, 0)
        layout_main.addSpacing(5)
        self.path_label = QLabel(global_settings.save_path)
        self.path_label.setStyleSheet("""
        QLabel {
            background-color:#cccccc;
            border-radius: 5px;
            font-size: 12px;
            color: #000000;
            padding:5px;
            }""")
        layout_main.addWidget(self.path_label)
        self.choose_path_button = QPushButton("选择保存路径")
        self.choose_path_button.setFixedSize(100, 30)
        self.choose_path_button.setStyleSheet(f"""
        QPushButton {{
            font-size: 14px;
            color: #000000;
            background-color: #FFFFFF;
            border: 1px solid #000000;
            border-radius: 5px;
            }}""")
        self.choose_path_button.clicked.connect(self.choose_save_path)
        layout_main.addWidget(self.choose_path_button)
        self.setLayout(layout_main)

    def choose_save_path(self):
        new_path = QFileDialog.getExistingDirectory(self, "请选择处理完的保存路径")
        if new_path:
            global_settings.save_path = new_path.replace("\\", "/")
            self.path_label.setText(global_settings.save_path)
