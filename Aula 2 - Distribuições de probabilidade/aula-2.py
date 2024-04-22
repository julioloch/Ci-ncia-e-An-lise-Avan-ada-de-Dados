import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import binom

n = 30
p = 0.5
x = np.arange(0, n+1)

binomial = binom.pmf(k=x, n=n, p=p)
bars = plt.bar(x, binomial)

for bar in bars:
  bar.set_width(1)

plt.xlabel("x", fontsize=12)
plt.ylabel("Probabilidade", fontsize=12)
plt.xlim([-1, n+1])
plt.title("Distribuição Binomial, n={0}, p={1}".format(n, p), fontsize=15)

# Definindo os ticks do eixo x como inteiros
plt.xticks(np.arange(0, n+1, step=1))

# Plotando a probabilidade máxima e mínima no eixo y em porcentagem
max_prob = np.max(binomial)
min_prob = np.min(binomial)
max_prob_percent = max_prob * 100
min_prob_percent = min_prob * 100
plt.ylim([0, max_prob*1.1])  # Aumenta um pouco para a visualização
plt.text(n, max_prob, f'{max_prob_percent:.2f}%', ha='right', va='bottom')
plt.text(n, min_prob, f'{min_prob_percent:.2f}%', ha='right', va='bottom')

plt.show()