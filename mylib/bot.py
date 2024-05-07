import wikipedia


def mylib_scrape(name):
    result = wikipedia.summary(name)
    return result
