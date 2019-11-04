from collections import defaultdict
import json
import sys 


def main(argv):
    if len(argv) > 1:
        print('hello world')
        cat = argv[1].lower().capitalize()
    else:
        print("Category not given")
        exit()

    with open('../data/%s_en.nt' %cat,'r') as g:
        g_dict = defaultdict(list)
        for line in g:
            g_dict[line[0]].append(line)

    with open('../data/%s_nl.nt' %cat,'r') as h:
        h_dict = defaultdict(list)
        for line in h:
            h_dict[line[0]].append(line)

    similar_keys = {k for k in g_dict if k in h_dict}

    types = [string.split()[1] for key in similar_keys for string in h_dict[key]]
    output_dict = defaultdict(list)
    i = 0
    for key in similar_keys:
        for string in g_dict[key]:
            if string.split()[1] not in types and "@en" not in string:
                output_dict[string.split()[0]].append(string)
    print(len(output_dict))
    with open("new_triples/new_property_nl_%s.json" %cat, 'w') as js:
        json.dump(output_dict, js)
    print("%s done" % cat)




if __name__ == '__main__':
    main(sys.argv)