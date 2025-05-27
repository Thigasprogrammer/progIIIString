def f_lerarquivo(nome_arquivo: str) -> list:

	lista = list()
	lista1 = list()

	# processamento

	for linha in nome_arquivo:
		lista1 = linha.split()
		lista.append(lista1)

	return lista

def f_sorespostas(lista: list) -> list:
	novalista = list()
	nova_lst_de_lsts = list()
	for i in range(len(lista)):
		for j in range(len(lista)-1):
			novalista.append(lista[i][j+1])
		nova_lst_de_lsts.append(novalista)
		novalista = []

	return nova_lst_de_lsts

def f_calcularpont(resposta1: list, resposta2: list) -> list:
	lst_pont = list()
	pont = int()
	for i in range(len(resposta1)):
		for j in range(len(resposta1[i][0])):
			if resposta1[i][j] == resposta2[i][j] and (resposta1[i][j] == "S" or resposta1[i][j] == "N"):
				pont = pont + 2
			else:
				if resposta1[i][j] == resposta2[i][j] and resposta1[i][j] == "I":
					pont = pont + 1

				else:
					pont = pont + 0
		lst_pont.append(pont)

	return lst_pont


