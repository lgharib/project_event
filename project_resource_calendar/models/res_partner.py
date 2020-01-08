# Copyright 2018 Savoir-faire Linux
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import fields, models


class Partner(models.Model):
    _inherit = "res.partner"

    allow_double_book = fields.Boolean(
        string='Allow Double Booking',
        help='Check if this employee '
             'can be booked as a participant in more than '
             'one meeting or event at the same '
             'time.',
        default=True,
    )
