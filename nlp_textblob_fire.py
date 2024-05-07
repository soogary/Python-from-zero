#!/usr/bin/env python
from textblob import TextBlob
import wikipedia
import fire
from mylib.nlp_textblob import get_phrases

if __name__ == "__main__":
    fire.Fire(get_phrases)
