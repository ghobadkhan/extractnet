from extractnet.pipeline import Extractor
from .version import __version__ as canonical_version

__version__ = canonical_version


_LOADED_MODELS = {}

def extract_news(html, encoding=None, as_blocks=False):
    if 'news_extraction' not in _LOADED_MODELS:
        _LOADED_MODELS['news_extraction'] = Extractor()

    return _LOADED_MODELS['news_extraction'].extract(html)

