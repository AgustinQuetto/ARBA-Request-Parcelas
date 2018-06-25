import json
from area import area
print('-----Convirtiendo-----')
file = open('parcelas.txt', 'r')

objects = []

with open('parcelas.txt') as myFile:
    objects = myFile.read().splitlines()

geoJson = {'type': 'FeatureCollection', 'features': [] }
features = []
version = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11']
parcelasHabilitadas = ['64838', '32739', '44750', '44751', '44752', '64824', '64825', '64841', '64826', '64840', '64827', '64839', '64828', '64308', '64829', '64837', '64830', '64836', '64835', '64833', '64832', '64831', '32740', '44381', '44382', '44383', '44384', '44385', '44386', '44405', '44387', '44388', '44404', '44389', '44403', '44390', '44402', '44391', '44401', '44400', '44399', '44398', '44397', '44396', '44395', '44392', '44393', '74300']

for obj in objects[0:110000]:
    polygon = {'type': 'Feature','properties': {},'geometry': {'type': 'Polygon','coordinates': [] }}
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
    if properties[3] in parcelasHabilitadas:
        features.append(polygon)

geoJson['features'] = features

fileGeoJson = open('geojson/parcelasDron.geojson', 'w')
json.dump(geoJson, fileGeoJson)
fileGeoJson.close()
print('-----Listo-----')