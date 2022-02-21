from django import template
from ..models import Mine


register = template.Library()



@register.inclusion_tag("config/mine_footer_list.html")
def category_navbar():
	return {
		"mine_list": Mine.objects.all()
	}


