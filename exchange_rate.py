import requests
import xml.etree.ElementTree as ET

url = "https://www.ecb.europa.eu/stats/eurofxref/eurofxref-daily.xml"

response = requests.get(url)
xml_data =  response.content

root = ET.fromstring(xml_data)

ns = {'gesmes': 'http://www.gesmes.org/xml/2002-08-01',
      'ecb': 'http://www.ecb.int/vocabulary/2002-08-01/eurofxref'}

rates = {}
for cube in root.findall('.//ecb:Cube[@currency]', ns):
    currency = cube.attrib['currency']
    rate = float(cube.attrib['rate'])
    rates[currency] = rate

print(" ")
usd = 1 / rates["USD"]
idr = rates["IDR"]

usdidr = usd * idr
