from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json
from backend1.web_editables import Indexer_of_Food_Menu,HorizontalMenuList

# Create your views here.

@csrf_exempt
def lobby(request):
    if request.method == 'POST':
        index_ = json.loads(request.body)
        print(index_)
        return JsonResponse(Indexer_of_Food_Menu[index_], safe = False)
    elif request.method == 'GET':
        return  JsonResponse(HorizontalMenuList,safe = False)