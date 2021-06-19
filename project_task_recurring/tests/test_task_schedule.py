# Copyright 2021 ACSONE SA/NV
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo.exceptions import ValidationError
from odoo.tests.common import SavepointCase


class TestTasckSchedule(SavepointCase):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.project = cls.env.ref("project_task_recurring.project_project_with_recurrence")
        cls.schedule_obj = cls.env["project.task.schedule"]

    def test_task_schedule(self):
        tasks_before = self.project.task_ids
        self.schedule_obj._schedule_cron()
        tasks_after = self.project.task_ids - tasks_before
        self.assertEqual(
            2,
            len(tasks_after)
        )
