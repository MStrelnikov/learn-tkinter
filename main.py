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


# создаем графические объекты
# ....

# запускаем главный цикл приложения
root.mainloop()