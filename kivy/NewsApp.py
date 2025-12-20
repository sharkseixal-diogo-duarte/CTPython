from kivy.app import App
from kivy.uix.screenmanager import ScreenManager,Screen
from kivy.uix.recycleview import RecycleView
from kivy.properties import ObjectProperty
from kivy.clock import Clock

news= [
    {"title": "5 mortos em fuga","descrição":"5 mortos fogem a nado","detalhes": "2 homens e 3 mulheres mortos fogem a nado..."},
    {"title": "6 mortos em fuga","descrição":"6 mortos fogem a nado","detalhes": "3 homens e 3 mulheres mortos fogem a nado..."},
    {"title": "7 mortos em fuga","descrição":"7 mortos fogem a nado","detalhes": "4 homens e 3 mulheres mortos fogem a nado..."},
    {"title": "10 mortos em fuga","descrição":"10 mortos fogem a nado","detalhes": "7 homens e 3 mulheres mortos fogem a nado..."}
]

class MainScreen(Screen):
    list = ObjectProperty(None)

    def on_enter(self):
        Clock.schedule_once(lambda dt:self.carregar())

    def carregar(self):
        self.lista.data = []

        for item in news:
            new = {
                "text": f"{item["title"]}\n{item["descrição"]}",
                "on_release": lambda x=item: self.open_details(x)
            }
            self.lista.data.append(news)

    def open_details(self,new):
        screen_details = self.manager.get_screen('details')
        screen_details.atualzar(new)
        self.manager.current= 'details'

class DetailsScreen(Screen):
    titulo = ObjectProperty(None)
    descricao = ObjectProperty(None)

    def atualizar(self,new):
        self.titulo.text = new['title']
        self.descriçao.text = new['descrição']