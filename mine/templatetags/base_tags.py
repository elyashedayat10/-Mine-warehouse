from django import template
from ..models import Mine


register = template.Library()



@register.inclusion_tag("mine/nav.html")
def category_navbar():
	return {
		"madan_list": Mine.objects.all()
	}



