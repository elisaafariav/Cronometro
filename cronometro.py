from kivy.app import App 
from kivy.uix.label import Label 
from kivy.uix.boxlayout import BoxLayout 
from kivy.uix.button import Button 
from kivy.clock import Clock 

class Cronometro(App): 
    def build(self): 
        self.tempo = 0 
        self.running = False 
        self.label = Label(text='0', font_size='50sp') 
        self.start_button = Button(text='Iniciar', on_press=self.iniciar) 
        self.stop_button = Button(text='Parar', on_press=self.parar) 
        
        layout = BoxLayout(orientation='vertical') 
        layout.add_widget(self.label) 
        layout.add_widget(self.start_button) 
        layout.add_widget(self.stop_button) 
        return layout
    def iniciar(self, instance): 
        if not self.running: 
            self.running = True 
            Clock.schedule_interval(self.atualizar, 1) 
    def parar(self, instance): 
        if self.running: 
            self.running = False 
            Clock.unschedule(self.atualizar) 
    def atualizar(self, dt): 
        if self.running: 
            self.tempo += 1 
            self.label.text = str(self.tempo) 

if __name__ == "__main__": Cronometro().run()
