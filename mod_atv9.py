def f_lerarquivo(nome_arquivo: str) -> list:

	lst_soma = list()
	ordenado = int()
	soma = int()

	# processamento

	with open(nome_arquivo, 'r', encoding='utf-8') as arq_escrito:
		for linha1 in arq_escrito:
			lista1 = linha1.split(",")
			for i in range(len(lista1)-5):
				ordenado = int(lista1[i + 5])
				soma = soma + ordenado
			lst_soma.append(soma)


	return lst_soma

def imprimir(lst_somas: list, texto: str, arquivo: str) -> None:
	# criando arquivo
	with open(arquivo, 'a', encoding='utf-8') as arquivo:
		arquivo.write(texto + "\n")		
		for i in range(91):
			arquivo.write("IDADE=" + str(i) + " QTD=" + str(lst_somas[i]) + "\n")
		

	print(texto)	
	for i in range(91):
		print("IDADE=%d QTD=%d" % (i, lst_somas[i]))

			