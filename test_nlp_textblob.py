from mylib.nlp_textblob import search_wikipedia, summarize_wikipedia, get_text_blob, get_phrases

def test_get_phrases():
    assert 'nba' in get_phrases("Los Angeles Lakers")