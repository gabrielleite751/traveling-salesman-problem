import sys
import time

citys = 4

def tsp(matrix, init):
	min_path = sys.maxsize
	path_list = []
	aux = []
	path = []
	
	for i in range(citys):
		if i != init:
			aux.append(i)

	while True:
		print(path)
		current_path_weight = 0
		
		k = init
		for i in range(len(aux)):
			current_path_weight += matrix[k][aux[i]]
			k = aux[i]

		current_path_weight += matrix[k][init]

		if current_path_weight < min_path:
			min_path = current_path_weight
			path = aux

		if not next_perm(aux):
			break

	return path

def next_perm(aux):
    n = len(aux)
    i = n-2

    while i >= 0 and aux[i] > aux[i+1]:
        i -= 1
    
    if i == -1:
        return False

    j = i+1
    while j < n and aux[j] > aux[i]:
        j += 1

    j -= 1

    aux[i], aux[j] = aux[j], aux[i]
    left = i+1
    right = n-1

    while left < right:
        aux[left], aux[right] = aux[right], aux[left]
        left += 1
        right -= 1
    return True

def output_print(path_list,path, matrix, init):
	print('*------- AV2 -------*')
	print('Equipe:\n\tGabriel Leite;\n\tRenan Didier;\n\tJoão Dowsley')
	print('Comentário:\n\tSolução desenvolvida com Programação Dinâmica')
	print(f'Numero total de cidades: {citys}')
	print(f'Numero de cidades da rota: {len(path)+1}')
	print(f'Sequencia da rota:\n\t', end='')
	print(f'{init}', end=' -> ')
	for i in path:
		print(f'{i}', end=' -> ')
	print(init)
	print(f"--- {(time.time() - start_time)} seconds ---")

if __name__ == "__main__":
	# Matriz exemplo
	
	start_time = time.time()

	#matrix = [[ 0,  5, 15, 20,  3,  8, 10,  2, 14, 20,  9, 17, 11,  6, 10], #1
    #          [ 5,  0, 11,  1,  4,  2, 14, 12,  3,  4,  6, 18, 14, 19,  3], #2
    #          [15, 11,  0, 16, 15,  3,  5,  7, 14, 18, 17,  3, 13,  9, 10], #3
    #          [20,  1, 16,  0, 14,  4, 13,  4, 16, 19, 20, 13,  9, 12, 11], #4
    #          [ 3,  4, 15, 14,  0, 15, 18, 14,  3,  5, 10,  6, 14, 10,  4], #5
    #          [ 8,  2,  3,  4, 15,  0, 10, 11,  4,  8,  9, 11, 23, 12,  7], #6
    #          [10, 14,  5, 18, 14, 10,  0, 12, 37, 11, 56,  1,  6,  9, 10], #7
    #          [ 2, 12,  7,  4, 14, 11, 12,  0, 13, 18, 20, 21, 47,  1,  4], #8
    #          [14,  3, 14, 16,  3,  4, 37, 12,  0,  9,  7, 10, 20, 45,  3], #9
    #          [20,  4, 18, 19,  5,  8, 11, 18,  9,  0,  1,  7,  5,  6,  1], #10
    #          [ 9,  6, 17, 20, 10,  9, 56, 20,  7,  1,  0,  3,  2,  5,  1], #11
    #          [17, 18,  3, 13,  6, 11,  1, 21, 10,  7,  3,  0,  4,  1,  8], #12
    #          [11, 14, 13,  9, 14, 23,  6, 47, 20,  5,  2,  4,  0, 3 ,  1], #13
    #          [ 6, 19,  9, 12, 10, 12,  9,  1,  6, 45,  6,  1, 63,  0, 12], #14
    #          [10,  3, 10, 11,  4,  7, 10,  4, 19,  3,  1,  8,  4,  1,  0]] #15

	matrix = [[0,10,15,20], [10,0,35,25], [15,35,0,30], [20,25,30,0]]

	init = 0
    
	path = tsp(matrix, init)
	print(path)
	output_print(path_list, path, matrix, init)