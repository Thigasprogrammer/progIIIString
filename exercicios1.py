# Programa que lê uma sequência da linha de comando e retorna uma tabela com as letras do alfabeto em ordem alfabética 

def main():
	texto = input("digite um texto para ser analisado: ")
	texto = texto.lower()
	dic = {}
	desconsiderar = "/|!@#$%¨&*(1234567890-_=+){}[]:; " #caracteres a desconsiderar


	for i in texto:
		if i not in desconsiderar:
			if i in dic:
				dic[i] = dic.get(i) + 1
			else:
				dic[i] = 1

	lstord = list(dic.keys())
	lstord.sort()

	for j in lstord:
		print(j, " ", dic.get(j))

	

if __name__ == '__main__':
	main()
