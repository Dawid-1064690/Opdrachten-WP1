# Ethernet capacity
ethernet_speed_mbps = 1000
efficiency = 0.7
maximum_capacity = ethernet_speed_mbps * efficiency
print(maximum_capacity)

#print capacity used on the ethernet
download_speed_average = 96.25
usage = ethernet_speed_mbps / download_speed_average
print(usage)

#speed of light in m/s
speed_of_light = 299_792_458
# Distance Rotterdam - New York in km
distance_Rotterdam_NewYork = 5_862.03
# Distance Rotterdam to New York in meters divided by the speed of light
time_to_reach_NYC = (distance_Rotterdam_NewYork * ethernet_speed_mbps) / speed_of_light
print(f'Time to reach New York is: {time_to_reach_NYC} seconds => {time_to_reach_NYC * ethernet_speed_mbps} milliseconds')