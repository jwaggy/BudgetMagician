from typing import NamedTuple, Optional, List

from PySide6 import __version__ as pyside_qt_version
from PySide6.QtCore import Qt
from PySide6.QtCore import __version__ as qt_version
from PySide6.QtWidgets import QDialog
from dateutil import __version__ as dateutil_version
from sqlalchemy import __version__ as sqlalchemy_version

from BudgetMagician.dialogs.AboutUi import Ui_About
from BudgetMagician.parameters.Language import LANGUAGES
from BudgetMagician.parameters.env import PYTHON_VERSION
from BudgetMagician.version import __display_name__, __version__, __app_url__, __app_bugtracker_url__, __app_license_url__


class Citation(NamedTuple):
    title: str
    version: Optional[str]
    author: str
    license: str
    url: str


class About(QDialog, Ui_About):
    def __init__(self, parent):
        super().__init__(parent)

        self.setupUi(self)
        self.setWindowFlag(Qt.WindowType.FramelessWindowHint)
        self.version.setText(self.tr("Version: {}").format(__version__))
        self.app_name_title.setText(__display_name__)
        self.ok.clicked.connect(self.close)

        about_info_strings = [
            self.tr('<p>This software is licensed under <a href="{}">GNU GPL</a> version 3.</p>').format(__app_license_url__),
            self.tr('<p>Source code is available on <a href="{}">GitHub</a>.<br/>').format(__app_url__),
            self.tr('Please send any suggestions and bug reports <a href="{}">here</a>.</p>').format(__app_bugtracker_url__),
        ]
        about_info = "".join(about_info_strings)

        self.info_box.setText(about_info)

        citations = {
            "core": [
                Citation(
                    "Python",
                    PYTHON_VERSION,
                    "Python Software Foundation",
                    "Python Software Foundation License",
                    "https://www.python.org/",
                ),
                Citation(
                    "Qt",
                    qt_version,
                    "Qt Project",
                    "GPL 2.0, GPL 3.0, and LGPL 3.0",
                    "https://www.qt.io/",
                ),
            ],
            "python": [
                Citation("Pyside6", pyside_qt_version, "Qt for Python Team", "GPL 3.0 and LGPL 3.0", "https://www.qt.io/qt-for-python"),
                Citation("qt-material", "2.14", "Signal Processing and Recognition Group", "BSD 2-Clause License", "https://github.com/UN-GCPDS/qt-material"),
                Citation("SQLAlchemy", sqlalchemy_version, "Mike Bayer", "MIT License", "https://github.com/sqlalchemy/sqlalchemy"),
                Citation("dateutil", dateutil_version, "Gustavo Niemeyer", "Dual Apache 2.0, BSD 3-Clause", "https://github.com/dateutil/dateutil")
            ],
            "gui": [
                Citation("flag-icons", "6.10.0", "Lipis", "MIT License", "https://github.com/lipis/flag-icons"),
                Citation("Feather", "4.29.1", "feathericons", "MIT License", "https://github.com/feathericons/feather"),
                Citation("Lucide", "0.269.0", "lucide-icons", "ISC License", "https://github.com/lucide-icons/lucide")
            ]
        }

        citations_text = [
            "<style>p, h3 {text-align: center;}</style>",
            "<h3>{}</h3>".format(self.tr("Core")),
            self._generate_citations(citations["core"]),
            "<h3>{}</h3>".format(self.tr("Python packages")),
            self._generate_citations(citations["python"]),
            "<h3>{}</h3>".format(self.tr("Graphics")),
            self._generate_citations(citations["gui"]),
            "<h3>{}</h3>".format(self.tr("Translations")),
            self._generate_translation_citations(),
        ]

        self.citations_box.setText("\n".join(citations_text))

    def _generate_citations(self, citations: List[Citation]) -> str:
        citations_text = []

        for citation in citations:
            app_title = "{} {}".format(citation.title, citation.version or "").strip()
            app_url = f'<a href="{citation.url}">{citation.author}</a>'
            citation_text = '<p style="line-height: 130%"><b>{}</b><br>{}<br><i>{}<br>{}</i></p>'.format(app_title, app_url, self.tr("Licensed under"), citation.license)

            citations_text.append(citation_text)

        return "\n".join(citations_text)

    @staticmethod
    def _generate_translation_citations():
        citations_text = []

        for language in LANGUAGES:
            if not language.authors:
                continue

            citation_text = '<p style="line-height: 130%"><b>{language}<br>({country})</b><br>{authors}</p>'.format(
                language=language.title_native, country=language.country_native, authors="<br/>".join(language.author_links)
            )

            citations_text.append(citation_text)

        return "\n".join(citations_text)
