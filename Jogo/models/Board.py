import models.Tile as tl

class Board():
    def __init__(self, tamanho):
        self.tamanho = tamanho
        self.colunas = {
            'A': 0,
            'B': 1,
            'C': 2,
            'E': 3,
            'F': 4,
            'G': 5
        }
        self.grade = [tl.Tile("_")]*self.tamanho
        for n in range(self.tamanho):
            self.grade[n] = [tl.Tile("_")]*self.tamanho

    def imprime(self):
        """
            Imprime a situacao autal do tabuleiro
        """
        print("  A B C D E F") #nome das colunas
        for linha in range(len(self.grade)): #linhas
            novaLinha =  str(linha) + " "
            for tile in self.grade[linha]: #espaco na linha
                novaLinha += tile.imagem + " "
            print(novaLinha)

    def __limpaEspaco(self, posicao: tuple) -> None:
        """
            Limpa um espaco especifico do tabuleiro
        """
        self.grade[posicao[0]][posicao[1]] = tl.Tile("_")

    def posicaoVazia(self, posicao: tuple) -> bool:
        """
            Verifica se uma determinada posicao esta vazia no tabuleiro

            Parametros:
                posicao -> Tupla representando a posicao a ser checada

            Retorno:
                True -> Se a posicao esta vazia \n
                False -> Se a posicao esta ocupada
        """
        coluna = self.colunas[posicao[1]]
        linha = posicao[0]
        tile = self.grade[linha][coluna]
        if(tile.imagem == '_'):
            return True
        return False

    def posicionarPeca(self, posicao: tuple, peca: tl.Tile):
        """
            Coloca uma peca especifica no tabuleiro

            Parametros:
                posicao -> Tupla com a nova posicao da peca \n
                tile -> Tile a ser movido para aquela posicao
            
            Retorno:
                True -> Se foi pocivel colocar a peca no local\n
                False -> Se nao foi pocivel colocar a peca no local
        """
        if(self.posicaoVazia(posicao)):
            coluna = self.colunas[posicao[1]]
            linha = posicao[0]
            ultimaPoseTile = peca.posicao
            print(type(peca))
            if(peca.mover((linha, coluna), self.tamanho)):
                self.__limpaEspaco(ultimaPoseTile)
                self.grade[linha][coluna] = peca
                return True
            else: return False
        else:
            return False
