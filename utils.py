import calendar
import os
import locale
from datetime import datetime

locale.setlocale(locale.LC_ALL, ("es_ES")) # Cambiar formato de fecha a español

clear_console = lambda: os.system('cls' if os.name == 'nt' else 'clear')

get_day = lambda: int(datetime.now().strftime("%d"))
get_month = lambda: int(datetime.now().strftime("%m"))
get_year = lambda: int(datetime.now().strftime("%Y"))

week_day = lambda: calendar.weekday(get_year(),get_month(),get_day()) # Guardar fecha

day_letter = lambda: calendar.day_name[week_day()].title()

month_letter = lambda: calendar.month_name[get_month()].title()

curent_date_letter = lambda: str(f"{day_letter()} {get_day()} de {month_letter()} del {get_year()}")

new_line = '\n'
line = '----------------------------\n'