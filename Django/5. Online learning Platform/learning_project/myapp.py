import json
import requests

URL = 'http://127.0.0.1:8000/course-create/'

data = {
    'title':'English',
    'description': 'learning IS AM ARE WITH ING',
    'instructor': 'Ali',
    'duration': '12 months',
    }

json_data = json.dumps(data)

r = requests.post(url=URL, data=json_data)

data1 = r.json
print(data1)
