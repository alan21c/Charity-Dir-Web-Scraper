import urllib.request
import re

contents = urllib.request.urlopen("https://www.charitydir.com/all/").read().decode()

#Ok so this regular expression is clearly not working but we want something like this. I'll figure out the problem in a bit.
data = re.findall('<a ui-sref="app.charity({BN: charity.BN})" href="/charities/\d+">', contents)

print(data)
input()
