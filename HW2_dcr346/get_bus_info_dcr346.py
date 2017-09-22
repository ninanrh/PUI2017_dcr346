from __future__ import print_function
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

if not len(sys.argv) == 4:
    print("Invalid number of arguments. Run as: python get_bus_info_dcr346.py MTA_KEY BUS_LINE BUS_LINE.csv")
    sys.exit()
    
MTA_KEY = sys.argv[1]
BUS_LINE = sys.argv[2]

url = "http://bustime.mta.info/api/siri/vehicle-monitoring.json?key=" + MTA_KEY + \
"&VehicleMonitoringDetailLevel=calls&LineRef=" + BUS_LINE + BUS_LINE

response = urllib.urlopen(url)
data = response.read().decode("utf-8")
data = json.loads(data)

allbuses = data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity']

fout = open(sys.argv[3], "w")

fout.write("Latitude,Longitude,Stop Name,Stop Status\n")

for bus in range(len(allbuses)):
    Latitude = allbuses[bus]['MonitoredVehicleJourney']['VehicleLocation'].values()[0]
    Longitude = allbuses[bus]['MonitoredVehicleJourney']['VehicleLocation'].values()[1]
    if len(Stop_Name) == 0:
        Stop_Name = "N/A"
        continue
    elif len(Stop_Status) == 0:
        Stop_Status = "N/A"
        continue
    else:
        Stop_Name = allbuses[bus]['MonitoredVehicleJourney']['OnwardCalls']['OnwardCall'][0]['StopPointName']
        Stop_Status = allbuses[bus]['MonitoredVehicleJourney']['OnwardCalls']['OnwardCall'][0]['Extensions']['Distances']['PresentableDistance']

    fout.write('{},{},{},{}\n'.format(Latitude, Longitude, Stop_Name, Stop_Status))