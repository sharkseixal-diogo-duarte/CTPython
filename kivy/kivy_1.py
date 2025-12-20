from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
class MyApp(App):

    def build(self):
        layout = BoxLayout(oriental='vertical')
        self.text = TextInput()
        self.label = Label(text='bla bla bla')
        btn = Button(text='clica')
        btn.bind(on_press=self.update)

        layout.add_widget(self.text)
        layout.add_widget(btn)
        layout.add_widget(self.label)

        return layout

    def update(self, instance):
        self.label.text = self.text.text

MyApp().run()