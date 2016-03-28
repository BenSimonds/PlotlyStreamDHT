"""
Let's try and stream the data from my rasperry pi / DHT 22 setup to plotly.
"""

import Adafruit_DHT
import plotly.plotly as pl
from plotly.graph_objs import *
import json
import time
import datetime

# Step 1. Set up DHT for polling temp/humidity.

DHT_TYPE = Adafruit_DHT.DHT22
DHT_PIN = 4

"""
# Getting data should be as simple as running:
humidity,temp = Adafruit_DHT.read(DHT_TYPE,DHT_PIN)

print(humidity,temp)
"""

#Might have to try this a few times though as timing is tricky. Sensor returns None sometimes.

#Step 2. Stream to plotly.
with open('./config.json') as config_file:
	plotly_user_config = json.load(config_file)
	pl.sign_in(plotly_user_config["plotly_username"],plotly_user_config["plotly_api_key"])

	trace1 = Scatter(
		x=[],
		y=[],
		mode = 'lines',
		stream = Stream(token=plotly_user_config['plotly_streaming_tokens'][0],maxpoints=100)
		)
	trace2 = Scatter(
		x=[],
		y=[],
		mode = 'lines',
		stream = Stream(token=plotly_user_config['plotly_streaming_tokens'][1],maxpoints=100)
		)

	data = Data([trace1,trace2])

	fig = Figure(date=data)
	url = py.plot(fig,filename = 'Raspberry Pi streaming DHT sensor readings.')

	print('View your streaming graph here:', url)

	#Now we start streaming

	stream1 = pl.Stream(plotly_user_config['plotly_streaming_tokens'][0])
	stream2 = pl.Stream(plotly_user_config['plotly_streaming_tokens'][1])
	stream1.open()
	stream2.open()

	while True:
		humidity,temp = Adafruit_DHT.read(DHT_TYPE,DHT_PIN)
		if humidity is None or temp is None:
			time.sleep(2)	# Wait a bit.
			continue

		stream1.write({'x':datetime.datetime.now(), 'y':humidity})
		stream2.write({'x':datetime.datetime.now(), 'y':temp})

		#Delay between stream posts.
		time.sleep(2)
