from typing import Union

from PySide6.QtWidgets import QTableWidget, QTableWidgetItem, QHeaderView
from PySide6.QtCore import Qt


def fill_account_table(table: QTableWidget, data: Union[list, None], headers: list):
    row = 0
    if data is not None:
        table.setColumnCount(2)
        table.setHorizontalHeaderLabels(headers)
        table.setRowCount(len(data))
        table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        for datas in data:
            table.setItem(row, 0, QTableWidgetItem(datas[0]))
            total_item = QTableWidgetItem(f"{datas[1]:.2f}")
            total_item.setTextAlignment(Qt.AlignmentFlag.AlignRight)
            table.setItem(row, 1, total_item)
            row += 1

