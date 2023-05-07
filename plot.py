import os
import pandas as pd
import matplotlib.pyplot as plt

# pasta onde estão os arquivos txt com os tempos de execução
dir_path = './tempos/'

# lista com os tamanhos de entrada (nome dos arquivos csv)
input_sizes = ['1k', '10k', '100k', '500k' ,'1M','5M','10M','25M']

# dicionário para armazenar os dados de tempo de execução médio para cada tamanho de entrada
mean_times = {}

# loop pelos tamanhos de entrada
for size in input_sizes:
    # caminho para o arquivo txt com os tempos de execução
    time_path = os.path.join(dir_path, f'tempo{size}.txt')
    # leitura dos dados com pandas
    df = pd.read_csv(time_path, header=None, names=['tempo'])
    # cálculo da média dos tempos de execução
    mean_time = df.mean().values[0]
    # armazenamento dos dados no dicionário
    mean_times[size] = mean_time

# criação do gráfico
plt.plot(mean_times.values(), mean_times.keys())
plt.xlabel('Tempo de Execução (milissegundos)')
plt.ylabel('Tamanho da Entrada')
plt.title('Gráfico de Tempo de Execução Médio')
plt.show()
