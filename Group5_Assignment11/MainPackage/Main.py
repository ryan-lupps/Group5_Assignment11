'''
Documentation
'''
import json
import requests     

response = requests.get('https://api.nasa.gov/neo/rest/v1/feed?start_date=2015-09-07&end_date=2015-09-08&api_key=j6CZh5icY9RFhZfRZoklyVmQRhCFrLBb06i8CihV')
json_string = response.content
    
parsed_json = json.loads(json_string)

total = parsed_json['element_count']

for solHours in parsed_json['near_earth_objects']:    
    print (solHours)

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
iterate_dictionary(solHours)
'''