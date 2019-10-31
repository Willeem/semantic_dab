import sys
import json


def main(argv):
    if len(argv) > 1:
        cat = argv[1].lower().capitalize()
    else:
        print("Category not given")
        exit()

    en_dict = json.load(open("../types/types_en.json"))
    ents = en_dict[cat]
    d = {}
    for ent in ents:
        first_char = ent.split("/")[4][0].lower()
        if first_char not in d:
            d[first_char] = [ent]
        else:
            d[first_char].append(ent)
    print("En")
    out = open("../data/%s_en.nt" % cat, "w")
    for char in sorted(d):
        print(char)
        chardict = json.load(open("../properties/props_en_%s.json" % char))
        for ent in d[char]:
            for line in chardict[ent]:
                out.write(line)
    out.close()

    nl_dict = json.load(open("../types/types_nl.json"))
    ents = nl_dict[cat]
    d = {}
    for ent in ents:
        first_char = ent.split("/")[4][0].lower()
        if first_char not in d:
            d[first_char] = [ent]
        else:
            d[first_char].append(ent)
    print("NL")
    out = open("../data/%s_nl.nt" % cat, "w")
    for char in sorted(d):
        print(char)
        chardict = json.load(open("../properties/props_nl_%s.json" % char))
        for ent in d[char]:
            for line in chardict[ent]:
                out.write(line)
    out.close()


if __name__ == '__main__':
    main(sys.argv)