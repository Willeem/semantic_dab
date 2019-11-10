from tqdm import tqdm
import os
import json


def main():
    if not os.path.isdir("../types"):
        try:
            os.mkdir("../types")
        except OSError:
            print("Creation of the directory ../types failed, please try again!")
            exit()
    d = {}
    with open("../data/instance_types_en.nt") as f:
        for line in tqdm(f):
            if line[0] != "#":
                l = line.split("/")
                type = l[-1][:-4]
                if l[4]:
                    if type.isalpha() and l[4][0].isalpha():
                        if type in d:
                            d[type].append(line.split()[0])
                        else:
                            d[type] = [line.split()[0]]
    with open("../types/types_en.json", "w") as js:
        json.dump(d, js)
    d = {}
    with open("../data/instance_types_en_uris_nl.nt") as f:
        for line in tqdm(f):
            if line[0] != "#":
                l = line.split("/")
                type = l[-1][:-4]
                if l[4]:
                    if type.isalpha() and l[4][0].isalpha():
                        if type in d:
                            d[type].append(line.split()[0])
                        else:
                            d[type] = [line.split()[0]]
    with open("../types/types_nl.json", "w") as js:
        json.dump(d, js)


if __name__ == '__main__':
    main()