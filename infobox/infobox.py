# Run infobox.py in de terminal. Ga in de browser naar het adres dat in de terminal staat om de webapp te bekijken.

from flask import Flask, render_template, request
import os, json
from collections import defaultdict
app = Flask(__name__)

# Hier moet de datafile geopend worden
# Hier moet een dictionary gemaakt worden met entity als key en een lijst met tuples (property, value) als value
# Voorbeeld:

new_entities, old_entities = {}, {}
BASE_DIR = os.getcwd()
abs_path = BASE_DIR + '/output_triples/'

for filename in os.listdir(abs_path): #laad alle files in de nieuwe triples map
    file_to_load = abs_path + filename
    if 'old' in file_to_load:
        a = json.load(open(file_to_load))
        old_entities.update(a) # en voeg ze toe aan 1 huge dictionary
    else:
        b = json.load(open(file_to_load))
        new_entities.update(b) # en voeg ze toe aan 1 huge dictionary
        

@app.route("/")  # krijg input van de user via een form
def form():
    return render_template('form.html')  # alle entities moeten nog worden toegevoegd in form.html


@app.route("/", methods=['POST'])  # haal input op en laat de bijbehorende infobox zien
def infobox():
    entity = request.form['entity']
    new_dict = defaultdict()
    old_dict = defaultdict()
    print(new_entities[entity])
    for item in new_entities[entity]:
        if "^^" in item[1]:
            value = item[1].split("^^")[0]
        elif "@" in item[1]:
            value = item[1].split("@")[0]
        else:
            value = item[1]
        #print(item[1].strip("'").strip('"').encode('utf-8'))
        new_dict[item[0]] = value.strip("'").strip('"').encode('utf-8')
        #print(new_dict)
    for item in old_entities[entity]:
        if "^^" in item[1]:
            value = item[1].split("^^")[0]
        elif "@" in item[1]:
            value = item[1].split("@")[0]
        else:
            value = item[1]
        #print(item[1].strip("'").strip('"').encode('utf-8'))
        old_dict[item[0]] = value.strip("'").strip('"').encode('utf-8')
    return render_template("infobox.html", new_dict = new_dict, old_dict = old_dict, entity=entity)


if __name__ == "__main__":
    app.run(debug=True)