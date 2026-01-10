from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty

DADOS_CLIMA = {
    "lisboa" : {"temp":"22ºC","condicao":"sol"},
    "porto" : {"temp":"18ºC","condicao":"Nublado"},
    "coimbra" : {"temp":"13ºC","condicao":"Chuva"},
    "setubal" : {"temp":"24ºC","condicao":"Parcialmente nublado"}
}

class TelaClima(BoxLayout):
    resultado = StringProperty("Insira uma cidade e carregue em pesquisar")

    def buscar_clima(self):
        cidade = self.ids.entrada.text.lower().strip()
        if cidade in DADOS_CLIMA:
            clima = DADOS_CLIMA[cidade]
            self.resultado = f"{cidade.title()}: {clima['temp']} - {clima['condicao']}"
        else:
            self.resultado = f"'{cidade.title()}:' não encontrada na base de dados"

class Clima(App):
    def build(self):
        return TelaClima()

Clima().run()