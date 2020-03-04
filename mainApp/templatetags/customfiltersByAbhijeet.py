from django import template
register = template.Library()



@register.filter
def indexFilter(arr, i):
    return arr[i]

@register.filter
def addString(str1:str, str2:str):
    return str1 + str2