from odoo.upgrade import util
import logging
_logger = logging.getLogger(__name__)
def migrate(cr, version):
    _logger.info("Installing post-migration for account_ux")
    env = util.env(cr)

    rule = env.ref(
        "account.journal_comp_rule",
        raise_if_not_found=False
    )

    if not rule:
        return

    new_domain = """[
        '|',
        ('company_id', 'in', company_ids),
        '&',
        ('company_id', 'parent_of', company_ids),
        ('shared_to_branches', '=', True)
    ]"""

    rule.write({
        "domain_force": new_domain,
    })