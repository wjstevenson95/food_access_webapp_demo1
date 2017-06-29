#!/usr/bin/env python3
# Process CORGIS food_access.json using Python

# Phill Conrad (UCSB) / Sky Adams (SBHS)
# 06/26/2017

import json
import pprint
import tabulate
import codecs

def get_county_dictionary(county_list):
   result = {}
   for c in county_list:
      key = c["State"]+" "+c["County"]
      result[key] = c

   return result
           
def main():
   print ("food_access.py main")
    
if __name__=="__main__":
    main()
