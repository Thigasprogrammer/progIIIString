def main():
    dicionario_pirata = {
        "sir": "matey",
        "hotel": "fleabag inn",
        "student": "swabbie",
        "boy": "matey",
        "madam": "proud beauty",
        "professor": "foul blaggart",
        "restaurant": "galley",
        "your": "yer",
        "excuse": "arr",
        "students": "swabbies",
        "are": "be",
        "lawyer": "foul blaggart",
        "the": "th’",
        "restroom": "head",
        "my": "me",
        "hello": "avast",
        "is": "be",
        "man": "matey"
    }

    pontuacoes = ".,!?;:()[]{}\"'"  # Pontuação a considerar
    frase = input("Digite uma frase em inglês: ")
    palavras = frase.split()
    traducao = []

    for palavra in palavras:
        # Isola pontuação no início e fim
        inicio = ""
        fim = ""
        while palavra and palavra[0] in pontuacoes:
            inicio += palavra[0]
            palavra = palavra[1:]
        while palavra and palavra[-1] in pontuacoes:
            fim = palavra[-1] + fim
            palavra = palavra[:-1]

        # Traduz a palavra se existir no dicionário
        traducao_palavra = dicionario_pirata.get(palavra.lower(), palavra)

        # Reconstrói com pontuação
        traducao.append(f"{inicio}{traducao_palavra}{fim}")

    print("Versão pirata:")
    print(' '.join(traducao))

if __name__ == '__main__':
    main()