import pytest

from RAKEkeywords import Rake
from RAKEkeywords import stopwrds


def test_langs_nonempty():
    assert "en" in stopwrds.langs()
    assert stopwrds.has_lang("en")


def test_stopwords_string():
    en = stopwrds.stopwords("en")
    assert isinstance(en, set)
    assert "the" in en


def test_stopwords_iterable():
    combo = stopwrds.stopwords(["en", "de"])
    assert stopwrds.stopwords("en").issubset(combo)
    assert stopwrds.stopwords("de").issubset(combo)


def test_stopwords_unknown_lang_returns_empty():
    assert stopwrds.stopwords("xxx") == set()


def test_stopwords_invalid_type_raises():
    with pytest.raises(TypeError):
        stopwrds.stopwords(123)


def test_rake_extract_keywords():
    rake = Rake("en")
    text = "Compatibility of systems of linear constraints over the set of natural numbers."
    keywords = rake.extract_keywords(text)
    assert isinstance(keywords, list)
    assert len(keywords) > 0
    for kw, score in keywords:
        assert isinstance(kw, str)
        assert isinstance(score, (int, float))


def test_rake_unsupported_lang_raises():
    with pytest.raises(ValueError):
        Rake("xxx")
