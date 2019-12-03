thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
# print(thisdict)
#
# model = thisdict["model"]
# #print(model)
#
# for x in thisdict:                                                  #pokaże key
#     print(x)
# print()
#
# for x in thisdict:                                                  #pokaże value
#     print(thisdict[x])
# print()
#
# for x,y in thisdict.items():                                        #pokaże key value
#     print(x,y)
# print()

myfamily = {                                                            #slownik gdzie values to kolejne slowniki
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}

y = myfamily["child1"]                                                  #pod zmienna wstawiamy wartosc pierwszego klucza (kolejny slownik)
for x in y:                                                             # dla kazdego elementu w kluczu (kolejnym slowniku)
    print(x)                                                            #wydrukuj klucz
print()
for x in y:                                                             #jak wyzej
    print(y[x])                                                         # wydrukuj wartosc dla klucza