## resource_allocator

The Resource Allocator is responsible for assigning servers for users based on their needs. 
Each server has X number of CPUs. 
The available servers types are:

● large     - 1 CPU
● xlarge    - 2 CPU
● 2xlarge   - 4 CPU
● 4xlarge   - 8 CPU
● 8xlarge   - 16 CPU
● 10xlarge  - 32 CPU

The cost per hour for each server would vary based on the data centre region.

Users will be able to request for

● minimum N CPUs for H hours
● maximum price they are willing to pay for H hours 
● or a combination of both.

Examples:
1. Alice would like to request for servers with minimum 135 CPUs for 24 hours.
2. Bob would like to request as many possible servers for $38 for 10 hours.
3. Charlie would like to request for minimum 180 CPUs and wouldn't want to pay for more than $65 for 6 hours.

### User inputs - 

1. instances - a dict of dicts for each region and which has the instance name and the cost per hour. Each region may not have all server types.
    
    example:
    
    {
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
        },
    }
2. hours - the number of hours he wants to use the servers. (int)
3. cpus - the minimum number of CPUs the user needs. (int)
4. price - the maximum price user is able to pay. (float)

### How to run

1. Download the files into a directory and open the python script run_script.py
2. Provide an instances dictionary input as mentioned in the example above.
3. Uncomment the print function for the required scenario and pass all the user inputs as parameters to the function - get_costs(instances, hours, cpus, price) in the same order. Provide 0 or None in case of not passing value for any of the parameters. 
4. Call the python3 interpreter along with the python script from the local directory where the file is present.

### Run command - python3 run_script.py
