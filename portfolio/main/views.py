from django.shortcuts import render
from django.views.generic import View
from django.core.mail import send_mail
import os

class home(View):
    def get(self, request, *args, **kwargs):
        emailPass = os.getenv('belchiebenEmailpass')
        print(emailPass)
        return render(request, 'main/index.html')
    def post(self, request, *args, **kwargs):
        name = self.request.POST.get("name")
        email = self.request.POST.get("email")
        message = self.request.POST.get("message")
        send_mail(
            f'{name} has sent you a message!',
            f'{message} From {email}',
            email,
            ['belchieben112@gmail.com']
        )
        return render(request, 'main/index.html')
