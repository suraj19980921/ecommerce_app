from django import template
import operator as op

register = template.Library()

@register.filter()
def catfilter(value,key):
   data = value
   key_list = []
   i=0
   j=0
   for element in data:
    if data[i].category == element.category:
            print(data[i].category)
            if j <= 4:
             key_list.append(element)
             j += 1
            
        
   return key_list