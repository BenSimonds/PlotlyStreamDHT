"""
Let's try and stream the data from my rasperry pi / DHT 22 setup to plotly.
"""

import Adafruit_DHT

# Step 1. Set up DHT for polling temp/humidity.

DHT_TYPE = Adafruit_DHT.DHT22
DHT_PIN = 4

# Getting data should be as simple as running:
humidity,temp = Adafruit_DHT.read(DHT_TYPE,DHT_PIN)

print(humidity,temp)