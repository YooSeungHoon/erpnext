import frappe

def execute():
	for doctype, fieldname in (
		("Sales Order", "against_sales_order"),
		("Purchase Order", "against_purchase_order"),
		("Sales Invoice", "against_invoice"),
		("Purchase Invoice", "against_voucher"),
		("Journal Entry", "against_jv"),
		("Expense Claim", "against_expense_claim"),
	):
		frappe.db.sql("""update `tabJournal Entry Detail`
			set reference_type=%s and reference_name={0} where ifnull({0}, '') != ''
		""".format(fieldname), doctype)