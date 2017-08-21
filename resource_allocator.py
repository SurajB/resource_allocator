
from operator import itemgetter

#Intialization

sorted_lst_west = []
sorted_lst_east = []
west_server_lst = []
east_server_lst = []
output_lst = []

server_dict = {
"large": 1,
"xlarge": 2,
"2xlarge": 4,
"4xlarge": 8,
"8xlarge": 16,
"10xlarge": 32
}

def get_costs(instances, hours = 0, cpus = 0, price = 0):

#Finding the costs per CPU for each server

	for k, v in instances.items():

		for key in v.keys():
			v[key] = v[key]/server_dict[key]

	#print("Cost per CPU: " + str(instances))

#Sorting the dictionary based on values

	for key, value in instances.items():

		if key == "us-west":	
			[ (sorted_lst_west.append((k, v))) for k, v in sorted(value.items(), key = itemgetter(1))]
		else:				
			[ (sorted_lst_east.append((k, v))) for k, v in sorted(value.items(), key = itemgetter(1))]

	#print("Sorted list of us_west: " + str(sorted_lst_west))	
	#print("Sorted list of us_east: " + str(sorted_lst_east))	

#Logic is to find the optimized solution when only no of CPUs and no of hours are given

	if (cpus != 0 or cpus != None) and (price == 0 or price == None):

		west_server_lst, west_cost, east_server_lst, east_cost = cpus_hours(instances, hours, cpus, price, sorted_lst_west, sorted_lst_east)

#Logic to find the optimized solution when only price and no of hours are given

	elif (price != 0 or price != None) and (cpus == 0 or cpus == None):

		west_server_lst, west_cost, east_server_lst, east_cost = price_hours(instances, hours, cpus, price, sorted_lst_west, sorted_lst_east)

#Logic to find optimized solution when no of cpus, price and no of hours are given

	elif (cpus != 0 or cpus != None) and (price != 0 or price != None):

		west_server_lst, west_cost, east_server_lst, east_cost = cpus_hours(instances, hours, cpus, price, sorted_lst_west, sorted_lst_east)

		if (west_cost * 24) > price and (east_cost * 24) > price:

			return "There is no optimal solution for the given inputs: cpus - {}, price - ${}, hours - {}".format(cpus, price, hours)

		elif (west_cost * 24) < price and (east_cost * 24) > price:

			output_lst.append({ "region": "us-west", "total_cost": "$" + str(west_cost * hours), "servers": west_server_lst})
			return output_lst

		elif (west_cost * 24) > price and (east_cost * 24) < price:

			output_lst.append({ "region": "us-east", "total_cost": "$" + str(east_cost * hours), "servers": east_server_lst})
			return output_lst

#Final output list

	if west_cost < east_cost:
		output_lst.append({ "region": "us-west", "total_cost": "$" + str(west_cost * hours), "servers": west_server_lst})
		output_lst.append({ "region": "us-east", "total_cost": "$" + str(east_cost * hours), "servers": east_server_lst})
	else:
		output_lst.append({ "region": "us-east", "total_cost": "$" + str(east_cost * hours), "servers": east_server_lst})
		output_lst.append({ "region": "us-west", "total_cost": "$" + str(west_cost * hours), "servers": west_server_lst})

	return output_lst

def cpus_hours(instances, hours, cpus, price, sorted_lst_west, sorted_lst_east):

	cpu_var = cpus
	west_cost = east_cost = 0

	for item in sorted_lst_west:

		if cpu_var >= int(server_dict[item[0]]):

			np_of_servers = cpu_var // server_dict[item[0]]
			cpu_var = cpu_var % server_dict[item[0]]

			west_server_lst.append((item[0], np_of_servers))
			west_cost += (np_of_servers * instances["us-west"][item[0]] * server_dict[item[0]])

		else:
			continue

	cpu_var = cpus

	for item in sorted_lst_east:

		if cpu_var >= int(server_dict[item[0]]):

			np_of_servers = cpu_var // server_dict[item[0]]
			cpu_var = cpu_var % server_dict[item[0]]

			east_server_lst.append((item[0], np_of_servers))
			east_cost += (np_of_servers * instances["us-east"][item[0]] * server_dict[item[0]])

		else:
			continue

	print("Optimial solution based on the given inputs: cpus - {}, hours - {}".format(cpus, hours))

	return west_server_lst, west_cost, east_server_lst, east_cost


def price_hours(instances, hours, cpus, price, sorted_lst_west, sorted_lst_east):

	price_per_hour = float(price)/hours
	west_cost = east_cost = 0

	for item in sorted_lst_west:

		if price_per_hour > (item[1] * server_dict[item[0]]):

			no_of_servers = int(price_per_hour // (item[1] * server_dict[item[0]]))
			price_per_hour = price_per_hour % (item[1] * server_dict[item[0]])

			west_server_lst.append((item[0], no_of_servers))
			west_cost += (no_of_servers * instances["us-west"][item[0]] * server_dict[item[0]])

		else:
			continue

	price_per_hour = float(price)/hours

	for item in sorted_lst_east:

		if price_per_hour > (item[1] * server_dict[item[0]]):

			no_of_servers = int(price_per_hour // (item[1] * server_dict[item[0]]))
			price_per_hour = price_per_hour % (item[1] * server_dict[item[0]])

			east_server_lst.append((item[0], no_of_servers))
			east_cost += (no_of_servers * instances["us-east"][item[0]] * server_dict[item[0]])
			
		else:
			continue

	print("Optimial solution based on the given inputs: price - ${}, hours - {}".format(price, hours))

	return west_server_lst, west_cost, east_server_lst, east_cost
