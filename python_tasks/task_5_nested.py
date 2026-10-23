# Task: Deep Dictionary Navigation
# Instructions: Extract 'year'. If any key is missing, return "Unknown".

def get_vehicle_year(data):
    # TODO: Write your logic here safely
    for k in data:
        if k == 'specs':
            ret_val = get_vehicle_year(data[k])
            if ret_val != 'Unknown':
                return ret_val
        elif k == 'model_info':
            ret_val = get_vehicle_year(data[k])
            if ret_val != 'Unknown':
                return ret_val 
        elif k == 'year':
            return data[k]
    return 'Unknown'
         

# Test Case
vehicle = {'specs': {'model_info': {'year': 2024}}}
# Expected: 2024
print(get_vehicle_year(vehicle))