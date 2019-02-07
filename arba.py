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

_file = open('parcelas.txt','a')
log = open('log.txt', 'a')
startCookie = ""

for i in range(0,200000):
  try:
    reqTwo = ssn.get('http://www.carto.arba.gov.ar/cartoArba/client/getPdoPda?pdo=63&pda='+str(i)+'&epsg=4326', cookies={'JSESSIONID': startCookie}, verify=False)
    isFound = json.loads(reqTwo.text.encode('utf-8'))
    print(reqTwo.text.encode('utf-8'))
    if isFound['found'] == True:
      log.write('\nok %d' % i)
      print(reqTwo.text + '\n')
      _file.write(reqTwo.text + '\n')
    else:
      log.write('\nno %d' % i)
  except:
    startCookie = ""
    reqTwo = ssn.get('http://www.carto.arba.gov.ar/cartoArba/client/getPdoPda?pdo=63&pda='+str(i)+'&epsg=4326', cookies={'JSESSIONID': startCookie}, verify=False)
    isFound = json.loads(reqTwo.text.encode('utf-8'))
    if isFound['found'] == True:
      log.write('ok: %d' % i)
      _file.write(reqTwo.text + '\n')
    else:
      log.write('no: %d' % i)

_file.close()
log.close()

print('-----FINISH-----')
