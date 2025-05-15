"""
friday_automations/filters.py
"""

from friday.filters import FridayFilterSet, django_filters
from friday_automations.models import MailAutomation


class AutomationFilter(FridayFilterSet):
    """
    AutomationFilter
    """

    search = django_filters.CharFilter(field_name="title", lookup_expr="icontains")

    class Meta:
        model = MailAutomation
        fields = "__all__"
