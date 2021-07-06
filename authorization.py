import tkinter as tk
import os

path = os.path.dirname(os.path.realpath(__file__)) + "\\"

root = tk.Tk()
root.geometry('300x256')
root.title('Profile')
root.iconbitmap(path + 'icon.ico')
#######################################################

def show_frame(frame):
    frame.tkraise()

    register_frame_password.delete(0, tk.END)
    register_frame_username.delete(0, tk.END)

    login_frame_password.delete(0, tk.END)
    login_frame_username.delete(0, tk.END)

    message.set('')

names = []
namespasswords = []

def regsubmit():
    del names[:]; del namespasswords[:]

    if 3 <= (len(register_frame_username.get())) <= 10 and 4 <= (len(register_frame_password.get())) <= 10:
        with open(path + 'data.txt', 'r') as data:
            name = str(register_frame_username.get()) + ' '
            for string in data:
                if name in string:
                    names.append(1)
                    break

        if len(names) == 0:
            with open(path + 'data.txt', 'a') as data:
                a = str(register_frame_username.get()) + ' ' + str(register_frame_password.get())
                data.write(f"""
{a} """)
            message.set('Thanks for registering!')

        if len(names) != 0:
            message.set('The name is already taken')

    if (len(register_frame_username.get()) < 3):
        message.set('Minimum username length is 3 symbols')
    
    elif (len(register_frame_username.get())) > 10:
        message.set('Maximum username length is 10 symbols')

    elif (len(register_frame_password.get()) < 4):
        message.set('Minimum password length is 4 symbols')

    elif (len(register_frame_password.get())) > 10:
        message.set('Maximum password length is 10 symbols')


def login():

    if 3 <= (len(login_frame_username.get())) <= 10 and 4 <= (len(login_frame_password.get())) <= 10:
        with open(path + 'data.txt', 'r') as data:
            logpas = str(login_frame_username.get()) + ' ' + str(login_frame_password.get()) + ' '
            for string in data:
                if logpas in string:
                    namespasswords.append(str(login_frame_username.get()))
                    break

        if len(namespasswords) == 1:
            show_frame(profile_frame)
            profile_frame_namelab.config(text=namespasswords[0])
        else:
            message.set('No such name or password')
    
    if (len(login_frame_username.get()) < 3):
        message.set('Minimum username length is 3 symbols')
    
    elif (len(login_frame_username.get())) > 10:
        message.set('Maximum username length is 10 symbols')

    elif (len(login_frame_password.get()) < 4):
        message.set('Minimum password length is 4 symbols')

    elif (len(login_frame_password.get())) > 10:
        message.set('Maximum password length is 10 symbols')

    del namespasswords[0]

###================================================= FRAMES

root.rowconfigure(0, weight=1)
root.columnconfigure(0, weight=1)

main_frame = tk.Frame(root, bg='#838A8C')
login_frame = tk.Frame(root, bg='#838A8C')
register_frame = tk.Frame(root, bg='#838A8C')
profile_frame = tk.Frame(root, bg='#838A8C')

for frame in (main_frame, login_frame, register_frame, profile_frame):
    frame.grid(row=0, column=0, sticky='nsew')

message = tk.StringVar()


#==============================Main window code

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

login_frame_password = tk.Entry(login_frame)
login_frame_username = tk.Entry(login_frame)

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

login_frame_message.place(relwidth=1, relheight=0.1, relx=0, rely=0.67)
login_frame_submit.place(relwidth=1, relheight=0.15, relx=0, rely=0.85)

#==============================Register code

register_frame_title = tk.Label(register_frame, text='Registration', bg='#1F1F1F', fg='#C9C2C0')
register_frame_btn = tk.Button(register_frame, text='Go back', bg='#BDB5B2', command=lambda:show_frame(main_frame))

register_frame_password = tk.Entry(register_frame)
register_frame_username = tk.Entry(register_frame)

register_frame_namelab = tk.Label(register_frame, text='User name (3-12 symbols):', bg='#B5B9BA')
register_frame_passlab = tk.Label(register_frame, text='Password (4-12 symbols): ', bg='#B5B9BA')

register_frame_message = tk.Label(register_frame, textvariable=message, bg='#838A8C')

register_frame_submit = tk.Button(register_frame, text='Register', bg='#BDB5B2', command=lambda:regsubmit())

#output

register_frame_title.place(relwidth=1, relheight=0.1, relx=0, rely=0)
register_frame_btn.place(relwidth=1, relheight=0.1, relx=0, rely=0.1)
register_frame_namelab.place(relwidth=1, relheight=0.1, relx=0, rely=0.2)
register_frame_username.place(relwidth=1, relheight=0.1, relx=0, rely=0.3)
register_frame_passlab.place(relwidth=1, relheight=0.1, relx=0, rely=0.4)
register_frame_password.place(relwidth=1, relheight=0.1, relx=0, rely=0.5)

register_frame_message.place(relwidth=1, relheight=0.1, relx=0, rely=0.67)
register_frame_submit.place(relwidth=1, relheight=0.15, relx=0, rely=0.85)
#============================================ Profile code

profile_frame_btn = tk.Button(profile_frame, text='Log out', bg='#BDB5B2', command=lambda:show_frame(main_frame))

profile_frame_usernamelab = tk.Label(profile_frame, text='User name:', bg='#B5B9BA')
profile_frame_namelab = tk.Label(profile_frame, bg='#838A8C', font="Helvetica 13")

profile_frame_head = tk.Label(profile_frame, text='Profile', bg='#1F1F1F', fg='#C9C2C0')

#output

profile_frame_head.place(relwidth=1, relheight=0.1, relx=0, rely=0)
profile_frame_usernamelab.place(relwidth=0.35, relheight=0.1, relx=0, rely=0.1)
profile_frame_namelab.place(relwidth=0.65, relheight=0.1, relx=0.35, rely=0.1)
profile_frame_btn.place(relwidth=1, relheight=0.15, relx=0, rely=0.85)


#============================================ END
show_frame(main_frame)

root.mainloop()