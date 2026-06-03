# -*- coding: utf-8 -*-
"""
@File    : migrate_1673_to_1674.py
@Date    : 2025-12-22

cmd:
$ python domain_admin/migrate/migrate_1673_to_1674.py
"""
from __future__ import print_function, unicode_literals, absolute_import, division

from domain_admin.migrate import migrate_common
from domain_admin.model.base_model import db
from domain_admin.model.host_model import HostModel
from domain_admin.model.issue_certificate_model import IssueCertificateModel


def execute_migrate():
    """
    版本升级 v1.6.73 => v1.6.74
    :return:
    """

    migrator = migrate_common.get_migrator(db)

    migrate_rows = [
        # HostModel.dns_id
        migrator.add_column(
            table=HostModel._meta.table_name,
            column_name=HostModel.dns_id.name,
            field=HostModel.dns_id
        ),

        # IssueCertificateModel.renew_status
        migrator.add_column(
            table=IssueCertificateModel._meta.table_name,
            column_name=IssueCertificateModel.renew_status.name,
            field=IssueCertificateModel.renew_status
        ),

        # IssueCertificateModel.renew_message
        migrator.add_column(
            table=IssueCertificateModel._meta.table_name,
            column_name=IssueCertificateModel.renew_message.name,
            field=IssueCertificateModel.renew_message
        )
    ]

    migrate_common.try_execute_migrate(migrate_rows)
