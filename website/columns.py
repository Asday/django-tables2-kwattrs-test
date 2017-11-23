from django_tables2 import Column


class StatusColumn(Column):
    attrs = {'td': {'class': lambda value: f'status-{value}'}}
