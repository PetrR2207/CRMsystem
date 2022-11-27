from django.shortcuts import render

def auth(request):
    return render(request, 'personal_account_admin/auth.html')