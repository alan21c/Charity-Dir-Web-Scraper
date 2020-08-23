import urllib.request
import re
import time

for i in range(3458):
    #What this does is open a database with the Buisness Numbers of each charity (alongside other stuff) according to the page number, i. We modify the url based on i.
    #Also, the reason we decode it is to convert it to a string.
    contents = urllib.request.urlopen(f"https://www.charitydir.com/views_2018_08_05/charities/getCharities.php?name=undefined&page={i + 1}&all=true").read().decode("utf-8")

    #So I've done some research and according to canada.ca, a Buisness Number consists of a 9 digit buisness number, followed by RR, followed by 0001.
    #Therefore, all we have to do is make a regex string that scans for 9 digits followed by RR0001.

    BN = re.findall("[0-9]{9}RR0001", contents)
    print(BN)
    time.sleep(1)
input()
