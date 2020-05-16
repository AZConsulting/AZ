from odoo import api, fields, models, _
from odoo.exceptions import UserError

class StockMove(models.Model):
    _inherit = "stock.move"

    @api.depends( 'sale_line_id')
    def get_product_description(self):
        for move in self:
            if move.sale_line_id:
                move.po_line_product_desc = move.sale_line_id.name

    po_line_product_desc = fields.Text(string="Description",
                                       compute="get_product_description")
