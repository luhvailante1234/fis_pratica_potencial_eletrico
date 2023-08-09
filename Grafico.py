 def desenha_linha_equipotencial(self, x, y):

        # Calcula o potencial do lugar clicado
        potencial_alvo = Carga.calcula_potencial(x, y, self.cargas)

        # Configura a linha de contorno
        levels = np.linspace(potencial_alvo - 1, potencial_alvo + 1, Constantes.pontos())

        # Calcula os valores de potencial em cada ponto do gráfico
        for i in range(Constantes.pontos()):
            for j in range(Constantes.pontos()):
                for carga in self.cargas:
                    temp_x = self.X[i, j] - carga.x
                    temp_y = self.Y[i, j] - carga.y
                    distancia = np.sqrt(temp_x**2 + temp_y**2)
                    self.VALORES_Q[i, j] += Constantes.constanteEletrostatica() * carga.q / distancia

        # Faz a linha equipotencial com base nos valores iguais ao potencial do ponto clicado
        plt.contour(self.X, self.Y, self.VALORES_Q, levels=levels, colors='grey')

    def atualiza_grafico(self, x, y):
        plt.clf()

        for carga in self.cargas:
            plt.scatter(carga.x, carga.y, s=200, marker='o', c='pink')
            plt.text(carga.x, carga.y, f"{carga.q} C", ha='center', va='center')

        self.desenha_linha_equipotencial(x, y)

        self.desenha_grafico(x, y)

        plt.xlabel("Coordenada x (m)")
        plt.ylabel("Coordenada y (m)")
        plt.grid()
        plt.draw()
