import frappe
import os

@frappe.whitelist()
def action1(*args, **kwargs):
    print("-------------WTTAPI Action1 On")
    # print(kwargs)
    values = {'company': 'Frappe Technologies Inc'}
    data = frappe.db.sql("""
        SELECT
            acc.account_number
            gl.debit
            gl.credit
        FROM `tabGL Entry` gl
            LEFT JOIN `tabAccount` acc
            ON gl.account = acc.name
        WHERE gl.company = %(company)s
    """, values=values, as_dict=0)
    print(os.getcwd())
    print("-------------WTTAPI Action1 End")

@frappe.whitelist(allow_guest=True)
def api1(*args, **kwargs):
    print("------------ wtt_api api 1")
    print(args)
    print("------------ api 11")
    print(kwargs)
    print("------------ api 1  -------- end")
    return "help me API"
