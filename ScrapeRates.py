import requests
from bs4 import BeautifulSoup

#
def ScrapeRates(target_url= "https://www.mortgagenewsdaily.com/mortgage-rates"):
    tempR = []
    headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36"}
    
    resp =  requests.get(target_url, headers=headers).text
    soup = BeautifulSoup(resp,'html.parser')

    rateInfo =  soup.find_all('div',{'class':'price'})
    rates = rateInfo[0].contents[0]
    
    #this is here because for some reason SMS wont correctly read the info unless its 
    #taken character by character [***this doesnt work either seems to be a gmail issue***]
    for c in rates:
        tempR.append(c)
    
    return tempR

rates = ScrapeRates()
