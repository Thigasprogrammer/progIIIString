import mod_atv11
import sys

def main():
	nomeArq1 = sys.argv[1]
	nomeArq2 = sys.argv[2]
	arq1 = open(nomeArq1, "r")
	Grupo1 = mod_atv11.f_crialista(arq1)
	arq1.close()

	arq2 = open(nomeArq2, "r")
	Grupo2 = mod_atv11.f_crialista(arq2)
	arq2.close()

	#função c) criando lista com pares e pontos das respostas
	lst_pontuacao = mod_atv11.f_formatacao(Grupo1, Grupo2)

	#print função d)
	mod_atv11.f_saidaformat(Grupo1)
	mod_atv11.f_saidaformat(Grupo2)

	print() #pular linha pra ficar mais estético

	#print função e)
	mod_atv11.f_pontpares(lst_pontuacao)


















if __name__ == "__main__":
	main()