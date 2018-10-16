# Copyright 2018, Jarsa Sistemas, S.A. de C.V.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import fields, models


class ResCurrency(models.Model):
    _inherit = 'res.currency'

    rate = fields.Float(
        digits=(10, 10))
