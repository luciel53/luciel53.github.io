from django.shortcuts import render
from .models import annimal_post
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, DeleteView

class HomeView(ListView):
    model = annimal_post
    template_name = 'breed/home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']

class PostListView(ListView):
    model = annimal_post
    template_name = 'breed/ads.html'
    ordering = ['-date_posted']
    paginate_by = 12
    context_object_name = 'consult_post'

    def get_queryset(self):
        sexlist = self.request.GET.getlist('sex')
        racelist = self.request.GET.getlist('race')
        eyecolorlist = self.request.GET.getlist('eyecolor')
        bloodtypelist = self.request.GET.getlist('bloodtype')
        locationlist = self.request.GET.getlist('location')
        if sexlist == []:
            sexlist = [1,2]
        if racelist == []:
            racelist = list(range(1, 17))
        if eyecolorlist == []:
            eyecolorlist = list(range(1, 5))
            eyecolorlist.append('')
        if bloodtypelist == []:
            bloodtypelist = list(range(1, 4))
            bloodtypelist.append('')
        if locationlist == []:
            locationlist = list(range(1, 23))
        return annimal_post.objects.filter(sexe__in=sexlist, race__in=racelist,
                        bloodtype__in=bloodtypelist, localisation__in=locationlist,
                        eye_color__in=eyecolorlist)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class PostDetailView(DetailView):
    model = annimal_post

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = annimal_post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.user:
            return True
        return False

class PostCreateView(LoginRequiredMixin, CreateView):
    model = annimal_post
    fields = ['price', 'localisation', 'name', 'photo',
              'sexe', 'race', 'bloodtype', 'viral_disease_tests',
              'identification', 'eye_color', 'age',
              'fur_color', 'qualities', 'flaws', 'free_descriptive_text']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

def about(request):
    return render(request,'breed/about.html', {'title': 'About'})

def add_ad(request):
    new_post = annimal_post.objects.all()
    return render(request,
                'breed/add_ad.html',
                {'title': 'add_ad',
                 'new_post' : new_post})

def contact(request):
    return render(request,'breed/contact.html', {'title': 'contact'})

@login_required
def messaging(request):
    return render(request,'breed/messaging.html', {'title': 'messaging'})

