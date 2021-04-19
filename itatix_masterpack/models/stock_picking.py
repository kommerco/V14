# -*- coding: utf-8 -*-

from odoo import models, api, fields, _


class StockPicking(models.Model):
    _inherit = 'stock.picking'

    total_box = fields.Integer(copy=False, compute='_compute_total_box', store=True)

    @api.depends('move_line_ids_without_package.subtotal_box', 'move_ids_without_package.subtotal_box', 'state')
    def _compute_total_box(self):
        boxes = 0
        for record in self.move_ids_without_package.filtered(lambda ln: ln.subtotal_box):
            boxes += record.subtotal_box
        self.total_box = boxes


class StockMove(models.Model):
    _inherit = 'stock.move'

    unit_box = fields.Integer(copy=False, compute='_compute_boxes', store=True)
    subtotal_box = fields.Float(copy=False, compute='_compute_boxes', store=True)
    has_wrong_boxes = fields.Boolean(copy=False)

    @api.depends('product_id', 'product_uom_qty', 'reserved_availability')
    def _compute_boxes(self):
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
            if record.subtotal_box % 1 == 0:
                continue
            else:
                record.has_wrong_boxes = True


class StockMoveLine(models.Model):
    _inherit = 'stock.move.line'

    unit_box = fields.Integer(copy=False, compute='_compute_boxes', store=True)
    subtotal_box = fields.Float(copy=False, compute='_compute_boxes', store=True)
    has_wrong_boxes = fields.Boolean(copy=False)

    @api.depends('product_id', 'product_uom_qty', 'qty_done')
    def _compute_boxes(self):
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
