import json
import tkinter as tk
import os
from tkinter import ttk
from iso3166 import countries

root = tk.Tk()
root.geometry('300x280')
root.title('Profile')
#root.iconbitmap(r'authorization\icon.ico')
#######################################################

path = os.path.dirname(os.path.realpath(__file__)) + "\\"

def show_frame(frame):
    frame.tkraise()

    register_frame_password.delete(0, tk.END)
    register_frame_username.delete(0, tk.END)

    login_frame_password.delete(0, tk.END)
    login_frame_username.delete(0, tk.END)

    message.set('')
    login_frame_password.configure(show = "*")
    register_frame_password.configure(show = "*")
    register_frame_showbutton.deselect()
    
    try:
        with open(path + 'data.json', 'r') as datajson:
            data = json.load(datajson)

    except FileNotFoundError:

        data = {"username_example": {"login": "userlogin","password": "userpassword","age": "userage","country": "usercountry","sex": "None"}}

        with open(path + "data.json", "w") as write_file:
            json.dump(data, write_file, indent=3)

    global choice
    global countrylist

    choice = tk.StringVar()

    countrylist = []

    for c in countries:
        new = c[0]
        countrylist.append(new)    

##################################################################### REGISTRATION

def regsubmit():

    regname = 'user_' + register_frame_username.get().lower()

    if 3 <= len(register_frame_username.get()) <= 12 and 4 <= len(register_frame_password.get()) <= 12:
        with open(path + 'data.json', 'r') as datajson:
            data = json.load(datajson)

        if regname in data:
            message.set('The name is already taken')

        else:
            userlogin = register_frame_username.get()
            userpassword = register_frame_password.get()

            new = {regname: {'login': userlogin, "password": userpassword, "status": 'None', "age": 'None', "country": "None", "sex": "None"}}

            with open(path + 'data.json', 'w', encoding='utf-8') as datajson:
                data.update(new)
                json.dump(data, datajson, indent=3)   
            message.set('Thanks for registering!')

    if len(register_frame_username.get()) < 3:
        message.set('Minimum username length is 3 symbols')
    
    elif len(register_frame_username.get()) > 10:
        message.set('Maximum username length is 10 symbols')

    elif len(register_frame_password.get()) < 4:
        message.set('Minimum password length is 4 symbols')

    elif len(register_frame_password.get()) > 10:
        message.set('Maximum password length is 10 symbols')

##################################################################### LOGIN

def login():
    global logname
    logname = 'user_' + login_frame_username.get().lower()

    if 3 <= len(login_frame_username.get()) <= 10 and 4 <= len(login_frame_password.get()) <= 10:
        with open(path + 'data.json', 'r') as datajson:
            data = json.load(datajson)

        if logname not in data:
            message.set('No such name')
        
        else:
            if login_frame_password.get() == data[logname]['password']:
                show_frame(profile_frame)
                profile_frame_namelab.config(text=data[logname]['login'])
                profile_frame_userage.config(text=data[logname]['age'])
                profile_frame_usercountry.config(text=data[logname]['country'])
                profile_frame_usersex.config(text=data[logname]['sex'])
                profile_frame_userstatus.config(text=data[logname]['status'])
            else:
                message.set('Wrong name or password')
                
    if len(login_frame_username.get()) < 3:
        message.set('Minimum username length is 3 symbols')
    
    elif len(login_frame_username.get()) > 10:
        message.set('Maximum username length is 10 symbols')

    elif len(login_frame_password.get()) < 4:
        message.set('Minimum password length is 4 symbols')

    elif len(login_frame_password.get()) > 10:
        message.set('Maximum password length is 10 symbols')

    ###############=================================================== EDIT DATA ( UI )

