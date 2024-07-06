import PySide6
from PySide6 import QtCore
from PySide6.QtCore import Qt, Signal, Slot
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QDialog, QMessageBox
from sqlalchemy import select
from sqlalchemy.orm import scoped_session, Session

from BudgetMagician.dialogs.ManageCategoriesUi import Ui_ManageCategories
from BudgetMagician.magician.models import BudgetCategory, BudgetSubcategory
from BudgetMagician.magician.queries import get_names_list
from BudgetMagician.utils.combox_utils import set_combo_box_by_data, fill_combo_box, get_combo_box_dict_from_list
from BudgetMagician.utils.db import get_magic_session
from BudgetMagician.utils.qt import translate


class ManageCategories(QDialog, Ui_ManageCategories):
    categories_changed = Signal()

    def __init__(self, parent, budget_file):
        super().__init__(parent)
        self.budget_file = budget_file
        self.setupUi(self)
        self.setWindowFlag(Qt.WindowType.FramelessWindowHint)
        self.installEventFilter(self)
        self.master_category_combo.installEventFilter(self)
        self.delete_button.setIcon(QIcon(":icons/lucide/delete.svg"))
        self.fill_ui()
        self.delete_button.clicked.connect(self.delete_master_category)
        self.cancel_button.clicked.connect(self.close)
        self.ok_button.clicked.connect(self.add_category)
        self.category_line_edit.textChanged.connect(self.check_disabled)
        self.delete_category_button.clicked.connect(self.delete_category)

    def fill_ui(self):
        master_category_combobox_dict = get_combo_box_dict_from_list(get_names_list(self.budget_file, BudgetCategory))
        fill_combo_box(self.master_category_combo, master_category_combobox_dict)
        set_combo_box_by_data(self.master_category_combo, 0)

        category_combobox_dict = get_combo_box_dict_from_list(get_names_list(self.budget_file, BudgetSubcategory))
        fill_combo_box(self.category_combobox, category_combobox_dict)
        set_combo_box_by_data(self.category_combobox, 0)

        self.category_line_edit.setText("")
        self.ok_button.setEnabled(False)

    @Slot()
    def check_disabled(self):
        enabled = bool(self.category_line_edit.text())
        self.ok_button.setEnabled(enabled)

    def add_master_category(self):
        master_category_text = self.master_category_combo.currentText()

        if len(master_category_text) == 0:
            QMessageBox.warning(self, translate("Dialog", "Warning"), translate("Warning", "You must provide a master category name."), QMessageBox.StandardButton.Ok)
        else:
            db: scoped_session[Session]
            with get_magic_session(self.budget_file) as db:
                master_category_from_db = db.scalars(select(BudgetCategory).where(BudgetCategory.name == master_category_text)).first()

                if master_category_from_db is None:
                    budget_category = BudgetCategory()
                    budget_category.name = master_category_text
                    db.add(budget_category)
                    db.commit()

                    self.fill_ui()
                    self.categories_changed.emit()
                else:
                    QMessageBox.warning(
                        self, translate("Dialog", "Warning"), translate("Warning", "The master category name provided already exists."), QMessageBox.StandardButton.Ok
                    )

    @Slot()
    def add_category(self):
        master_category_text = self.master_category_combo.currentText()
        new_category = self.category_line_edit.text()

        if len(new_category) == 0:
            QMessageBox.warning(self, translate("Dialog", "Warning"), translate("Warning", "You must provide a category name."), QMessageBox.StandardButton.Ok)
        else:
            db: scoped_session[Session]
            with get_magic_session(self.budget_file) as db:
                master_category_id = db.execute(select(BudgetCategory.id).where(BudgetCategory.name == master_category_text)).first()
                category = db.scalars(select(BudgetSubcategory).where(BudgetSubcategory.name == new_category)).first()

                if category is None:
                    if master_category_id is None:
                        QMessageBox.critical(
                            self,
                            translate("Dialog", "Critical"),
                            translate("Critical", "There was an error and the master category selected cannot be found."),
                            QMessageBox.StandardButton.Ok,
                        )
                    else:
                        category = BudgetSubcategory()
                        category.name = new_category
                        category.budget_category_id = master_category_id.id
                        db.add(category)
                        db.commit()

                        self.categories_changed.emit()
                        self.close()
                else:
                    QMessageBox.warning(self, translate("Dialog", "Warning"), translate("Warning", "The category name provided already exists."), QMessageBox.StandardButton.Ok)

    @Slot()
    def delete_master_category(self):
        current_text = self.master_category_combo.currentText()

        db: scoped_session[Session]
        with get_magic_session(self.budget_file) as db:
            budget_category = db.scalars(select(BudgetCategory).where(BudgetCategory.name == current_text)).first()

            if budget_category is not None:
                db.delete(budget_category)
                db.commit()
                self.categories_changed.emit()

        self.fill_ui()

    @Slot()
    def delete_category(self):
        current_text = self.category_combobox.currentText()

        db: scoped_session[Session]
        with get_magic_session(self.budget_file) as db:
            budget_subcategory = db.scalars(select(BudgetSubcategory).where(BudgetSubcategory.name == current_text)).first()

            if budget_subcategory is not None:
                db.delete(budget_subcategory)
                db.commit()
                self.categories_changed.emit()

        self.fill_ui()

    def open(self) -> None:
        self.fill_ui()
        return super().open()

    def eventFilter(self, arg__1: PySide6.QtCore.QObject, arg__2: PySide6.QtCore.QEvent) -> bool:
        if arg__1 == self.master_category_combo and arg__2.type() == QtCore.QEvent.Type.KeyPress:
            if arg__2.key() in (Qt.Key.Key_Return, Qt.Key.Key_Enter):
                self.add_master_category()
                return True
        if arg__1 is self and arg__2.type() == QtCore.QEvent.Type.KeyPress:
            if arg__2.key() in (Qt.Key.Key_Return, Qt.Key.Key_Escape, Qt.Key.Key_Enter):
                return True
        return super().eventFilter(arg__1, arg__2)
