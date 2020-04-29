import sys
import sqlite3
from PyQt5.QtWidgets import *
from PyQt5.QtGui import * 

conn = sqlite3.connect("data.db")
c = conn.cursor()
c.execute("""CREATE TABLE IF NOT EXISTS info(sname, fname, mname, bday, username, email, password)""")

class Home(QMainWindow):
    def __init__(self):
        super(Home, self).__init__()
        self.setWindowTitle('WIND')
        self.setFixedSize(600, 460)
        self.wind()
        self.buttons()
        self.show()

    def wind(self):
        text1 = QLabel("W. I. N. D.", self)
        text1.move(260, 150)    

        text2 = QLabel("WEATHER - INFORMATION - NETWORK - DATABASE", self)
        text2.resize(1000, 10)
        text2.move(150, 200)

    def buttons(self):
        # login button
        login = QPushButton("Login", self)
        login.move(240, 240)
        login.clicked.connect(self.log)

        # signup button
        signup = QPushButton("Signup", self)
        signup.move(240, 300)
        signup.clicked.connect(self.sign)

    def log(self):
        # connects to where you can choose between admin or user
        self.choice = Choice()
        win = Choice()
        self.close()

    def sign(self):
        # connects to signup page
        self.signup = Signup()
        win = Signup()
        self.close()

class Choice(QMainWindow):
    def __init__(self):
        super(Choice, self).__init__()
        self.setWindowTitle('WIND')
        self.setFixedSize(600, 460)
        self.wind()
        self.buttons()
        self.show()

    def wind(self):
        text1 = QLabel("W. I. N. D.", self)
        text1.move(260, 150)    

        text2 = QLabel("WEATHER - INFORMATION - NETWORK - DATABASE", self)
        text2.resize(1000, 10)
        text2.move(150, 200)

    def buttons(self):
        # user button
        user = QPushButton("User", self)
        user.move(240, 240)
        user.clicked.connect(self.user)

        #admin button
        admin = QPushButton("Admin", self)
        admin.move(240, 300)
        admin.clicked.connect(self.admin)

 
    def user(self):
        # connects to user
        self.u = userLog()
        win = userLog()
        self.close()

    def admin(self):
        # connects to admin
        self.signup = adminLog()
        win = adminLog()
        self.close()

