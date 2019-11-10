from tqdm import tqdm
import os
import json


def main():
    if not os.path.isdir("../properties"):
        try:
            os.mkdir("../properties")
        except OSError:
            print("Creation of the directory ../properties failed, please try again!")
            exit()
    for letter in "abcdefghijklmnopqrstuvwxyz":
        print(letter)
        d = {}
        with open("../data/mappingbased_properties_en.nt") as f:
            for line in tqdm(f):
                if line[0] == "<":
                    l = line.split("/")
                    if l[4] and l[4][0].lower() == letter:
                        l = line.split()
                        if l[0] not in d:
                            d[l[0]] = [line]
                        else:
                            d[l[0]].append(line)
        with open("../properties/props_en_%s.json" % letter, "w") as out_en:
            json.dump(d, out_en)
        d = {}
        with open("../data/mappingbased_properties_en_uris_nl.nt") as f:
            for line in tqdm(f):
                if line[0] == "<":
                    l = line.split("/")
                    if l[4] and l[4][0].lower() == letter:
                        l = line.split()
                        if l[0] not in d:
                            d[l[0]] = [line]
                        else:
                            d[l[0]].append(line)
        with open("../properties/props_nl_%s.json" % letter, "w") as out_nl:
            json.dump(d, out_nl)


if __name__ == '__main__':
    main()