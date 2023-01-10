
import os
import json
import geojson

files = [file for file in os.listdir("./municipios_geojson")]

with open("./municipios_geojson/" + files[25], encoding="utf8") as f:
    data = json.load(f)
    gj = geojson.loads(json.dumps(data))
    for municipios in gj.features:

        meu_feature_collection = {
            "type": "FeatureCollection",
            "features": [municipios]
        }

        with open("./Tocantins/" + municipios.properties["NM_MUN"] + "-" + municipios.properties["SIGLA"] + ".geojson", "w") as outfile:
            json.dump(meu_feature_collection, outfile)
