def f_crialista(nome_arquivo: str) -> list: #função que cria a lista

	#definindo variaveis
	lista = list()
	lista1 = list()	

	# processamento

	for linha in nome_arquivo:
		semN = linha.replace('\n', '')  #tirar o \n
		lista1 = semN.split(",")
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

def f_formatacao(lst_grupo1: list, lst_grupo2: list) -> list: #função retorna lista ['cpf1', 'cpf2', 'pontução']
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

def f_saidaformat(lst_grupo: list) -> None: #função print cpf e respectiva resposta
	#definindo variaveis
	lst_respostas = list()
	#processamento
	lst_respostas = f_sorespostas(lst_grupo)
	for i in range(len(lst_grupo)): # lst_respostas tem o mesmo tamanho de lst_grupo porquê só tira o cpf da sublista
		print(f"CPF{i+1}: {lst_grupo[i][0]} Respostas:{lst_respostas[i]}")
	print() #pular linha para ficar mais evidente a divisão de listas no terminal

def f_pontpares(lst_pares: list) -> None: #função print pares e respectiva pontuação
	for i in range(len(lst_pares)):
		print(f"PAR: {lst_pares[i][0]} E {lst_pares[i][1]} PONTUACAO: {lst_pares[i][2]}")













