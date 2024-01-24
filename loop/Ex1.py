anos = 0

a = 80000
b = 200000

taxa_a = 0.03
taxa_b = 0.015

while a < b:
    a += a * taxa_a
    b += b * taxa_b
    anos += 1

print(anos)