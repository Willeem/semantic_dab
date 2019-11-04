from SPARQLWrapper import SPARQLWrapper, JSON
import sys, json

def main(argv):
    if len(argv) > 1:
        print('hello world')
        cat = argv[1].lower().capitalize()
    else:
        print("Category not given")
        exit()
    
    with open("new_triples/new_property_nl_%s.json" %cat, 'r') as js:
        to_translate = json.load(js)

    sparql = SPARQLWrapper("http://dbpedia.org/sparql")
    output_dict = {}
    print(len(to_translate))
    for triple in to_translate:
        for string in to_translate[triple]:
            third_query = False
            first_value = ""
            second_value = ""
            third_value = ""
            first = string.split()[0]
            second = string.split()[1]
            if second[:28] == '<http://dbpedia.org/ontology':
                second_query =  """
                    PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
                    SELECT ?label
                    WHERE {""" + second + """ rdfs:label ?label .}
                """
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
                    output_dict[first_value] = str(second_value) + " " + str(third_value)
                else:
                    print(third)

    print(len(output_dict))
    with open("output_triples/triples_nl_%s.json" % cat , 'w') as js:
        json.dump(output_dict,js)


if __name__ == "__main__":
    main(sys.argv)