def edit(x, y, z, c, what):

    with open(path + 'data.json', 'r') as datajson:
        data = json.load(datajson)

    if what == 'country':
        choice.set(data[logname]['country'])
        countrymenu = ttk.Combobox(profile_frame, textvariable=choice, values=[*countrylist])
        countrymenu.place(relwidth=x, relheight=y, relx=z, rely=c)

    elif what == 'sex':
        clicked.set(data[logname]['sex'])
        menu = tk.OptionMenu(profile_frame, clicked, 'None', 'Male', 'Female')
        menu.place(relwidth=x, relheight=y, relx=z, rely=c)

    elif what == 'age' or 'name' or 'status' or 'pass': 
        new = tk.Entry(profile_frame)
        new.place(relwidth=x, relheight=y, relx=z, rely=c)
        
    profile_frame_newpass = tk.Label(profile_frame, text='Changed')
    ok = tk.Button(profile_frame, text="Ok", command=lambda:clean('pass'))

    submit = tk.Button(profile_frame, text="Ok", command=lambda:change(what))
    submit.place(relwidth=0.10, relheight=0.1, relx=0.80, rely=c)

    close = tk.Button(profile_frame, text="X", command=lambda:clean(what))
    close.place(relwidth=0.10, relheight=0.1, relx=0.90, rely=c)

        #######################======================================= EDIT DATA ( LOGIC )

    def change(what):
        with open(path + 'data.json', 'r') as datajson:
            data = json.load(datajson)

        if what == 'name':
            newname = new.get()
            if 3 <= len(newname) <= 10: 
                names = []
                for i in data:
                    if newname == data[i]['login']:
                        names.append(1)

                if len(names) == 0:
                    with open(path + 'data.json', 'w', encoding='utf-8') as file:
                        data[logname]['login'] = newname
                        json.dump(data, file, indent=3)
                        clean(what)
                        profile_frame_namelab.config(text=newname)
                        profile_message.set('')
                else:
                    profile_message.set('The name is already taken')

            if len(newname) < 3:
                profile_message.set('Minimum username length is 3 symbols')

            elif len(newname) > 10:
                profile_message.set('Maximum username length is 10 symbols')

        elif what == 'age':
            newname = new.get()
            try:
                if 120 >= int(newname) >= 1:  

                    with open(path + 'data.json', 'w', encoding='utf-8') as file:
                        data[logname]['age'] = newname
                        json.dump(data, file, indent=3)
                        clean(what)
                        profile_frame_userage.config(text=newname)
                        profile_message.set('')
                
                if int(newname) > 120:
                    profile_message.set('Age must be less than 120')

                elif int(newname) < 1:
                    profile_message.set('Age must be greater than 0')
    
            except ValueError:
                profile_message.set('Age must be an integer number')

        elif what == 'status':
            newname = new.get()

            if len(newname) < 15:

                with open(path + 'data.json', 'w', encoding='utf-8') as file:
                    data[logname]['status'] = newname
                    json.dump(data, file, indent=3)
                    clean(what)
                    profile_frame_userstatus.config(text=newname)
                    profile_message.set('')

            else:
                profile_message.set('Status must be less than 15 characters')


        elif what == 'sex':
            with open(path + 'data.json', 'w', encoding='utf-8') as file:
                data[logname]['sex'] = clicked.get()
                json.dump(data, file, indent=3)

            profile_frame_usersex.config(text=clicked.get())
            clean(what)

        elif what == 'country':

            values = [*countrylist]
            if choice.get() in values:

                with open(path + 'data.json', 'w', encoding='utf-8') as file:
                    data[logname]['country'] = choice.get()
                    json.dump(data, file, indent=3)

                profile_frame_usercountry.config(text=countrymenu.get())
                clean(what)
            else:
                profile_message.set('No such country')

        elif what == 'pass':
            newname = new.get()

            if 4 <= len(newname) <= 12:  
                
                if newname == data[logname]['password']:
                    profile_message.set('Old and new Password cannot be same') 
                
                else:
                    with open(path + 'data.json', 'w', encoding='utf-8') as file:
                        data[logname]['password'] = newname
                        json.dump(data, file, indent=3)
                        profile_message.set('')
                        new.destroy(); submit.destroy(); close.destroy()

                        profile_frame_newpass.place(relwidth=0.55, relheight=0.1, relx=0.35, rely=0.6)
                        ok.place(relwidth=0.10, relheight=0.1, relx=0.90, rely=0.6)

            elif len(newname) < 4:
                profile_message.set('Password must be greater than 4 characters')            

            else:
                profile_message.set('Password must be less than 12 characters')      


        #######################============================= EDIT DATA ( CLEAN AFTER EDIT )  
        
    def clean(what):
        
        if what == 'sex':
            menu.destroy(); close.destroy(); submit.destroy()

        elif what == 'pass':
            new.destroy(); submit.destroy(); close.destroy(); profile_frame_newpass.destroy(); ok.destroy(); profile_message.set('')

        elif what == 'country':
            countrymenu.destroy(); close.destroy(); submit.destroy(); profile_message.set('')

        elif what == 'age' or 'name':
            new.destroy(); submit.destroy(); close.destroy(); profile_message.set('')

#######################============================= HIDE/SHOW PASSWORD

def showpass():
    if var.get() == 1:
        login_frame_password.configure(show = "")
        register_frame_password.configure(show = "")
    elif var.get() == 0:
        login_frame_password.configure(show = "*")
        register_frame_password.configure(show = "*")

###================================================= FRAME SELECTION / CONST 

root.rowconfigure(0, weight=1)
root.columnconfigure(0, weight=1)

