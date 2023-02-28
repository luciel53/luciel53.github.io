from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import *
from django.views.generic import ListView, DetailView, CreateView, DeleteView

def register (request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}! Please login.')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})

@login_required
def profile (request):

    context = {
        'change' : False,
        'object' : request.user.profile,
    }

    return render(request, 'users/profile.html', context)

class ProfileDetailView(DetailView):
    model = Profile
    template_name = 'users/profile.html'

@login_required
def profile_change (request):
    if request.method == 'POST':
        u_form = UsernameUpdateForm(request.POST, instance=request.user)
        e_form = EmailUpdateForm(request.POST, instance=request.user)
        i_form = ImageUpdateForm(   request.POST, request.FILES,
                                    instance=request.user.profile)
        bd_form = BirthdateUpdateForm(  request.POST, request.FILES,
                                        instance=request.user.profile)
        b_form = BioUpdateForm( request.POST, request.FILES,
                                instance=request.user.profile)
        el_form = External_linkUpdateForm(  request.POST, request.FILES,
                                            instance=request.user.profile)
        fl_form = Facebook_linkUpdateForm(  request.POST, request.FILES,
                                            instance=request.user.profile)


        if (u_form.is_valid() and i_form.is_valid() and b_form.is_valid()
            and e_form.is_valid() and bd_form.is_valid() and el_form.is_valid()
            and fl_form.is_valid()):
            u_form.save()
            i_form.save()
            b_form.save()
            e_form.save()
            bd_form.save()
            el_form.save()
            fl_form.save()
            messages.success(request, f'Profil mis à jour')
            return redirect('profile')
    else:
        u_form = UsernameUpdateForm(instance=request.user)
        e_form = EmailUpdateForm(instance=request.user)
        i_form = ImageUpdateForm(instance=request.user.profile)
        bd_form = BirthdateUpdateForm(instance=request.user.profile)
        b_form = BioUpdateForm(instance=request.user.profile)
        el_form = External_linkUpdateForm(instance=request.user.profile)
        fl_form = Facebook_linkUpdateForm(instance=request.user.profile)


    context = {
        'u_form' : u_form,
        'i_form' : i_form,
        'b_form' : b_form,
        'e_form' : e_form,
        'bd_form' : bd_form,
        'el_form' : el_form,
        'fl_form' : fl_form,
        'change' : True,
    }

    return render(request, 'users/profile.html', context)

class MemberListView(ListView):
    model = Profile
    template_name = 'users/members.html'
    context_object_name = 'consult_post'
    paginate_by = 12

