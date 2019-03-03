from django.contrib.auth import login, authenticate
from django.views.generic import FormView


from .forms import LoginForm

class CreateViewLogin(FormView):
    form_class = LoginForm
    success_url = '/calendar'
    template_name = 'homepage/login.html'

    def form_valid(self, form):
        email = form.cleaned_data.get('email')
        password = form.cleaned_data.get('password')
        user = authenticate(request=self.request, email=email, password=password)

        if user:
            login(self.request, user)
            return super(CreateViewLogin, self).form_valid(form)

        return super(CreateViewLogin, self).form_invalid(form)