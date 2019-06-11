from django.shortcuts import render, render_to_response
from django.urls import reverse_lazy
from django.views import generic
from .models import Student
from .filters import StudentFilterSet
from .filters import StudentFilterSet
# Create your views here.


class StudentList(generic.ListView):
    model = Student
    template_name = 'student_list.html'
    def get_context_data(self,  **kwargs):
        context=super().get_context_data(**kwargs)
        context['filter']=StudentFilterSet(self.request.GET,queryset=self.get_queryset())
        return  context



class StudentView(generic.DetailView):
    model = Student
    template_name = 'student_details.html'

class StudentCreate(generic.CreateView):
    model = Student
    fields = ['id', 'name','roll_number','age','gender']
    template_name = 'student_form.html'

    success_url = reverse_lazy('student_list')

class StudentUpdate(generic.UpdateView):
    model = Student
    fields = ['name', 'roll_number','age','gender']
    template_name = 'student_edit.html'
    success_url = reverse_lazy('student_list')

class StudentDelete(generic.DeleteView):
    model = Student
    success_url = reverse_lazy('student_list')
    template_name = 'student_confirm_delete.html'
