def f_lerarquivo() -> list:
	lst_pessoas = list()
	lst_ord = list()
	arquivo = str(input())
	with open(arquivo, 'r', encoding='utf-8') as arq_escrito:
		for linha in arq_escrito:
			lista = linha.split(";")
			i1 = float(lista[1])
			i2 = float(lista[2])
			lst_ord = [lista[0], i1, i2]
			lst_pessoas.append(lst_ord)


	
	return lst_pessoas

def f_ordIMC(lst_pessoas:list)->list:
	lst_pessoas.sort(key=lambda lista:f_calcularIMC(lista[1], lista[2]))

	return lst_pessoas

def f_calcularIMC(peso: float, altura:float) ->float: 
	IMC = float
	IMC = peso/altura**2

	return IMC

def imprimir(lst_pessoas:list) -> None:
	arquivo = "saida.txt"
	lst_ordenada = f_ordIMC(lst_pessoas)
	with open(arquivo, 'w', encoding='utf-8') as arquivo:
		for i in lst_ordenada:
			arquivo.write(str (i[0]) + ";%.2f" % f_calcularIMC(i[1], i[2]) + "\n")

