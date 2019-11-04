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
    for triple in to_translate:
        for tup in 
        string = """
            PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
            SELECT ?label
            WHERE {""" + triple + """ rdfs:label ?label }
        """
        print(string)
        sparql.setQuery(string)
        sparql.setReturnFormat(JSON)
        results = sparql.query().convert()

        for result in results["results"]["bindings"]:
            print('%s: %s' % (result["label"]["xml:lang"], result["label"]["value"]))

if __name__ == "__main__":
    main(sys.argv)