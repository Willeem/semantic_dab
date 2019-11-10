# Final project Semantic Web
Martijn Baas, Willem Datema, Iris Schepers, Elvira Slaghekke 

## Packages
The necessary packages can be installed via running: 

```
pip install -r requirements.txt 
```
## Explanation

To recreate our experiment please download the English and Dutch types and properties through the following links, extract the files from the bz2 compression and save them in a directory with path ./data: 

- http://data.dws.informatik.uni-mannheim.de/dbpedia/2014/en/instance_types_en.nt.bz2
- http://data.dws.informatik.uni-mannheim.de/dbpedia/2014/nl/instance_types_en_uris_nl.nt.bz2
- http://data.dws.informatik.uni-mannheim.de/dbpedia/2014/en/mappingbased_properties_en.nt.bz2
- http://data.dws.informatik.uni-mannheim.de/dbpedia/2014/nl/mappingbased_properties_en_uris_nl.nt.bz2


After downloading the data run the scripts in the following order:

- preprocess_types.py 
- properties.py 
- subset.py [category]
- compare_properties.py [category]
- translate_triples.py [category]
- infobox.py 

To recreate the results of the paper and the presentation, category should be 'philosopher'. Note: Running properties.py takes a lot of time, up to half an hour. The rest of the scripts are fairly quick to run. To view the infoboxes, the names should be spelled exactly like on DBpedia.


