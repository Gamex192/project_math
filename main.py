import flet as ft


def main(page: ft.Page):
    t = ft.Text(value="oi")
    page.add(t)


ft.app(target=main)

altura = float(input("Qual sua altura em metros?")) ** 2
peso = float(input("Qual seu peso em quilogramas?"))
imc = peso / altura

if imc < 16:
    print(f"seu imc é de {imc}, isso indica que você tem o baixo peso de grau 1.")
elif 16 <= imc < 17:
    print(f"seu imc é de {imc}, isso indica que você tem o baixo peso de grau 2.")
elif 17 <= imc < 18.5:
    print(f"seu imc é de {imc}, isso indica que você tem o baixo peso de grau 3.")
elif 18.5 <= imc < 25:
    print(f"seu imc é de {imc}, isso indica que você está na faixa de peso ideal.")
elif 25 <= imc < 30:
    print(f"seu imc é de {imc}, isso indica que você está com sobrepeso.")
elif 30 <= imc < 35:
    print(f"seu imc é de {imc}, isso indica que você está com obesidade de grau 1.")
elif 35 <= imc < 40:
    print(f"seu imc é de {imc}, isso indica que você está com obesidade de grau 2.")
elif imc > 40:
    print(f"seu imc é de {imc}, isso indica que você está com obesidade de grau 3.")
