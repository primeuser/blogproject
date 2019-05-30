import operator
# from django.shortcuts import render
from django.views.generic import *
from .models import *
# from django.http import HttpResponse
from django.shortcuts import render
# Create your views here.
from .forms import StudentForm, PostForm, BookForm
from django.db.models import Q


class HomeView(TemplateView):
    template_name = 'home.html'


class ContactView(TemplateView):
    template_name = 'contact.html'


class BaseView(TemplateView):
    template_name = 'base1.html'


class AboutView(TemplateView):
    template_name = 'about.html'


class LoginView(TemplateView):
    template_name = 'login.html'


class RegisterView(TemplateView):
    template_name = 'register.html'


class LocationView(TemplateView):
    template_name = 'location.html'


class TestView(TemplateView):
    template_name = 'test.html'


class StudentListView(ListView):
    template_name = 'studentlist.html'
    queryset = Student.objects.all().order_by('-id')
    context_object_name = "studentlist"


class StudentDetailView(DetailView):
    template_name = 'studentdetail.html'
    model = Student
    context_object_name = "studentdetail"


class StudentCreateView(CreateView):
    template_name = "studentcreate.html"
    form_class = StudentForm
    success_url = "/"


class StudentUpdateView(UpdateView):
    template_name = "studentcreate.html"
    form_class = StudentForm
    model = Student
    success_url = "/"


class StudentDeleteView(DeleteView):
    template_name = "studentdelete.html"
    model = Student
    success_url = "/student/list"


class BookListView(ListView):
    template_name = "booklist.html"
    model = Book
    context_object_name = "booklist"


class BookDetailView(DetailView):
    template_name = "bookdetail.html"
    model = Book
    context_object_name = "bookdetail"


class BookCreateView(CreateView):
    template_name = "bookcreate.html"
    form_class = BookForm
    success_url = "/"


class BookUpdateView(UpdateView):
    template_name = "bookcreate.html"
    form_class = BookForm
    model = Book
    success_url = "/"


class BookDeleteView(DeleteView):
    template_name = "studentdelete.html"
    model = Book
    success_url = "/book/list"


class BlogListView(ListView):
    template_name = 'bloglist.html'
    queryset = Post.objects.all().order_by('-id')
    context_object_name = "bloglist"


class BlogDetailView(DetailView):
    template_name = 'blogdetail.html'
    model = Post
    context_object_name = "blogdetail"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['bloglist'] = Post.objects.all()
        return context


class BlogCreateView(CreateView):
    template_name = "blogcreate.html"
    form_class = PostForm
    success_url = "/"


class BlogUpdateView(UpdateView):
    template_name = "blogcreate.html"
    form_class = PostForm
    model = Post
    success_url = "/"


class BlogDeleteView(DeleteView):
    template_name = "blogdelete.html"
    model = Post
    success_url = "/blog/list"


class SearchResultView(TemplateView):
    template_name = 'searchresult.html'
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        query = self.request.GET.get('q')  # to GET is used to get data
        print(query, ":::::::::::::")
        if query:
            # parameter for filter done using lookup
            lookup = Q(name__icontains=query)
            # gives data that are defined by lookup
            slists = Student.objects.filter(lookup)
            context["slists"] = slists
        return context

    # def get_queryset(self):
    # 	result = super(SearchListView, self).get_queryset()

    # 	query = self.request.GET.get('q')
        # if query:
        # 	query_list = query.split()
        # 	result = result.filter(
        # 		reduce (operator . and_,
        # 			(Q(title__icontains=q) for q in query_list)) |
        # 		reduce (operator . and_,
        # 			(Q(description__icontains=q) for q in query_list))
        # 		)
        # 	return result


# def home_page(request):
# 	return render(request,"home_page.html", {})


# def home_page(request):
#  	html_code = """
# ..................
# ..................
#  	"""
# 	return HttpResponse(html_code)
