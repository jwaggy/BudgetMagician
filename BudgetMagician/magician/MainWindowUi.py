# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWindow.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCharts import QChartView
from PySide6.QtCore import QCoreApplication, QDate, QDateTime, QLocale, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt
from PySide6.QtGui import (
    QBrush,
    QColor,
    QConicalGradient,
    QCursor,
    QFont,
    QFontDatabase,
    QGradient,
    QIcon,
    QImage,
    QKeySequence,
    QLinearGradient,
    QPainter,
    QPalette,
    QPixmap,
    QRadialGradient,
    QTransform,
)
from PySide6.QtWidgets import (
    QAbstractItemView,
    QApplication,
    QComboBox,
    QDateEdit,
    QFrame,
    QHBoxLayout,
    QHeaderView,
    QLabel,
    QLayout,
    QMainWindow,
    QMenuBar,
    QPushButton,
    QSizePolicy,
    QSpacerItem,
    QTabWidget,
    QTableView,
    QTableWidget,
    QTableWidgetItem,
    QVBoxLayout,
    QWidget,
)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1366, 768)
        MainWindow.setWindowTitle("BudgetMagician")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.budget_tab = QWidget()
        self.budget_tab.setObjectName("budget_tab")
        self.verticalLayout_4 = QVBoxLayout(self.budget_tab)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.manage_categories_button = QPushButton(self.budget_tab)
        self.manage_categories_button.setObjectName("manage_categories_button")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.manage_categories_button.sizePolicy().hasHeightForWidth())
        self.manage_categories_button.setSizePolicy(sizePolicy)
        self.manage_categories_button.setFocusPolicy(Qt.NoFocus)

        self.horizontalLayout_7.addWidget(self.manage_categories_button)

        self.budget_month_combo = QComboBox(self.budget_tab)
        self.budget_month_combo.setObjectName("budget_month_combo")
        sizePolicy.setHeightForWidth(self.budget_month_combo.sizePolicy().hasHeightForWidth())
        self.budget_month_combo.setSizePolicy(sizePolicy)
        self.budget_month_combo.setSizeAdjustPolicy(QComboBox.AdjustToContents)

        self.horizontalLayout_7.addWidget(self.budget_month_combo)

        self.budget_year_combo = QComboBox(self.budget_tab)
        self.budget_year_combo.setObjectName("budget_year_combo")
        sizePolicy.setHeightForWidth(self.budget_year_combo.sizePolicy().hasHeightForWidth())
        self.budget_year_combo.setSizePolicy(sizePolicy)
        self.budget_year_combo.setSizeAdjustPolicy(QComboBox.AdjustToContents)

        self.horizontalLayout_7.addWidget(self.budget_year_combo)

        self.horizontalSpacer_14 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_14)

        self.verticalLayout_4.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.not_budgeted_label = QLabel(self.budget_tab)
        self.not_budgeted_label.setObjectName("not_budgeted_label")
        sizePolicy.setHeightForWidth(self.not_budgeted_label.sizePolicy().hasHeightForWidth())
        self.not_budgeted_label.setSizePolicy(sizePolicy)
        font = QFont()
        font.setBold(True)
        self.not_budgeted_label.setFont(font)

        self.horizontalLayout_11.addWidget(self.not_budgeted_label)

        self.not_budgeted = QLabel(self.budget_tab)
        self.not_budgeted.setObjectName("not_budgeted")
        sizePolicy.setHeightForWidth(self.not_budgeted.sizePolicy().hasHeightForWidth())
        self.not_budgeted.setSizePolicy(sizePolicy)
        self.not_budgeted.setFont(font)

        self.horizontalLayout_11.addWidget(self.not_budgeted)

        self.horizontalSpacer_15 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_11.addItem(self.horizontalSpacer_15)

        self.verticalLayout_4.addLayout(self.horizontalLayout_11)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.overspent_label = QLabel(self.budget_tab)
        self.overspent_label.setObjectName("overspent_label")
        sizePolicy.setHeightForWidth(self.overspent_label.sizePolicy().hasHeightForWidth())
        self.overspent_label.setSizePolicy(sizePolicy)
        self.overspent_label.setFont(font)

        self.horizontalLayout_12.addWidget(self.overspent_label)

        self.horizontalSpacer_18 = QSpacerItem(13, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_12.addItem(self.horizontalSpacer_18)

        self.overspent = QLabel(self.budget_tab)
        self.overspent.setObjectName("overspent")
        sizePolicy.setHeightForWidth(self.overspent.sizePolicy().hasHeightForWidth())
        self.overspent.setSizePolicy(sizePolicy)
        self.overspent.setFont(font)

        self.horizontalLayout_12.addWidget(self.overspent)

        self.horizontalSpacer_16 = QSpacerItem(1040, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_12.addItem(self.horizontalSpacer_16)

        self.verticalLayout_4.addLayout(self.horizontalLayout_12)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.income_label = QLabel(self.budget_tab)
        self.income_label.setObjectName("income_label")
        sizePolicy.setHeightForWidth(self.income_label.sizePolicy().hasHeightForWidth())
        self.income_label.setSizePolicy(sizePolicy)
        self.income_label.setFont(font)

        self.horizontalLayout_13.addWidget(self.income_label)

        self.horizontalSpacer_19 = QSpacerItem(134, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer_19)

        self.income = QLabel(self.budget_tab)
        self.income.setObjectName("income")
        sizePolicy.setHeightForWidth(self.income.sizePolicy().hasHeightForWidth())
        self.income.setSizePolicy(sizePolicy)
        self.income.setFont(font)

        self.horizontalLayout_13.addWidget(self.income)

        self.horizontalSpacer_17 = QSpacerItem(1040, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer_17)

        self.verticalLayout_4.addLayout(self.horizontalLayout_13)

        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.budgeted_label = QLabel(self.budget_tab)
        self.budgeted_label.setObjectName("budgeted_label")
        sizePolicy.setHeightForWidth(self.budgeted_label.sizePolicy().hasHeightForWidth())
        self.budgeted_label.setSizePolicy(sizePolicy)
        self.budgeted_label.setFont(font)

        self.horizontalLayout_14.addWidget(self.budgeted_label)

        self.horizontalSpacer_20 = QSpacerItem(121, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_14.addItem(self.horizontalSpacer_20)

        self.budgeted = QLabel(self.budget_tab)
        self.budgeted.setObjectName("budgeted")
        sizePolicy.setHeightForWidth(self.budgeted.sizePolicy().hasHeightForWidth())
        self.budgeted.setSizePolicy(sizePolicy)
        self.budgeted.setFont(font)

        self.horizontalLayout_14.addWidget(self.budgeted)

        self.horizontalSpacer_21 = QSpacerItem(1040, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_14.addItem(self.horizontalSpacer_21)

        self.verticalLayout_4.addLayout(self.horizontalLayout_14)

        self.horizontalLayout_17 = QHBoxLayout()
        self.horizontalLayout_17.setObjectName("horizontalLayout_17")
        self.available_to_budget_label = QLabel(self.budget_tab)
        self.available_to_budget_label.setObjectName("available_to_budget_label")
        sizePolicy.setHeightForWidth(self.available_to_budget_label.sizePolicy().hasHeightForWidth())
        self.available_to_budget_label.setSizePolicy(sizePolicy)
        self.available_to_budget_label.setFont(font)

        self.horizontalLayout_17.addWidget(self.available_to_budget_label)

        self.horizontalSpacer_22 = QSpacerItem(25, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_17.addItem(self.horizontalSpacer_22)

        self.available_to_budget_equal = QLabel(self.budget_tab)
        self.available_to_budget_equal.setObjectName("available_to_budget_equal")
        sizePolicy.setHeightForWidth(self.available_to_budget_equal.sizePolicy().hasHeightForWidth())
        self.available_to_budget_equal.setSizePolicy(sizePolicy)

        self.horizontalLayout_17.addWidget(self.available_to_budget_equal)

        self.horizontalSpacer_23 = QSpacerItem(24, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_17.addItem(self.horizontalSpacer_23)

        self.available_to_budget = QLabel(self.budget_tab)
        self.available_to_budget.setObjectName("available_to_budget")
        sizePolicy.setHeightForWidth(self.available_to_budget.sizePolicy().hasHeightForWidth())
        self.available_to_budget.setSizePolicy(sizePolicy)
        self.available_to_budget.setFont(font)

        self.horizontalLayout_17.addWidget(self.available_to_budget)

        self.horizontalSpacer_24 = QSpacerItem(1040, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_17.addItem(self.horizontalSpacer_24)

        self.verticalLayout_4.addLayout(self.horizontalLayout_17)

        self.line_2 = QFrame(self.budget_tab)
        self.line_2.setObjectName("line_2")
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_4.addWidget(self.line_2)

        self.budget_table = QTableView(self.budget_tab)
        self.budget_table.setObjectName("budget_table")

        self.verticalLayout_4.addWidget(self.budget_table)

        self.tabWidget.addTab(self.budget_tab, "")
        self.accounts_tab = QWidget()
        self.accounts_tab.setObjectName("accounts_tab")
        self.horizontalLayout_19 = QHBoxLayout(self.accounts_tab)
        self.horizontalLayout_19.setObjectName("horizontalLayout_19")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout_3.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.on_budget_label = QLabel(self.accounts_tab)
        self.on_budget_label.setObjectName("on_budget_label")
        sizePolicy.setHeightForWidth(self.on_budget_label.sizePolicy().hasHeightForWidth())
        self.on_budget_label.setSizePolicy(sizePolicy)
        self.on_budget_label.setFont(font)

        self.verticalLayout_3.addWidget(self.on_budget_label)

        self.on_budget_accounts_table = QTableWidget(self.accounts_tab)
        self.on_budget_accounts_table.setObjectName("on_budget_accounts_table")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.on_budget_accounts_table.sizePolicy().hasHeightForWidth())
        self.on_budget_accounts_table.setSizePolicy(sizePolicy1)
        self.on_budget_accounts_table.setMaximumSize(QSize(250, 16777215))
        self.on_budget_accounts_table.setSelectionMode(QAbstractItemView.SingleSelection)
        self.on_budget_accounts_table.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.on_budget_accounts_table.verticalHeader().setVisible(False)

        self.verticalLayout_3.addWidget(self.on_budget_accounts_table)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.on_budget_total_label = QLabel(self.accounts_tab)
        self.on_budget_total_label.setObjectName("on_budget_total_label")
        sizePolicy.setHeightForWidth(self.on_budget_total_label.sizePolicy().hasHeightForWidth())
        self.on_budget_total_label.setSizePolicy(sizePolicy)
        self.on_budget_total_label.setFont(font)

        self.horizontalLayout_9.addWidget(self.on_budget_total_label)

        self.on_budget_total = QLabel(self.accounts_tab)
        self.on_budget_total.setObjectName("on_budget_total")
        sizePolicy.setHeightForWidth(self.on_budget_total.sizePolicy().hasHeightForWidth())
        self.on_budget_total.setSizePolicy(sizePolicy)
        self.on_budget_total.setFont(font)

        self.horizontalLayout_9.addWidget(self.on_budget_total)

        self.horizontalSpacer_11 = QSpacerItem(145, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_11)

        self.verticalLayout_3.addLayout(self.horizontalLayout_9)

        self.off_budget_label = QLabel(self.accounts_tab)
        self.off_budget_label.setObjectName("off_budget_label")
        sizePolicy.setHeightForWidth(self.off_budget_label.sizePolicy().hasHeightForWidth())
        self.off_budget_label.setSizePolicy(sizePolicy)
        self.off_budget_label.setFont(font)

        self.verticalLayout_3.addWidget(self.off_budget_label)

        self.off_budget_accounts_table = QTableWidget(self.accounts_tab)
        self.off_budget_accounts_table.setObjectName("off_budget_accounts_table")
        sizePolicy1.setHeightForWidth(self.off_budget_accounts_table.sizePolicy().hasHeightForWidth())
        self.off_budget_accounts_table.setSizePolicy(sizePolicy1)
        self.off_budget_accounts_table.setMaximumSize(QSize(250, 16777215))
        self.off_budget_accounts_table.setSelectionMode(QAbstractItemView.SingleSelection)
        self.off_budget_accounts_table.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.off_budget_accounts_table.verticalHeader().setVisible(False)

        self.verticalLayout_3.addWidget(self.off_budget_accounts_table)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.off_budget_total_label = QLabel(self.accounts_tab)
        self.off_budget_total_label.setObjectName("off_budget_total_label")
        sizePolicy.setHeightForWidth(self.off_budget_total_label.sizePolicy().hasHeightForWidth())
        self.off_budget_total_label.setSizePolicy(sizePolicy)
        self.off_budget_total_label.setFont(font)

        self.horizontalLayout_10.addWidget(self.off_budget_total_label)

        self.off_budget_total = QLabel(self.accounts_tab)
        self.off_budget_total.setObjectName("off_budget_total")
        sizePolicy.setHeightForWidth(self.off_budget_total.sizePolicy().hasHeightForWidth())
        self.off_budget_total.setSizePolicy(sizePolicy)
        self.off_budget_total.setFont(font)

        self.horizontalLayout_10.addWidget(self.off_budget_total)

        self.horizontalSpacer_12 = QSpacerItem(145, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_12)

        self.verticalLayout_3.addLayout(self.horizontalLayout_10)

        self.manage_accounts_button = QPushButton(self.accounts_tab)
        self.manage_accounts_button.setObjectName("manage_accounts_button")
        sizePolicy.setHeightForWidth(self.manage_accounts_button.sizePolicy().hasHeightForWidth())
        self.manage_accounts_button.setSizePolicy(sizePolicy)
        self.manage_accounts_button.setFocusPolicy(Qt.NoFocus)

        self.verticalLayout_3.addWidget(self.manage_accounts_button, 0, Qt.AlignHCenter)

        self.horizontalLayout_19.addLayout(self.verticalLayout_3)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.account_name_label = QLabel(self.accounts_tab)
        self.account_name_label.setObjectName("account_name_label")
        sizePolicy.setHeightForWidth(self.account_name_label.sizePolicy().hasHeightForWidth())
        self.account_name_label.setSizePolicy(sizePolicy)
        font1 = QFont()
        font1.setPointSize(14)
        font1.setBold(True)
        self.account_name_label.setFont(font1)

        self.verticalLayout_5.addWidget(self.account_name_label, 0, Qt.AlignHCenter)

        self.transactions_table = QTableView(self.accounts_tab)
        self.transactions_table.setObjectName("transactions_table")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.transactions_table.sizePolicy().hasHeightForWidth())
        self.transactions_table.setSizePolicy(sizePolicy2)
        self.transactions_table.setMinimumSize(QSize(1025, 0))
        self.transactions_table.setMaximumSize(QSize(16777215, 16777215))
        self.transactions_table.verticalHeader().setVisible(False)

        self.verticalLayout_5.addWidget(self.transactions_table)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.add_transaction_button = QPushButton(self.accounts_tab)
        self.add_transaction_button.setObjectName("add_transaction_button")
        sizePolicy.setHeightForWidth(self.add_transaction_button.sizePolicy().hasHeightForWidth())
        self.add_transaction_button.setSizePolicy(sizePolicy)
        self.add_transaction_button.setFocusPolicy(Qt.NoFocus)

        self.horizontalLayout_8.addWidget(self.add_transaction_button)

        self.make_a_transfer_button = QPushButton(self.accounts_tab)
        self.make_a_transfer_button.setObjectName("make_a_transfer_button")
        sizePolicy.setHeightForWidth(self.make_a_transfer_button.sizePolicy().hasHeightForWidth())
        self.make_a_transfer_button.setSizePolicy(sizePolicy)
        self.make_a_transfer_button.setFocusPolicy(Qt.NoFocus)

        self.horizontalLayout_8.addWidget(self.make_a_transfer_button)

        self.horizontalSpacer_13 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_13)

        self.cleared_balance_label = QLabel(self.accounts_tab)
        self.cleared_balance_label.setObjectName("cleared_balance_label")
        sizePolicy.setHeightForWidth(self.cleared_balance_label.sizePolicy().hasHeightForWidth())
        self.cleared_balance_label.setSizePolicy(sizePolicy)
        self.cleared_balance_label.setFont(font)

        self.horizontalLayout_8.addWidget(self.cleared_balance_label)

        self.cleared_balance = QLabel(self.accounts_tab)
        self.cleared_balance.setObjectName("cleared_balance")
        sizePolicy.setHeightForWidth(self.cleared_balance.sizePolicy().hasHeightForWidth())
        self.cleared_balance.setSizePolicy(sizePolicy)
        self.cleared_balance.setFont(font)

        self.horizontalLayout_8.addWidget(self.cleared_balance)

        self.plus_label = QLabel(self.accounts_tab)
        self.plus_label.setObjectName("plus_label")

        self.horizontalLayout_8.addWidget(self.plus_label)

        self.uncleared_transactions_label = QLabel(self.accounts_tab)
        self.uncleared_transactions_label.setObjectName("uncleared_transactions_label")
        self.uncleared_transactions_label.setFont(font)

        self.horizontalLayout_8.addWidget(self.uncleared_transactions_label)

        self.uncleared_transactions = QLabel(self.accounts_tab)
        self.uncleared_transactions.setObjectName("uncleared_transactions")
        sizePolicy.setHeightForWidth(self.uncleared_transactions.sizePolicy().hasHeightForWidth())
        self.uncleared_transactions.setSizePolicy(sizePolicy)
        self.uncleared_transactions.setFont(font)

        self.horizontalLayout_8.addWidget(self.uncleared_transactions)

        self.equals_label = QLabel(self.accounts_tab)
        self.equals_label.setObjectName("equals_label")
        self.equals_label.setFont(font)

        self.horizontalLayout_8.addWidget(self.equals_label)

        self.working_balance_label = QLabel(self.accounts_tab)
        self.working_balance_label.setObjectName("working_balance_label")
        self.working_balance_label.setFont(font)

        self.horizontalLayout_8.addWidget(self.working_balance_label)

        self.working_balance = QLabel(self.accounts_tab)
        self.working_balance.setObjectName("working_balance")
        self.working_balance.setFont(font)

        self.horizontalLayout_8.addWidget(self.working_balance)

        self.reconcile_account_button = QPushButton(self.accounts_tab)
        self.reconcile_account_button.setObjectName("reconcile_account_button")
        sizePolicy.setHeightForWidth(self.reconcile_account_button.sizePolicy().hasHeightForWidth())
        self.reconcile_account_button.setSizePolicy(sizePolicy)
        self.reconcile_account_button.setFocusPolicy(Qt.NoFocus)

        self.horizontalLayout_8.addWidget(self.reconcile_account_button)

        self.verticalLayout_5.addLayout(self.horizontalLayout_8)

        self.horizontalLayout_19.addLayout(self.verticalLayout_5)

        self.tabWidget.addTab(self.accounts_tab, "")
        self.Reports_tab = QWidget()
        self.Reports_tab.setObjectName("Reports_tab")
        self.verticalLayout_2 = QVBoxLayout(self.Reports_tab)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.spending_by_category_button = QPushButton(self.Reports_tab)
        self.spending_by_category_button.setObjectName("spending_by_category_button")
        sizePolicy3 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.spending_by_category_button.sizePolicy().hasHeightForWidth())
        self.spending_by_category_button.setSizePolicy(sizePolicy3)
        self.spending_by_category_button.setFocusPolicy(Qt.ClickFocus)

        self.horizontalLayout.addWidget(self.spending_by_category_button)

        self.spending_by_payee_button = QPushButton(self.Reports_tab)
        self.spending_by_payee_button.setObjectName("spending_by_payee_button")
        sizePolicy3.setHeightForWidth(self.spending_by_payee_button.sizePolicy().hasHeightForWidth())
        self.spending_by_payee_button.setSizePolicy(sizePolicy3)
        self.spending_by_payee_button.setFocusPolicy(Qt.ClickFocus)

        self.horizontalLayout.addWidget(self.spending_by_payee_button)

        self.spending_trends_button = QPushButton(self.Reports_tab)
        self.spending_trends_button.setObjectName("spending_trends_button")
        sizePolicy3.setHeightForWidth(self.spending_trends_button.sizePolicy().hasHeightForWidth())
        self.spending_trends_button.setSizePolicy(sizePolicy3)
        self.spending_trends_button.setFocusPolicy(Qt.ClickFocus)

        self.horizontalLayout.addWidget(self.spending_trends_button)

        self.income_v_expense_button = QPushButton(self.Reports_tab)
        self.income_v_expense_button.setObjectName("income_v_expense_button")
        sizePolicy3.setHeightForWidth(self.income_v_expense_button.sizePolicy().hasHeightForWidth())
        self.income_v_expense_button.setSizePolicy(sizePolicy3)
        self.income_v_expense_button.setFocusPolicy(Qt.ClickFocus)

        self.horizontalLayout.addWidget(self.income_v_expense_button)

        self.net_worth_button = QPushButton(self.Reports_tab)
        self.net_worth_button.setObjectName("net_worth_button")
        sizePolicy3.setHeightForWidth(self.net_worth_button.sizePolicy().hasHeightForWidth())
        self.net_worth_button.setSizePolicy(sizePolicy3)
        self.net_worth_button.setFocusPolicy(Qt.ClickFocus)

        self.horizontalLayout.addWidget(self.net_worth_button)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.line = QFrame(self.Reports_tab)
        self.line.setObjectName("line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_2.addWidget(self.line)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.spending_by_category_label = QLabel(self.Reports_tab)
        self.spending_by_category_label.setObjectName("spending_by_category_label")
        sizePolicy.setHeightForWidth(self.spending_by_category_label.sizePolicy().hasHeightForWidth())
        self.spending_by_category_label.setSizePolicy(sizePolicy)
        self.spending_by_category_label.setFont(font1)

        self.horizontalLayout_2.addWidget(self.spending_by_category_label, 0, Qt.AlignRight)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.pdf_export = QPushButton(self.Reports_tab)
        self.pdf_export.setObjectName("pdf_export")
        sizePolicy.setHeightForWidth(self.pdf_export.sizePolicy().hasHeightForWidth())
        self.pdf_export.setSizePolicy(sizePolicy)
        self.pdf_export.setFocusPolicy(Qt.NoFocus)

        self.horizontalLayout_2.addWidget(self.pdf_export, 0, Qt.AlignLeft)

        self.print = QPushButton(self.Reports_tab)
        self.print.setObjectName("print")
        sizePolicy.setHeightForWidth(self.print.sizePolicy().hasHeightForWidth())
        self.print.setSizePolicy(sizePolicy)
        self.print.setFocusPolicy(Qt.NoFocus)

        self.horizontalLayout_2.addWidget(self.print, 0, Qt.AlignLeft)

        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.time_frame_label = QLabel(self.Reports_tab)
        self.time_frame_label.setObjectName("time_frame_label")
        sizePolicy.setHeightForWidth(self.time_frame_label.sizePolicy().hasHeightForWidth())
        self.time_frame_label.setSizePolicy(sizePolicy)
        self.time_frame_label.setFont(font)

        self.horizontalLayout_3.addWidget(self.time_frame_label)

        self.horizontalSpacer_7 = QSpacerItem(10, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_7)

        self.report_date_one = QDateEdit(self.Reports_tab)
        self.report_date_one.setObjectName("report_date_one")
        sizePolicy.setHeightForWidth(self.report_date_one.sizePolicy().hasHeightForWidth())
        self.report_date_one.setSizePolicy(sizePolicy)
        self.report_date_one.setCalendarPopup(True)

        self.horizontalLayout_3.addWidget(self.report_date_one)

        self.report_date_two = QDateEdit(self.Reports_tab)
        self.report_date_two.setObjectName("report_date_two")
        sizePolicy.setHeightForWidth(self.report_date_two.sizePolicy().hasHeightForWidth())
        self.report_date_two.setSizePolicy(sizePolicy)
        self.report_date_two.setCalendarPopup(True)

        self.horizontalLayout_3.addWidget(self.report_date_two)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_3)

        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.categories_label = QLabel(self.Reports_tab)
        self.categories_label.setObjectName("categories_label")
        sizePolicy.setHeightForWidth(self.categories_label.sizePolicy().hasHeightForWidth())
        self.categories_label.setSizePolicy(sizePolicy)
        self.categories_label.setFont(font)

        self.horizontalLayout_4.addWidget(self.categories_label)

        self.horizontalSpacer_8 = QSpacerItem(11, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_8)

        self.reports_categories_combo = QComboBox(self.Reports_tab)
        self.reports_categories_combo.setObjectName("reports_categories_combo")
        sizePolicy.setHeightForWidth(self.reports_categories_combo.sizePolicy().hasHeightForWidth())
        self.reports_categories_combo.setSizePolicy(sizePolicy)
        self.reports_categories_combo.setSizeAdjustPolicy(QComboBox.AdjustToContents)

        self.horizontalLayout_4.addWidget(self.reports_categories_combo)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_4)

        self.verticalLayout_2.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.payees_label = QLabel(self.Reports_tab)
        self.payees_label.setObjectName("payees_label")
        sizePolicy.setHeightForWidth(self.payees_label.sizePolicy().hasHeightForWidth())
        self.payees_label.setSizePolicy(sizePolicy)
        self.payees_label.setFont(font)

        self.horizontalLayout_5.addWidget(self.payees_label)

        self.horizontalSpacer_6 = QSpacerItem(31, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_6)

        self.reports_payees_combo = QComboBox(self.Reports_tab)
        self.reports_payees_combo.setObjectName("reports_payees_combo")
        sizePolicy.setHeightForWidth(self.reports_payees_combo.sizePolicy().hasHeightForWidth())
        self.reports_payees_combo.setSizePolicy(sizePolicy)
        self.reports_payees_combo.setSizeAdjustPolicy(QComboBox.AdjustToContents)

        self.horizontalLayout_5.addWidget(self.reports_payees_combo)

        self.horizontalSpacer_5 = QSpacerItem(595, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_5)

        self.verticalLayout_2.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.accounts_label = QLabel(self.Reports_tab)
        self.accounts_label.setObjectName("accounts_label")
        sizePolicy.setHeightForWidth(self.accounts_label.sizePolicy().hasHeightForWidth())
        self.accounts_label.setSizePolicy(sizePolicy)
        self.accounts_label.setFont(font)

        self.horizontalLayout_6.addWidget(self.accounts_label)

        self.horizontalSpacer_10 = QSpacerItem(17, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_10)

        self.reports_accounts_combo = QComboBox(self.Reports_tab)
        self.reports_accounts_combo.setObjectName("reports_accounts_combo")
        sizePolicy.setHeightForWidth(self.reports_accounts_combo.sizePolicy().hasHeightForWidth())
        self.reports_accounts_combo.setSizePolicy(sizePolicy)
        self.reports_accounts_combo.setSizeAdjustPolicy(QComboBox.AdjustToContents)

        self.horizontalLayout_6.addWidget(self.reports_accounts_combo)

        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_9)

        self.verticalLayout_2.addLayout(self.horizontalLayout_6)

        self.chart_viewer = QChartView(self.Reports_tab)
        self.chart_viewer.setObjectName("chart_viewer")
        font2 = QFont()
        font2.setStyleStrategy(QFont.PreferDefault)
        self.chart_viewer.setFont(font2)
        self.chart_viewer.setRenderHints(QPainter.Antialiasing | QPainter.TextAntialiasing)

        self.verticalLayout_2.addWidget(self.chart_viewer)

        self.tabWidget.addTab(self.Reports_tab, "")

        self.verticalLayout.addWidget(self.tabWidget)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName("menubar")
        self.menubar.setGeometry(QRect(0, 0, 1366, 22))
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)

        QMetaObject.connectSlotsByName(MainWindow)

    # setupUi

    def retranslateUi(self, MainWindow):
        # if QT_CONFIG(tooltip)
        self.manage_categories_button.setToolTip(QCoreApplication.translate("MainWindow", "Add Master Category", None))
        # endif // QT_CONFIG(tooltip)
        self.manage_categories_button.setText(QCoreApplication.translate("MainWindow", "Manage Categories", None))
        self.not_budgeted_label.setText(QCoreApplication.translate("MainWindow", "Not budgeted in previous month:", None))
        self.not_budgeted.setText("")
        self.overspent_label.setText(QCoreApplication.translate("MainWindow", "Overspent in previous month:", None))
        self.overspent.setText("")
        self.income_label.setText(QCoreApplication.translate("MainWindow", "Income:", None))
        self.income.setText("")
        self.budgeted_label.setText(QCoreApplication.translate("MainWindow", "Budgeted:", None))
        self.budgeted.setText("")
        self.available_to_budget_label.setText("")
        self.available_to_budget_equal.setText("")
        self.available_to_budget.setText("")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.budget_tab), QCoreApplication.translate("MainWindow", "Budget", None))
        self.on_budget_label.setText(QCoreApplication.translate("MainWindow", "On Budget", None))
        self.on_budget_total_label.setText(QCoreApplication.translate("MainWindow", "Total:", None))
        self.on_budget_total.setText("")
        self.off_budget_label.setText(QCoreApplication.translate("MainWindow", "Off Budget", None))
        self.off_budget_total_label.setText(QCoreApplication.translate("MainWindow", "Total:", None))
        self.off_budget_total.setText("")
        self.manage_accounts_button.setText(QCoreApplication.translate("MainWindow", "Manage Accounts", None))
        self.account_name_label.setText("")
        self.add_transaction_button.setText(QCoreApplication.translate("MainWindow", "Add Transaction", None))
        self.make_a_transfer_button.setText(QCoreApplication.translate("MainWindow", "Make a Transfer", None))
        self.cleared_balance_label.setText(QCoreApplication.translate("MainWindow", "Cleared Balance:", None))
        self.cleared_balance.setText("")
        self.plus_label.setText("")
        self.uncleared_transactions_label.setText(QCoreApplication.translate("MainWindow", "Uncleared Transactions:", None))
        self.uncleared_transactions.setText("")
        self.equals_label.setText("")
        self.working_balance_label.setText(QCoreApplication.translate("MainWindow", "Working Balance:", None))
        self.working_balance.setText("")
        self.reconcile_account_button.setText(QCoreApplication.translate("MainWindow", "Reconcile Account", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.accounts_tab), QCoreApplication.translate("MainWindow", "Accounts", None))
        self.spending_by_category_button.setText(QCoreApplication.translate("MainWindow", "Spending By Category", None))
        self.spending_by_payee_button.setText(QCoreApplication.translate("MainWindow", "Spending By Payee", None))
        self.spending_trends_button.setText(QCoreApplication.translate("MainWindow", "Spending Trends", None))
        self.income_v_expense_button.setText(QCoreApplication.translate("MainWindow", "Income v. Expense", None))
        self.net_worth_button.setText(QCoreApplication.translate("MainWindow", "Net Worth", None))
        self.spending_by_category_label.setText(QCoreApplication.translate("MainWindow", "Spending By Category", None))
        self.pdf_export.setText(QCoreApplication.translate("MainWindow", "Export To PDF", None))
        self.print.setText(QCoreApplication.translate("MainWindow", "Print", None))
        self.time_frame_label.setText(QCoreApplication.translate("MainWindow", "Timeframe:", None))
        self.categories_label.setText(QCoreApplication.translate("MainWindow", "Categories:", None))
        self.payees_label.setText(QCoreApplication.translate("MainWindow", "Payees:", None))
        self.accounts_label.setText(QCoreApplication.translate("MainWindow", "Accounts:", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Reports_tab), QCoreApplication.translate("MainWindow", "Reports", None))
        pass

    # retranslateUi
