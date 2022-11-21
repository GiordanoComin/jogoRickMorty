def ler_arquivo():
    try:
        arquivo = open("historico.txt" , "r")
    except:
        arquivo = open("historico.txt" , "w")
        arquivo.close()
        arquivo = open("historico.txt" , "r")
    dados = arquivo.readlines()
    arquivo.close()
    return dados

def salvar_arquivo(dados):
        arquivo = open("historico.txt" , "w")
        arquivo.writelines(dados)
        arquivo.close()

