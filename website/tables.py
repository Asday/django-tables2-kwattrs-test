from django_tables2 import Table

from .columns import StatusColumn


class DemoTable(Table):
    status = StatusColumn()
