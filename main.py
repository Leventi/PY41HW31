from application.db.people import get_employees
from application.salary import calculate_salary
import datetime



if __name__ == '__main__':
    get_employees()
    calculate_salary()

    print("Сегодня", datetime.date.today())
