import sys
from tqdm import tqdm
import numpy as np
def main(argv):
    if len(argv) > 1:
        cat = argv[1].lower().capitalize()
    else:
        print("Category not given")
        exit()
    e = []
    with open("data/types_en.json") as f:
        ents = ijson.items(f, "%s.item" % cat)
        for ent in ents:
            e.append(ent)
    print("reading done")
    w = open("data/%s_props_en.nt" % cat, "w")
    with open("data/mappingbased_properties_en.nt") as f:
        for line in tqdm(f):
            if line.split()[0] in e:
                w.write(line)






    """"#t0 = time.time()
    g = Graph()
    g.parse("data/instance_types_en.nt", format="nt")
    print(len(g))
    dbo = Namespace("http://dbpedia.org/ontology/")
    qres = g.query("SELECT * WHERE { ?i ?p dbo:Philosopher }", initNs={'dbo': dbo})
    for row in qres:
        print(row)
    # Iterate over triples in store and print them out.
    #print("--- printing raw triples ---")
    #for s, p, o in g:
     #   print((s, p, o))

    #print(dbo.Philosopher)
    #print(g.serialize(format="nt"))
    #print(time.time() - t0)"""

if __name__ == '__main__':
    main(sys.argv)