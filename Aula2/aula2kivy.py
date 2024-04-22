from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
class MainApp(App):

    def build(self):
        # Generate random list of numbers 
        import random
        tabela_numeros = []
        numero_de_numeros =100

        for i in range(numero_de_numeros):
            tabela_numeros.append(random.randint(0, numero_de_numeros)) #adiciona 100 numeros  de 0 a 99   
            #print(f"Valor tabela numeros {tabela_numeros}")

        # temos de ver o tamanho da tabela
        maior_numero = 0
        for i in range(numero_de_numeros):
            if tabela_numeros[i] >= maior_numero:
                maior_numero = tabela_numeros[i]
                print(f"Maior numero na pos {i} tabela é {maior_numero}")
       # print(f"O maior numero  é {maior_numero}")
        return Button(text=str(maior_numero), 
                        font_size=150,
                        color=[1, 0.4, 0, 1],
                        size_hint=(0.8, .5),
                        pos_hint={'center_x':.5, 'center_y':.5})
        
if __name__ == "__main__":
    MainApp().run()