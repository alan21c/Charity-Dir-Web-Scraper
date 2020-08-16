import urllib.request

contents = urllib.request.urlopen("http://quotes.toscrape.com/").read()
print(contents)
input()