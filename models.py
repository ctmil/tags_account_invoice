# -*- coding: utf-8 -*-
from openerp import models, api, fields, exceptions
from openerp.exceptions import ValidationError
from datetime import date

class account_invoice(models.Model):
	_inherit = "account.invoice"

	customer_tags = fields.Many2many(comodel_name='res.partner.category',relation='invoice_category',column1='partner_id',column2='invoice_id')

	@api.model
	def _update_customer_tags(self):
		invoices = self.search([('customer_tags','=',False)])
		for invoice in invoices:
			if invoice.partner_id.category_id:
				categ = []
				for category in invoice.partner_id.category_id:
					categ.append(category.id)
				vals = {
					'customer_tags': [(6,0,categ)]
					}
				invoice.write(vals)
		return None
