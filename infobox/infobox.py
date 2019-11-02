# Run infobox.py in de terminal. Ga in de browser naar het adres dat in de terminal staat om de webapp te bekijken.

from flask import Flask, render_template, request

app = Flask(__name__)

# Hier moet de datafile geopend worden
# Hier moet een dictionary gemaakt worden met entity als key en een lijst met tuples (property, value) als value
# Voorbeeld:
entities = {"Aristoteles": [("geboren", "384 v.Chr."), ("overleden", "322 v.Chr.")],
            "Plato": [("geboren", "427 v.Chr."), ("overleden", "347 v.Chr.")],
            "Descartes": [("geboren", "31 maart 1596"), ("overleden", "11 februari 1650")]}


@app.route("/")  # krijg input van de user via een form
def form():
    return render_template('form.html')  # alle entities moeten nog worden toegevoegd in form.html


@app.route("/", methods=['POST'])  # haal input op en laat de bijbehorende infobox zien
def infobox():
    entity = request.form['entity']
    value_dict = {"entity": entity}
    for i, property in enumerate(entities[entity]):
        name = "property" + str(i)
        name2 = "value" + str(i)
        value_dict[name] = property[0]
        value_dict[name2] = property[1]

    return render_template("infobox.html", **value_dict)


if __name__ == "__main__":
    app.run(debug=True)