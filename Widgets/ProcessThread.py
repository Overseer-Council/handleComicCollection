import os
import shutil

from PySide6.QtCore import Signal, QThread

from GlobalSettings import global_settings


class ProcessThread(QThread):
    finish_signal = Signal(bool)

    def __init__(self):
        super(ProcessThread, self).__init__()
        self.stop_flag = False

    def run(self):
        for path in global_settings.choose_folder_paths:
            if self.stop_flag:
                self.finish_signal.emit(False)
                return
            cur_origin_parent_folder_path = path
            if os.path.exists(os.path.join(global_settings.save_path, os.path.basename(path))):
                shutil.rmtree(os.path.join(global_settings.save_path, os.path.basename(path)))
            os.makedirs(os.path.join(global_settings.save_path, os.path.basename(path)))
            cur_aim_parent_folder_path = os.path.join(global_settings.save_path, os.path.basename(path))
            if global_settings.enable_secondary_folder:
                for secondary_folder in os.listdir(cur_origin_parent_folder_path):
                    if self.stop_flag:
                        self.finish_signal.emit(False)
                        return
                    if not os.path.isdir(os.path.join(cur_origin_parent_folder_path, secondary_folder)):
                        shutil.copy(os.path.join(cur_origin_parent_folder_path, secondary_folder), os.path.join(cur_aim_parent_folder_path, secondary_folder))
                        continue
                    is_choose_folder = False
                    for choose_folder_name in global_settings.choose_folder_names:
                        if self.stop_flag:
                            self.finish_signal.emit(False)
                            return
                        if choose_folder_name in secondary_folder:
                            is_choose_folder = True
                            break
                    if is_choose_folder:
                        if not os.path.exists(os.path.join(cur_aim_parent_folder_path, secondary_folder)):
                            os.makedirs(os.path.join(cur_aim_parent_folder_path, secondary_folder))
                        for content_folder in os.listdir(os.path.join(cur_origin_parent_folder_path, secondary_folder)):
                            if self.stop_flag:
                                self.finish_signal.emit(False)
                                return
                            if not os.path.isdir(os.path.join(cur_origin_parent_folder_path, secondary_folder, content_folder)):
                                shutil.copy(os.path.join(cur_origin_parent_folder_path, secondary_folder, content_folder),
                                            os.path.join(cur_aim_parent_folder_path, secondary_folder, content_folder))
                                continue
                            is_denied = False
                            for deny_word in global_settings.deny_words:
                                if self.stop_flag:
                                    self.finish_signal.emit(False)
                                    return
                                if deny_word in content_folder:
                                    is_denied = True
                                    break
                            if not is_denied:
                                for hint_word in global_settings.hint_words:
                                    if self.stop_flag:
                                        self.finish_signal.emit(False)
                                        return
                                    if hint_word in content_folder:
                                        shutil.copytree(os.path.join(cur_origin_parent_folder_path, secondary_folder, content_folder), os.path.join(cur_aim_parent_folder_path, secondary_folder, content_folder))
                                        break
                        if global_settings.remain_no_translate_japanese_version:
                            for content_folder in os.listdir(os.path.join(cur_origin_parent_folder_path, secondary_folder)):
                                if self.stop_flag:
                                    self.finish_signal.emit(False)
                                    return
                                if not os.path.isdir(os.path.join(cur_origin_parent_folder_path, secondary_folder, content_folder)):
                                    continue
                                is_denied = False
                                for deny_word in global_settings.deny_words:
                                    if self.stop_flag:
                                        self.finish_signal.emit(False)
                                        return
                                    if deny_word in content_folder:
                                        is_denied = True
                                        break
                                if not is_denied:
                                    is_hint = False
                                    for hint_word in global_settings.hint_words:
                                        if self.stop_flag:
                                            self.finish_signal.emit(False)
                                            return
                                        if hint_word in content_folder:
                                            is_hint = True
                                            break
                                    if not is_hint:
                                        is_translation_version_available = False
                                        for exist_folder in os.listdir(os.path.join(cur_aim_parent_folder_path, secondary_folder)):
                                            if self.stop_flag:
                                                self.finish_signal.emit(False)
                                                return
                                            if content_folder in exist_folder:
                                                is_translation_version_available = True
                                                break
                                        if not is_translation_version_available:
                                            shutil.copytree(os.path.join(cur_origin_parent_folder_path, secondary_folder, content_folder), os.path.join(cur_aim_parent_folder_path, secondary_folder, content_folder))
                    else:
                        if global_settings.not_choose_secondary_folder_copy:
                            shutil.copytree(os.path.join(cur_origin_parent_folder_path, secondary_folder), os.path.join(cur_aim_parent_folder_path, secondary_folder))
            else:
                for content_folder in os.listdir(os.path.join(cur_origin_parent_folder_path)):
                    if self.stop_flag:
                        self.finish_signal.emit(False)
                        return
                    if not os.path.isdir(os.path.join(cur_origin_parent_folder_path, content_folder)):
                        shutil.copy(os.path.join(cur_origin_parent_folder_path, content_folder),
                                    os.path.join(cur_aim_parent_folder_path, content_folder))
                        continue
                    is_denied = False
                    for deny_word in global_settings.deny_words:
                        if self.stop_flag:
                            self.finish_signal.emit(False)
                            return
                        if deny_word in content_folder:
                            is_denied = True
                            break
                    if not is_denied:
                        for hint_word in global_settings.hint_words:
                            if self.stop_flag:
                                self.finish_signal.emit(False)
                                return
                            if hint_word in content_folder:
                                shutil.copytree(os.path.join(cur_origin_parent_folder_path, content_folder), os.path.join(cur_aim_parent_folder_path, content_folder))
                                break
                if global_settings.remain_no_translate_japanese_version:
                    for content_folder in os.listdir(os.path.join(cur_origin_parent_folder_path)):
                        if self.stop_flag:
                            self.finish_signal.emit(False)
                            return
                        if not os.path.isdir(os.path.join(cur_origin_parent_folder_path, content_folder)):
                            continue
                        is_denied = False
                        for deny_word in global_settings.deny_words:
                            if self.stop_flag:
                                self.finish_signal.emit(False)
                                return
                            if deny_word in content_folder:
                                is_denied = True
                                break
                        if not is_denied:
                            is_hint = False
                            for hint_word in global_settings.hint_words:
                                if self.stop_flag:
                                    self.finish_signal.emit(False)
                                    return
                                if hint_word in content_folder:
                                    is_hint = True
                                    break
                            if not is_hint:
                                is_translation_version_available = False
                                for exist_folder in os.listdir(
                                        os.path.join(cur_aim_parent_folder_path)):
                                    if content_folder in exist_folder:
                                        is_translation_version_available = True
                                        break
                                if not is_translation_version_available:
                                    shutil.copytree(os.path.join(cur_origin_parent_folder_path, content_folder), os.path.join(cur_aim_parent_folder_path, content_folder))
        self.finish_signal.emit(True)

    def cancel(self):
        self.stop_flag = True
