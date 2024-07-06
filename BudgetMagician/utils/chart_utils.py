from PySide6.QtCharts import QChart, QPieSeries, QBarSeries, QBarSet, QBarCategoryAxis, QValueAxis, QPieSlice
from PySide6.QtCore import Qt


def get_pie_chart_from_dict(title: str, error_message: str, data: dict) -> QChart:
    if len(data) == 0:
        chart = QChart()
        chart.setTitle(error_message)
    else:
        series = QPieSeries()
        for k, v in data.items():
            series.append(k, v)

        series.setLabelsPosition(QPieSlice.LabelPosition.LabelInsideHorizontal)
        for pie_slice in series.slices():
            pie_slice.setLabelVisible(True)
            old_label = pie_slice.label()
            pie_slice.setLabel(f"{old_label}: {100 * pie_slice.percentage():.2f}%")
    
        chart = QChart()
        chart.setTitle(title)
        chart.addSeries(series)
        chart.legend().setAlignment(Qt.AlignmentFlag.AlignBottom)

    return chart


def get_bar_char_from_dict(title: str, error_message: str, x_axis_categories: list, y_axis_max_val: float, y_axis_min_val: float, data: dict[str, list]) -> QChart:
    if len(data) == 0:
        chart = QChart()
        chart.setTitle(error_message)
    else:
        series = QBarSeries()
        for k, v in data.items():
            bar = QBarSet(k)
            bar.append(v)
            series.append(bar)

        chart = QChart()
        chart.setTitle(title)
        chart.addSeries(series)

        x_axis = QBarCategoryAxis()
        x_axis.append(x_axis_categories)
        chart.addAxis(x_axis, Qt.AlignmentFlag.AlignBottom)

        y_axis = QValueAxis()
        chart.addAxis(y_axis, Qt.AlignmentFlag.AlignLeft)

        if y_axis_min_val > 0:
            y_axis_min_val = 0

        y_axis.setRange(y_axis_min_val, y_axis_max_val)

        chart.legend().setVisible(True)
        chart.legend().setAlignment(Qt.AlignmentFlag.AlignBottom)

    return chart
