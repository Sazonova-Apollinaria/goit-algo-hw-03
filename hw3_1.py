from datetime import datetime

def get_days_from_today(date):
    try:
        prepared_date = datetime.strptime(date, "%Y-%m-%d").date()
    except ValueError:
        return "Error: invalid date format. Use format YYYY-MM-DD"
    
    now = datetime.today().date()
    delta = now - prepared_date
    return delta.days


print(get_days_from_today("2021-10-09"))
print(get_days_from_today("13.14.20000"))
