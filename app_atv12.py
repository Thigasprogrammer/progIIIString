import mod_atv12
import sys

def main():
	nomeArq1 = sys.argv[1]
	nomeArq2 = sys.argv[2]
	arq1 = open(nomeArq1, "r")
	Grupo1 = mod_atv12.f_criadict(arq1)
	arq1.close()

	arq2 = open(nomeArq2, "r")
	Grupo2 = mod_atv12.f_criadict(arq2)
	arq2.close()

	# chamando a função d)
	mod_atv12.f_saidaformat(Grupo1)
	mod_atv12.f_saidaformat(Grupo2)

	# printando toscamente os dicionarios
	print(Grupo1)
	print()
	print(Grupo2)
	print()

	#chamando função c)
	c = dict()
	c = mod_atv12.f_dicjunto(Grupo1, Grupo2)
	
	#chamando função e)
	mod_atv12.f_pontpares(c)
	print()
	
	#printando toscamente o dicionario da função c)
	print(c)
	


















if __name__ == "__main__":
	main()