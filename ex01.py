A = 35
B = 7
C = 3
soma = 0
if A%B != 0:
    soma += 10
else:
    if (A+B)%C == 0:
        soma += 15
    else:
        soma += 5
soma += 5
if soma%C == 0 and soma < A:
    soma += 4
else:
    soma -= 4
if soma <= A and soma % 2 == 0:
    soma += 5
else:
    soma -= 9
if not(soma/2 > B) or (True and False):
    soma += 5
else:
    soma -= 5
print(f"O valor de soma é: {soma}")
#O valor da soma é 16