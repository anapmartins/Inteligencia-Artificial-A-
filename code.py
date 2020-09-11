# retorna o indice do menor elemento 
import numpy


def imprime_matriz(mat):
	for i in range(5):
		for j in range(6):
			print(mat[i][j], end = " ")
		print()


# funcao que encontra os caminhos possiveis a partir de um no
def expande_nos(pos, l1, l2, mat, xf, yf, g, custo):
	if pos[0] >= 0 and pos[0] <= 4 and pos[1] >= 0 and pos[1] <= 5 and mat[pos[0]][pos[1]] != 1:
			if pos not in l1 and pos not in l2:
				h = abs(xf - pos[0]) + abs(yf - pos[1])
				g = g + 1
				l2.append(pos)
				custo.append(g+h)

				
def heuristica(mat, xi, yi, xf, yf):
	g = 0
	h = (xf - xi) + (yf - yi)
	destino = [xf, yf]

	# matriz que direciona os possiveis caminhos do ponto atual
	delta = [[-1, 0],   # cima
			 [0, -1],   # esquerda
			 [1, 0],    # baixo
			 [0, 1]]    # direita
	
	caminho = []
	atual = [xi, yi]
	l_fechada = []
	l_aberta = [[xi, yi]]
	custo = [[g+h]]
	
	while len(l_aberta) > 0 and atual != destino:	
		menor_indice = numpy.argmin(custo)
		atual = l_aberta[menor_indice]
		del l_aberta[menor_indice]
		del custo[menor_indice]
		l_fechada.append(atual)
		
		cima = [atual[0]+delta[0][0], atual[1]+delta[0][1]]
		esquerda = [atual[0]+delta[1][0], atual[1]+delta[1][1]]
		baixo = [atual[0]+delta[2][0], atual[1]+delta[2][1]]
		direita = [atual[0]+delta[3][0], atual[1]+delta[3][1]]
	
		expande_nos(cima, l_fechada, l_aberta, mat, xf, yf, g, custo)	
		expande_nos(esquerda, l_fechada, l_aberta, mat, xf, yf, g, custo)
		expande_nos(baixo, l_fechada, l_aberta, mat, xf, yf, g, custo)
		expande_nos(direita, l_fechada, l_aberta, mat, xf, yf, g, custo)
		
		caminho.append(atual)
		
	print(caminho)
	
	
def main():
	mat = [[0,1,0,0,0,0],
		  [0,1,0,0,0,0],
		  [0,1,0,0,0,0],
		  [0,1,0,0,0,0],
		  [0,0,0,0,1,0]]
	
	imprime_matriz(mat)
	
	xi = int(input("Valor da coordenada x do ponto inicial: "))
	yi = int(input("Valor da coordenada y do ponto inicial: "))
	if xi == 1 or yi == 1:
		print("O ponto (%d, %d) eh um ponto inválido" % (xi, yi))

	xf = int(input("Valor da coordenada x do ponto final: "))
	yf = int(input("Valor da coordenada y do ponto final: "))
	if xf == 1 or yf == 1:
		print("O ponto (%d, %d) eh um ponto inválido" % (xf, yf))
	
	heuristica(mat, xi, yi, xf, yf)
	
main()
