# import unittest
# import frappe
# # import BaseTestCommand

# # class TestCommand(BaseTestCommands, unittest.TestCase):
# class TestCommand(unittest.TestCase):
#     def test_execute(self):
#         # test 1: execute a command expecting a numeric output
#         self.execute("bench --site {site} execute frappe.db.get_database_size")
#         self.assertEqual(self.returncode, 0)
#         self.assertIsInstance(float(self.stdout), float)

#         # test 2: execute a command expecting an errored output as local won't exist
#         self.execute("bench --site {site} execute frappe.local.site")
#         self.assertEqual(self.returncode, 1)
#         self.assertIsNotNone(self.stderr)

#         # test 3: execute a command with kwargs
#         # Note:
#         # terminal command has been escaped to avoid .format string replacement
#         # The returned value has quotes which have been trimmed for the test
#         self.execute("""bench --site {site} execute frappe.bold --kwargs '{{"text": "DocType"}}'""")
#         self.assertEqual(self.returncode, 0)
#         self.assertEqual(self.stdout[1:-1], frappe.bold(text='DocType'))