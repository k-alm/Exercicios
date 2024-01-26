notas = []
aprovado = False
av_final = False

def calcular_media(notas):
   return sum(notas)/len(notas)


for i in range(1, 6):
    nota = int(input(f"Digite a sua {i}º nota: "))
    notas.append(nota)

media = calcular_media(notas)

if(media >= 7):
    aprovado = True
elif(media < 7 and media >= 4):
    av_final = True
else:
    aprovado = False

print(f"Média: {media} | Aprovado: {aprovado} | Avaliação Final: {av_final}")