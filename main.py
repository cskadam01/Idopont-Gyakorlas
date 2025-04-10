from models import User, engine
from sqlalchemy.orm import sessionmaker
import tkinter as tk





Session = sessionmaker(bind=engine)

session = Session()
felhasz1 = User(name="Kakas", age=20, password = "123456" )
#session.add_all([user1, user2]) Ezt ha több sort akarunk hozzá adni a táblázathoz
# session.add(felhasz1)
 
session.commit()


def changeToRegister():
   RegisterPage.config(width=1000, height=1000)
   LoginPage.config(width=0, height=0)


def changeToLogin():
    RegisterPage.config(width=0, height=0)
    LoginPage.config(width=1000, height=1000)

def HandleRegister():

        
    
        username = regName.get()
        passInput = regPass.get()
        passConf = regPassConf.get()

        if username == "" or passInput == "" or passConf == "":
            print("Van leglább egy kitöltetlen mező, kérlek pótold!")
            return


        existing_user = session.query(User).filter_by(name=username).first()
        if existing_user:
            print("Ez a felhasználónév már foglalt!")
            return

        if passInput == passConf:
            try:
                user = User(name = username, age = 0, password = passInput)
                session.add(user)
                session.commit()
                RegisterPage.config(height=0, width=0)
            except:
                print("Hiba lépett fel az adatbázissal való kapcsolat során")
        else:
            print("A jelszavak nem egyeznek, próbáld újra")      
    



def HandleLogin():
    try:
        names = []
        users = session.query(User).all()
        for user in users:
            names.append(user.name)

        username = logName.get()

        # Ellenőrizzük, hogy létezik-e a név
        if username in names:
        # Ha igen, megkeressük a felhasználót a teljes listában
            for user in users:
                if user.name == username:
                    actual_password = user.password
                    break

        # A beírt jelszó
            entered_password = logPass.get()

        # Ellenőrizzük a jelszót
            if entered_password == actual_password:
                print("Sikeres belépés!")
                LoginPage.config(height=0, width=0)
            else:
                print("Hibás jelszó!")
        else:
            print("Nincs ilyen felhasználó!")

            
    except:
        pass





window = tk.Tk()
window.geometry('1000x1000')

LoginPage = tk.Canvas(window, height=1000, width=1000, borderwidth=0, highlightthickness=0, background="grey")
LoginPage.place(x=0, y=0)

loginCanva = tk.Canvas(LoginPage, height= 400, width= 300, borderwidth=0, highlightthickness=0, background="#352dcf")
loginCanva.place(x=350, y=300)

loginTitle = tk.Label(loginCanva, text="Bejelentkezés", background='#352dcf', font=('Glock 11') )
loginTitle.place(x=106, y=10)

logName = tk.Entry(loginCanva,)
logName.place(x= 25, y=100,width=250, height=40)

logPass = tk.Entry(loginCanva)
logPass.place(x= 25, y=150, width=250, height=40)

logButton = tk.Button(loginCanva, command=HandleLogin)
logButton.place(x=50, y=200,width=200, height=40, )



toRegLable = tk.Label(loginCanva, text="Nincs még fiókod? Hozz létre egyet!")
toRegLable.place(x=50, y=350,)

toRegButton = tk.Button(loginCanva, command=changeToRegister, text="Belépéshez")
toRegButton.place(x=100, y=375,width=100, height=20)






RegisterPage = tk.Canvas(window, height=0, width=0, borderwidth=0, highlightthickness=0, background="grey", )
RegisterPage.place(x=0, y=0)



RegisterCanva = tk.Canvas(RegisterPage, height= 400, width= 300, borderwidth=0, highlightthickness=0, background="#352dcf")
RegisterCanva.place(x=350, y=300)


RegisterTitle = tk.Label(RegisterCanva, text="Regisztráció", background='#352dcf', font=('Glock 11') )
RegisterTitle.place(x=106, y=10)

regName = tk.Entry(RegisterCanva,)
regName.place(x= 25, y=100,width=250, height=40)

regPass = tk.Entry(RegisterCanva)
regPass.place(x= 25, y=150, width=250, height=40)

regPassConf = tk.Entry(RegisterCanva)
regPassConf.place(x= 25, y=200, width=250, height=40)

regButton = tk.Button(RegisterCanva, command=HandleRegister)
regButton.place(x=50, y=250,width=200, height=40)

toLogLable = tk.Label(RegisterCanva, text="Már van Felhasználód? Jelentkezz be!")
toLogLable.place(x=50, y=350,)

toLogButton = tk.Button(RegisterCanva, command=changeToLogin, text="Regisztrációhoz")
toLogButton.place(x=100, y=375,width=100, height=20)








window.mainloop()