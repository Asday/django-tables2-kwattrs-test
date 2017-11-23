from django.views.generic import TemplateView

from .models import Thing
from .tables import DemoTable


class TableView(TemplateView):
    template_name = 'table.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['demo_table'] = DemoTable([
            Thing(status='failed'),
            Thing(status='succeeded'),
            Thing(status='failed'),
        ])

        return context
