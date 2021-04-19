# -*- coding: utf-8 -*-

from odoo import models, api, fields, _


class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'

    total_box = fields.Integer(copy=False, compute='_compute_total_box', store=True)

    @api.depends('order_line')
    def _compute_total_box(self):
        boxes = 0
        for record in self.order_line.filtered(lambda ln: ln.subtotal_box):
            boxes += record.subtotal_box
        self.total_box = boxes


class PurchaseOrderLine(models.Model):
    _inherit = 'purchase.order.line'

    unit_box = fields.Integer(copy=False)
    subtotal_box = fields.Float(copy=False)
    has_wrong_boxes = fields.Boolean(copy=False)

    @api.onchange('product_id', 'product_qty', 'unit_box')
    def _onchange_unit_box(self):
        for record in self.filtered(lambda ln: ln.product_id.master_pack):
            master_pack = record.product_id.master_pack
            record.unit_box = master_pack
            if record.product_uom_qty < record.unit_box:
                record.subtotal_box = record.product_uom_qty / record.unit_box
            if record.product_uom_qty >= record.unit_box:
                record.subtotal_box = record.product_uom_qty / record.unit_box

    @api.onchange('subtotal_box')
    def _onchange_has_wrong_boxes(self):
        for record in self.filtered(lambda ln: ln.subtotal_box > 0.0):
            record.has_wrong_boxes = False
            if record.subtotal_box % 1 == 0:
                continue
            else:
                record.has_wrong_boxes = True

