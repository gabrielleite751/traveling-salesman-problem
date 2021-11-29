import sys
import time


citys = 15 # Number of cities


def tsp(matrix, init):
	""" Return the shortest way
        
        Args:
            matrix (array): Matrix with the distance between cities.
            init (int): City of origin.
        
        Returns:
            list: Fastest way list.
    """
	min_path = sys.maxsize
	aux = []
	path = []
	
	for i in range(citys):
		if i != init:
			aux.append(i)

	while True:
		current_path_weight = 0
		
		k = init
		
		for i in range(len(aux)):
			current_path_weight += matrix[k][aux[i]]
			k = aux[i]

		current_path_weight += matrix[k][init]

		if current_path_weight < min_path:
			min_path = current_path_weight
			path = aux.copy()

		if not next_permutation(aux):
			break

	return path


def next_permutation(aux):
	""" Check if there is a next permutation.
        
        Args:
            aux (list): list with actual permutation.
        
        Returns:
            bool: Whether if the operation was sucessful or not.
    """
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


def output_print(path, matrix, init):
	end_time = time.time() - start_time
	print('---------------------------------------------------------------')
	print('|                             AV2                             |')
	print('---------------------------------------------------------------')
	print('\nEquipe:\n\tGabriel Leite;\n\tRenan Didier;\n\tJoão Dowsley')
	print('\nComentário:\n\tSolução desenvolvida ultilizando método de Força Bruta')
	print(f'\nNumero total de cidades: {citys}')
	print(f'\nNumero de cidades da rota: {len(path)+1}')
	print(f'\nSequencia da rota:\n\t', end='')
	print(f'{init}', end=' -> ')
	for i in path:
		print(f'{i}', end=' -> ')
	print(init)
	print(f"\nTempo de execução: {end_time} seconds")


if __name__ == "__main__":
	# Matriz exemplo
	
	start_time = time.time()

			#   1   2   3   4   5   6   7   8   9  10  11  12  13  14  15
	matrix = [[ 0,  5, 15, 20,  3,  8, 10,  2, 14, 20,  9, 13, 11,  6, 12], #1
              [ 5,  0,  1,  1,  4,  2, 14, 12,  3,  4,  6, 18, 14, 19,  7], #2
              [15,  1,  0, 16, 15,  3,  5,  7, 14, 18, 17,  3, 13,  9, 10], #3
              [20,  1, 16,  0, 14,  4, 13,  4, 16, 19, 20, 13,  9, 12, 11], #4
              [ 3,  4, 15, 14,  0, 15, 18, 14,  3,  5, 10,  6, 14, 10,  4], #5
              [ 8,  2,  3,  4, 15,  0, 10, 11,  4,  8,  9, 11, 23, 12,  7], #6
              [10, 14,  5, 18, 14, 10,  0, 12, 37, 11, 56,  1,  6,  9, 10], #7
              [ 2, 12,  7,  4, 14, 11, 12,  0, 13, 18, 20, 21, 47,  1,  4], #8
              [14,  3, 14, 16,  3,  4, 37, 12,  0,  9,  7, 10, 20, 45,  3], #9
              [20,  4, 18, 19,  5,  8, 11, 18,  9,  0,  1,  7,  5,  6,  1], #10
              [ 9,  6, 17, 20, 10,  9, 56, 20,  7,  1,  0,  3,  2,  5,  1], #11
              [13, 18,  3, 13,  6, 11,  1, 21, 10,  7,  3,  0,  4,  1,  8], #12
              [11, 14, 13,  9, 14, 23,  6, 47, 20,  5,  2,  4,  0, 3 ,  1], #13
              [ 6, 19,  9, 12, 10, 12,  9,  1,  6, 45,  6,  1, 63,  0, 12], #14
              [12,  7, 10, 11,  4,  7, 10,  4, 19,  3,  1,  8,  4,  1,  0]] #15

	# Simple test case	
	#matrix = [[ 0,  5, 15, 20,  3,  8, 10,  2, 14, 20], #1
    #          [ 5,  0,  1,  1,  4,  2, 14, 12,  3,  4], #2
    #          [15,  1,  0, 16, 15,  3,  5,  7, 14, 18], #3
    #          [20,  1, 16,  0, 14,  4, 13,  4, 16, 19], #4
    #          [ 3,  4, 15, 14,  0, 15, 18, 14,  3,  5], #5
    #          [ 8,  2,  3,  4, 15,  0, 10, 11,  4,  8], #6
    #          [10, 14,  5, 18, 14, 10,  0, 12, 37, 11], #7
    #          [ 2, 12,  7,  4, 14, 11, 12,  0, 13, 18], #8
    #          [14,  3, 14, 16,  3,  4, 37, 12,  0,  9], #9
    #          [20,  4, 18, 19,  5,  8, 11, 18,  9,  0]] #10
	init = 9 # City of origin

	path = tsp(matrix, init)
	output_print(path, matrix, init)
