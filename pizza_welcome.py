from tkinter import *
from tkinter import messagebox as ms
from PIL import Image, ImageTk
import time
import sqlite3
import pizza_made


#creating database if there is not database
with sqlite3.connect('pizza.db') as db:
    c = db.cursor()
c.execute('CREATE TABLE IF NOT EXISTS users (username TEXT NOT NULL ,password TEXT NOT NULL);')
c.execute('CREATE TABLE IF NOT EXISTS user_orders (username TEXT NOT NULL, pizza_id  TEXT NOT NULL,price INT);')
db.commit()
db.close()

class main:
    def __init__(self,window):
        #window screen
        self.window = window
        self.window.title("PIZZA MIZZA")
        self.window.geometry("800x800")
        self.window.configure(bg="yellow")

        self.username = StringVar()
        self.password = StringVar()
        self.n_username = StringVar()
        self.n_password = StringVar()

        self.widgets()
    #Signin function
    def signin(self):
        with sqlite3.connect('pizza.db') as db:
            c = db.cursor()

        find_user = ('SELECT * FROM users WHERE username = ? and password = ?')
        c.execute(find_user,[(self.username.get()),(self.password.get())])
        result = c.fetchall()
        #username and password for Admin
        if self.username.get()=="Admin" and self.password.get()=="admin":
            self.sin.pack_forget()
            self.admin_b_seeorders.place(x=150,y=300)
            self.admin_b_income.place(x=150,y=200)

        elif result:
            self.sin.pack_forget()
            self.label_main.place(x=25,y=140)
            self.label2_main.place(x=25,y=370)
            self.pizza1.place(x=210,y=310)
            self.pizza2.place(x=223,y=540)
            self.l1.place(x=452,y=140)
            self.button1.place(x=490,y=200)
            self.button2.place(x=490,y=260)
            self.label_extention.place(x=450,y=385)
            self.b_mozzarella.place(x=430,y=440)
            self.b_tomato_sauce.place(x=560,y=440)
            self.b_mushroom.place(x=430,y=495)
            self.b_pineapple.place(x=560,y=495)
            self.b_order.place(x=350,y=620)
            self.b_prev.place(x=300,y=680)

        else:
            ms.showerror('Not found','Username Not Found!')

    #to check admin's income
    def admin_income(self):
        with sqlite3.connect('pizza.db') as db:
            c=db.cursor()
        result = [x[0] for x in c.execute("SELECT price FROM user_orders")]
        count=0
        for i in result:
            count+=i
        string="Revenue is "+str(count)+" dollars"
        self.admin_l1=Label(self.window,text=string,bg='purple2',fg='gold',font=("arial",22))
        self.admin_l1.place(x=440,y=210)

    #to check all orders
    def admin_orders(self):
        with sqlite3.connect('pizza.db') as db:
            c=db.cursor()
        result1=[x[0] for x in c.execute('SELECT username FROM user_orders')]
        result2=[x[0] for x in c.execute('SELECT pizza_id FROM user_orders')]

        for i in range(len(result1)):
            print(result1[i],result2[i])

    #pizza made function
    def create_pizza(self,a):
        if a=="Funghi":
            self.pizza=pizza_made.PizzaBuilder(a)
        elif a=="Hawaii":
            self.pizza=pizza_made.PizzaBuilder(a)

    #add extensions to the pizza
    def add_remove(self,pizza_type,extention,z):
        if z=="add":
            self.pizza.add_extention(extention)
        elif z=="remove":
            self.pizza.remove_extention(extention)

    #check order's total price
    def order_price(self,pizza):
        with sqlite3.connect('pizza.db') as db:
            c=db.cursor()
        insert='INSERT INTO user_orders(username,pizza_id,price) VALUES(?,?,?)'
        c.execute(insert,[(self.username.get()),(self.pizza.get_status()),(self.pizza.get_price())])
        db.commit()
        ms.showinfo('Price','Your order {} is {} dollars'.format(self.pizza.get_status(),self.pizza.get_price()))

    #check previous orders' list
    def previous_order(self):
        with sqlite3.connect('pizza.db') as db:
            c=db.cursor()
        find_user=('SELECT * FROM user_orders WHERE username=?')
        c.execute(find_user,[(self.username.get())])
        result=c.fetchall()
        print("Username is",result[0][0])
        for i in result:
            print("Order:",i[1],end="|")
            print("Price:",i[2],"dollar")

    #register function
    def register_user(self):
        user_data = username.get()
        pw_data = password.get()
        pw2_data = password2.get()

        register_parameters=(user_data,pw_data)
        with sqlite3.connect('pizza.db') as db:
            c = db.cursor()
        c.execute("SELECT username FROM users WHERE username=?",(user_data,))
        result=c.fetchall()
        if user_data=="":
            ms.showerror("Error","Enter username!")
        elif len(result)>0:
          ms.showerror("Username already taken!","Try another username!")
        else:
          if pw_data!=pw2_data:
            ms.showerror("Error","Passwords don't match!")
            password3.delete(0, END)
            password4.delete(0, END)
          elif pw_data==pw_data:
              c.execute("INSERT INTO users VALUES ( ?, ? )", register_parameters)
              db.commit()
              username1.delete(0, END)
              password3.delete(0, END)
              password4.delete(0, END)
              Label(rwindow, text = "Successfully registered!",bg ='light cyan', fg = "purple2" ,font = ("calibri", 10, 'bold')).pack()

    #creating account 
    def signup(self):
        global rwindow
        rwindow=Toplevel(self.window)
        rwindow.title("Registery page")
        rwindow.geometry("365x315")

        global username
        global password
        global password2
        global username1
        global password3
        global password4
        username = StringVar()
        password = StringVar()
        password2 = StringVar()
        rwindow.configure(bg="purple1")
        Label(rwindow, text = "Please enter details:",bg='purple1',fg='yellow', font=("Times",14,"bold")).pack()
        Label(rwindow, text = "",bg='purple1').pack()
        #username/password1/password2
        Label(rwindow, text = "Username:",bg='purple1',fg='yellow').pack()
        username1 = Entry(rwindow, textvariable = username)
        username1.pack()
        Label(rwindow, text = "Password:",bg='purple1',fg='yellow').pack()
        password3 =  Entry(rwindow, textvariable = password)
        password3.pack()
        Label(rwindow, text = "Again password:",bg='purple1',fg='yellow').pack()
        password4 =  Entry(rwindow, textvariable = password2)
        password4.pack()
        Label(rwindow, text = "",bg='purple1').pack()
        Button(rwindow, text = "Register",bg='yellow',fg='purple1', width = 15, height = 1, command = self.register_user).pack()

    #widgets interface
    def widgets(self):
        Label(self.window,text = 'Welcome Pizza Mizza!',bg = "purple", fg= "gold", width = "600", height = "3", font = ("MS San Serif", 25, 'bold')).pack()
        self.sin = Frame(self.window,bg='yellow')
        self.sin.pack()
        Label(self.sin ,text = '', bg="yellow").pack()
        Label(self.sin , text = "Username: ",bg='yellow', fg="dark violet",font=('Times',22),width=40,height=2).pack()
        Entry(self.sin ,width='44', textvariable = self.username).pack()
        Label(self.sin , text = "Password: ",bg='yellow',  fg="dark violet",font=('Times',22),width=40,height=2).pack()
        Entry(self.sin ,width='44', textvariable = self.password).pack()
        Label(self.sin ,text = '', bg="yellow").pack()
        Label(self.sin ,text = '', bg="yellow").pack()
        Button(self.sin ,text = ' Signin ',width = 20, bg="purple",fg= "gold",  font = ('"MS Serif',15,), height = 1, command=self.signin).pack()
        Label(self.sin ,text = '', bg="yellow").pack()
        Button(self.sin ,text = ' Signup ',width = 20, bg="purple",fg= "gold", font = ('"MS Serif',15), height = 1, command=self.signup).pack()
        Label(self.sin ,text = '', bg="yellow").pack()
        Label(self.sin ,text = '', bg="yellow").pack()
        Label(self.sin ,text = '', bg="yellow").pack()
        Label(self.sin ,text = '', bg="yellow").pack()
        Label(self.sin ,text = '', bg="yellow").pack()
        Label(self.sin ,text = '', bg="yellow").pack()
        

        self.label_main=Label(self.window)
        self.label_main.img=ImageTk.PhotoImage(file="pizza-funghi.png")
        self.label_main.config(image=self.label_main.img)
        self.label_main.pack_forget()
        

        self.label2_main=Label(self.window)
        self.label2_main.img=ImageTk.PhotoImage(file="Hawaii_pizza.jpg")
        self.label2_main.config(image=self.label2_main.img)
        self.label2_main.pack_forget()

        self.pizza1=Label(self.window,text="Funghi",padx= '30',font=("arial",17,'bold'),bg="deep pink", fg='dark blue')
        self.pizza1.pack_forget()
        self.pizza2=Label(self.window,text="Hawaii",padx= '30',font=("arial",17,'bold'),bg="deep pink", fg='dark blue')
        self.pizza2.pack_forget()
        self.l1=Label(self.window,text="Choose pizza:",padx= '36',font=("Times",20),bg="dark orange")
        self.l1.pack_forget()
        
        

        self.v=IntVar()
        self.button1=Radiobutton(self.window,variable=self.v,value=1,text="FUNGHI",bg='purple2', fg='gold', padx ='25',font=('',15),command=lambda:self.create_pizza("Funghi"))
        self.button2=Radiobutton(self.window,variable=self.v,value=2,text="HAWAII", bg='purple2', fg='gold',padx ='25',font=('',15),command=lambda:self.create_pizza("Hawaii"))
        self.button1.pack_forget()
        self.button2.pack_forget()
        self.label_extention=Label(self.window,text="Additional ingridients:",padx=20, pady= 5,bg='purple4',fg='deep pink',font=("arial",15))
        self.label_extention.pack_forget()
        self.b_mozzarella=Button(self.window,text="Mozzarella",bg='lemon chiffon', fg='midnight blue',bd=3,relief=SUNKEN,font=('',15),command=lambda:self.add_remove(self.pizza,"Mozzarella","add"))
        self.b_mozzarella.pack_forget()
        self.b_tomato_sauce=Button(self.window,text="Tomato Sauce",bg='red2', fg='white',bd=3,relief=SUNKEN,font=('',15),command=lambda:self.add_remove(self.pizza,"Tomato_Sauce","add"))
        self.b_tomato_sauce.pack_forget()
        self.b_mushroom=Button(self.window,text="Mushroom",bg='khaki',fg='saddle brown',bd=3,relief=SUNKEN,font=('',15),command=lambda:self.add_remove(self.pizza,"Mushroom","add"))
        self.b_mushroom.pack_forget()
        self.b_pineapple=Button(self.window,text="Pineapple",bg='goldenrod1',fg='dark green',bd=3,relief=SUNKEN, font=('',15),command=lambda:self.add_remove(self.pizza,"Pineapple","add"))
        self.b_pineapple.pack_forget()
        self.b_order=Button(self.window,text="ORDER",bg='navy' ,fg='red',bd=3,font=('',15),command=lambda:self.order_price(self.pizza))
        self.b_order.pack_forget()
        self.b_prev=Button(self.window,text="Previous Orders",bg='dark green',fg='orange',bd=3,font=('',15),command=lambda:self.previous_order())
        self.b_prev.pack_forget()

        self.admin_b_seeorders=Button(self.window,text="Check total orders",bd=3,font=('arial',20),bg="orange red",command=lambda:self.admin_orders())
        self.admin_b_seeorders.pack_forget()
        self.admin_b_income=Button(self.window,text="Check total income",bd=3,font=('arial',20),bg="green4",command=lambda:self.admin_income())
        self.admin_b_income.pack_forget()

root = Tk()
root.geometry("1000x1000")

main(root)
root.mainloop()