main_frame = tk.Frame(root, bg='#838A8C')
login_frame = tk.Frame(root, bg='#838A8C')
register_frame = tk.Frame(root, bg='#838A8C')
profile_frame = tk.Frame(root, bg='#838A8C')

for frame in (main_frame, login_frame, register_frame, profile_frame):
    frame.grid(row=0, column=0, sticky='nsew')

message = tk.StringVar()
profile_message = tk.StringVar()
clicked = tk.StringVar()
choice = tk.StringVar()
var = tk.IntVar()
#============================== Main window code

main_frame_title = tk.Label(main_frame, text='Main', bg='#1F1F1F', fg='#C9C2C0')

regbutton = tk.Button(main_frame, text='Register', bg='#BDB5B2', command=lambda:show_frame(register_frame))
logbutton = tk.Button(main_frame, text='Log in', bg='#BDB5B2', command=lambda:show_frame(login_frame))

#output

main_frame_title.place(relwidth=1, relheight=0.1, relx=0, rely=0)
regbutton.place(relwidth=0.5, relheight=0.15, relx=0, rely=0.1)
logbutton.place(relwidth=0.5, relheight=0.15, relx=0.5, rely=0.1)

#==============================Log in window code

login_frame_title = tk.Label(login_frame, text='Login', bg='#1F1F1F', fg='#C9C2C0')
login_frame_btn = tk.Button(login_frame, text='Go back', bg='#BDB5B2', command=lambda:show_frame(main_frame))

login_frame_password = tk.Entry(login_frame, show='*')
login_frame_username = tk.Entry(login_frame)
login_frame_showbutton = tk.Checkbutton(login_frame, variable = var, command=lambda:showpass())

login_frame_namelab = tk.Label(login_frame, text='User name:', bg='#B5B9BA')
login_frame_passlab = tk.Label(login_frame, text='Password: ', bg='#B5B9BA')

login_frame_message = tk.Label(login_frame, textvariable=message, bg='#838A8C')

login_frame_submit = tk.Button(login_frame, text='Log in', bg='#BDB5B2', command=lambda:login())

#output

login_frame_title.place(relwidth=1, relheight=0.1, relx=0, rely=0)
login_frame_btn.place(relwidth=1, relheight=0.1, relx=0, rely=0.1)
login_frame_namelab.place(relwidth=1, relheight=0.1, relx=0, rely=0.2)
login_frame_username.place(relwidth=1, relheight=0.1, relx=0, rely=0.3)
login_frame_passlab.place(relwidth=1, relheight=0.1, relx=0, rely=0.4)
login_frame_password.place(relwidth=1, relheight=0.1, relx=0, rely=0.5)
login_frame_showbutton.place(relwidth=0.10, relheight=0.1, relx=0.90, rely=0.5)

login_frame_message.place(relwidth=1, relheight=0.1, relx=0, rely=0.67)
login_frame_submit.place(relwidth=1, relheight=0.15, relx=0, rely=0.85)

#==============================Register code

register_frame_title = tk.Label(register_frame, text='Registration', bg='#1F1F1F', fg='#C9C2C0')
register_frame_btn = tk.Button(register_frame, text='Go back', bg='#BDB5B2', command=lambda:show_frame(main_frame))

register_frame_password = tk.Entry(register_frame, show='*')
register_frame_username = tk.Entry(register_frame)
register_frame_showbutton = tk.Checkbutton(register_frame, variable = var, command=lambda:showpass())

register_frame_namelab = tk.Label(register_frame, text='User name (3-10 symbols):', bg='#B5B9BA')
register_frame_passlab = tk.Label(register_frame, text='Password (4-10 symbols): ', bg='#B5B9BA')

register_frame_message = tk.Label(register_frame, textvariable=message, bg='#838A8C')

register_frame_submit = tk.Button(register_frame, text='Register', bg='#BDB5B2', command=lambda:regsubmit())

#output

register_frame_title.place(relwidth=1, relheight=0.1, relx=0, rely=0)
register_frame_btn.place(relwidth=1, relheight=0.1, relx=0, rely=0.1)
register_frame_namelab.place(relwidth=1, relheight=0.1, relx=0, rely=0.2)
register_frame_username.place(relwidth=1, relheight=0.1, relx=0, rely=0.3)
register_frame_passlab.place(relwidth=1, relheight=0.1, relx=0, rely=0.4)
register_frame_password.place(relwidth=1, relheight=0.1, relx=0, rely=0.5)
register_frame_showbutton.place(relwidth=0.10, relheight=0.1, relx=0.90, rely=0.5)

register_frame_message.place(relwidth=1, relheight=0.1, relx=0, rely=0.67)
register_frame_submit.place(relwidth=1, relheight=0.15, relx=0, rely=0.85)
#============================================ Profile code

