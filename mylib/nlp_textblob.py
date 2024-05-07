from textblob import TextBlob
import wikipedia

def search_wikipedia(name):
    """Searches wikipedia"""
    print(f"searching for name: {name}")
    return wikipedia.search(name)

def summarize_wikipedia(name):
    """Summarize wikipedia your search entry"""

    print(f"finding wikipedia summary for search entry: {name}")
    return wikipedia.summary(name)

def get_text_blob(text):
    """getting text blob and returns it"""
    blob = TextBlob(text)
    return blob 

def get_phrases(name):
    """find wikipedia names and return back phrases"""
    text = summarize_wikipedia(name)
    blob = get_text_blob(text)
    phrases = blob.noun_phrases
    return phrases

#lal = wikipedia.summary("Los Angeles Laker")
#blob.tags
#blob.noun_phrases
