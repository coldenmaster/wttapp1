# Copyright (c) 2023, Wangtao and contributors
# For license information, please see license.txt

import frappe
from frappe.model.docstatus import DocStatus

from frappe.website.website_generator import WebsiteGenerator

class Article(WebsiteGenerator):
	def validate(self):
		print("article validate")
		print("自定义代码区：")

	
	def autoname(self):
		print("autoname wangtao ...")

	def on_trash(self):
		print("trash wangtao ...")

	def on_submit(self):
		print("on_submit wangtao ...")
