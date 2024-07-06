from PySide6.QtCore import QCoreApplication


QT_LOG_IGNORED = ("requestActivate() called for",)


def tr(text: str) -> str:
    return QCoreApplication.translate("@default", text, None)


def translate(context, text, disambiguation=None) -> str:
    return QCoreApplication.translate(context, text, disambiguation)


def is_qt_log_ignored(message: str) -> bool:
    for ignored in QT_LOG_IGNORED:
        if ignored in message:
            return True

    return False
