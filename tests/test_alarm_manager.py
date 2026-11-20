"""Pruebas iniciales para AlarmManager."""

import unittest

from src.core.alarm_manager import AlarmManager
from src.models import Alarm


class TestAlarmManager(unittest.TestCase):
    """Verifica operaciones básicas del gestor de alarmas."""

    def test_add_and_remove_alarm(self) -> None:
        manager = AlarmManager()
        alarm = Alarm(id="1", hour=7, minute=30, label="Despertar")

        manager.add_alarm(alarm)
        self.assertEqual(len(manager.list_alarms()), 1)

        removed = manager.remove_alarm("1")
        self.assertTrue(removed)
        self.assertEqual(len(manager.list_alarms()), 0)


if __name__ == "__main__":
    unittest.main()
