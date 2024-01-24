notas = []
aprovado = False
av_final = False

def calcular_media(notas):
    media = sum(notas)/len(notas)
    return media


for i in range(1, 6):
    nota = int(input(f"Digite a sua {i}º nota: "))
    notas.append(nota)

if(calcular_media(notas) >= 7):
    aprovado = True
elif(calcular_media(notas) < 7 and calcular_media(notas) >= 4):
    av_final = True
else:
    aprovado = False