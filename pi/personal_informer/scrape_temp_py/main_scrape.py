import requests
import xml.etree.ElementTree as ET

url = "https://meteo.arso.gov.si/uploads/probase/www/observ/surface/text/sl/observation_LJUBL-ANA_BEZIGRAD_latest.xml"
data_file = "data.xml"

resp = requests.get(url)
with open(data_file, "wb") as f:
    f.write(resp.content)

tree = ET.parse(data_file)
root = tree.getroot()

status = "unknown"
temp = "-100"

for target1 in root.iter("nn_icon"):
  status = target1.text

for target2 in root.iter("t"):
  temp = target2.text

print(status, temp)
