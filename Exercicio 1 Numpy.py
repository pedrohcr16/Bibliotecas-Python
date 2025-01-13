1.**Utilizando uma biblioteca numpy siga as instruções abaixo**:

    1.Crie uma array 6x6 preenchida com zero.

    2.Preencha o centro desse array  com uma array preenchida com 4x4 com nº 1.

    3.Preencha o centro desse array  com uma array preenchida com 2x2 com nº 2.

    4.Gere um segundo array 6x6 numeros inteiros aleatórios entre 0 e 2 (seed 0).

    5.Subtraia o primeiro array pelo segundo.

import numpy as np

array_1 = np.full ((6,6),0)
array_1

array_2 = array_1.copy()
array_2 [1:-1, 1:-1] = np.full((4,4),1)
array_2

array_3 = array_2.copy()
array_3 [2:-2, 2:-2] = np.full((2,2),2)
array_3

np.random.seed(0)
array_4 = np.random.randint(low=0, high=3, size= (6,6))
array_4

array_3 - array_4
