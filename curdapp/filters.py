import django_filters
from .models import Student
class StudentFilterSet(django_filters.FilterSet):
    class Meta:
        model = Student
        fields = {
            'name':['icontains'],
        }