from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager,Screen
import json
import glob
import random
from kivy.uix.image import Image
from kivy.uix.behaviors import ButtonBehavior
from hoverable import HoverBehavior
from pathlib import Path
from datetime import datetime

#builder is used to combine the .py and the .kv file together into a single app
# the uix.screenmanger is for the frontend design 
Builder.load_file('design.kv')

# every rule inside the .kv file HAS to be defined as a class in the .py file and inhereit whatever type of rule it is <> is a 'rule'

class LoginScreen(Screen):
    def sign_up(self):
        self.manager.transition.direction = "left"
        self.manager.current = "sign_up_screen"
    # this is setting the screen manager (what loads our pages) to a new current screen - the screen we want to move to 
    def login(self, uname,pword):
        with open("wellbeing app with Kivy/users.json") as file:
            users = json.load(file)
        if uname in users and users[uname]['password'] == pword:
# this is if checking that the username passed in the fucntion (uname) is in the json list and if the [uname] <- dictonary key[password]<- dictonary pair of key value is the same as the password (pword) that was passed in the funtion           
            self.manager.current = "log_in_screen_success"
        else:
            self.ids.login_wrong.text = "wrong username or password"
# this else statement is accessing the id from the kivy file for the label called login_wrong and setting a new value(default balnk) so it will show a new meassage

class RootWidget(ScreenManager):
    pass

class SignUpScreen(Screen):
    def add_user(self,uname,pword):
        with open("wellbeing app with Kivy/users.json") as file:
            users = json.load(file)
        users[uname] = {'username': uname, 'password': pword,
        'created': datetime.now().strftime("%Y-%m-%d %H-%m-%S")}
# the above is createing a new dict to be added to our users.json file to add a new username and password - this is made with the text input the kivy file and added to the 
        with open("wellbeing app with Kivy/users.json", 'w') as file:
            json.dump(users,file)
# the above is opening the json file and saving all the new data to the file as it is in write mode            
        self.manager.current = "sign_up_confirm"

class SignUpScreenConfirm(Screen):
    def menu_main(self):
        self.manager.transition.direction = 'right'
        self.manager.current = "login_screen"

class LoginSuccess(Screen):
    def log_out(self):
        self.manager.transition.direction = "right"
        self.manager.current = "login_screen"

    def get_quote(self, feel):
        feel = feel.lower()
        available_fleeings = glob.glob("wellbeing app with Kivy/quotes/*txt")
        #glob.glob allows the collection of all the filepaths in a directory or folder
        available_fleeings = [Path(filename).stem for filename in available_fleeings]
        #the list comp here gives a new list of all the file names in the folder
# the Path is a build in lib to python - it has many methods to pull out various parts of a filepath, we are using .stem this will remove the suffix and prefix of the path and leave the file name only
        if feel in available_fleeings:
            with open(f"wellbeing app with Kivy/quotes/{feel}.txt",encoding="utf8") as file:
                quotes = file.readlines()
            self.ids.quote.text = random.choice(quotes)
        else:
            self.ids.quote.text = "Only, happy,sad, unloved currently"

class ImageButton(ButtonBehavior,HoverBehavior,Image):
    pass

# one class every Kivy app needs is a "MainApp" that inheriats App we imported above - this needs a build function 
class MainApp(App):
    def build(self):
        return RootWidget()

# the below is a conditional to say if this is the executing file i.e. its name is __main__ , will only have this is being run, not if called from another .py file etc 
if __name__=="__main__":
    MainApp().run()