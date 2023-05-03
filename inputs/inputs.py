import random
import csv

def gerar_csv(nome_arquivo, n):
    with open(nome_arquivo, 'w', newline='') as arquivo:
        writer = csv.writer(arquivo)
        for i in range(n):
            valor = random.randint(1, 100000000)
            writer.writerow([valor])
        


# Gerando os arquivos CSV
# gerar_csv('arquivo_1k.csv', 1000)
# gerar_csv('arquivo_10k.csv', 10000)
# gerar_csv('arquivo_100k.csv', 100000)
# gerar_csv('arquivo_500k.csv', 500000)
# gerar_csv('arquivo_1m.csv',1000000)
# gerar_csv('arquivo_10m.csv',10000000)
gerar_csv('arquivo_25m.csv',25000000)

