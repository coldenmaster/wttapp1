# Copyright (c) 2023, Wangtao and Contributors
# See license.txt

import frappe
from frappe.tests.utils import FrappeTestCase


class TestLibraryMember(FrappeTestCase):
	def test(self):
		frappe.get_last_doc("Task")
