"""test"""
#from mylib.nlp_textblob import search_wikipedia, summarize_wikipedia, get_text_blob, get_phrases
from mylib.nlp_textblob import get_phrases

def test_get_phrases():
    """check sample values are present in the output"""
    assert 'nba' in get_phrases("Los Angeles Lakers")
