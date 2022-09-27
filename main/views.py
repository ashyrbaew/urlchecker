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
    links = Urls.objects.filter(user=request.user).order_by("-id")

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
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def delete_url(request, pk):
    url_item = get_object_or_404(Urls, id=pk, user=request.user)
    url_item.delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def play_pause_check(request, pk):
    url_item = get_object_or_404(Urls, id=pk, user=request.user)
    if url_item.is_active:
        url_item.is_active = False
    else:
        url_item.is_active = True
    url_item.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def update_interval(request, pk):
    url = get_object_or_404(Urls, id=pk, user=request.user)
    url.update_interval = request.POST.get("interval")
    url.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

# import aiohttp
# import asyncio
#
# url_list = [
#     'https://google.com/',
#     'https://facebook.com/',
#     'https://stackoverflow.com/'
# ]
# result=[]
#
# async def main():
#     async with aiohttp.ClientSession() as session:
#         for i in url_list:
#             async with session.get(i) as response:
#                 result.append(response.status)
# loop = asyncio.get_event_loop()
# loop.run_until_complete(main())
