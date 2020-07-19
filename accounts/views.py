
# Create your views here.

from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from django .http import HttpResponse
from .forms import RegisterForm
from django.shortcuts import redirect

from django.contrib.auth import login
from django.http import HttpResponseRedirect

from django.views.generic.edit import CreateView
from django.urls import reverse
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from .models import CustomUser
 


def index(request):
    return render(request, 'accounts/index.html')


@login_required
def home(request):
    return render(request, 'accounts/home.html')




#def login(request):
 #   return render(request, 'registration/login.html')

def signup(request):
    return render(request, 'accounts/signup.html')


class SignUp(CreateView):
    model = CustomUser
    form_class = RegisterForm
    template_name = "accounts/signup.html" 
    
    def get_success_url(self):
        return reverse('index')

    def form_valid(self, form):
        user = form.save() # formの情報を保存
        login(self.request, user) # 認証
        self.object = user 
        return HttpResponseRedirect(self.get_success_url()) # リダイレクト