profile_frame_head = tk.Label(profile_frame, text='Profile', bg='#1F1F1F', fg='#C9C2C0')

profile_frame_usernamelab = tk.Label(profile_frame, text='User name:', bg='#B5B9BA')
profile_frame_namelab = tk.Label(profile_frame, bg='#838A8C', font="Helvetica 13")
profile_frame_editname = tk.Button(profile_frame, text='Edit', bg='#838A8C', borderwidth=0, command=lambda:edit(0.55, 0.1, 0.35, 0.1, 'name'))

profile_frame_status = tk.Label(profile_frame, text='Status:', bg='#B5B9BA')
profile_frame_userstatus = tk.Label(profile_frame, bg='#838A8C', font="Helvetica 13")
profile_frame_editstatus = tk.Button(profile_frame, text='Edit', bg='#838A8C', borderwidth=0, command=lambda:edit(0.55, 0.1, 0.35, 0.2, 'status'))

profile_frame_age = tk.Label(profile_frame, bg='#B5B9BA', text='Age:')
profile_frame_userage = tk.Label(profile_frame, bg='#838A8C', font="Helvetica 13", text='None')
profile_frame_editage = tk.Button(profile_frame, text='Edit', bg='#838A8C', borderwidth=0, command=lambda:edit(0.55, 0.1, 0.35, 0.3, 'age'))

profile_frame_country = tk.Label(profile_frame, bg='#B5B9BA', text='Country:')
profile_frame_usercountry = tk.Label(profile_frame, bg='#838A8C', font="Helvetica 13", text='None')
profile_frame_editcountry = tk.Button(profile_frame, text='Edit', bg='#838A8C', borderwidth=0, command=lambda:edit(0.45, 0.1, 0.35, 0.4, 'country'))

profile_frame_sex = tk.Label(profile_frame, bg='#B5B9BA', text='Sex:')
profile_frame_usersex = tk.Label(profile_frame, bg='#838A8C', font="Helvetica 13", text='None')
profile_frame_editsex = tk.Button(profile_frame, text='Edit', bg='#838A8C', borderwidth=0, command=lambda:edit(0.55, 0.1, 0.35, 0.5, 'sex'))

profile_frame_editpass = tk.Button(profile_frame, text='Change password', bg='#B5B9BA', borderwidth=1, command=lambda:edit(0.55, 0.1, 0.35, 0.6, 'pass'))

profile_frame_message = tk.Label(profile_frame, textvariable=profile_message, bg='#838A8C')
profile_frame_btn = tk.Button(profile_frame, text='Log out', bg='#BDB5B2', command=lambda:show_frame(main_frame))

#output

profile_frame_head.place(relwidth=1, relheight=0.1, relx=0, rely=0)

profile_frame_usernamelab.place(relwidth=0.35, relheight=0.1, relx=0, rely=0.1)
profile_frame_namelab.place(relwidth=0.55, relheight=0.1, relx=0.35, rely=0.1)
profile_frame_editname.place(relwidth=0.10, relheight=0.1, relx=0.90, rely=0.1)

profile_frame_status.place(relwidth=0.35, relheight=0.1, relx=0, rely=0.2)
profile_frame_userstatus.place(relwidth=0.55, relheight=0.1, relx=0.35, rely=0.2)
profile_frame_editstatus.place(relwidth=0.10, relheight=0.1, relx=0.90, rely=0.2)

profile_frame_age.place(relwidth=0.35, relheight=0.1, relx=0, rely=0.3)
profile_frame_userage.place(relwidth=0.55, relheight=0.1, relx=0.35, rely=0.3)
profile_frame_editage.place(relwidth=0.10, relheight=0.1, relx=0.90, rely=0.3)

profile_frame_country.place(relwidth=0.35, relheight=0.1, relx=0, rely=0.4)
profile_frame_usercountry.place(relwidth=0.55, relheight=0.1, relx=0.35, rely=0.4)
profile_frame_editcountry.place(relwidth=0.10, relheight=0.1, relx=0.90, rely=0.4)

profile_frame_sex.place(relwidth=0.35, relheight=0.1, relx=0, rely=0.5)
profile_frame_usersex.place(relwidth=0.55, relheight=0.1, relx=0.35, rely=0.5)
profile_frame_editsex.place(relwidth=0.10, relheight=0.1, relx=0.90, rely=0.5)

profile_frame_editpass.place(relwidth=0.35, relheight=0.1, relx=0, rely=0.6)

profile_frame_message.place(relwidth=1, relheight=0.1, relx=0, rely=0.72)
profile_frame_btn.place(relwidth=1, relheight=0.15, relx=0, rely=0.85)

#============================================ END
show_frame(main_frame)

root.mainloop()