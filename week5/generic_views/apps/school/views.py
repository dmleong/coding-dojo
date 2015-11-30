from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from apps.school.models import Student, Teacher, Subject


class Subjects(TemplateView):
    template_name = 'school/index.html'

    def get_context_data(self, **kwargs):
        subjects = Subject.objects.all()
        return {'subjects': subjects}


class SubjectsDetailView(DetailView):
    model = Subject
    template_name = 'school/show.html'

    def get_context_data(self, **kwargs):
        context = super(SubjectsDetailView, self).get_context_data(**kwargs)
        return context


class TeachersDetailView(DetailView):
    model = Teacher
    template_name = 'school/show.html'

    def get_context_data(self, **kwargs):
        teacher = super(TeachersDetailView, self).get_context_data(**kwargs)
        courses = Subject.objects.filter(teacher=teacher['teacher'].id)
        context = {
            'teacher_info': teacher,
            'course_list': courses,
        }
        return context


class TeachersListView(ListView):
    model = Teacher
    template_name = 'school/index.html'

    def get_context_data(self, **kwargs):
        context = super(TeachersListView, self).get_context_data(**kwargs)
        return context


class StudentsDetailView(DetailView):
    model = Student
    template_name = 'school/show.html'

    def get_context_data(self, **kwargs):
        student = super(StudentsDetailView, self).get_context_data(**kwargs)
        courses = Subject.objects.filter(student=student['student'].id)
        context = {
            'student_info': student,
            'course_list': courses,
        }
        return context


class StudentsListView(ListView):
    model = Student
    template_name = 'school/index.html'

    def get_context_data(self, **kwargs):
        context = super(StudentsListView, self).get_context_data(**kwargs)
        return context
