from kivy.app import App
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.popup import Popup
from kivy.uix.button import Button
from kivy.graphics import Color, RoundedRectangle
from kivy.uix.image import Image
from kivy.animation import Animation
from kivy.clock import Clock

class PurpleWindow(RelativeLayout):
    def __init__(self, **kwargs):
        super(PurpleWindow, self).__init__(**kwargs)

        self.image = Image(source="C:/Users/sawhn/OneDrive/Desktop/51727.jpg", allow_stretch=True,
                           size_hint=(None, None), size=(1920,1080))
        self.add_widget(self.image)

        self.label = Label(text="Welcome to the Purple Window!", size_hint=(0.8, 0.1),
                           pos_hint={'center_x': 0.5, 'center_y': 0.9})
        self.add_widget(self.label)

        self.login_button = Button(text="Login", size_hint=(0.1, 0.05), pos_hint={'center_x': 0.515, 'center_y': 0.1})
        self.login_button.bind(on_press=self.open_login_screen)
        self.add_widget(self.login_button)

    def open_login_screen(self, instance):
        login_popup = Popup(title='', size_hint=(None, None), size=(400, 200), auto_dismiss=False,
                            title_color=[0, 0, 0, 0], separator_color=[0, 0, 0, 0], border=(0, 0, 0, 0))

        login_layout = RelativeLayout()
        with login_layout.canvas.before:
            Color(0.4, 0.6, 0.9, 0.8)  # Set the background color with transparency
            #RoundedRectangle(pos=login_layout.pos, size=login_layout.size, radius=[20,])

        username_label = Label(text='Username:', size_hint=(0.2, 0.1), pos_hint={'center_x': 0.1, 'center_y': 0.7})
        login_layout.add_widget(username_label)

        self.username_input = TextInput(multiline=False, size_hint=(0.6, 0.2), pos_hint={'center_x': 0.57, 'center_y': 0.7})
        login_layout.add_widget(self.username_input)
      
        save_button = Button(text='Save', size_hint=(0.3, 0.15), pos_hint={'center_x': 0.5, 'center_y': 0.4})
        save_button.bind(on_press=self.save_username)
        login_layout.add_widget(save_button)

        login_popup.background_color = (0, 0, 0, 0)  # Set the popup background color to transparent
        login_popup.content = login_layout


           # Animation to rise from the bottom
        login_layout.opacity = 0  # Start with opacity 0
        login_layout.y = -100  # Start slightly above the screen
        animation = Animation(opacity=1, y=0, duration=1)
        animation.start(login_layout)

        # Animation to rise the whole login screen to the middle
        login_popup.opacity = 0  # Start with opacity 0
        login_popup.y = -100  # Start slightly above the screen
        animation = Animation(opacity=1, y=0.7, duration=1)
        animation.start(login_popup)

        login_popup.open()

        
        
     
    def save_username(self, instance):
        username = self.username_input.text.strip()
        #load all usernames into a list called lines
        with open("names.txt", 'r') as file:
            lines = file.readlines()
            lines = [line.rstrip('\n') for line in lines]
        numofppl=len(lines)
        if username.lower() in lines:
            popup = Popup(title='Woopsie', content=Label(text='Big snoopy says : homie username already Exists!'), size_hint=(None, None),
                          size=(500, 100))
            popup.open()

    
        elif username.lower() == "snoopy":
            
            self.teaser = Image(source="C:/Users/sawhn/OneDrive/Desktop/51714.jpg", allow_stretch=True,
                           size_hint=(None, None), size=(1920, 1080))
            self.add_widget(self.teaser)
            popup = Popup(title='The book of Snoopy :)', content=Label(text="Who is in the book of snoopie you may as, well its: \n"+'\n'.join(lines)), size_hint=(None, None),
                          size=(500, (75*numofppl)))
            popup.open()
            

        elif username:
            try:
                with open('names.txt', 'a') as file:
                    file.write(username + '\n')
                self.username_input.text = ''
                popup = Popup(title='WOIII', content=Label(text='You are in the book of Snoopy!'), size_hint=(None, None),
                              size=(300, 100))
                popup.open()
            except Exception as e:
                popup = Popup(title='Error', content=Label(text=str(e)), size_hint=(None, None), size=(400, 200))
                popup.open()
        else:
            popup = Popup(title='Error', content=Label(text='Please enter a username.'), size_hint=(None, None),
                          size=(200, 100))
            popup.open()


class MyApp(App):
    def build(self):
        return PurpleWindow()


if __name__ == '__main__':
    MyApp().run()
