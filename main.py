from requests import get
from pprint import PrettyPrinter 
from datetime import date

today = date.today()

#gets data from
BASE_URL = "https://data.covid19india.org"
ALL_JSON = "/v4/min/timeseries.min.json"

#pretty output
printer = PrettyPrinter()

#gets responce
data = get(BASE_URL + ALL_JSON).json()

#gets data of AN state
links = data['AN']

#gets dates of cases
date = links['dates']

#selected random date from the available dates
keys = date['2021-07-28']

#total cases from that date
total = keys['total']

# confirmed cases
confirmed = total['confirmed']
# dead cases
dead = total['deceased']
# recovered cases
recovered = total['recovered']

#prints the cases
print(f"confirmed = {confirmed} \nrecovered = {recovered} \ndead = {dead}")

# def recovered():
    # recover = date[str(today)]
    # printer.pprint(links)
    
    
# recovered()