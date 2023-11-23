# Copyright (c) 2023, Wangtao and contributors
# For license information, please see license.txt

import frappe
import json
import os
from frappe.model.document import Document

class MachCheck(Document):
	
	"""This is a virtual doctype controller for demo purposes.

    - It uses a single JSON file on disk as "backend".
    - Key is docname and value is the document itself.

    Example:
    {
            "doc1": {"name": "doc1", ...}
            "doc2": {"name": "doc2", ...}
    }
    """
    
	DATA_FILE = "data_file_mc.json"
	
	@staticmethod
	def get_current_data() -> dict[str, dict]:
		"""Read data from disk"""
		print("os.path.curdir 工作目录显示：", os.path.curdir)
		if not os.path.exists(MachCheck.DATA_FILE):
			print("json 文件不存在")
			return {}
		
		with open(MachCheck.DATA_FILE) as f:
			print("json 文件存在 !!")
			# print(f)
			return json.load(f)

	@staticmethod
	def update_data(data:dict[str, dict]) -> None:
		"""Flush updated data to disk"""
		with open(MachCheck.DATA_FILE, "w+", encoding = 'utf8') as data_file:
			json.dump(data, data_file, ensure_ascii=False)
			print("进行虚拟doc插入 完成")


	modified = 0

	def db_insert(self, *args, **kwargs):
		print("进行虚拟doc插入")
		d = self.get_valid_dict(convert_dates_to_str=True)
		data = self.get_current_data()
		data[d.name] = d
		
		self.update_data(data)


	def load_from_db(self):
		print("进行虚拟doc load_from_db")
		data = self.get_current_data()
		d = data.get(self.name)
		super(Document, self).__init__(d)

	def db_update(self, *args, **kwargs):
		print("进行虚拟doc db_update")
		self.db_insert(*args, **kwargs)

	def delete(self, *args, **kwargs) -> None:
		"""Delete the current document from backend"""
		...


	@staticmethod
	def get_list(args):
		print("进行虚拟doc get_list")
		data = MachCheck.get_current_data()
		# print([frappe._dict(doc) for name, doc in data.items()])
		return [frappe._dict(doc) for name, doc in data.items()]

	@staticmethod
	def get_count(args):
		print("进行虚拟doc get_count")
		data = MachCheck.get_current_data()
		return len(data)

	@staticmethod
	def get_stats(args):
		print("进行虚拟doc get_stats")
		return {}
	
		# test Doc Action
	@frappe.whitelist()
	@staticmethod
	def action1inner(*args, **kwargs):
		print("Action1 On")
		print(kwargs)
		print("Action1 End")



# test Doc Action
@frappe.whitelist()
def action1(*args, **kwargs):
	print("Action1 On")
	print(kwargs)
	print("Action1 End")





# 对虚拟doc的控制器以及拥有的方法进确认
from frappe.model.base_document import get_controller
from frappe import _
import inspect

def validate_controller(doctype: str) -> None:
	try:
		controller = get_controller(doctype)
	except ImportError:
		frappe.msgprint(
			_("Failed to import virtual doctype {}, is controller file present?").format(doctype)
		)
		return

	def _as_str(method):
		if hasattr(method, "__module__"):
			return f"{method.__module__}.{method.__qualname__}"
		return "None"

	expected_static_method = ["get_list", "get_count", "get_stats"]
	for m in expected_static_method:
		method = inspect.getattr_static(controller, m, None)
		if not isinstance(method, staticmethod):
			frappe.msgprint(
				_("Virtual DocType {} requires a static method called {} found {}").format(
					frappe.bold(doctype), frappe.bold(m), frappe.bold(_as_str(method))
				),
				title=_("Incomplete Virtual Doctype Implementation"),
			)

	expected_instance_methods = ["db_insert", "db_update", "load_from_db", "delete"]
	parent_class = controller.mro()[1]
	for m in expected_instance_methods:
		method = getattr(controller, m, None)
		original_method = getattr(parent_class, m, None)
		if method == original_method:
			frappe.msgprint(
				_("Virtual DocType {} requires overriding an instance method called {} found {}").format(
					frappe.bold(doctype), frappe.bold(m), frappe.bold(_as_str(method))
				),
				title=_("Incomplete Virtual Doctype Implementation"),
			)