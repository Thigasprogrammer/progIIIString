def main():
    nome = "poesia.txt"    # poderia ser um input("Digite o nome do arquivo: ")
    #caso o arquivo nao esteja na pasta deve se especificar o caminho até o arquivo
    # nome = "C:/Users/20241tiimi0194/Desktop/POO1/poesia.txt"   faz com que o arquivo seja criado em outro local
    
    nome = str(input("digite o nome do arquivo que quer ser criado: "))
    # with open(nome, 'w', encoding='utf-8') as arq: 
    #     # CORPO DO WITH
    #     arq.write("    O poeta é um bobão.       ")
    #     arq.write("    Finge tão completamente      ")
    #     arq.write("    Que chega a fingir que é dor ")
    #     arq.write("    A dor que deveras sente.     ")
    #     arq.write("                Fernando Pessoa. ")

    with open(nome, 'a', encoding='utf-8') as arq: #esse adiciona no final do arquivo
        # CORPO DO WITH
        arq.write("    AAAAAAAAAAAAAA       ")
        arq.write("    AAAAAAAAAAAAAAAAAA      ")
        arq.write("    AAAAAAAAAAAAAAAAAAAAAAAAAAA ")
        arq.write("    AAAAAAAAAAAAAAAAAAAA     ")
        arq.write("                Fernando Pessoa. ")


        

    '''pode usar 
    arq = open(nome, 'w', encoding='utf-8') 'w' serve para escrever um dado 'a' (append), acrescenta no final do arquivo, 'r' le o arquivo
    arq.write (write escre um dado no arquivo)'''
        
if __name__ == '__main__':
    main()
