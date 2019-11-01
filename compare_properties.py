import rdflib 
from collections import defaultdict 
import json 

for letter in "abcdefghijklmnopqrstuvwxyz":
    with open('properties/props_en_%s.json' %letter,'r') as g:
        g_dict = json.load(g)

    with open('properties/props_nl_%s.json' %letter,'r') as h:
        h_dict = json.load(h)

    similar_keys = {k for k in g_dict if k in h_dict}

    types = [string.split()[1] for key in similar_keys for string in h_dict[key]]
    output_dict = defaultdict(set)
    for key in similar_keys:
        for string in g_dict[key]:
            if string.split()[1] not in types and "@en" not in string:
                output_dict[string.split()[0]].add(string)
    with open("new_triples/new_property_nl_%s.json" %letter, 'w') as js:
        json.dump(output_dict,js)
    print("%s done" %letter)
