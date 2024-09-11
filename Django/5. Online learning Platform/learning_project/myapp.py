import json
import requests
import datetime
    
# my_model = MyModel()
# my_model.duration = datetime.timedelta(days=20, hours=10)

URL = 'http://127.0.0.1:8000/course-create/'

data = {
    'course_id': 102,
    'title':'English',
    'description': 'learning IS AM ARE',
    'instructor': 'Ali',
    'duration': str(datetime.timedelta(seconds=18000)),
    }

print('Data = ', data)
json_data = json.dumps(data)


r = requests.post(url=URL, data=json_data)

data1 = r.json
print(data1)
