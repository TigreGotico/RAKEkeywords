# RAKEkeywords

RAKEkeywords implements RAKE (Rapid Automatic Keyword Extraction), an algorithm that finds keywords in a document. The algorithm comes from [Rose, Engel, Cramer, and Cowley (2010), "Automatic keyword extraction from individual documents"](https://onlinelibrary.wiley.com/doi/10.1002/9780470689646.ch1), in *Text Mining: Applications and Theory* (John Wiley and Sons).

The package includes stopword lists for many languages, from [stopwords-iso](https://github.com/stopwords-iso/stopwords-iso). It also registers as a keyword-extractor plugin for [OVOS Plugin Manager (OPM)](https://github.com/OpenVoiceOS/ovos-plugin-manager).

## Install

```bash
pip install RAKEkeywords
```

## Usage

```python
from RAKEkeywords import Rake

rake = Rake()

keywords = rake.extract_keywords("Mycroft is a free and open-source voice assistant for Linux-based operating systems that uses a natural language user interface")

"""
[('natural language user interface', 16.0),
 ('open-source voice assistant', 9.0),
 ('linux-based operating systems', 9.0),
 ('mycroft', 1.0),
 ('free', 1.0)]
"""
```

Pass a `lang` code to use the stopword list for another language.

```python
from RAKEkeywords import Rake

rake = Rake(lang="pt")
keywords = rake.extract_keywords("Portugal, oficialmente República Portuguesa, é um país cujo território se situa na zona ocidental da Península Ibérica.")
```

Pass `stop_words_path` to use a custom stopword file instead of the built-in list.

```python
from RAKEkeywords import Rake
from os.path import join, dirname

my_list = join(dirname(__file__), "stopwords", "en", "FoxStoplist.txt")
rake = Rake(stop_words_path=my_list)
```

## Related projects

- [OpenVoiceOS/ovos-plugin-manager](https://github.com/OpenVoiceOS/ovos-plugin-manager): the plugin framework this package registers with under the `opm.keywords` entry point.
- [stopwords-iso/stopwords-iso](https://github.com/stopwords-iso/stopwords-iso): the multi-language stopword lists bundled with this package.

## License

[MIT](LICENSE.md)
