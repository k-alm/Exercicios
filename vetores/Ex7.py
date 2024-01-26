vetor = [1, 1, 2, 1, 1, 1, 1, 5, 5, 1]

a = int(input("Digite o valor A: "))
b = int(input("Digite o valor B: "))
c = int(input("Digite o valor C: "))

rep_a = vetor.count(a)
rep_b = vetor.count(b)
rep_c = vetor.count(c)

print(f"""O número A aparece {rep_a} vezes no vetor
O número B aparece {rep_b} vezes no vetor
O número C aparece {rep_c} vezes no vetor""")
