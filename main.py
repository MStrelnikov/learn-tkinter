# подключаем библиотеку tkinter
# синтаксис:
#  import <название библиотеки> as <псевдоним библиотеки>
import tkinter as tk

# создаем главное окно
root = tk.Tk()

# задаем заголовок окна
root.title("Графика Tkinter")

# создаем холст - объект Canvas
# первый аргумент - окно, для которого будет создан Canvas
# width - ширина холста в пикселях
# height - высота холста в пикселях
# bg - цвет фона
canvas = tk.Canvas(root, width=500, height=500,bg="white")

# размещаем холст в окне
canvas.pack()


# создаем горизонтальные и вертикальные линии с шагом 20 пикселей
p = 10
for i in range(10):
    canvas.create_line(p, 10, p, 190, fill="green", width=3)
    canvas.create_line(10, p, 190, p, fill="red", width=3)
    p += 20

# запускаем главный цикл приложения
root.mainloop()