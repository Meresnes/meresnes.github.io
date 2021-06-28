try:
    import json

except (ImportError):
    print('lib import error')
def json_input(json_file):
    

    with open(json_file) as f:
        try:
            user_data = json.load(f)
        except json.JSONDecodeError:
            print('Its not json file!')
        except FileNotFoundError :
            print('File is not found')
        except


    return user_data

def json_output(data):
    '''
    Testing
    >>> json_output([{"id":1,"first_name":"Susann","last_name":"Wyldish","email":"swyldish0@bing.com","gender":"Female","ip_address":"112.109.35.15"}])
    id  :  1
    first_name  :  Susann
    last_name  :  Wyldish
    email  :  swyldish0@bing.com
    gender  :  Female
    ip_address  :  112.109.35.15

    '''
    try:
        for element in data:

            for item in element:
                try:
                    print(item, ' : ', element.get(item))
                except KeyError:
                    print('Неверное взятие по ключу')

    except IndexError:
        print('Неверное итерирование по объекту')
k = json_input('Json_data.json')
json_output(k)
input()



