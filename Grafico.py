import matplotlib.pyplot as plt

from Carga import Carga
from Constantes import Constantes


class Grafico:
    def __init__(self):
        self.cargas = [] # Lista de cargas
        
        self.grid = np.linspace(-40, 40, Constantes.pontos())

        '''
        Cria uma grade que vai de -30 até 30 que
        pode ser alterada a depdender da posição
        das cargas ou da posição do clique.
        
        Estes valores serão utilizados para calcular
        o potencial em cada ponto do gráfico.
        '''
        self.X, self.Y = np.meshgrid(self.grid, self.grid)
        '''
        Recebe o mesmo valor de X e Y, mas substitui por zeros.
        
        O valor de cada posição deste array será utilizado
        para desenhar a equipotencial.
        '''
        self.VALORES_Q = np.zeros_like(self.X)

    def desenha_grafico(self, x, y):
        potencial = Carga.calcula_potencial(x, y, self.cargas)
        plt.title(f"Potencial elétrico: {potencial:.2f} Volts")
        plt.scatter(x, y, s=200, marker='o', c='purple')
        plt.text(x, y, f"({x:.2f}, {y:.2f})", ha='center', va='bottom')

