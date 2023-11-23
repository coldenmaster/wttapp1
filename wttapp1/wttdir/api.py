import frappe

@frappe.whitelist(allow_guest=True)
def api1(**kwargs):
    print("------------ wttdir api.api1 1")
    print(kwargs)
    return "help me API"
    print("------------ api 1  -------- end")
