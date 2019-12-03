import requests, json                                                                                                   #zaimportowane pakiety
response = requests.get("https://reqres.in/api/users")                                                                  #zdefiniowana zmienna jako funkcja
print(response.status_code)                                                                                             #metoda zwraca status code zmiennej (response)

def json_print(x):                                                                                                      #funkcja do wydrukowania responsu jako jsona
    txt_response = json.dumps(x, sort_keys = True, indent = 3)                                                          #converts python object (x) to json
    print(txt_response)

def api_file_save (x):                                                                                                  #funkcja do zapisania api do pliku
    api_file = open("api_file.txt", "w")                                                                                #stworzenie pliku
    txt_response = json.dumps(x, sort_keys = True, indent = 3)
    #api_file.write(x.text)                                                                                             #parametr 'text' funkcji requests zeby zmienic do str
    api_file.write(txt_response)
    api_file.close()

#json_print(response.json())                                                                                            #wywolana funkcja stworzona powyzej

api_file_save(response.json())                                                                                          #metoda .json() parsuje zmienna do formatu json
