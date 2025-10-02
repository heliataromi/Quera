import json

from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.views.decorators.http import require_http_methods

from watchlist.models import WatchItem

def list_create_view(request):
    if request.method == 'GET':
        watchlist = WatchItem.objects.all().order_by('-created_at')
        context = {'items': watchlist}
        return render(request, 'list_create.html', context)

    elif request.method == 'POST':
        title = request.POST.get('title')
        item_type = request.POST.get('type')
        url = request.POST.get('url')
        poster = request.FILES.get('poster')

        if title and item_type:
            new_item = WatchItem(title=title, type=item_type, url=url)
            if poster:
                new_item.poster = poster
            new_item.save()

        watchlist = WatchItem.objects.all().order_by('-created_at')
        context = {
            'message': 'آیتم جدید با موفقیت اضافه شد!',
            'items': watchlist
        }

        return render(request, 'list_create.html', context)


def detail_view(request, pk):
    item = get_object_or_404(WatchItem, pk=pk)
    return render(request, 'detail_item.html', {'item': item })

def update_view(request, pk):
    item = get_object_or_404(WatchItem, pk=pk)
    context = {'item': item}
    return render(request, 'update_item.html', context)

@require_http_methods(['PUT', 'PATCH'])
def update_api_view(request, pk: int) -> JsonResponse:
    try:
        data = json.loads(request.body)
    except json.JSONDecodeError:
         response = {
            'message': 'فرمت JSON نامعتبر است!',
            'is_ok': False
         }
         return JsonResponse(response, status=400)

    item = get_object_or_404(WatchItem, pk=pk)

    title = data.get('title')
    item_type = data.get('type')
    url = data.get('url')
    is_watched = data.get('is_watched')

    if request.method == 'PUT':
        if title and item_type:
            item.title = title
            item.type = item_type
            item.url = url
            item.is_watched = is_watched
            item.save()

            response = {
              'message': "آیتم موردنظر با موفقیت به‌روزرسانی شد!",
              'is_ok': True
            }
            return JsonResponse(response, status=200)

        response = {
          'message': "امکان ذخیره آیتم بدون وارد کردن «عنوان» و «نوع» وجود ندارد.",
          'is_ok': False
        }
        return JsonResponse(response, status=400)

    if request.method == 'PATCH':
        if is_watched:
            item.is_watched = is_watched
            item.save()

            response = {
              'message': "وضعیت مشاهده با موفقیت به‌روزرسانی شد.",
              'is_ok': True
            }
            return JsonResponse(response, status=200)

        response = {
          'message': "درخواست نامعتبر است.",
          'is_ok': False
        }
        return JsonResponse(response, status=400)

def delete_view(request, pk):
    item = get_object_or_404(WatchItem, pk=pk)

    context = {'item': item}
    return render(request, 'delete_item.html', context)

@require_http_methods(['DELETE'])
def delete_api_view(request, pk: int) -> JsonResponse:
    try:
        item = WatchItem.objects.get(pk=pk)
        item.delete()

        response = {}
        return JsonResponse(response, status=204)
    except WatchItem.DoesNotExist:
        response = {
          "message": "آیتم موردنظر یافت نشد!"
        }
        return JsonResponse(response, status=404)
