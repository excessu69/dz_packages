import datetime
from application.salary import calculate_salary
from application.db.people import get_employees
import matplotlib.pyplot as mp
import numpy as np

def plot_example():
    x = np.linspace(-12, 10, 300)  # Определение диапазона значений x
    y = x**2 + 2*x + 4  # Рассчитываем значения y для каждого x


    mp.plot(x, y, label='y = $x^2 + 2x + 4$', color='r')  # Построение графика квадратного уравнения

    mp.title('Графики')
    mp.xlabel('X')
    mp.ylabel('Y')

    mp.grid(True)  # Сетка
    mp.legend()

    mp.show()

def main():
    calculate_salary()
    get_employees()
    print("Текущая дата:", datetime.date.today())

if __name__ == "__main__":
    main()
    plot_example()








