from django.shortcuts import render

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