class Signup(QMainWindow):
    def __init__(self):
        super(Signup, self).__init__()
        self.setWindowTitle('Signup')
        self.setFixedSize(600, 460)
        self.wind()
        self.textbox()
        self.signupButton()
        self.show()

    def wind(self):
        wind = QLabel("W. I. N. D.", self)
        wind.move(15, 20)    

        name = QLabel("Name: ", self)
        name.move(15, 60)    

        bday = QLabel("Birthday: ", self)
        bday.move(15, 120)    

        un = QLabel("Username: ", self)
        un.move(15, 180)    
        
        email = QLabel("Email: ", self)
        email.move(15, 240)    

        pw = QLabel("Password: ", self)
        pw.move(15, 300)    

        pw2 = QLabel("Retype Password: ", self)
        pw2.move(15, 360)    


    def textbox(self):
        # name
        self.sname = QLineEdit(self)
        self.sname.move(140, 60)
        self.sname.resize(100, 40)
        self.sname.setPlaceholderText("Surname")

        self.fname = QLineEdit(self)
        self.fname.move(250, 60)
        self.fname.resize(100, 40)
        self.fname.setPlaceholderText("First Name")

        self.mname = QLineEdit(self)
        self.mname.move(360, 60)
        self.mname.resize(50, 40)
        self.mname.setPlaceholderText("Middle Initial")

        # bday
        self.bday = QLineEdit(self)
        self.bday.move(140, 120)
        self.bday.resize(280, 40)
        self.bday.setPlaceholderText("yyyy/mm/dd")
        
        # username
        self.username = QLineEdit(self)
        self.username.move(140, 180)
        self.username.resize(280, 40)
        self.username.setPlaceholderText("Username")

        # email
        self.email = QLineEdit(self)
        self.email.move(140, 240)
        self.email.resize(280, 40)
        self.email.setPlaceholderText("Email")

        # password box
        self.password = QLineEdit(self)
        self.password.move(140, 300)
        self.password.resize(280, 40)
        self.password.setPlaceholderText("Password")

        # retype
        self.pw = QLineEdit(self)
        self.pw.move(140, 360)
        self.pw.resize(280, 40)
        self.pw.setPlaceholderText("Retype Password")

    def signupButton(self):
        # signup button
        singup = QPushButton('Sign Up', self)
        singup.move(480, 420)
        singup.clicked.connect(self.save)

    def save(self): # add to database
        # makes line edit to string
        sname = self.sname.text()
        fname = self.fname.text()
        mname = self.mname.text()
        bday = self.bday.text()
        email = self.email.text()
        pw = self.pw.text()
        username = self.username.text() 
        password = self.password.text() 

        if sname != '' and fname != '' and mname != '' and bday != '' and email != '' and pw != '' and username != '' and password != '':  # if everything is filled up
            if password == pw: #compare password and retype password
                c.execute("INSERT INTO info VALUES(?, ?, ?, ?, ?, ?, ? )", (sname, fname, mname, bday, username, email, password)) # insert to database
                # pop up that it is already inserted
                QMessageBox.question(self, 'Saved', '\n Name: {}, {} {} \n Birthday: {} \n Username: {} \n Password:{} \n Email: {}'
                .format(sname, fname, mname, bday, username, email, password), QMessageBox.Ok)
                conn.commit()
                #back to home 
                self.home = Home()
                win = Home()
                self.close()
            else: # password and retype password not the same
                QMessageBox.question(self, 'Error', "Password is not the same", QMessageBox.Ok)
                self.home = Home()
                win = Home()
                self.close()

        else:  # sends error if a box is empty
            QMessageBox.question(self, 'Error', "Incomplete info", QMessageBox.Ok)
            self.home = Home()
            win = Home()
            self.close()

class adminLog(QMainWindow):
    def __init__(self):
        super(adminLog, self).__init__()
        self.setWindowTitle('Admin')
        self.setFixedSize(600, 460)
        self.wind()
        self.info()
        self.buttons()
        self.show()

    def wind(self):
        text1 = QLabel("W. I. N. D.", self)
        text1.move(260, 100)    

        text2 = QLabel("WEATHER - INFORMATION - NETWORK - DATABASE", self)
        text2.resize(1000, 10)
        text2.move(150, 160)

    def info(self):
        self.username = QLineEdit(self)
        self.username.move(160, 200)
        self.username.resize(280, 40)
        self.username.setPlaceholderText("Username")

        self.password = QLineEdit(self)
        self.password.move(160, 260)
        self.password.resize(280, 40)
        self.password.setPlaceholderText("Password")

    def buttons(self):
        # check if input is valid
        login = QPushButton("Login", self)
        login.move(160, 320)
        login.clicked.connect(self.login)

        back = QPushButton("Back", self)
        back.move(340, 320)
        back.clicked.connect(self.back)

    def back(self):
        self.home = Home()
        win = Home()
        self.close()   

    def login(self):
        un = self.username.text()
        pw = self.password.text()

        if un == "admin" and pw == "admin": # if valid
            self.a = admin()
            win = admin()
            self.close()
        else:   # not valid
            win = Home()
            self.close()   

