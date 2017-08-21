from resource_allocator import get_costs

instance_dict = {
        "us-east": {
            "large": 0.12,
            "xlarge": 0.23,
            "2xlarge": 0.45,
            "4xlarge": 0.774,
            "8xlarge": 1.4,
            "10xlarge": 2.82
        },
        "us-west": {
            "large": 0.14,
            "2xlarge": 0.413,
            "4xlarge": 0.89,
            "8xlarge": 1.3,
            "10xlarge": 2.97
        }
    }

#Scenario 1 - cpus and hours given
#print(get_costs(instance_dict, 24, 135, 0))

#Scenario 2 - price and hours given
#print(get_costs(instance_dict, 10, 0, 38))

#Scenario 3 - cpus, price and hours are given
print(get_costs(instance_dict, 6, 180, 65))


