import matplotlib.pyplot as plt
import numpy as np
import customtkinter


def f(x, y, a):
    return (x**2)**(1/3) + (y**2)**(1/3) - (a**2)**(1/3)


def doit(a):
    x_min, x_max = -6, 6
    y_min, y_max = -6, 6
    step = 5
    
    x = np.linspace(x_min, x_max, step)
    y = np.linspace(y_min, y_max, step)
    X, Y = np.meshgrid(x, y)

    plt.contour(X, Y, f(X, Y, a), levels=[0], colors='black')
    plt.axis('equal')
    plt.xlabel("x")
    plt.ylabel("y")
    plt.show()


# интерфейс
customtkinter.set_appearance_mode("system")

customtkinter.set_default_color_theme("dark-blue")

root = customtkinter.CTk()
root.geometry("320x240")

frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=20, padx=60, fill="both", expand=True)

label1 = customtkinter.CTkLabel(master=frame, text="Параметр:")
label1.pack(pady=10, padx=10)

entry1 = customtkinter.CTkEntry(master=frame, placeholder_text="параметр а")
entry1.pack(pady=5, padx=10)


def DoIt():
    v1 = float(entry1.get())
    doit(v1)


button = customtkinter.CTkButton(master=frame, text="Рисуем", command=DoIt)
button.pack(pady=10, padx=10)

root.mainloop()