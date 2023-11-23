// Copyright (c) 2023, Wangtao and contributors
// For license information, please see license.txt

frappe.ui.form.on('Library Member', {
	refresh: function(frm) {

		let page = frm.page
		let $btn = page.set_secondary_action('Refresh2b', () => refresh(), 'octicon octicon-sync')
		page.add_inner_button('New Post', () => new_post(), 'Make')

		let field = page.add_field({
			label: 'Status',
			fieldtype: 'Select',
			fieldname: 'status',
			options: [
				'Open',
				'Closed',
				'Cancelled'
			],
			change() {
				console.log(field.get_value());
			}
		});

		
		page.set_indicator('Pending', 'orange')
		frm.add_custom_button(__("Create Membership"), () => {
			frappe.utils.play_sound("error")
			console.log("sb1")
			let page = frm.page

			console.log(frm)
			console.log(page)
			// page.show()
		})

		frm.add_custom_button(__("Create Transaction"), () => {
			frappe.utils.play_sound("alert")
			console.log("sb15291")

			frappe.new_doc('Library Transaction', {
				library_member: frm.doc.name
			})
		})

		if (!frm.doc.description) {
			frm.set_intro('Please set the value of description\
			\n我们的祖国是花园', 'blue');
		}

	},

	trig_method(frm) {
		console.log("trig_method .wt", frm)
	}
});


frappe.ui.form.ControlLink.link_options = function(link) {
	return [
		{
			html: '<span class="text-primary link-option">'
				+ '<i class="fa fa-search" style="margin-right: 5px;"></i> '
				+ __("Custom Link Option")
				+ "</span>",
			label: __("Custom Link Option"),
			value: "custom__link_option",
			action: () => {
				console.log("sb15291")
				frappe.utils.play_sound("alert")

			}
		}
	];
};

// frappe.ui.form.make_control({
//     // parent: $wrapper.find('.my-control'),
//     df: {
//         label: 'Due Date',
//         fieldname: 'due_date',
//         fieldtype: 'Date'
//     },
//     render_input: true
// });