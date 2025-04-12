from models import User, Exercise, engine
from sqlalchemy.orm import sessionmaker
import tkinter as tk



current_user = None




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
    global current_user  # globális változó, hogy mindenhol elérjük a bejelentkezett felhasználót

    try:
        # Beolvasott értékek a Tkinter mezőkből
        username_input = logName.get()
        entered_password = logPass.get()

        # Lekérdezzük az adatbázisból a felhasználót név alapján
        user = session.query(User).filter_by(name=username_input).first()

        # Ellenőrzés: létezik-e a felhasználó
        if user:
            # Jelszó egyezés ellenőrzés
            if user.password == entered_password:
                print("Sikeres belépés!")
                current_user = user  # Beállítjuk a globális felhasználó változót
                LoginPage.config(height=0, width=0)
                excercisePage.config(height=1000, width=1000)
            else:
                print("Hibás jelszó!")
        else:
            print("Nincs ilyen felhasználó!")

    except Exception as e:
        print("Hiba történt a bejelentkezés során:", e)




def addExcercise():
    excercise_type =selected_option.get()
    excercise_name = excerciseName.get()
    excercise_descriotion = excerciseDescriotion.get()

    if not excercise_name:
        print("Nem adtál meg feladat nevet, kérlek Pótold")
    
    try:
        newExcercise = Exercise(name=excercise_name, description = excercise_descriotion, etype=excercise_type, created_by= current_user.id)
        session.add(newExcercise)
        session.commit()
        print("feladat hozzáadva")
    except Exception as e:
        print("Hiba lépett fel:", e)
        



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






excercisePage = tk.Canvas(window, height=0, width=0, background='red', highlightthickness=0, borderwidth=0)
excercisePage.place(x=0, y=0)

#Feldat hozzaadasa

excerciseName = tk.Entry(excercisePage)
excerciseName.place(x=100, y=100)

excerciseDescriotion = tk.Entry(excercisePage)
excerciseDescriotion.place(x= 300, y=100)

excerciseSubmit = tk.Button(excercisePage, height=2, width=10, text="Hozzáadás", command= addExcercise)
excerciseSubmit.place(x=500, y=100)


types= ["Mell", "Hát", "Láb", "Bicepsz", "Tricepsz", "Váll", "Alkar"]
selected_option = tk.StringVar()
selected_option.set(types[0])
excerciseType = tk.OptionMenu(excercisePage, selected_option, *types)
excerciseType.place(x=0, y=100)





window.mainloop()