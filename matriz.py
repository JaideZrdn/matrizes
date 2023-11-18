# Matrizes com Programação orientada a Objetos

class Matriz:

    def __init__(self, conteudo: [[float]]):
        self.num_linhas = len(conteudo)
        self.num_colunas = len(conteudo[0])
        self.matriz = conteudo

    def __getitem__(self, indices):
        i, j = indices
        return self.matriz[i][j]

    def __repr__(self) -> str:
        matriz = ""
        for linha in self.matriz:
            linha_str = " ".join(str(elemento) for elemento in linha)
            matriz += linha_str + "\n"
        return f"Matriz ({self.num_linhas}x{self.num_colunas})\n{matriz}"

    def __mul__(self, outro):
        if isinstance(outro, (float, int)):
            matriz_nova = [[elemento * outro for elemento in linha] for linha in self.matriz]
            return Matriz(matriz_nova)
        elif isinstance(outro, Matriz):
            return self._mulmatrizes(outro)

    def __add__(self, other):
        if isinstance(other, Matriz):
            if self.num_colunas != other.num_colunas or self.num_linhas != other.num_linhas:
                raise ValueError("As matrizes precisam ser da mesma ordem")
            else:
                matriz_nova = [[self.matriz[i][j] + other.matriz[i][j] for j in range(self.num_colunas)] for i in
                               range(self.num_linhas)]
                return Matriz(matriz_nova)

    @staticmethod
    def matrix(linhas: int, colunas: int) -> 'Matriz':
        matriz = []
        for i in range(linhas):
            matriz.append([])
            for j in range(colunas):
                matriz[i].append(0)
        return Matriz(matriz)

    @property
    def transposta(self) -> 'Matriz':
        transposta_da_matriz = [[self.matriz[j][i] for j in range(self.num_linhas)] for i in range(self.num_colunas)]
        return Matriz(transposta_da_matriz)

    @property
    def determinante(self):
        if self.num_colunas != self.num_linhas:
            raise ValueError('Não é uma matriz quadrada')
        if self.num_linhas == 1:
            return self.matriz[0][0]
        else:
            determinante = 0
            for i in range(self.num_linhas):
                determinante += self.matriz[i][0] * self.cofator(i, 0)
        return determinante

    @property
    def adjunta(self):
        adjunta = Matriz.matrix(self.num_linhas, self.num_colunas)
        for i in range(self.num_linhas):
            for j in range(self.num_colunas):
                adjunta.matriz[i][j] = self.cofator(i, j)
        return adjunta

    @property
    def inversa(self):
        determinante = self.determinante
        if determinante == 0:
            raise ValueError('Não é possível calcular a inversa')
        return self.adjunta.transposta * (1 / determinante)

    def cofator(self, linha, coluna):
        matriz2 = []
        for i in range(self.num_linhas):
            if i != linha:
                linha_temp = []
                for j in range(self.num_linhas):
                    if j != coluna:
                        linha_temp.append(self.matriz[i][j])
                matriz2.append(linha_temp)

        cofators = (-1) ** (linha + coluna) * Matriz(matriz2).determinante
        return cofators

    def _mulmatrizes(self, outro):
        if self.num_colunas != self.num_linhas:
            raise ValueError("Número de Colunas da 1º é diferente do número de Linhas da 2º")
        matriz_nova = Matriz.matrix(self.num_linhas, outro.num_colunas)
        for i in range(self.num_linhas):
            for y in range(self.num_colunas):
                for j in range(outro.num_colunas):
                    matriz_nova.matriz[i][j] += self.matriz[i][y] * outro.matriz[y][j]
        return matriz_nova


m1 = Matriz(([1, 2], [3, 4]))
m2 = Matriz(([5, 6], [7, 8]))

print(m1 + m2)
