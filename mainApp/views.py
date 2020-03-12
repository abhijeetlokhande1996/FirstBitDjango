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
        "packageNamesArr":list(uiJsonData["packageDesc"].keys()),
        "packages":uiJsonData["packageDesc"],
        "allCoursesImageUrl": uiJsonData["allCoursesImageUrl"],
        "testomonial":uiJsonData["testomonial"],
        "emailId": uiJsonData["emailId"],
        "contactNumber": uiJsonData["contactNumber"],
        "idx" : 0 
    }
    
    return render(request, "index.html", context)
