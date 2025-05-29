def f_crialista(nome_arquivo: str) -> list: #função que cria a lista

	#definindo variaveis
	lista = list()
	lista1 = list()	

	# processamento

	for linha in nome_arquivo:
		lista1 = linha.split()
		lista.append(lista1)

	return lista

def f_sorespostas(lista: list) -> list: #função que só deixa as respostas
	#definindo variaveis
	novalista = list()
	nova_lst_de_lsts = list()

	#processacemento
	for i in range(len(lista)):
		for j in range(len(lista[i])-1):
			novalista.append(lista[i][j+1])
		nova_lst_de_lsts.append(novalista)
		novalista = []

	return nova_lst_de_lsts

def f_calcularpont(lista1: list, lista2: list) -> list: #função que calcula pontuação
	#definindo variaveis
	lst_pont = list()
	pont = int()
	resposta1 = list()
	resposta2 = list()

	#processacemento
	resposta1 = f_sorespostas(lista1)
	resposta2 = f_sorespostas(lista2)

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

def f_formatacao(lst_grupo1: list, lst_grupo2: list) -> list:
	#definindo variaveis
	lst_pessoas = list()
	lst_total = list()
	lst_pontos = list()


	#processacemento
	lst_pontos = f_calcularpont(lst_grupo1, lst_grupo2)

	for i in range(len(lst_grupo1)):
		lst_pessoas.append(lst_grupo1[i][0])
		lst_pessoas.append(lst_grupo2[i][0])
		lst_pessoas.append(lst_pontos[i])
		lst_total.append(lst_pessoas)
		lst_pessoas = []

	return lst_total






