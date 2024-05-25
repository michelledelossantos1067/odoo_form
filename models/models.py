# -*- coding: utf-8 -*-

from odoo import models, fields, api

class MyModule(models.Model):
    _name = 'my_module.my_module'
    _description = 'Description of My Module'

    name = fields.Char(string="Name", required=True)
    value = fields.Integer(string="Value", required=True)
    description = fields.Text(string="Description")
    value2 = fields.Float(string="Value in Percentage", compute="_compute_value_percentage", store=True)

    @api.depends('value')
    def _compute_value_percentage(self):
        for record in self:
            record.value2 = record.value / 100
