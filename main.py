#Importanto biblioteca
import time

print('Olá')

# colocando nome
resposta1 = input('Qual o seu nome?: ')
resposta2 = print('Prazer! Vou te ajudar a montar sua dieta personalizada, vamos lá?')

#colocando peso e altura
resposta3 = int(input('Qual seu peso (em kg): '))
resposta4 = float(input('Qual a sua altura (em metros): '))

#calculando o IMC
imc = resposta3 / (resposta4)**2

print('Vou calcular seu IMC (Índice de massa corporal)')

#tempo para calcular o IMC (opcional)
print('...')
time.sleep(2)
print('...')
time.sleep(2)
print('...')
time.sleep(2)

#resultado do IMC
print(f'Seu IMC é: {imc}')

#condição
if imc < 18.5:
    print('De acordo com o cálculo do seu IMC você está abaixo do peso indicado')
else:
    print('...')
time.sleep(2)
print('...')
time.sleep(2)
print('...')
time.sleep(2)

if imc > 18.5 <= 24.9:
    print('De acordo o cálculo do seu IMC você está no peso indicado.')
else:
    print('...')

if imc > 25 <= 29.9:
    print('De acordo com cálculo do seu IMC você está no sobrepeso.')
else:
    print('...')

if imc > 30 <= 34.9:
    print('De acordo com cálculo do seu IMC você está na obesidade grau 1.')
else:
    print('...')

if imc > 35 <= 39.9:
    print('De acordo com cálculo do seu IMC você está na obesidade grau 2.')
else:
    print('...')

if imc >= 40:
    print('De acordo com cálculo do seu IMC você está na obesidade móbida.')
else:
    print('...')

# imprimindo dieta
if imc < 18.5:
    print(
        'Vamos te passar algumas dicas de como regular seu peso, mas não se esqueça que de procurar ajuda médica o mais rápido possível! \n1. Comer de 3 em 3 horas; \n2. Incluir proteínas em todas as refeições; \n3. Consumir gorduras boas; \n4. Comer pelo menos 3 frutas por dia; \n5.Beber pelo menos 2,5 L de água por dia; \n6. Realizar atividade física.')
else:
    print('...')

if imc > 18.5 < 24.9:
    print(
        'Vamos te passar algumas dicas para manter sua saúde!\n1. Alimente-se devagar; \n2. Beba, no mínimo, 2 litros de água por dia; \n3. Reduza os níveis de açúcar; \n4. Dê preferência para alimentos integrais; \n5. Inclua alimentos orgânicos em sua alimentação; \n6. Aposte em lanches saudáveis; \n7. Coma a salada primeiro; \n8. Consuma frutas todos os dias.')
else:
    print('...')

if imc > 25 < 39.9:
    print('Vamos te passar algumas dicas de como regular seu peso, mas não se esqueça que de procurar ajuda médica o mais rápido possível! \n1. Reeduque sua alimentação; \n2. Coma fracionado; \n3. Inove no cardápio; \n4. Evite o açúcar refinado; \n5. Dê preferência aos alimentos integrais; \n6. Faça pratos coloridos; \n7. Beba água; \n8. Faça exercícios físicos.')
else:
    print('...')

if imc >= 40:
    print('Procure com extrema urgência o atendimento médico!')
else:
    print('...')