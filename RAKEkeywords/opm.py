from ovos_plugin_manager.templates.keywords import KeywordExtractor
from RAKEkeywords import Rake
from typing import Dict, Optional, Set
from RAKEkeywords import stopwrds as stopwordsiso


class RakeKeywordExtractor(KeywordExtractor):

    def __init__(self, config=None):
        super().__init__(config)
        self._xtractors: Dict[str, Rake] = {}

    @property
    def supported_langs(self) -> Set[str]:
        return stopwordsiso.langs()

    def get_extractor(self, lang: Optional[str] = None) -> Rake:
        lang = lang or self.lang
        if lang.lower().split("-")[0] not in self.supported_langs:
            raise ValueError(f"Unsupported language: {lang}")
        if lang not in self._xtractors:
            self._xtractors[lang] = Rake(lang)
        return self._xtractors[lang]

    def extract(self, text: str, lang: Optional[str] = None) -> Dict[str, float]:
        kx = self.get_extractor(lang)
        return {
            kw: score for kw, score in kx.extract_keywords(text)
        }
