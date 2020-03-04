from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
# from mainApp.templates.templateTags.customfiltersByAbhijeet import indexFilter
import json





# Create your views here.
def index(request):
    uiJsonFilePath = settings.STATICFILES_DIRS[0]
    uiJsonDataInString = open(uiJsonFilePath+"/json/ui.json")
    uiJsonData = json.load(uiJsonDataInString)
    context = {
        "uiJsonData": uiJsonData,
        "idx" : 0 
    }
    return render(request, "index.html", context)
