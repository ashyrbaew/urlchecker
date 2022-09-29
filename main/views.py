import aiohttp
import asyncio

from .forms import UserRegistrationForm
from .models import Urls
from .serializers import UrlsSerializer

from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import get_object_or_404, render, redirect
from django.core.paginator import Paginator

from celery import shared_task
from rest_framework import viewsets, mixins
from rest_framework.permissions import AllowAny


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


# In case of needed API
class UrlsViewSet(viewsets.GenericViewSet, mixins.ListModelMixin):
    permission_classes = [AllowAny]
    serializer_class = UrlsSerializer
    queryset = Urls.objects.all()


@login_required
def dashboard(request):
    per_page_item_count = 20
    if request.method == 'POST':
        lnk = request.POST.get("link")
        title = request.POST.get("title")
        new_url = Urls.objects.create(title=title, url=lnk, user=request.user)
        new_url.save()
        return redirect("dashboard")

    links = Urls.objects.filter(user=request.user).order_by("-id")
    paginator = Paginator(links, per_page_item_count)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    context = {"user_links": links, "page_obj": page_obj}
    return render(request, "main/crud.html", context)


@shared_task
def update_url_statuses_db(interval):
    url_items = Urls.objects.filter(update_interval=interval, is_active=True)

    async def check_url():
        async with aiohttp.ClientSession() as session:
            for item in url_items:
                async with session.get(item.url) as response:
                    item.status_code = response.status
    loop = asyncio.get_event_loop()
    loop.run_until_complete(check_url())
    Urls.objects.bulk_update(url_items, ['status_code'])

    return HttpResponse(status=204)


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
