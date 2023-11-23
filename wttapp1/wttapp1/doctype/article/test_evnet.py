import frappe
import unittest

def create_events():
    if frappe.flags.test_events_created:
        return
    
    frappe.set_user("Administrator")
    doc = frappe.get_doc({
        "doctype": "Event",
        "subject": "_Test Event 1",
        "starts_on": "2014-01-01",
        "event_type": "Public"
    }).insert()

    doc = frappe.get_doc({
        "doctype": "Event",
        "subject":"_Test Event 3",
        "starts_on": "2014-01-01",
        "event_type": "Public",
        "event_individuals": [{
            "person": "test1@example.com"
        }]
    }).insert()

    frappe.flages.test_events_created = True

class TestEvent(unittest.TestCase):
    def setUp(self):
        create_events()
    
    def tearDown(self):
        frappe.set_user("Administrator")
    
    def test_allowed_public(self):
        frappe.set_user("test1@example.com")
        doc = frappe.get_doc("Event", frappe.db.get_value("Event",
            {"subject": "_Test Event 1"}))
        self.assertTrue(frappe.has_permission("Event", doc = doc))

    def test_not_allowed_private(self):
        frappe.set_user("test1@example.com")
        doc = frappe.get("Event", frappe.db.get_value("Event",
            {"subject":"_Test Event 2"}))
        self.assertFalse(frappe.has_permission("Event", doc = doc))
        

