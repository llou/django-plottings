import math
from datetime import timedelta
import numpy as np


class ActivityMap:
    num_days = 365
    weekdays = ["mon", "", "wed", "", "fri", "", "sun"]
    months = ["jan", "feb", "mar", "apr", "may", "jun", "jul", "aug", "sep",
              "oct", "nov", "dec"]

    def __init__(self, today):
        self.today = today
        self.num_days = self.get_num_days(today)
        self.base = self.get_base(today, self.num_days)
        self.weeks = self.get_weeks()
        self.reset()

    def reset(self):
        self.data = np.zeros((7, self.weeks), dtype=np.uint8)

    def get_num_days(self, day):
        return self.num_days

    def get_base(self, today, num_days):
        year_ago = today - timedelta(num_days)
        return year_ago - timedelta(year_ago.weekday())

    def get_weeks(self):
        return math.ceil((self.num_days + self.base.weekday()) / 7)

    def get_month(self, month):
        return self.months[month - 1]

    def inc_date(self, date):
        week = (date - self.base).days // 7
        week_day = date.weekday()
        self.data[week_day, week] = self.data[week_day, week] + 1

    def get_x_ticks(self):
        result = [""] * self.weeks
        for week in range(self.weeks):
            for weekday in range(7):
                d = self.base + timedelta(week * 7 + weekday)
                if d.day == 1:
                    result[week] = self.get_month(d.month)
        return result

    def get_y_ticks(self):
        return self.weekdays

    def load_activity(self, activity):
        for d in activity:
            self.inc_date(d)

    def get_data(self):
        return self.data


def activity_plot(data, **kwargs):
    return None
