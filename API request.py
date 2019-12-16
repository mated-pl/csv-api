import requests, json, csv  # zaimportowane pakiety

response1 = requests.get("https://reqres.in/api/users")  # zdefiniowana zmienna jako funkcja
#print(response1.status_code)  # metoda zwraca status code zmiennej (response)


def json_print(x):  # funkcja do wydrukowania responsu jako jsona
    txt_response = json.dumps(x, sort_keys=True, indent=3)  # converts python object (x) to json
    print(txt_response)

def api_file_save(x):  # funkcja do zapisania api do pliku
    api_file = open("api_file.txt", "w")  # stworzenie pliku
    txt_response = json.dumps(x, sort_keys=True, indent=3)
    # api_file.write(x.text)    # parametr 'text' funkcji requests zeby zmienic do str
    api_file.write(txt_response)
    api_file.close()

def api_filter(x,key, time):       # funkcja filtruje responsa
    filtered_values = []
    for n in x:
        check = n[key]
        if check > time:
            filtered_values.append(check)
    print(filtered_values)
    return (filtered_values)

def save_csv(x):
    with open('resp.csv', 'w', newline='') as plik:
        writer = csv.writer(plik)
        for n in x:
            writer.writerow([n])

def print_value_for_key_json(x,y):
    key_values = []
    for n in x:
        key_values.append(n[y])
    print(key_values)



# json_print(response1.json())               # wywolana funkcja pokaze calego jsona
# api_file_save(response1.json())            # metoda .json() parsuje zmienna do formatu json

# slownik z parametrami do responsa 2
resp2_param = {
    "lat" : 50.06,
    "lon" : 19.93
}

response2 = requests.get("http://api.open-notify.org/iss-pass.json", params=resp2_param)
print(response2.status_code)
# json_print(response2.json())               # pokaze caly response

pass_time = response2.json()['response']    # extract the pass times from our JSON object. Szuka w slowniku 'response'
response2_key = 'risetime'                          # podaje klucz do szukania
risetime = 1576580000

# risetimes = []                              # pokaze wszystkie wartosci dla klucza risetime i doda do listy
# for x in pass_time:                         # robimy to w kodzie - ponizej funkcja
#     risetimes.append(x['risetime'])
# print(risetimes)

print_value_for_key_json(pass_time,response2_key)   # wywoluje funkcje z 2 zmiennymi

api_filter(pass_time,response2_key,risetime )                # wywolana funkcja do filtrowania
save_csv(api_filter(pass_time, response2_key,risetime))         #dwie funkcje w jednej



