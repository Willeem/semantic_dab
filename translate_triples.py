from SPARQLWrapper import SPARQLWrapper, JSON
import sys, json
from collections import defaultdict 


def main(argv):
    if len(argv) > 1:
        print('hello world')
        cat = argv[1].lower().capitalize()
    else:
        print("Category not given")
        exit()
    
    with open("new_triples/new_property_nl_%s.json" %cat, 'r') as js:
        to_translate = json.load(js)
    with open("new_triples/new_property_nl_%s_old.json" % cat, 'r') as js:
        old = json.load(js)

    sparql = SPARQLWrapper("http://dbpedia.org/sparql")
    output_dict = defaultdict(list)
    old_dict = defaultdict(list)
    print(len(to_translate))
    for triple in to_translate:
        for string in to_translate[triple]:
            third_query = False
            first_value = ""
            second_value = ""
            third_value = ""
            first = string.split()[0]
            second = string.split()[1]
            third = " ".join(string.split()[2:])
            third = third[:-1]
            if '<http://www.w3.org/2001/XMLSchema#gYear>' in third:
                third_value = (int(third.split('^^')[0].replace('"','')))
            elif third[0] == "<":
                third_query = True 
            else:
                third_value = third
            sparql.setReturnFormat(JSON)
            first_string = """
                    PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
                    SELECT ?label
                    WHERE {""" + first + """ rdfs:label ?label .}
                """
            sparql.setQuery(first_string)
            results = sparql.query().convert()
            for result in results["results"]["bindings"]:
                if result['label']['xml:lang'] == 'nl':
                    first_value = result["label"]["value"]
            if first_value != "":
                if second.split('/')[-1] != "mainInterest>":
                    second_string =  """
                            PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
                            SELECT ?label
                            WHERE {""" + second + """ rdfs:label ?label .}
                        """
                    sparql.setQuery(second_string)
                    results = sparql.query().convert()
                    for result in results["results"]["bindings"]:
                        if result['label']['xml:lang'] == 'nl':
                            second_value = result["label"]["value"]
                else:
                    second_value = "Vakgebied"
                
                if second_value != "":
                    if third_query == True:
                        third_string =  """
                            PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
                            SELECT ?label
                            WHERE {""" + third + """ rdfs:label ?label .}
                        """
                        sparql.setQuery(third_string)
                        results = sparql.query().convert()
                        for result in results["results"]["bindings"]:
                            if result['label']['xml:lang'] == 'nl':
                                third_value = result["label"]["value"]
                        if third_value != "":
                            continue
                        else:
                            third_string =  """
                            PREFIX owl: <http://www.w3.org/2002/07/owl#>
                            SELECT ?same
                            WHERE {""" + third + """ owl:sameAs ?same .}
                            """
                            sparql.setQuery(third_string)          
                            results = sparql.query().convert()
                            for result in results["results"]["bindings"]:
                                if result['same']['value'].split('/')[2][:2] == "nl":
                                    third_value = result['same']['value'].split('/')[-1]
                                    print(str(second_value) + " " + str(third_value))       
                    if third_value != "":                     
                        output_dict[first_value].append((str(second_value),str(third_value)))
                if string in old[triple]:
                    old_dict[first_value].append((str(second_value),str(third_value)))

    for key in output_dict:
        for line in old_dict[key]:
            print(line)
        for line in output_dict[key]:
            print(line)


    with open("output_triples/triples_nl_%s.json" % cat , 'w') as js:
        json.dump(output_dict, js)

    with open("output_triples/triples_nl_%s_old.json" % cat , 'w') as js:
        json.dump(old_dict, js)


if __name__ == "__main__":
    main(sys.argv)