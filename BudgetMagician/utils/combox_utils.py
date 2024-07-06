from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QComboBox


def fill_combo_box_with_icon(combo_box: QComboBox, data_dict: dict):
    combo_box.clear()
    for idd, name in data_dict.items():
        combo_box.addItem(QIcon(name["icon"]), name["title"], idd)


def fill_combo_box(combo_box: QComboBox, data_dict: dict):
    combo_box.clear()
    for idd, name in data_dict.items():
        combo_box.addItem(name, idd)


def set_combo_box_by_data(combo_box: QComboBox, data_value):
    index = combo_box.findData(data_value)
    combo_box.setCurrentIndex(index)


def set_combo_box_by_text(combo_box: QComboBox, text: str):
    index = combo_box.findText(text)
    combo_box.setCurrentIndex(index)


def get_combo_box_dict_from_list(le_list: list) -> dict[int, str]:
    box_dict = {}
    row_number = 0

    for item in le_list:
        box_dict[row_number] = str(item)
        row_number += 1

    return box_dict
