'''
Documentation
'''
import json
import requests     

response = requests.get('https://api.nasa.gov/neo/rest/v1/neo/3553060?api_key=j6CZh5icY9RFhZfRZoklyVmQRhCFrLBb06i8CihV')
json_string = response.content
    
parsed_json = json.loads(json_string)

#total = parsed_json['estimated_diameter'] --- Might not need this

# Shows the distance of an asteroid away from Earth in different units (first in the list)
print(parsed_json['close_approach_data'][0]['miss_distance'])

# Shows data on asteroids that closely approached Earth
for closeApproach in parsed_json['close_approach_data']:
    print (closeApproach)

'''
def iterate_dictionary(myDictionary):
    for k, v in myDictionary.items():
        print ("key is " + str(type(k)) + ", value is " + str(type(v)))
        if isinstance(v, dict):
            iterate_dictionary(v)
        else:
            print("{0} : {1}".format(k, v))
            if (isinstance(v, list)):
                for vv in v:
                    if (isinstance(vv, dict)):
                        iterate_dictionary(vv)
iterate_dictionary(closeApproach)
'''