import mod_atv9
def main():
	arquivoH = "pl_homem.csv"
	arquivoM = "pl_mulher.csv"
	arquivo = input("digite qual será o nome do arquivo de saída: ")
	lst_homens = list()
	lst_mulheres = list()
	lst_homens = mod_atv9.f_lerarquivo(arquivoH)
	lst_mulheres= mod_atv9.f_lerarquivo(arquivoM)

	mod_atv9.imprimir(lst_mulheres, "MULHERES", arquivo)
	mod_atv9.imprimir(lst_homens, "HOMENS", arquivo)

	

if __name__ == '__main__':
	main()