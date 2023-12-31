import requests
import json

URL = 'http://127.0.0.1:8000/stuapi/'

def get_data(id = None ):
    data = {}
    if id is not None:
        data = {'id':id}
    json_data = json.dumps(data)
    response = requests.get(url=URL ,data=json_data)
    data = response.json()
    print(data)
    

# get_data(2)

def post_data():
    data = {
        'name':'sugiyan',
        'roll':300,
        'city':'calicut'
    }
    
    json_data = json.dumps(data)
    r = requests.post(url=URL , data = json_data)
    data = r.json()
    print(data)
    
# post_data()


def update_data():
    data = {
        'id':8,
        'name':'sugiyan',
        'roll':200,
        'city':'calicut'
    }
    json_data = json.dumps(data)
    r = requests.put(url=URL,data = json_data)
    data = r.json()
    print(data)
    
update_data()
    
    
def delete_data():
    data = {'id':9}
    json_data = json.dumps(data)
    r = requests.delete(url=URL,data = json_data)
    data = json.loads(r.content)
    print(data)


# delete_data()