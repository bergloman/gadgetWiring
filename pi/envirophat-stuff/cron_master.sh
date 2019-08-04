# cd /home/pi/dev/event_hubs
# python ../demo_envirophat.py | node test1.js

cd /home/pi/dev
python demo_envirophat.py > /home/pi/dev/sensor_state.txt

cd send_to_perun
/usr/local/bin/node index.js

