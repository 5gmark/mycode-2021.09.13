#!/usr/bin/python3
"""Alta3 || Tracking ISS"""

import urllib.request
import json
import pprint

## Define URL
MAJORTOM = 'http://api.open-notify.org/astros.json'

def Convert(lst):
    res_dct = {lst[i]: lst[i + 1] for i in range(0, len(lst), 2)}
    return res_dct

def main():
        
    ## Call the webservice
    groundctrl = urllib.request.urlopen(MAJORTOM)
    
    ## put fileobject into helmet
    helmet = groundctrl.read()
    
    ## decode JSON to Python data structure
    helmetson = json.loads(helmet.decode('utf-8'))
    
    ## display our Pythonic data
    print("\n\nConverted Python data")
    print(helmetson)
    
    print('\n\nPeople in Space: ', helmetson['number'])
    people = helmetson['people']
    print(people)
#    print(Convert(people))
    print(type(helmetson))
    
#    pp = pprint.PrettyPrinter(indent=4)
#    pp.pprint(people)
#    print("XXXXXXXXXX")
#    for key, value in helmetson.items() :
#        print (key, value)
#    print("XXXXXXXXXX")

    print(f'People in space: {len(helmetson["people"])}')
    print(f'People in space: {helmetson["number"]}')
    for x in helmetson["people"]:
        print(f"{x['name']} is on the {x['craft']}.")
    
main()
