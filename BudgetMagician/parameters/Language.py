from typing import NamedTuple, List
from PySide6.QtCore import QLocale


class LanguageAuthor(NamedTuple):
    name: str
    url: str


class Language(NamedTuple):
    code: str
    completion: int
    authors: List[LanguageAuthor]

    @property
    def author_names(self) -> list:
        return [author.name for author in self.authors]

    @property
    def author_links(self) -> list[str]:
        return ['<a href="{0}">{1}</a>'.format(author.url, author.name) for author in self.authors]

    @property
    def title_native(self) -> str:
        return QLocale(self.code).nativeLanguageName().title()

    @property
    def country_native(self) -> str:
        return QLocale(self.code).nativeCountryName().title()

    @property
    def icon_path(self) -> str:
        return f":/icons/flag_{self.code}.svg"


def get_system_language() -> str:
    system_language_code = QLocale.system().name()

    language_codes = {language.code for language in LANGUAGES}

    if system_language_code in language_codes:
        return system_language_code

    return "en_US"


LANGUAGES = [
    Language(code="en_US", completion=100, authors=[LanguageAuthor("Joseph Waggy", "https://github.com/jwaggy")]),
    # Language(code="en_ES", completion=0, authors=[])
]
