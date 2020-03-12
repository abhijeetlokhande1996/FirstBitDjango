from django import template
register = template.Library()



@register.filter
def indexFilter(arr, i):
    return arr[i]

@register.filter
def addString(str1:str, str2:str):
    return str1 + str2

@register.filter
def testFilter(packageDict, key: str):
    return packageDict[key]

@register.filter
def calculateFees(packageDict, key: str):
    #print(packageDict[key])
    totalHours = 0
    for item in packageDict[key]:
        totalHours = totalHours + int(item["hours"])
    return totalHours