import requests
import json

ssn = requests.Session()
"""
start = ssn.get('http://carto.arba.gov.ar/cartoArba2/')
startCookie = ssn.cookies.get_dict()['JSESSIONID']
ssn.cookies.update({'JSESSIONID': startCookie})
print(ssn.cookies)

second = ssn.post('http://carto.arba.gov.ar/cartoArba2/j_spring_security_check', cookies={'JSESSIONID': startCookie})
print(second.text.encode('utf-8'))
secondCookie = ssn.cookies.get_dict()['JSESSIONID']
ssn.cookies.update({'JSESSIONID': secondCookie})
print(ssn.cookies)
"""

file = open('parcelas.txt','a')
log = open('log.txt', 'a')
startCookie = input('Ingrese el cookie:')

for i in range(58413,150000):
  try:
    reqTwo = ssn.get('http://carto.arba.gov.ar/cartoArba2/client/getPdoPda?pdo=118&pda='+str(i)+'&epsg=4326', cookies={'JSESSIONID': startCookie})
    isFound = json.loads(reqTwo.text.encode('utf-8'))
    if isFound['found'] == True:
      log.write('ok: %d' % i)
      file.write(reqTwo.text + '\n')
    else:
      log.write('no: %d' % i)
  except:
    startCookie = input('Ingrese el cookie:')
    reqTwo = ssn.get('http://carto.arba.gov.ar/cartoArba2/client/getPdoPda?pdo=118&pda='+str(i)+'&epsg=4326', cookies={'JSESSIONID': startCookie})
    isFound = json.loads(reqTwo.text.encode('utf-8'))
    if isFound['found'] == True:
      log.write('ok: %d' % i)
      file.write(reqTwo.text + '\n')
    else:
      log.write('no: %d' % i)

file.close()
log.close()

print('-----FINISH-----')
