from datetime import datetime

def get_days_from_today(date):
    prepared_date = datetime.strptime(date, "%Y-%m-%d").date()
    now = datetime.today().date()
    delta = now - prepared_date
    return delta.days

print(get_days_from_today("2021-10-09"))