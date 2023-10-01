print('Bem-vindo(a) à calculadora de Índice de Massa Corporal (IMC)!')

nome = input('Informe seu nome: ')
peso = float(input('Informe seu peso(em kg): '))
altura = float(input('Informe sua altura(em m e utilize . no lugar da ,): '))

print(f'Agora vamos calcular seu IMC!')

imc = (peso/(altura*altura))

print(f'{nome}, seu IMC é {imc:.2f}.')

if imc < 18.5:
    print(f'Você está abaixo do peso ideal.')
elif imc < 25.0:
    print(f'Você está com o peso ideal. Parabéns e continue assim!')
elif imc < 30:
    print(f'Você está com sobrepeso. Reveja seus hábitos alimentares e pratique exercícios físicos.')
elif imc < 35:
    print(f'Você está com obesidade grau I. Procure equipe multiprofissional de saúde')
elif imc < 40:
    print(f'Você está com obesidade grau II. Procure equipe multiprofissional de saúde')
else:
    print(f'Você está com obesidade grau III. Procure equipe multiprofissional de saúde')
