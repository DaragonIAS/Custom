# -*- coding: utf-8 -*-
from odoo import fields, models, api


class EventEvent(models.Model):
    _name = "atracciones"

    name = fields.Char("Nombre")
    disponibilidad = fields.Selection([('disponible', 'Disponible'), ('no disponible', 'No disponible')])