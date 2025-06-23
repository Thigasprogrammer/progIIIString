def f_limpartexto(texto):
    texto = texto.lower()
    desconsiderar = "/|!@#$%&*(1234567890—’”_=+){}[]:;,.?!\"'\n"

    for caractere in desconsiderar:
        texto = texto.replace(caractere, " ")

    palavras = texto.split()
    return palavras


def f_contpalavras(palavras):
    contagem = {}
    for palavra in palavras:
        contagem[palavra] = contagem.get(palavra, 0) + 1
    return contagem

def f_maior_palavra(palavras):
    return max(palavras, key=len)


def f_criararquivo(dic_palavras, nome_arquivo, maior_palavra):
    with open(nome_arquivo, 'w', encoding='utf-8') as f:
        f.write(f"Maior palavra encontrada: {maior_palavra}\n")
        f.write(f"Tamanho da maior palavra: {len(maior_palavra)} caracteres\n\n")
        f.write("Contagem de palavras:\n")
        for palavra in sorted(dic_palavras):
            f.write(f"{palavra}: {dic_palavras[palavra]}\n")


def main():
    with open("alice.txt", "r", encoding="utf-8") as arquivo:
        texto = arquivo.read()

    palavras = f_limpartexto(texto)
    contagem = f_contpalavras(palavras)
    maior_palavra = f_maior_palavra(palavras)
    f_criararquivo(contagem, "alice_words.txt", maior_palavra)


if __name__ == '__main__':
    main()