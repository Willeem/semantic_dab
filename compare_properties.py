from collections import defaultdict
import json
import sys 


def main(argv):
    if len(argv) > 1:
        cat = argv[1].lower().capitalize()
    else:
        print("Category not given")
        exit()

    with open('data/%s_en.nt' %cat,'r') as g:
        g_dict = defaultdict(list)
        for line in g:
            g_dict[line.split()[0]].append(line)

    with open('data/%s_nl.nt' %cat,'r') as h:
        h_dict = defaultdict(list)
        for line in h:
            h_dict[line.split()[0]].append(line)

    similar_keys = {k for k in g_dict if k in h_dict}

    output_dict = defaultdict(list)
    old_dict = defaultdict(list)
    for key in similar_keys:
        for string in h_dict[key]:
            print(string)
            print(key)
            old_dict[key].append(string)
            output_dict[key].append(string)
        for string in g_dict[key]:
            if string not in h_dict[key] and "@en" not in string:
                output_dict[key].append(string)
    with open("new_triples/new_property_nl_%s.json" %cat, 'w') as js:
        json.dump(output_dict, js)

    with open("new_triples/new_property_nl_%s_old.json" %cat, 'w') as sd:
        json.dump(old_dict, sd)
    print("%s done" % cat)


if __name__ == '__main__':
    main(sys.argv)