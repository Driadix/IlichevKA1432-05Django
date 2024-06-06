from django import template
from main.models import News

register = template.Library()

@register.inclusion_tag('main/news_item.html')
def render_news(news):
    return {'news': news}
