def f_criadict(nome_arquivo: str) -> dict: #função que o dicionario

	#definindo variaveis
	lista = list()
	lista1 = list()
	dicgrupo = dict()	

	# processamento

	for linha in nome_arquivo:
		semN = linha.replace('\n', '')  #tirar o \n
		lista1 = semN.split(",")
		dicgrupo[lista1[0]]=lista1[1:]

	return dicgrupo

def f_sorespostas(dicgrupo: dict) -> list: #função que só deixa as respostas
	#definindo variaveis
	novalista = list()
	lst_respostas  = list()

	#processacemento
	for key in dicgrupo.keys(): # pegando as chaves do dict
		lst_respostas.append(dicgrupo[key]) #colocando so as respostas na lista

	return lst_respostas

def f_calcularpont(grupo1: dict, grupo2: dict) -> list: #função que calcula pontuação
	#definindo variaveis
	lst_pont = list()
	pont = int()
	resposta1 = f_sorespostas(grupo1)
	resposta2 = f_sorespostas(grupo2)


	#processacemento

	for i in range(len(resposta1)):
		for j in range(len(resposta1[i])):
			if resposta1[i][j] == resposta2[i][j] and (resposta1[i][j] == "S" or resposta1[i][j] == "N"): #verifica se a lista1 na posição n tem resposta igual a da lista 2
				pont = pont + 2

			else:
				if resposta1[i][j] == resposta2[i][j] and resposta1[i][j] == "I":
					pont = pont + 1

				else:
					pont = pont + 0
		
		lst_pont.append(pont) #colocar tudo em uma lista
		pont = 0 #zera o pont pra retomar o loop

	return lst_pont

def f_dicjunto(dic_grupo1: dict, dic_grupo2: dict) -> dict: #função retorna o dict {('cpf1', 'cpf2') : 'pontução'}
	#definindo variaveis
	lst_pessoas1 = list() 
	lst_pessoas2 = list()
	lst_total = list()
	lst_pontos = list()
	resposta1 = list()
	resposta2 = list()
	dicionario = dict() #dicionario com as tuplas
	tupla = tuple()

	#processacemento
	lst_pessoas1 = list(dic_grupo1.keys()) #transofrmando as chaves do dicionario em uma lista
	lst_pessoas2 = list(dic_grupo2.keys())
	lst_pontos = f_calcularpont(dic_grupo1, dic_grupo2)

	for i in range(len(lst_pessoas1)):
		tupla = (lst_pessoas1[i], lst_pessoas2[i])
		pont = lst_pontos[i]
		dicionario[tupla] = pont
	
	return dicionario

def f_saidaformat(dicgrupo: dict) -> None: #função print cpf e respectiva resposta
	#definindo variaveis
	lst_respostas = list()
	i = int()
	#processamento
	lst_respostas = f_sorespostas(dicgrupo)
	for key in dicgrupo: 
		print(f"CPF{i+1}: {key} Respostas:{lst_respostas[i]}")
		i = i + 1 #contadorzinho do cpf
	print() #print para pular linha só pra ficar mais estético

def f_pontpares(dicgrupo: dict) -> None: #função print pares e respectiva pontuação
	for key in dicgrupo.keys():
		print(f"PAR: {key[0]} E {key[1]} PONTUACAO: {dicgrupo[key]}")













