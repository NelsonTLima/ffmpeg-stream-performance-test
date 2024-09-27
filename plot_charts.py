import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from os import system

df_cpu = pd.read_csv("./reports/cpu.csv")
df_mem = pd.read_csv("./reports/mem.csv")
df_cpu_time = pd.read_csv("./reports/cpu-time.csv")

media_cpu = df_cpu.rolling(window=5).mean().iloc[-1]
media_mem = df_mem.rolling(window=5).mean().iloc[-1]
media_cpu_time = df_cpu_time.rolling(window=5).mean().iloc[-1]

system("mkdir -p charts/cpu")
for i in range(1,6):
        cpu_experiment = df_cpu.iloc[i-1]
        cpu_experiment.plot()
        plt.title(f"Evolução da CPU no Experimento {i}")
        plt.xlabel("Tempo (s)")
        plt.xticks(ticks=range(len(cpu_experiment)))
        plt.ylabel("Uso da CPU (%)")
        plt.savefig(f'./charts/cpu/cpu-{i}.png')
        plt.close()

media_cpu.plot()
plt.title(f"Evolução da CPU (média dos experimentos)")
plt.xlabel("Tempo (s)")
plt.xticks(ticks=range(len(media_cpu)))
plt.ylabel("Uso da CPU (%)")
plt.savefig('./charts/cpu/cpu-average.png')
plt.close()

system("mkdir -p charts/mem")
for i in range(1,6):
        mem_experiment = df_mem.iloc[i-1]
        mem_experiment.plot()
        plt.title(f"Evolução da Memoria no Experimento {i}")
        plt.xlabel("Tempo (s)")
        plt.xticks(ticks=range(len(mem_experiment)))
        plt.ylabel("Uso da Memoria (%)")
        plt.savefig(f'./charts/mem/mem-{i}.png')
        plt.close()

media_mem.plot()
plt.title(f"Evolução da Memoria (media dos experimentos)")
plt.xlabel("Tempo (s)")
plt.xticks(ticks=range(len(media_mem)))
plt.ylabel("Uso da Memoria (%)")
plt.savefig(f'./charts/mem/mem-average.png')
plt.close()


system("mkdir -p charts/cpu-time")
for i in range(1,6):
        cpu_time_experiment = df_cpu_time.iloc[i-1]
        cpu_time_experiment.plot()
        plt.title(f"Evolução do tempo de CPU no Experimento {i}")
        plt.xlabel("Tempo (s)")
        plt.xticks(ticks=range(len(cpu_time_experiment)))
        plt.ylabel("Tempo de CPU (s)")
        plt.savefig(f'./charts/cpu-time/cpu-time-{i}.png')
        plt.close()

media_cpu_time.plot()
plt.title(f"Evolução do tempo de CPU (em media)")
plt.xlabel("Tempo (s)")
plt.xticks(ticks=range(len(media_cpu_time)))
plt.ylabel("Tempo de CPU (s)")
plt.savefig(f'./charts/cpu-time/cpu-time-average.png')
plt.close()
