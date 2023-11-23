from frappe import _

def get_data():
    return [
        {
            "label": _("Library Management"),
            "icon": "octicon octicon-book",
            "items": [
                {
                    "type": "doctype",
                    "name": "Article",
                    "label": _("Article"),
                    "description": _("Manage Books"),
                    "onboard": 1,
                },
                {
                    "type": "doctype",
                    "name": "Library Member",
                    "label": _("Library Member"),
                    "description": _("Manage Members"),
                    # Not displayed on dropdown list action but on page after click on module
                    "onboard": 0,
                }
            ]
        }
    ]