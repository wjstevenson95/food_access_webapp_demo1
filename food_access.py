#!/usr/bin/env python3
# Process CORGIS food_access.json using Python

# Phill Conrad (UCSB) / Sky Adams (SBHS)
# 06/26/2017

import json
import pprint
import tabulate
import codecs

def get_county_list(filename='food_access.json'):
   with open(filename) as f:
      return json.loads(f.read())

def get_county_neighbors_dictionary(filename='county_adjacency.json'):
   '''
   Return a dictionary where keys are of the form "XX Foo" where XX is the state abbreviation,
   and Foo is the name of a county, and the values are lists of strings of the same form, 
   indicating adjacent counties.  

   Every county is considered adjacent to itself, and is included in the list.
   Data comes from https://github.com/pconrad/python-county-adjacency/,
   and ultimately from https://www.census.gov/geo/reference/county-adjacency.html
   '''

   with open(filename) as f:
      return json.loads(f.read())

def get_states_list(county_list):

    states = set()
    for county in county_list:
       states.add(county["State"])

    states_list = list(states)
    states_list.sort()
    return states_list

def get_counties_for_state(county_list, state):

    counties = []
    for county in county_list:
       if county["State"]==state:
           counties.append(county)

    counties.sort()
    return counties

def get_county_names_for_state(county_list, state):

    county_names = []
    for county in county_list:
       if county["State"]==state:
           county_names.append(county["County"])

    county_names.sort()
    return county_names

def get_county_dictionary(county_list=get_county_list()):
   result = {}
   for c in county_list:
      key = c["State"]+" "+c["County"]
      result[key] = c

   return result
 
 
def demo1():
    county_list = get_county_list()
    states = get_states_list(county_list)
    print("states",states,"len(states)",len(states))
   
    CA_counties = get_counties_for_state(county_list,"CA")
    print("len(CA_counties)",len(CA_counties))

    CA_county_names = get_county_names_for_state(county_list,"CA")
    print("len(CA_county_names)",len(CA_county_names))
    print("CA_county_names",CA_county_names)

    DE_counties = get_counties_for_state(county_list,"DE")
    print("len(DE_counties)",len(DE_counties))

    DE_county_names = get_county_names_for_state(county_list,"DE")
    print("len(DE_county_names)",len(DE_county_names))
    print("DE_county_names",DE_county_names)
    

def demo2():
    counties = get_county_dictionary(get_county_list())
    sb = counties["CA Santa Barbara"]
    pprint.pprint(sb)
    

def demo3():
    neighbors = get_county_neighbors_dictionary()
    n = neighbors["CA Santa Barbara"]
    print("n",n)
    
def demo4():
    counties = get_county_dictionary(get_county_list())
    neighbors = get_county_neighbors_dictionary()
    sb_neighbors = neighbors["CA Santa Barbara"]

    for n in sb_neighbors:
       data = counties[n]
       pprint.pprint(data,indent=1,compact=True)

def demo5():
    counties = get_county_dictionary(get_county_list())
    selected = ["CA Santa Barbara","CA Ventura","CA Los Angeles"]

    with codecs.open("report.txt","w","utf-8") as outfile:

       for c in selected:
          data = counties[c]
          outfile.write(pprint.pformat(data,indent=1,compact=True))
          
def main():
   # demo1()
   # demo2()
   # demo3()
   # demo4()
   demo5()
    
if __name__=="__main__":
    main()
