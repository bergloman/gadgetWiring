from envirophat import weather
from envirophat import light
import datetime
import json

d = datetime.datetime.now().isoformat()
#d = datetime.now(timezone.utc).astimezone().isoformat()

#print(d)
#print(weather.temperature())
#print(weather.pressure(unit='hPa'))

#print("tmp=" + str(weather.temperature()))
#print("pressure=" + str(weather.pressure(unit='hPa')))

temp = weather.temperature()
pressure = weather.pressure(unit='hPa')
light_val = light.light()
r, g, b = light.rgb()

payload_1 = { "data_source": "temperature", "ts": d, "val": temp }
print(json.dumps(payload_1))

payload_2 = { "data_source": "pressure", "ts": d, "val": pressure }
print(json.dumps(payload_2))

payload_2 = { "data_source": "light", "ts": d, "val": light_val }
print(json.dumps(payload_2))

payload_2 = { "data_source": "light_r", "ts": d, "val": r }
print(json.dumps(payload_2))

payload_2 = { "data_source": "light_g", "ts": d, "val": g }
print(json.dumps(payload_2))

payload_2 = { "data_source": "light_b", "ts": d, "val": b }
print(json.dumps(payload_2))


