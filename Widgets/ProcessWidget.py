from PySide6.QtWidgets import QWidget, QHBoxLayout, QProgressBar, QPushButton, QMessageBox

from Widgets.ProcessThread import ProcessThread


class ProcessWidget(QWidget):
    def __init__(self):
        super(ProcessWidget, self).__init__()
        self.is_running = False
        self.thread = ProcessThread()
        self.thread.finish_signal.connect(self.end_thread_dealer)
        self.setup_ui()

    def setup_ui(self):
        layout_main = QHBoxLayout()
        layout_main.setContentsMargins(0, 0, 0, 0)
        layout_main.setSpacing(5)
        self.progress_bar = QProgressBar()
        self.progress_bar.setTextVisible(False)
        layout_main.addWidget(self.progress_bar)
        self.control_button = QPushButton("运行")
        self.control_button.setFixedSize(60, 30)
        self.control_button.setStyleSheet("""
            QPushButton{
                font-size: 14px;
                color: #000000;
                background-color: #007F00;
                border: 1px solid #000000;
                border-radius: 5px;
            }""")
        self.control_button.clicked.connect(self.switch_running_status)
        layout_main.addWidget(self.control_button)
        self.setLayout(layout_main)

    def end_thread_dealer(self, state):
        self.control_button.setText("运行")
        self.control_button.setStyleSheet("""
            QPushButton{
                font-size: 14px;
                color: #000000;
                background-color: #007F00;
                border: 1px solid #000000;
                border-radius: 5px;
            }""")
        self.progress_bar.setMinimum(0)
        self.progress_bar.setMaximum(100)
        self.is_running = False
        if state:
            QMessageBox.information(self, "执行结果", "执行成功！", QMessageBox.Ok, QMessageBox.Ok)
        else:
            QMessageBox.critical(self, "执行结果", "执行取消！", QMessageBox.Ok, QMessageBox.Ok)

    def switch_running_status(self):
        if self.is_running:
            self.thread.cancel()
        else:
            self.is_running = True
            self.control_button.setText("中止")
            self.control_button.setStyleSheet("""
                QPushButton{
                    font-size: 14px;
                    color: #000000;
                    background-color: #FF6B68;
                    border: 1px solid #000000;
                    border-radius: 5px;
                }""")
            self.progress_bar.setMinimum(0)
            self.progress_bar.setMaximum(0)
            self.thread.start()
