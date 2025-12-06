from django import template

register = template.Library()

@register.filter
def currency(val):
    return f"${val}"

@register.filter
def discount(val,per):
    intVal= int(val)
    intPer = int(per)
    return intVal-(intVal*intPer/100)