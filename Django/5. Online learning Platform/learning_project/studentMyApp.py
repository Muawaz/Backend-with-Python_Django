import json
import requests

URL = 'http://127.0.0.1:8000/student-create/'

data = {
    'rollNo' :  101,
    'name' :    'Aqeel Zaidi',
    'city' :    'Lahore'
    }


json_data = json.dumps(data)
print('Data = ', json_data)


r = requests.post(url=URL, data=json_data)

data1 = r.json
print(data1)
