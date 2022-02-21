from django import template
from blog.models import Blog


register = template.Library()



@register.inclusion_tag("blog/blog_footer_list.html")
def blog_list():
	return {
		"blog_list": Blog.objects.all()[:2]
	}
