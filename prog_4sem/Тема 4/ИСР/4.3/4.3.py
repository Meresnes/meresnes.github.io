try:
    import json
    import pytest
except (ImportError):
    print('lib import error')
def json_input(json_file):
    

    with open(json_file) as f:
        try:
            user_data = json.load(f)
        except json.JSONDecodeError:
            print('Its not json file!')

    return user_data

def json_output(data):
    str_json = ""
    try:
        for element in data:
            for item in element:
                try:
                    print(item, ' : ', element.get(item))
                    str_json += str(item) + ' : ' + str(element.get(item))+ ""
                except KeyError:
                    print('Key erroe!')

    except IndexError:
        print('Itereting in object error')
    return str_json
def test_1():
    assert json_output([{"id":1,"first_name":"Susann"}]) == "id : 1first_name : Susann"   
k = json_input('Json_data.json')
json_output(k)




