# My first python calculator
import tkinter as tk

window = tk.Tk()
window.geometry(f"250x300")
window['bg'] = '#8fffff'
window.title('My Python calculator')

first = tk.Label(text='Первое число')
first.grid(column=0, row=0, padx=10, pady=10)
second = tk.Label(text='Второе число')
second.grid(column=0, row=1)
result = tk.Label(text='Результат')
result.grid(column=0, row=2, padx=10, pady=10)


firstEntry = tk.Entry()
firstEntry.grid(column=1, row=0)
secondEntry = tk.Entry()
secondEntry.grid(column=1, row=1)
resultLabel = tk.Label(text='                ')
resultLabel.grid(column=1, row=2)

window.mainloop()
