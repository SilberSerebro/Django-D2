from django_filters import FilterSet, ModelChoiceFilter,  DateFilter, CharFilter
from .models import *
from django.forms.widgets import DateInput

class PostFilter(FilterSet):
    category = ModelChoiceFilter(lookup_expr='exact',
                                 queryset=Category.objects.all()
                                 )

    class Meta:
        model = Post
        fields = ['category']

    date = DateFilter(field_name='dateCreation',
                        lookup_expr='gte',
                        label='Create after',
                        widget=DateInput(attrs={'type': 'date'}))
    date.field.error_messages = {'invalid': 'Enter date in format DD.MM.YYYY. Example: 31.12.2020'}
    date.field.widget.attrs = {'placeholder': 'DD.MM.YYYY'}


    class Meta:
        model = Post
        fields = {
            'title': ['icontains'],
        }




