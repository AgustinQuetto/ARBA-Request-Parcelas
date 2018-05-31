import requests
import json
 
ssn = requests.Session()
#ssn.cookies.update({'visit-month': 'February'})
print('------------------------------------------------')
file = open('parcelas.txt','a')

#ultima http://carto.arba.gov.ar/cartoArba2/client/getPdoPda?pdo=11&pda=302187epsg=EPSG%3A900913
for i in range(22001,32188): #32188
  reqTwo = ssn.get('http://carto.arba.gov.ar/cartoArba2/client/getPdoPda?pdo=118&pda='+str(i)+'&epsg=4326', cookies={'JSESSIONID': '42F8572CC7119FACD6676CCBCC2784C1'})
  isFound = json.loads(reqTwo.text)
  if isFound['found'] == True:
    print(i)
    file.write(reqTwo.text+'\n')

file.close()

print('-----FINISH-----')