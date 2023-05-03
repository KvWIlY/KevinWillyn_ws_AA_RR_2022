import subprocess

tempos = []
for i in range(13):
    # Chama o arquivo executável e captura a saída
    processo = subprocess.Popen(['./TreeRedBlack'], stdout=subprocess.PIPE)
    saida, _ = processo.communicate()
    # Converte a saída para um número de ponto flutuante em milissegundos e adiciona à lista de tempos
    tempos.append(float(saida.decode('utf-8')))

# Calcula a média dos tempos capturados
media = sum(tempos) / len(tempos)

print("A média dos tempos é:", media, "milissegundos")