class userLog(QMainWindow):
    def __init__(self):
        super(userLog, self).__init__()
        self.setWindowTitle('User')
        self.setFixedSize(600, 460)
        self.wind()
        self.info()
        self.buttons()
        self.show()

    def wind(self):
        text1 = QLabel("W. I. N. D.", self)
        text1.move(260, 100)    

        text2 = QLabel("WEATHER - INFORMATION - NETWORK - DATABASE", self)
        text2.resize(1000, 10)
        text2.move(150, 160)

    def info(self):
        self.username = QLineEdit(self)
        self.username.move(160, 200)
        self.username.resize(280, 40)
        self.username.setPlaceholderText("Username")

        self.password = QLineEdit(self)
        self.password.move(160, 260)
        self.password.resize(280, 40)
        self.password.setPlaceholderText("Password")

    def buttons(self):
        login = QPushButton("Login", self)
        login.move(160, 320)
        login.clicked.connect(self.login)

        back = QPushButton("Back", self)
        back.move(340, 320)
        back.clicked.connect(self.back)

    def back(self):
        self.home = Home()
        win = Home()
        self.close()   

    def login(self):
        un = self.username.text()
        pw = self.password.text()

        if un == '' or pw == '':  # if a box is empty
            QMessageBox.question(self, 'Error', "One box is empty", QMessageBox.Ok)

        elif un != '' or pw != '': # both boxes are filled
            c.execute("SELECT * FROM info WHERE username =? AND password =?",(un,pw)) # search in database
            result = c.fetchone()
            if result == None: # if found
                QMessageBox.question(self, 'Search Results', "No Record", QMessageBox.Ok)
                self.home = Home()
                win = Home()
                self.close()  

            else: # not found
                QMessageBox.question(self, 'Search Results', "Record Found", QMessageBox.Ok)
                self.close()
                self.found = user()
                win = user()
                self.close()
          
class admin(QMainWindow):
    def __init__(self):
        super(admin, self).__init__()
        self.setWindowTitle('Admin')
        self.setFixedSize(600, 460)
        self.buttons()
        self.show()

    def buttons(self):
        openDB = QPushButton("Open Database", self)
        openDB.move(50, 150)
        openDB.resize(150, 30)
        #openDB.clicked.connect()

        updateDB = QPushButton("Update Database", self)
        updateDB.move(50, 200)
        updateDB.resize(150, 30)
        #updateDB.clicked.connect()

        signout = QPushButton("Signout", self)
        signout.move(400, 400)
        #signout.clicked.connect()

class user(QMainWindow):
    def __init__(self):
        super(user, self).__init__()
        self.setWindowTitle('User')
        self.setFixedSize(600, 460)
        self.wind()
        self.buttons()
        self.show()

    def wind(self):
        text1 = QLabel("W. I. N. D.", self)
        text1.move(260, 70)    

        text2 = QLabel("WEATHER - INFORMATION - NETWORK - DATABASE", self)
        text2.resize(1000, 10)
        text2.move(150, 130)
    
    def buttons(self):
        today = QPushButton("TODAY", self)
        today.move(150, 170)
        today.clicked.connect(self.today)

        five = QPushButton("5 DAYS", self)
        five.move(150, 220)
        #five.clicked.connect()
        
        seven = QPushButton("7 DAYS", self)
        seven.move(350, 170)
        #seven.clicked.connect()

        back = QPushButton("Signout", self)
        back.move(350, 220)
        back.clicked.connect(self.back)

    def back(self):
        self.home = Home()
        win = Home()
        self.close()   

    def today(self):
        self.today = Today()
        win = Today()
        self.close() 

    def five(self):
        self.five = Five()
        win = Today()
        self.close() 

    def seven(self):
        self.seven = Seven()
        win = Today()
        self.close() 

