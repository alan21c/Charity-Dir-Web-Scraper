import urllib.request
import re
import time

charities = open("charities.csv", "w")
charities.write("Contact Name, Email, Phone Number, Website, Charity Name, Revenue\n")
row = []
#3458
for i in range(3458):
    #What this does is open a database with the Buisness Numbers of each charity (alongside other stuff) according to the page number, i. We modify the url based on i.
    #Also, the reason we decode it is to convert it to a string.
    links = urllib.request.urlopen(f"https://www.charitydir.com/views_2018_08_05/charities/getCharities.php?name=undefined&page={i + 1}&all=true").read().decode("utf-8")

    #So I've done some research and according to canada.ca, a Buisness Number consists of a 9 digit buisness number, followed by RR, followed by 0001.
    #Therefore, all we have to do is make a regex string that scans for 9 digits followed by RR0001.
    BN = re.findall("[0-9]{9}RR0001", links)
    for bn in BN:
        row = []
        #Opens data for specific CSV file
        data = urllib.request.urlopen(f"https://www.charitydir.com/views_2018_08_05/charity/getCharityBasic.php?BN={bn}").read().decode("utf-8")

        #Get Contact Name 
        x = re.findall('"PublicContactName":"(.*)","Contact',data)
        x.append(None)
        row.append(x[0])

        #Get Email
        x = re.findall('"Email":"(.*)","Web',data)
        x.append(None)
        row.append(x[0])

        #Get Phone Number
        x = re.findall('ContactPhoneNumber":"(.*)","status',data)
        x.append(None)
        row.append(x[0])

        #Get Website
        x = re.findall('Website":"(.*)","Address',data)
        x.append(None)
        row.append(x[0])

        #Get Charity Name
        x = re.findall('LegalName":"(.*)","AccountName',data)
        x.append(None)
        row.append(x[0])

        #Revenue is stored in a different php file
        data = urllib.request.urlopen(f"https://www.charitydir.com/views_2018_08_05/charity/getCharity.php?BN={bn}").read().decode("utf-8")

        #Get Revenue
        x = re.findall('4700":"(.*)","4800', data)
        x.append(0)
        row.append(x[0])

        #Writes it to CSV
        if(float(row[5]) > 200000):
            for cell in row:
                if cell == None:
                    charities.write(",")
                else:
                    charities.write('"'+cell+'",')
            charities.write('\n')
                









charities.close()
