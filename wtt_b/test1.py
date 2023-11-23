import frappe

def long_job(arg1, arg2):
    frappe.publish_realtime('msgprint', 'Starting long job...')