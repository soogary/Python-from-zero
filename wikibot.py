import wikipedia

#wikipedia.summary("Facebook", sentences=1)
#result = wikipedia.summary("Microsoft", sentences=1)
#print(result)

def scrape(name="Microsoft", length=1):
    result = wikipedia.summary(name, sentences=1)
    return result

#print(scrape())
print(scrape("Microsoft"))

