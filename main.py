import os
import sys
import datetime

sys.path.insert(0, f'{os.getcwd()}\\application')
sys.path.insert(0, f'{os.getcwd()}\\application\db')

from people import get_employees
from salary import calculate_salary


if __name__ == '__main__':

    get_employees()
    calculate_salary()

    print("Сегодня", datetime.date.today())
