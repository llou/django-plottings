import math
import random
from datetime import date, timedelta
from pathlib import Path
from unittest import TestCase
import numpy as np
from ..plots.activity import ActivityMap

FIXTURES_DIR = Path(__file__).resolve().parent / "fixtures"


def random_activity(today, num_days=365, num_choices=200):
    result = []
    choices = range(num_choices)
    for i in choices:
        o = random.choice(choices)
        result.append(today - timedelta(o))
    return result


class ActivityMapTest(TestCase):
    today = date(2024, 6, 12)
    num_days = 365
    activity_class = ActivityMap

    def setUp(self):
        self.map = self.activity_class(self.today)

    def test_methods(self):
        self.assertEqual(self.map.get_num_days(self.today), self.num_days)
        base = self.map.get_base(self.today, self.num_days)
        self.assertEqual(base.weekday(), 0)
        dist = self.today - base
        self.assertGreater(dist.days, self.num_days)
        self.assertLess(dist.days, self.num_days + 7)
        self.assertEqual(self.map.get_month(8), "aug")
        weeks = self.map.get_weeks()
        ticks = self.map.get_x_ticks()
        self.assertEqual(len(ticks), weeks)

    def test_a_lot_of_extra_weeks(self):
        from_date = date(2000, 1, 1)
        to_date = date(2025, 1, 1,)
        delta_days = (to_date - from_date).days
        for d1 in range(delta_days):
            today = from_date + timedelta(d1, 0, 0)
            amap = self.activity_class(today)
            for d2 in range(math.ceil(self.num_days / 7) * 7):
                base = amap.base
                day = base + timedelta(d2)
                amap.inc_date(day)
            unique, counts = np.unique(amap.data, return_counts=True)
            self.assertNotIn(0, unique)

    def test_blackbox(self):
        activity = random_activity(self.today)
        activity_map = self.activity_class(self.today)
        activity_map.load_activity(activity)
