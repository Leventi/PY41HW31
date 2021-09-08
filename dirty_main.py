from application.db.people import *
from application.salary import *
import datetime



if __name__ == '__main__':
    get_employees()
    calculate_salary()

    print("Сегодня", datetime.date.today())