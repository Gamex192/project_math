import flet as ft
import openai

openai.api_key = "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"


def main(page: ft.Page):
    def gpt(e):
        if not altura1.value:
            altura1.error_text = "Para que possamos fazer sua dieta é nescessario que saibamos sua altura."
            page.update()
        if not peso1.value:
            peso1.error_text = "Para que possamos fazer sua dieta é nescessario que saibamos seu peso."
            page.update()
        if not idade.value:
            idade.error_text = "Para que possamos fazer sua dieta é nescessario que saibamos sua idade."
            page.update()
        page.clean()
        page.update()
        tamanho = float(altura1.value) ** 2
        massa = float(peso1.value)
        imc = massa / tamanho
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": f"""faça de conta que você é o melhor nutricionista do mundo, e crie 
            uma dieta para uma pessoa com o imc de {imc} e com {idade} anos de idade."""}])
        real_response = response["choices"][0]["message"]["content"]
        v_response = ft.Text(value=real_response)
        imc_response = ft.Text(value=f'')
        if imc < 16:
            imc_response.value = f"seu imc é de {imc}, isso indica que você tem o baixo peso de grau 1."

        elif 16 <= imc < 17:
            imc_response.value = f"seu imc é de {imc}, isso indica que você tem o baixo peso de grau 2."

        elif 17 <= imc < 18.5:
            imc_response.value = f"seu imc é de {imc}, isso indica que você tem o baixo peso de grau 3."

        elif 18.5 <= imc < 25:
            imc_response.value = f"seu imc é de {imc}, isso indica que você está na faixa de peso ideal."

        elif 25 <= imc < 30:
            imc_response.value = f"seu imc é de {imc}, isso indica que você está com sobrepeso."

        elif 30 <= imc < 35:
            imc_response.value = f"seu imc é de {imc}, isso indica que você está com obesidade de grau 1."

        elif 35 <= imc < 40:
            imc_response.value = f"seu imc é de {imc}, isso indica que você está com obesidade de grau 2."

        elif imc > 40:
            imc_response.value = f"seu imc é de {imc}, isso indica que você está com obesidade de grau 3."

        page.clean()
        page.update()
        page.add(imc_response, v_response)

    t = ft.Text(value="Qual sua altura em metros?")
    altura1 = ft.TextField(label="Digite sua altura aqui!")
    t2 = ft.Text(value="Qual seu peso?")
    peso1 = ft.TextField(label="Digite seu peso aqui!")
    t3 = ft.Text(value="Qual sua idade?")
    idade = ft.TextField(label="Digite sua idade aqui!")
    btns = ft.ElevatedButton("clique aqui", on_click=gpt)
    page.add(t, altura1, t2, peso1, t3, idade, btns)
    print(peso1, altura1)


ft.app(target=main)

altura = float(input("Qual sua altura em metros?")) ** 2
peso = float(input("Qual seu peso em quilogramas?"))
