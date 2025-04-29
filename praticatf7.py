def main():
	total = int()
	media = float()
	arquivo = "idades.txt"
	with open(arquivo, 'r', encoding='utf-8') as arq_entrada:
	 	#CORPO DO WITH
		conteudo = arq_entrada.read()

	lst_idades = conteudo.split()

	
	for i in lst_idades:
		total = total + int(i)
	media = total/len(lst_idades)
	print("MEDIA IDADES=%.2f" % media)

if __name__ == '__main__':
	main()
