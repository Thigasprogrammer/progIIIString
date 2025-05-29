import mod_atv10
import sys

def main():
	nomeArq1 = sys.argv[1]
	nomeArq2 = sys.argv[2]
	arq1 = open(nomeArq1, "r")
	Grupo1 = mod_atv10.f_crialista(arq1)
	arq1.close()

	arq2 = open(nomeArq2, "r")
	Grupo2 = mod_atv10.f_crialista(arq2)
	arq2.close()

	G1 = mod_atv10.f_sorespostas(Grupo1)
	G2 = mod_atv10.f_sorespostas(Grupo2)
	print(G1, G2)
	print(mod_atv10.f_formatacao(Grupo1, Grupo2))

















if __name__ == "__main__":
	main()