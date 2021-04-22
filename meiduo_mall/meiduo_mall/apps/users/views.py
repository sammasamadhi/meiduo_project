from django.shortcuts import render
from django.views import View
# Create your views here.


class RegisterView(View):
    """注册用户"""
    def get(self, request):
        """提供用户注册页面"""
        return render(request, 'register.html')