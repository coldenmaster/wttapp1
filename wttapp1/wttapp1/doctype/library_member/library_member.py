# Copyright (c) 2023, Wangtao and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class LibraryMember(Document):

	@property
	def age(self):
		# return frappe.utils.now_datetime() - self.birth # type is wrong
		return 51
	
	 #this method will run every time a document is saved
	def before_save(self):
		self.full_name = f'{self.last_name}.{self.first_name or ""}'
	
	def autoname(self):
		self.name = f'{self.last_name}{self.first_name or ""}'


	def get_test_str(self):
		""" Returns the person's full name """
		return f"{self.full_name}-{self.first_name}:{self.age}"
	
	def save(self, *args, **kwargs):
		super().save(*args, **kwargs)
		print(self.get_test_str())

