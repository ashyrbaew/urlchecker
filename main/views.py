from .forms import UserRegistrationForm
from .models import Urls
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from django.core.paginator import Paginator


def register(request):
    form = UserRegistrationForm()
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
    else:
        form = UserRegistrationForm()

    context = {"form": form}
    return render(request, "main/register.html", context)


@login_required
def dashboard(request):
    if request.method == 'POST':
        lnk = request.POST.get("link")
        title = request.POST.get("title")
        new_url = Urls.objects.create(title=title, url=lnk, user=request.user)
        new_url.save()
        return redirect("dashboard")

    # retrieving current users links
    links = Urls.objects.filter(user=request.user, is_active=True).order_by("-id")

    # paginating 4 items per page
    paginator = Paginator(links, 4)
    # It's URL param for getting the current page number
    page_number = request.GET.get("page")
    # retrieving all the url items for that page
    page_obj = paginator.get_page(page_number)

    context = {"user_links": links, "page_obj": page_obj}
    return render(request, "main/crud.html", context)


def update_url(request, pk):
    url = get_object_or_404(Urls, id=pk, user=request.user)
    url.title = request.POST.get(f"title_{pk}")
    url.url = request.POST.get(f"url_{pk}")
    url.save()
    # return redirect("dashboard")
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def delete_url(request, pk):
    todo = get_object_or_404(Urls, id=pk, user=request.user)
    todo.delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def deactivate_url(request, pk):
    todo = get_object_or_404(Urls, id=pk, user=request.user)
    todo.is_active = False
    todo.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
