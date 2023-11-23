# Copyright (c) 2023, Wangtao and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from frappe.model.docstatus import DocStatus

class LibraryTransaction(Document):
	def before_submit(self):
		if self.type == "Issue":
			self.validate_issue()
			self.validate_maximum_limit()
			article = frappe.get_doc("Article", self.article)
			article.status = "Issued"
			article.save()

		elif self.type == "Return":
			self.validate_return()
			article = frappe.get_doc("Article", self.article)
			article.status = "Available"
			article.save()

	def validate_issue(self):
		self.validate_membership()
		article = frappe.get_doc("Article", self.article)
		if article.status == "Issued":
			frappe.throw("此书已经借出")

	def validate_return(self):
		article = frappe.get_doc("Article", self.article)
		if article.status == "Available":
			frappe.throw("此书已经在图书馆内")

	def validate_maximum_limit(self):
		max_articles = frappe.db.get_single_value("Library Settings", "max_number")
		count = frappe.db.count(
			"Library Transaction",
			{
				"library_member": self.library_member,
				"type": "Issue", 
				"docstatus": DocStatus.submitted(),
			}
		)
		if count >= max_articles:
			frappe.throw("超过最大借书数量")

	def validate_membership(self):
		valid_membership = frappe.db.exists(
			"Library Membership",
			{
				"library_member": self.library_member,
				"docstatus": DocStatus.submitted(),
				"from_date": ("<", self.date),
				"to_date": (">", self.date),
			},
		)
		if not valid_membership:
			frappe.throw("此会员不存在")