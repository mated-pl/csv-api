import requests, json
response = requests.get("https://reqres.in/api/users")      #zdefiniowana zmienna jako funkcja
print(response.status_code)
#print(response.json())

def json_print(x):                                              #funkcja do formatowania jsona
    text = json.dumps(x, sort_keys = True, indent = 3)
    print(text)

json_print(response.json())                             #wywolana funkcja stworzona powyzej