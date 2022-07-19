import requests

# Making a GET request
url = "https://meteo.arso.gov.si/uploads/probase/www/observ/surface/text/sl/observation_LJUBL-ANA_BEZIGRAD_latest.xml"
r = requests.get(url)

# check status code for response received
# success code - 200
print(r)

# print content of request
print(r.content)
