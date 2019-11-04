# Run infobox.py in de terminal. Ga in de browser naar het adres dat in de terminal staat om de webapp te bekijken.

from flask import Flask, render_template, request
import os, json
app = Flask(__name__)

# Hier moet de datafile geopend worden
# Hier moet een dictionary gemaakt worden met entity als key en een lijst met tuples (property, value) als value
# Voorbeeld:

entities = {}
BASE_DIR = os.getcwd()
abs_path = BASE_DIR + '/output_triples/'

for filename in os.listdir(abs_path): #laad alle files in de nieuwe triples map
    file_to_load = abs_path + filename
    a = json.load(open(file_to_load))
    entities.update(a) # en voeg ze toe aan 1 huge dictionary

@app.route("/")  # krijg input van de user via een form
def form():
    return render_template('form.html')  # alle entities moeten nog worden toegevoegd in form.html


@app.route("/", methods=['POST'])  # haal input op en laat de bijbehorende infobox zien
def infobox():
    entity = request.form['entity']
    value_dict = {}
    print(entities[entity])
    for item in entities[entity]:
        item = item.split()
        value_dict[item[1]] = item[2]
    print(value_dict)
    return render_template("infobox.html", value_dict = value_dict, entity=entity)


if __name__ == "__main__":
    app.run(debug=True)