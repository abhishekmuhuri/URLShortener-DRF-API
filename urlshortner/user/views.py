from django.http import JsonResponse
from django.shortcuts import  render, redirect
from .forms import NewUserForm
from django.contrib.auth import login,authenticate,logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import redirect
from rest_framework.decorators import api_view
from django.contrib.auth.decorators import login_required


def register_request(request):
    # Check if the user is already authenticated, redirect if true
    if request.user.is_authenticated:
        return JsonResponse({'message':'User is already authenticated','user':request.user.username})

    # Process registration form when the request method is "POST"
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            # Save the new user, log them in, and redirect to the homepage
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful.")
            return redirect("webapp:homepage")
        else:
            # Display error message if the form is invalid
            messages.error(request, "Unsuccessful registration. Invalid information.")

    # Render the registration form when the request method is not "POST"
    form = NewUserForm()
    return render(
        request=request,
        template_name="register.html",
        context={"register_form": form, "form_errors": form.errors}
    )


def login_request(request):
    if request.user.is_authenticated:
        return JsonResponse({'message': 'User already logged in','user':request.user.username})

    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                print(f'LOGGED IN as {username}')
                messages.info(request, f"You are now logged in as {username}.")
                return JsonResponse({'success': True,'user':request.user.username})
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    else:
        form = AuthenticationForm()

    return render(request=request, template_name="login.html", context={"login_form": form})

@login_required(login_url='/user/login')
def logout_request(request):
    username = request.user.username
    logout(request)
    messages.info(request, "You have successfully logged out.")
    return JsonResponse({'success':'User logged out.','user':username})

def test(request):
    if request.user.is_authenticated:
        return JsonResponse({'message':f'{request.user.username} is authenticated'})
    else:
        return JsonResponse({'message':'User not authenticated'})
        