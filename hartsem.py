import urllib2
import re
import csv
from bs4 import BeautifulSoup
urlpath = 'http://hirr.hartsem.edu/cgi-bin/mosque/db.pl?view_records=1&ID=*'
print "Start"
with open('hartsem.csv','wb') as csvfile:
    f = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
    f.writerow(["Name","Name1","Address","City", "Zip","State","Phone","Email","Web Link"])
    for i in range(1, 3):
        response = urllib2.urlopen(urlpath+"&nh="+str(i))
        html = response.read()
        ##print html
        soup = BeautifulSoup(html, 'html.parser')
        result = soup.find_all("tr", bgcolor="#E2E2E2")
        print i, len(result)
        for j in range(0,len(result)):
            ##print j,result[j]
            td_result = result[j].find_all("td")
            link = [a["href"] for a in td_result[0].select("a")]
            if (len(link)>0):
                link = link[0].strip()
            else:
                link=""                
            name = td_result[0].find("b").get_text().strip()
            name1 = td_result[0].find("br").get_text().strip()
            street = td_result[1].get_text().strip()
            city = td_result[2].get_text().strip()
            state = td_result[3].get_text().strip()
            zip = td_result[4].get_text().strip()
            phone = td_result[5].get_text().strip()
            phone = phone.replace("email","").strip()
            email = [a["href"] for a in td_result[5].select("a[href^=mailto:]")]
            if (len(email)>0):
                email= re.search('mailto:(.*)',email[0]).group(1).strip()
            else:
                email=""
            ##print j, len(td_result), td_result[0], len(name)
            ##print "\t", j,name+"\t"+name1+"\t"+street+"\t"+city+"\t"+zip+"\t"+state+"\t"+phone+"\t"+email+"\t"+link
            ##print>>f,  name+"\t"+name1+"\t"+street+"\t"+city+"\t"+zip+"\t"+state+"\t"+phone+"\t"+email+"\t"+link
            f.writerow([name,name1,street,city,zip,state,phone,email,link])
print "Done"    
    
