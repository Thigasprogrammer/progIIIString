dic1 = {}
dic2 = dict()

dic1["Alex"] = 987.5
dic1["Pedro"] = 44.2
dic1["Lancha"] = 87.3

for i in dic1:
	print("Chave", i)
	print("valor", dic1[i])

print(len(dic1))
chaves = dic1.keys() #atribui as chaves de dic1 a chaves, com o tipo dict_keys
print(chaves)
print(type(chaves)) #printa o tipo de chaves dict_keys
print(len(chaves))
lst_chaves = list(chaves) #transforma chaves originalmente no tipo dict_keys em lista
print(lst_chaves)

valores = dic1.values()
print(type(valores)) #printa o tipo de valores dict_values
print(len(valores))
dic1["Alex"]=99.0
print(dic1)
