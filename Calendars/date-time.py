import pprint
from datetime import datetime, timezone, date
import pytz

pp = pprint.PrettyPrinter(indent=4)
tz = pytz.timezone('America/Los_Angeles')


def general_date_time():
    today = date.today()
    print("Today date is: ", today)
    print(datetime.now(timezone.utc))
    print(datetime.now())

    dt1 = datetime.strptime("21/11/06 16:30", "%d/%m/%y %H:%M")
    print(dt1)


def epoch(key):
    # s = float(key) / 1000.0
    s = float(key)
    return datetime.fromtimestamp(s, tz).strftime('%Y-%m-%d %H:%M:%S')


if __name__ == "__main__":
    now = datetime.now()
    print(now.strftime("%Y-%m-%d %H:%M:%S").format(datetime.now()))
