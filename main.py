height = float(input('Digite sua altura em m: '))
weight = float(input('Digite seu peso em kg: '))

bmi = weight / (height ** 2)
print(round(bmi, 2))