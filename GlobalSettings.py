class GlobalSettings:
    choose_folder_paths = []
    enable_secondary_folder = True
    not_choose_secondary_folder_copy = True
    remain_no_translate_japanese_version = True
    choose_folder_names = ["同人志", "商业志", "单行本"]
    hint_words = ["汉化", "漢化", "单行本", "重嵌", "禁漫天堂", "简体中文", "中文版", "CE家族社", "譯", "4K掃圖組"]
    deny_words = ["別スキャン", "英訳", "韩訳"]
    save_path = "D:/nan_comic_save"

    def set_settings(self, settings):
        self.enable_secondary_folder = settings["enable_secondary_folder"]
        self.not_choose_secondary_folder_copy = settings["not_choose_secondary_folder_copy"]
        self.remain_no_translate_japanese_version = settings["remain_no_translate_japanese_version"]
        self.choose_folder_names = settings["choose_folder_names"]
        self.hint_words = settings["hint_words"]
        self.deny_words = settings["deny_words"]
        self.save_path = settings["save_path"]

    def get_settings(self):
        return {
            "enable_secondary_folder": self.enable_secondary_folder,
            "not_choose_secondary_folder_copy": self.not_choose_secondary_folder_copy,
            "remain_no_translate_japanese_version": self.remain_no_translate_japanese_version,
            "choose_folder_names": self.choose_folder_names,
            "hint_words": self.hint_words,
            "deny_words": self.deny_words,
            "save_path": self.save_path
        }


global_settings = GlobalSettings()
