from django.http import JsonResponse
from django.http.multipartparser import MultiPartParser
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods

from musify.models import Music, Singer


def serialize_music(music):
    return {
        "id": music.id,
        "title": music.title,
        "singer": {
            "id": music.singer.id,
            "name": music.singer.name,
        },
        "description": music.description,
        "year": int(music.year) if music.year else None,
        "file": music.file.url if music.file else None
    }

@csrf_exempt
@require_http_methods(["GET", "POST"])
def list_create_view(request):
    if request.method == "GET":
        musics = Music.objects.all()

        title = request.GET.get("title")
        singer = request.GET.get("singer")
        year = request.GET.get("year")

        if title:
            musics = musics.filter(title__icontains=title)
        if singer:
            musics = musics.filter(singer__name__icontains=singer)
        if year:
            musics = musics.filter(year=year)

        context = [serialize_music(music) for music in musics]
        return JsonResponse(context, safe=False, status=200)

    if request.method == "POST":
        text_data, file_data = MultiPartParser(
            request.META, request, request.upload_handlers
        ).parse()

        print(text_data)

        title = text_data.get("title")
        description = text_data.get("description")
        year = text_data.get("year")
        singer_name = text_data.get("singer")
        file = file_data.get("music_file")

        if not title or not singer_name or not year:
            return JsonResponse({"error": "Missing required fields."}, status=400)

        singer, _ = Singer.objects.get_or_create(name=singer_name.title())
        music = Music.objects.create(
            title=title,
            singer=singer,
            description=description,
            year=year,
            file=file,
        )

        context = serialize_music(music)
        return JsonResponse(context, status=201)

@csrf_exempt
@require_http_methods(["GET", "PATCH", "PUT", "DELETE"])
def retrieve_update_delete_view(request, pk):
    try:
        music = Music.objects.get(pk=pk)
    except Music.DoesNotExist:
        return JsonResponse({"error": "Music not found."}, status=404)

    if request.method == "GET":
        context = serialize_music(music)
        return JsonResponse(context, status=200)

    if request.method == "PUT":
        text_data, file_data = MultiPartParser(request.META, request, request.upload_handlers).parse()

        title = text_data.get("title")
        singer_name = text_data.get("singer")
        year = text_data.get("year")
        description = text_data.get("description")

        if not title or not singer_name or not year:
            return JsonResponse({"error": "Missing required fields."}, status=400)

        singer, _ = Singer.objects.get_or_create(name=singer_name.title())

        music.title = title
        music.singer = singer
        music.description = description
        music.year = year

        if file := file_data.get("music_file"):
            music.file = file
        else:
            music.file = None

        music.save()

        context = {
            "message": "Music updated successfully.",
            "music": serialize_music(music)
        }
        return JsonResponse(context)

    if request.method == "PATCH":
        text_data, file_data = MultiPartParser(request.META, request, request.upload_handlers).parse()

        title = text_data.get("title", music.title)
        singer_name = text_data.get("singer")
        year = text_data.get("year", music.year)
        description = text_data.get("description", music.description)

        if singer_name:
            singer, _ = Singer.objects.get_or_create(name=singer_name.title())
        else:
            singer = music.singer

        music.title = title
        music.singer = singer
        music.description = description
        music.year = year

        if file := file_data.get("music_file"):
            music.file = file

        music.save()

        context = {
            "message": "Music updated successfully.",
            "music": serialize_music(music)
        }
        return JsonResponse(context)

    if request.method == "DELETE":
        music.delete()

        return JsonResponse({}, status=204)
