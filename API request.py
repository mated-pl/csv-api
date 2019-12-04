import requests, json  # zaimportowane pakiety

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


#json_print(response1.json())  # wywolana funkcja stworzona powyzej
#api_file_save(response1.json())  # metoda .json() parsuje zmienna do formatu json

# slownik z parametrami do responsa 2
resp2_param = {
    "lat" : 50.06,
    "lon" : 19.93
}

response2 = requests.get("http://api.open-notify.org/iss-pass.json", params=resp2_param)
print(response2.status_code)
#json_print(response2.json())
pass_time = response2.json()['response']    # extract the pass times from our JSON object
#json_print(pass_time[0])                   # pokaze pierwszy el z listy jsona

risetimes = []
for x in pass_time:                         #pokaze wszystkie wartosci dla klucza risetime i doda do listy
    risetimes.append(x['risetime'])
print(risetimes)

risetimes_filtered = []
for x in pass_time:
    check = x['risetime']
    if check > 1575470000:
        risetimes_filtered.append(check)
print(risetimes_filtered)
