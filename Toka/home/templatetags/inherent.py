from django import template

register = template.Library()

def underbar_select(c):
    return c + "-underbar"
