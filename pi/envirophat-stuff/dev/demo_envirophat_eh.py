import sys
import logging
import datetime
import time
import os
from envirophat import weather
import datetime

from azure.eventhub import EventHubClient, Sender, EventData

logger = logging.getLogger("azure")

# Address can be in either of these formats:
# "amqps://<URL-encoded-SAS-policy>:<URL-encoded-SAS-key>@<mynamespace>.servicebus.windows.net/myeventhub"
# "amqps://<mynamespace>.servicebus.windows.net/myeventhub"
# For example:
ADDRESS = "amqps://carvic-eh-ns-demo.servicebus.windows.net/carvic-test1-eh"

# SAS policy and key are not required if they are encoded in the URL
USER = "1mlmiPu9JU3fmEADieTqSBxbVpJCRTEv1QaamD2UtjE"
KEY = "asa-policy-demo"

try:
    if not ADDRESS:
        raise ValueError("No EventHubs URL supplied.")

    # Create Event Hubs client
    client = EventHubClient(ADDRESS, debug=False, username=USER, password=KEY)
    sender = client.add_sender(partition="0")
    client.run()
    try:
        # start_time = time.time()
        # for i in range(100):
        #     print("Sending message: {}".format(i))
        #     sender.send(EventData(str(i)))
        d = datetime.datetime.utcnow().isoformat()

        #print(d)
        #print(weather.temperature())
        #print(weather.pressure(unit='hPa'))

        payload_1 = { "data_source": "temp", "ts": d, "val": weather.temperature() }
        print(payload_1)
        sender.send(EventData(payload_1))
        payload_2 = { "data_source": "pressure", "ts": d, "val": weather.pressure(unit='hPa') }
        print(payload_2)
        sender.send(EventData(payload_2))
        print("done")
    except:
        raise
    finally:
        end_time = time.time()
        client.stop()
        run_time = end_time - start_time
        logger.info("Runtime: {} seconds".format(run_time))

except KeyboardInterrupt:
    pass
