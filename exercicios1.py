# Escreva um programa que lê em uma sequência da linha de comando e retorna uma tabela com as letras do alfabeto em ordem alfabética 
# que ocorrem na sequência junto com o número de vezes que cada letra ocorre. 
# Ignore se as letras são maiúsculas ou minúsculas. Um exemplo de execução do programa ficaria assim
def main():
	texto = input("digite um texto para ser analisado: ")
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