class Today(QMainWindow):
    def __init__(self):
        super(Today, self).__init__()
        self.setWindowTitle('Today')
        self.setFixedSize(600, 460)
        self.wind()
        self.button()
        self.show()

    def wind(self):
        wind = QLabel("W. I. N. D.", self)
        wind.move(15, 20)    

        date = QLabel("DATE: {}".format("1"), self)
        date.move(15, 60) 
        date.resize(1000, 10)
   

        temp = QLabel("TEMPERATURE: {}".format("1"), self)
        temp.move(15, 100)    
        temp.resize(1000, 10)

        fl = QLabel("FEELS LIKE: {}".format("1"), self)
        fl.move(15, 140)    
        fl.resize(1000, 10)
        
        pres = QLabel("PRESSURE: {}".format("1"), self)
        pres.move(15, 180)    
        pres.resize(1000, 10)
        
        hum = QLabel("HUMIDITY: {}".format("1"), self)
        hum.move(15, 220)    
        hum.resize(1000, 10)

        speed = QLabel("WIND SPEED: {}".format("1"), self)
        speed.move(15, 260)   
        speed.resize(1000, 10)

        direct = QLabel("WIND DIRECTION: {}".format("1"), self)
        direct.move(15, 300)   
        direct.resize(1000, 10)

    def button(self):
        back = QPushButton("Back", self)
        back.move(450, 20)
        back.clicked.connect(self.back)

    def back(self):
        self.home = Home()
        win = Home()
        self.close() 

class Five(QMainWindow):
    def __init__(self):
        super(Five, self).__init__()
        self.setWindowTitle('Today')
        self.setFixedSize(600, 460)
        self.wind()
        self.button()
        self.show()

    def wind(self):
        wind = QLabel("W. I. N. D.", self)
        wind.move(15, 20)    

        date = QLabel("DATE: {}".format("1"), self)
        date.move(15, 60) 
        date.resize(1000, 10)
   

        temp = QLabel("TEMPERATURE: {}".format("1"), self)
        temp.move(15, 100)    
        temp.resize(1000, 10)

        fl = QLabel("FEELS LIKE: {}".format("1"), self)
        fl.move(15, 140)    
        fl.resize(1000, 10)
        
        pres = QLabel("PRESSURE: {}".format("1"), self)
        pres.move(15, 180)    
        pres.resize(1000, 10)
        
        hum = QLabel("HUMIDITY: {}".format("1"), self)
        hum.move(15, 220)    
        hum.resize(1000, 10)

        speed = QLabel("WIND SPEED: {}".format("1"), self)
        speed.move(15, 260)   
        speed.resize(1000, 10)

        direct = QLabel("WIND DIRECTION: {}".format("1"), self)
        direct.move(15, 300)   
        direct.resize(1000, 10)

    def button(self):
        back = QPushButton("Back", self)
        back.move(450, 20)
        back.clicked.connect(self.back)

    def back(self):
        self.home = Home()
        win = Home()
        self.close() 
        
class Seven(QMainWindow):
    def __init__(self):
        super(Seven, self).__init__()
        self.setWindowTitle('Today')
        self.setFixedSize(600, 460)
        self.wind()
        self.button()
        self.show()

    def wind(self):
        wind = QLabel("W. I. N. D.", self)
        wind.move(15, 20)    

        date = QLabel("DATE: {}".format("1"), self)
        date.move(15, 60) 
        date.resize(1000, 10)
   

        temp = QLabel("TEMPERATURE: {}".format("1"), self)
        temp.move(15, 100)    
        temp.resize(1000, 10)

        fl = QLabel("FEELS LIKE: {}".format("1"), self)
        fl.move(15, 140)    
        fl.resize(1000, 10)
        
        pres = QLabel("PRESSURE: {}".format("1"), self)
        pres.move(15, 180)    
        pres.resize(1000, 10)
        
        hum = QLabel("HUMIDITY: {}".format("1"), self)
        hum.move(15, 220)    
        hum.resize(1000, 10)

        speed = QLabel("WIND SPEED: {}".format("1"), self)
        speed.move(15, 260)   
        speed.resize(1000, 10)

        direct = QLabel("WIND DIRECTION: {}".format("1"), self)
        direct.move(15, 300)   
        direct.resize(1000, 10)

    def button(self):
        back = QPushButton("Back", self)
        back.move(450, 20)
        back.clicked.connect(self.back)

    def back(self):
        self.home = Home()
        win = Home()
        self.close() 

if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = Home()
    sys.exit(app.exec_())
    conn.close()