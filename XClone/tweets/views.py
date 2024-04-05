from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Tweet

def home_view(request, *args, **kwargs):
    print(args, kwargs)
    return HttpResponse("<h1>Hello World</h1>")


def tweet_detail_view(request, tweet_id, *args, **kwargs):
    data = {
        "id": tweet_id,
        "content": ""
    }
    
    status= 200
    try:
        obj = Tweet.objects.get(id=tweet_id)
        data['content'] = obj.content
    except:
        data['message'] = "Not found"
        status = 404
    
    return JsonResponse(data, status=status)
