# Eindproject Semantic Web
Martijn Baas, Willem Datema, Iris Schepers, Elvira Slaghekke 

## Packages
The necessary packages can be installed via running: 

```
pip install -r requirements.txt 
```
## Explanation
To recreate our experiment please download the English and Dutch types and properties from https://wiki.dbpedia.org/Downloads2014#h395-1 and run the scripts in the following order:

- preprocess_types.py 
- properties.py 
- subset.py [category]
- compare_properties.py [category]
- translate_triples.py [category]
- infobox.py 

To recreate the results of the paper and the presentation, category should be 'philosopher'. Note: Running properties.py takes a lot of time, up to half an hour. The rest of the scripts are fairly quick to run. To view the infoboxes, the names should be spelled exactly like on DBpedia.


