import urllib2
from bs4 import BeautifulSoup
urlpath = 'http://eciresults.nic.in/ConstituencywiseS22'
print "Start"
for i in range(1, 235):
    response = urllib2.urlopen(urlpath+str(i)+".htm?ac="+str(i))
    html = response.read()
    soup = BeautifulSoup(html, 'html.parser')
    result = (soup.find_all(id="div1"))[0].prettify()
    soup = BeautifulSoup(result, 'html.parser')
    result = soup.find_all("td")
    soup = BeautifulSoup(str(result[0]), 'html.parser')
    place = soup.get_text().strip()
    f = open(str(i)+'.csv','w')
    print>>f, place
    print>>f, "Candidate\tParty\tVotes"
    #print place
    #print "Candidate\tParty\tVotes"
    k=1
    for r in result[2:len(result)-2]:
        soup = BeautifulSoup(str(r), 'html.parser')
        res = soup.get_text().strip()
        if k%3==1:
            candidate =  res
        elif k%3==2:
            party =  res
        elif k%3==0:
            vote =  res
            print>>f,  candidate+"\t"+party+"\t"+vote;
        k+=1
    f.close()
    print i
print "Done"    
    
