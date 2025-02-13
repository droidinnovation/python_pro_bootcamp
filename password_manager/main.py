from tkinter import *
from tkinter import messagebox

# ------- save data ---------
def save_data():
    website = website_entry.get()
    email = username_entry.get()
    password = password_entry.get()

    if len(website) <= 0 or len(password) <= 0:
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any field empty!")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"There are the details entered:\n"
                                                      f"Email: {email}\nPassword: {password}\n"
                                                      f"Is it ready to save?")
        if is_ok:
            with open("data.txt", mode="a") as data_file:
                data_file.write(f"{website} | {email} | {password} \n")
            website_entry.delete(0, END)
            password_entry.delete(0, END)





# ------- UI Setup ---------
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100,100, image=logo_img)
canvas.grid(row=0, column=1)

website_label = Label(text="Website:")
website_label.grid(row=1, column=0)
username_label = Label(text="Email/Username:")
username_label.grid(row=2, column=0)
password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

# Entries
website_entry = Entry(width=38)
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.focus()
username_entry = Entry(width=38)
username_entry.grid(row=2, column=1, columnspan=2)
username_entry.insert(0, "emailexample@email.com")
password_entry = Entry(width=21)
password_entry.grid(row=3, column=1)

# Buttons
generate_password_button = Button(text="Generate Password")
generate_password_button.grid(row=3, column=2)
add_button = Button(text="Add", width=35, command=save_data)
add_button.grid(row=4, column=1, columnspan= 2)



window.mainloop()
