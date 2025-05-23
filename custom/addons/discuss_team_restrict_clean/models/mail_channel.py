from odoo import models, fields

class MailChannel(models.Model):
    _inherit = 'mail.channel'

    allowed_team_ids = fields.Many2many(
        'hr.department',
        string='접근 허용 팀',
        help='선택된 팀에 속한 사용자만 이 채널에 접근할 수 있습니다.'
    )
