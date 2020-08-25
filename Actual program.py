import urllib.request
import re
import time
import json
charities = open("charities.csv", "w")
charities.write("Contact Name, Email, Phone Number, Website, Charity Name, Revenue\n")
temprow = []
#3458
for i in range(1):
    #What this does is open a database with the Buisness Numbers of each charity (alongside other stuff) according to the page number, i. We modify the url based on i.
    links = json.loads(urllib.request.urlopen(f"https://www.charitydir.com/views_2018_08_05/charities/getCharities.php?name=undefined&page={i + 1}&all=true").read())
    BN = []
    for row in links["charities"]:
        BN.append(row["BN"])
    for bn in BN:
        #Opens data for specific CSV file
        data = json.loads(urllib.request.urlopen(f"https://www.charitydir.com/views_2018_08_05/charity/getCharityBasic.php?BN={bn}").read())["charity"]

        #Adds everything
        temprow = [data["PublicContactName"], data["Email"], data["ContactPhoneNumber"], data["Website"], data["LegalName"]]

        #Revenue is stored in a different php file
        data = json.loads(urllib.request.urlopen(f"https://www.charitydir.com/views_2018_08_05/charity/getCharity.php?BN={bn}").read())["charity"]["financial"]

        #Get Revenue
        temprow.append(data["4700"])
        #Writes it to CSV
        if(float(temprow[5]) > 200000):
            for cell in temprow:
                if cell == None:
                    charities.write(",")
                else:
                    charities.write('"'+cell+'",')
            charities.write('\n')
                
charities.close()
