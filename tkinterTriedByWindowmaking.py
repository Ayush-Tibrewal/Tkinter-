from tkinter import *
# imported tinker


from PIL import ImageTk,Image
#python imaging library ImageTk is a module that
# provides a PhotoImage class which can be used to display images in a Tkinter window.


from tkinter import messagebox

def handle_login():
    email = email_input.get() # input of the email
    password = password_input.get() # input of the pass

    if email == 'nitish@gmail.com' and password == '1234':
        messagebox.showinfo('Yayyy','Login Successful')
    else:
        messagebox.showerror('Error','Login Failed')
    #This function is called when the login_btn button is clicked. It retrieves the
    # email and password entered by the user from the email_input and password_input Entry widgets,
    # respectively, using the get() method. It then checks if the email and password are correct,
    # and displays an appropriate message using the messagebox module from tkinter.
#If the email and password are correct, the showinfo() method of the messagebox module is called to
# display a message box with the title 'Yayyy' and message 'Login Successful'. If the email or password is
# incorrect, the showerror() method is called to display a message box with the title 'Error' and message
# 'Login Failed'.
#So, in summary, the command parameter is used to specify the function to
# call when a button is clicked, and the handle_login function is called when the
# login_btn button is clicked to retrieve the user's email and password, and display a message
# indicating whether the login was successful or not.


root = Tk()  # we have to define the class so tk here is the main class

root.title('Login Form')
root.iconbitmap('favicon.ico')  # to change the icon







root.geometry('350x500')
#size of the window






root.configure(background='#0096DC')
# colour of the window




img = Image.open('wallpapers/img1.jpg')
# opening of the image
resized_img = img.resize((70,70))
img = ImageTk.PhotoImage(resized_img)
#In this code snippet, we create a PIL
# image object by opening the image file using Image.open('wallpapers/img1.jpg')




img_label = Label(root,image=img)#In Tkinter, Label is a class that is used to create
# a widget that displays text and/or images. In the code snippet
# provided, we create an instance of the Label class using the following code:
img_label.pack(pady=(10,10))
#n Tkinter, the pack() method is used to add widgets to a
# parent widget and to adjust their layout. When we create a Label
# widget and want to display it in a window, we need to add it to the parent window using the pack() method.



text_label = Label(root,text='Flipkart',fg='white',bg='#0096DC')
text_label.pack()
text_label.config(font=('verdana',24))

email_label = Label(root,text='Enter Email',fg='white',bg='#0096DC')
email_label.pack(pady=(20,5))
email_label.config(font=('verdana',12))

email_input = Entry(root,width=50)
#entry is used to max the box type attribute blank box
email_input.pack(ipady=6,pady=(1,15))
#here we created the input box which will take the input




password_label = Label(root,text='Enter Password',fg='white',bg='#0096DC')
password_label.pack(pady=(20,5))
password_label.config(font=('verdana',12))

password_input = Entry(root,width=50)
password_input.pack(ipady=6,pady=(1,15))



login_btn = Button(root,text='Login Here',bg='white',fg='black',width=20,height=2,command=handle_login)
#here we used command to call that function when we press the login button
login_btn.pack(pady=(10,20))
login_btn.config(font=('verdana',10))
#here we made login button which has click in option by using button label


root.mainloop()
#In a Tkinter program, root.mainloop() must be called at the end of the program
#to start the event loop and keep the GUI window running.
#Without it, the window will be displayed briefly and then immediately close.
