from lib.requests_html import HTMLSession

session = HTMLSession()
r = session.get('https://www.charitydir.com/all/1')
r.html.render()

print(r.html.links)