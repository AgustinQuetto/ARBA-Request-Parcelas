import json
from area import area
print('-----Convirtiendo-----')
file = open('parcelas.txt', 'r')

objects = []

with open('parcelas.txt') as myFile:
    objects = myFile.read().splitlines()

geoJson = {"type": "FeatureCollection", "features": [] }
features = []

for obj in objects:
    polygon = {"type": "Feature","properties": {},"geometry": {"type": "Polygon","coordinates": [] }}
    dic = json.loads(obj)

    coorsString = ''
    for i in dic['result']:
        if i != 'M' and i != 'U' and i != 'L' and i != 'T' and i != 'I' and i != 'P' and i != 'O' and i != 'L' and i != 'Y' and i != 'G' and i != 'O' and i != 'N' and i != '(' and i != ')':
            coorsString = coorsString + i

    latLng = coorsString.split(',')
    propertiesString = dic['message']
    properties = propertiesString.split(' ')
    polygon['properties']['Partido'] = properties[1]
    polygon['properties']['Parcela'] = properties[3]
    coords = []

    for coor in latLng:
        finallyCoor = coor.split(' ')
        finallyCoor[0] = float(finallyCoor[0])
        finallyCoor[1] = float(finallyCoor[1])
        coords.append(finallyCoor)

    #polygon['properties']['m2'] = area(polygon['geometry'])
    #print(polygon['properties']['m2'])
    polygon['geometry']['coordinates'] = [coords]
    features.append(polygon)

geoJson['features'] = features

fileGeoJson = open('parcelas.geojson', 'w')
json.dump(geoJson, fileGeoJson)
fileGeoJson.close()
print('-----Listo-----')