import tkinter as tk

def change_bg_color():
    color = entry.get()
    canvas.config(bg=color)


def clear():
  entry.delete(0,'end')




root = tk.Tk()
root.geometry('300x300')
root.title("Выбор цвета")
root.resizable(False, False)



canvas = tk.Canvas(root, width=200, height=200, bg='white')
canvas.pack()

entry = tk.Entry(root)
entry.pack()



button = tk.Button(root, text="Изменить цвет", command=change_bg_color)
button.pack()

clear_button = tk.Button(root, text='Очистить', command=clear)
clear_button.pack()

root.mainloop()

