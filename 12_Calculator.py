# My first python calculator
import tkinter as tk

window = tk.Tk()
window.geometry(f"250x300")
window['bg'] = '#8fffff'
window.title('My Python calculator')

first = tk.Label(text='Первое число')
first['bg'] = '#8fffff'
first.grid(column=0, row=0, padx=10, pady=10)
second = tk.Label(text='Второе число')
second['bg'] = '#8fffff'
second.grid(column=0, row=1)
result = tk.Label(text='Результат')
result['bg'] = '#8fffff'
result.grid(column=0, row=2, padx=10, pady=10)

first_entry = tk.Entry()
first_entry.grid(column=1, row=0)
second_entry = tk.Entry()
second_entry.grid(column=1, row=1)
result_label = tk.Label(text="")
result_label.grid(column=1, row=2, sticky="w")
result_label['bg'] = '#8fffff'


def get_sum():
    a = int(first_entry.get())
    b = int(second_entry.get())
    c = a + b

    result_label['text'] = c


button = tk.Button(window, text='Вычислить сумму', command=get_sum)
button.grid(column=1, row=3)

window.mainloop()
