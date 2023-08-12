from PySide6.QtWidgets import QWidget, QHBoxLayout, QCheckBox

from GlobalSettings import global_settings


class CheckBoxWidget(QWidget):
    def __init__(self):
        super(CheckBoxWidget, self).__init__()
        self.setup_ui()

    def setup_ui(self):
        layout_widget = QHBoxLayout()
        layout_widget.setContentsMargins(0, 0, 0, 0)
        layout_widget.setSpacing(5)
        self.is_enable_secondary_folder = QCheckBox("是否启用二级文件夹处理(关闭后将认为一级文件夹下即为所需处理内容文件夹)")
        self.is_enable_secondary_folder.setChecked(global_settings.enable_secondary_folder)
        self.is_enable_secondary_folder.stateChanged.connect(lambda state: self.is_enable_secondary_folder_change(state))
        layout_widget.addWidget(self.is_enable_secondary_folder)
        self.is_not_choose_secondary_folder_copy = QCheckBox("是否复制未选二级文件夹(关闭后将不复制不符合条件的内容文件夹)")
        self.is_not_choose_secondary_folder_copy.setChecked(global_settings.not_choose_secondary_folder_copy)
        self.is_not_choose_secondary_folder_copy.stateChanged.connect(lambda state: self.is_not_choose_secondary_folder_copy_change(state))
        layout_widget.addWidget(self.is_not_choose_secondary_folder_copy)
        self.is_remain_no_translate_japanese_version = QCheckBox("是否保留无翻译的日文版")
        self.is_remain_no_translate_japanese_version.setChecked(global_settings.remain_no_translate_japanese_version)
        self.is_remain_no_translate_japanese_version.stateChanged.connect(lambda state: self.is_remain_no_translate_japanese_version_change(state))
        layout_widget.addWidget(self.is_remain_no_translate_japanese_version)
        self.setLayout(layout_widget)

    def is_enable_secondary_folder_change(self, state):
        global_settings.enable_secondary_folder = state

    def is_not_choose_secondary_folder_copy_change(self, state):
        global_settings.not_choose_secondary_folder_copy = state

    def is_remain_no_translate_japanese_version_change(self, state):
        global_settings.remain_no_translate_japanese_version = state
