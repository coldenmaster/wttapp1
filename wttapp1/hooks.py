from . import __version__ as app_version
from frappe import _

app_name = "wttapp1"
app_title = "Wttapp1"
app_publisher = "Wangtao"
app_description = "Library Management System"
app_email = "15894368@qq.com"
app_license = "MIT"


test_string = "value"
test_list = ["value"]
test_dict = {
    "key": "value"
}

sounds = [
	{"name": "email", "src": "/assets/frappe/sounds/email.mp3", "volume": 0.8},
	{"name": "submit", "src": "/assets/frappe/sounds/submit.mp3", "volume": 0.8},
	{"name": "cancel", "src": "/assets/frappe/sounds/cancel.mp3", "volume": 0.8},
	{"name": "delete", "src": "/assets/frappe/sounds/delete.mp3", "volume": 0.75},
	{"name": "click", "src": "/assets/frappe/sounds/click.mp3", "volume": 0.75},
	{"name": "error", "src": "/assets/frappe/sounds/error.mp3", "volume": 0.8},
	{"name": "alert", "src": "/assets/frappe/sounds/alert.mp3", "volume": 0.9},
	# {"name": "chime", "src": "/assets/frappe/sounds/chime.mp3"},
]

standard_portal_menu_items = [
# portal_menu_items = [
	{"title": _("Projects2"), "route": "/article", "reference_doctype": "Article"},
	# {
	# 	"title": _("Request for Quotations"),
	# 	"route": "/rfq",
	# 	"reference_doctype": "Request for Quotation",
	# 	"role": "Supplier",
	# },
    {"title": _("Article"), "route": "/article", "reference_doctype": "Library Member"},

]

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/wttapp1/css/wttapp1.css"
# app_include_js = "/assets/wttapp1/js/wttapp1.js"

# include js, css files in header of web template
# web_include_css = "/assets/wttapp1/css/wttapp1.css"
# web_include_js = "/assets/wttapp1/js/wttapp1.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "wttapp1/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
#	"methods": "wttapp1.utils.jinja_methods",
#	"filters": "wttapp1.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "wttapp1.install.before_install"
# after_install = "wttapp1.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "wttapp1.uninstall.before_uninstall"
# after_uninstall = "wttapp1.uninstall.after_uninstall"

# Integration Setup
# ------------------
# To set up dependencies/integrations with other apps
# Name of the app being installed is passed as an argument

# before_app_install = "wttapp1.utils.before_app_install"
# after_app_install = "wttapp1.utils.after_app_install"

# Integration Cleanup
# -------------------
# To clean up dependencies/integrations with other apps
# Name of the app being uninstalled is passed as an argument

# before_app_uninstall = "wttapp1.utils.before_app_uninstall"
# after_app_uninstall = "wttapp1.utils.after_app_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "wttapp1.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
#	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
#	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
#	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
#	"*": {
#		"on_update": "method",
#		"on_cancel": "method",
#		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
#	"all": [
#		"wttapp1.tasks.all"
#	],
#	"daily": [
#		"wttapp1.tasks.daily"
#	],
#	"hourly": [
#		"wttapp1.tasks.hourly"
#	],
#	"weekly": [
#		"wttapp1.tasks.weekly"
#	],
#	"monthly": [
#		"wttapp1.tasks.monthly"
#	],
# }

# Testing
# -------

# before_tests = "wttapp1.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
#	"frappe.desk.doctype.event.event.get_events": "wttapp1.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
#	"Task": "wttapp1.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["wttapp1.utils.before_request"]
# after_request = ["wttapp1.utils.after_request"]

# Job Events
# ----------
# before_job = ["wttapp1.utils.before_job"]
# after_job = ["wttapp1.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
#	{
#		"doctype": "{doctype_1}",
#		"filter_by": "{filter_by}",
#		"redact_fields": ["{field_1}", "{field_2}"],
#		"partial": 1,
#	},
#	{
#		"doctype": "{doctype_2}",
#		"filter_by": "{filter_by}",
#		"partial": 1,
#	},
#	{
#		"doctype": "{doctype_3}",
#		"strict": False,
#	},
#	{
#		"doctype": "{doctype_4}"
#	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
#	"wttapp1.auth.validate"
# ]
