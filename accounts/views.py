from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse




# Create your views here.
class SignUpView(CreateView):
    from_class = UserCreationForm
    template_name = "registration/signup.html"
    success_url = reverse("login")