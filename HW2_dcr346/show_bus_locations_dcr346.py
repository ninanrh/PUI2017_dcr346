import sys
import numpy as np
import pandas as pd
import os 
import pylab as pl
import json
try:
    import urllib2 as urllib
except ImportError:
    import urllib.request as urllib

if not len(sys.argv) == 3:
    print("Invalid number of arguments. Run as: python show_bus_locations_dcr346.py MTA_KEY BUS_LINE")
    sys.exit()
    
MTA_KEY = sys.argv[1]
BUS_LINE = sys.argv[2]

url = "http://bustime.mta.info/api/siri/vehicle-monitoring.json?key=" + MTA_KEY + \
"&VehicleMonitoringDetailLevel=calls&LineRef=" + BUS_LINE

response = urllib.urlopen(url)
data = response.read().decode("utf-8")
data = json.loads(data)

allbuses = data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity']

buses = []
for bus in range(len(allbuses)):
    name = allbuses[bus]['MonitoredVehicleJourney']['PublishedLineName']
    location = allbuses[bus]['MonitoredVehicleJourney']['VehicleLocation']
    buses.append((name, location))

print('Bus line: {}'.format(name))
for i in range(len(buses)):
    print ('Bus {} is at latitude {} and longitude {}'.format(i, buses[i][1].values()[0], buses[i][1].values()[1]))