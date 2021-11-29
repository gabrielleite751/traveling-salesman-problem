# Problema do Caxeiro Viajante
## Descrição do Problema
O Problema do Caixeiro Viajante (PCV) é um problema que tenta determinar a menor rota para percorrer uma série de cidades (visitando uma única vez cada uma delas), retornando à cidade de origem. Ele é um problema de otimização NP-Difícil inspirado na necessidade dos vendedores em realizar entregas em diversos locais percorrendo o menor caminho possível, reduzindo o tempo necessário para a viagem e os possíveis custos com transporte e combustível.


## Força Bruta.
A ideia por trás da nossa implementação pode ser descrita no seguinte passo a passo:

2. Consideramos a cidade 1 como ponto inicial e final. Como a rota é cíclica, consideramos qualquer ponto como ponto de partida.
4. verificamos todas (n-1)! permutações de cidades.
5. Calculamos o custo de todas as permutações e comparamos com as menores encontradas no processo.
6. Retornamos a permutação com menor custo.

A complexidade desse algoritmo é O(n!)

## Conclusão
Devido ao status 2 e outras entregas de fim de período, acabamos deixando o desenvolvimento e escolha do algoritmo para ultima hora. Logo a implementação de uma busca por força bruta foi a melhor solução devido as circunstâncias.

### Outras possíveis soluções:
- A melhor abordagem pra esse cenário talvez fosse o uso de programação dinamica, ja que reduziria o número de possíveis combinações e eliminaria as que não fariam parte de uma solução ótima do problema, deixando o algoritmo mais eficiente.
- Em casos de PCVs contendo de 40 a 60 cidades, uasr o algoritmo branch-and-bound seria a melhor escolha. 
- Em casos de PCVs contendo até 200 cidades, algoritmos de melhoria progressiva que usam técnicas que lembram a programação linear funcionam bem.
