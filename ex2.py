# Calculadora de IMC.
import os

nome = input('Digite seu nome: ')
print(f'\tOlá, {nome}! Vamos calcular seu IMC?\n\tInsira os seus dados abaixo:\n')
altura = input('Sua Altura: ')
massa = input('Sua Massa Corpórea: ')
imc = float(massa) / (float(altura) ** 2)
os.system('cls')
print(f'\t{nome.upper()}\n\tTem {altura} de altura e pesa {massa} kg.\n\tSeu IMC é {imc:.2f} !')
