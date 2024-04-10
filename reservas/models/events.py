# -*- coding: utf-8 -*-
from odoo import fields, models, api


class EventEvent(models.Model):
    _name = "event.event"
    _inherit = "event.event"

    def _get_default_stage_id(self):
        return self.env['event.stage'].search([], limit=1)

    stage_id = fields.Many2one(
        'event.stage', ondelete='restrict', default=_get_default_stage_id,
        group_expand='_read_group_stage_ids', tracking=True, copy=False, 
        attrs="{'readonly': [('estado', '=', False)],'invisible': [('estado','=',False)]}")
    medio_pago = fields.Selection([('efectivo', 'Efectivo'), ('datafono', 'Datafono')])
    medio_transporte = fields.Selection([('bus', 'Bus'), ('avion', 'Avion')])
    estado = fields.Boolean('Reservado', default=False, compute="compute_estado")

    @api.depends('registration_ids')
    def compute_estado(self):
        self.estado = False
        for client in self.registration_ids:
            if client.state == 'open' or client.state == 'done':
                self.estado = True
