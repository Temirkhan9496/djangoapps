from django.contrib.auth.decorators import login_required
from django.shortcuts import render

@login_required
def admin_only_page(request):
    return render(request, 'page3.html')