
from operator import itemgetter

sorted_lst_west = []
sorted_lst_east = []
sorted_lst = []
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

# instance_dict = {
#         "us-east": {
#             "large": 0.12,
#             "xlarge": 0.23,
#             "2xlarge": 0.45,
#             "4xlarge": 0.774,
#             "8xlarge": 1.4,
#             "10xlarge": 2.82
#         },
#         "us-west": {
#             "large": 0.14,
#             "2xlarge": 0.413,
#             "4xlarge": 0.89,
#             "8xlarge": 1.3,
#             "10xlarge": 2.97
#         }
#     }

def get_costs(instances, hours = 0, cpus = 0, price = 0):

	west_cost = 0
	east_cost = 0

#Finding the costs per CPU for each server

	for k, v in instances.items():

		for key in v.keys():
			v[key] = v[key]/server_dict[key]

	print("Cost per CPU: " + str(instances))

#Sorting the dictionary based on values

	#print("Sorting the dictionary based on values: ")
	for key, value in instances.items():

		if key == "us-west":	
			[ (sorted_lst_west.append((k, v))) for k, v in sorted(value.items(), key = itemgetter(1))]
		else:				
			[ (sorted_lst_east.append((k, v))) for k, v in sorted(value.items(), key = itemgetter(1))]

	print("Details of us_west: " + str(sorted_lst_west))	
	print("Details of us_east: " + str(sorted_lst_east))	

	#print(hours, cpus, price)

#Logic is to find the optimized solution when only no of CPUs and no of hours are given

	if cpus != 0 and (price == 0 or price == null):

		#print("first scenario")
		cpu_var = cpus

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

#Logic to find the optimized solution when only price and no of hours are given

	elif (price != 0) and (cpus == 0 or cpus == null):

		#print("second scenario")
		price_per_hour = float(price)/hours

		for item in sorted_lst_west:

			if price_per_hour > (item[1] * server_dict[item[0]]):

				no_of_servers = int(price_per_hour // (item[1] * server_dict[item[0]]))
				price_per_hour = price_per_hour % (item[1] * server_dict[item[0]])

				#print(item[0], (item[1] * server_dict[item[0]]), price_per_hour)

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

#Final output list

	if west_cost < east_cost:
		output_lst.append({ "region": "us-west", "total_cost": "$" + str(west_cost * hours), "servers": west_server_lst})
		output_lst.append({ "region": "us-east", "total_cost": "$" + str(east_cost * hours), "servers": east_server_lst})
	else:
		output_lst.append({ "region": "us-east", "total_cost": "$" + str(east_cost * hours), "servers": east_server_lst})
		output_lst.append({ "region": "us-west", "total_cost": "$" + str(west_cost * hours), "servers": west_server_lst})

	print(output_lst)

#get_costs(instance_dict, 24, 135)
#get_costs(instance_dict, 10, 0, 38)
