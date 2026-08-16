# Exercício 28 — Gráfico de Barras
import matplotlib.pyplot as plt
alunos = ['Ana', 'Bruno', 'Carlos', 'Diana'] #coloquei um exemplo real, para ve a ilustração do grafico
notas = [7.5, 8.0, 6.0, 9.0]
plt.bar(alunos, notas) #cria o gráfico de barras
plt.title('Notas dos Alunos')
plt.xlabel('Alunos')
plt.ylabel('Notas')
plt.show()