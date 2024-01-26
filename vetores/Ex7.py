vetor = [1, 1, 2, 1, 1, 1, 1, 5, 5, 1]

rep_a = 0
rep_b = 0
rep_c = 0

a = int(input("Digite o valor A: "))
b = int(input("Digite o valor B: "))
c = int(input("Digite o valor C: "))


for i in vetor:
    match i:
        case a:
            rep_a += 1
        case b:
            rep_b += 1
        case c:
            rep_c += 1

print(f"""O número A aparece {rep_a} vezes no vetor
O número B aparece {rep_b} vezes no vetor
O número C aparece {rep_c} vezes no vetor""")
