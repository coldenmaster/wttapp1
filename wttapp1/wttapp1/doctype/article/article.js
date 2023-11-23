// Copyright (c) 2023, Wangtao and contributors
// For license information, please see license.txt

frappe.ui.form.on('Article', {
	refresh: function(frm) {
		frm.add_custom_button(__("test info"), 
			() => {
				console.log(__("test info"));
				// frappe.new_doc('Library Membership', {
				// 	library_member: frm.doc.name
				// })
				console.log(frm)
				frappe.msgprint(__('test info'))
				frappe.msgprint(frm.doc.name)
				frappe.msgprint('1,2,3')
			},
			__("Utilities")
		)
	}

});

// frappe.ui.form.ControlLink.link_option = function(link) {
// 	return [
// 		{
// 			html: '<span class="text-primary link-option">'
// 			+ '<i class="fa fa-search" style="margin-right: 5px;"></i>'
// 			+ __("Custom Link Option")
// 			+ "</span>",
// 			label: __("Custom Link Option w"),
// 			value: "custom__link_option",
// 			action: () => {console.log("sb1593")}
// 		}
// 	];
// };
