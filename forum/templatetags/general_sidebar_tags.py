from django import template
from forum.models import Tag, Award
from forum import settings

from extra_filters import static_content

register = template.Library()

@register.inclusion_tag('sidebar/markdown_help.html')
def markdown_help():
    return {}

@register.inclusion_tag('sidebar/recent_awards.html')
def recent_awards():
    return {'awards': Award.objects.order_by('-awarded_at')[:settings.RECENT_AWARD_SIZE]}

@register.inclusion_tag('sidebar/sidebar.html')
def sidebar_upper(user=None):
    return {
        'show': settings.SIDEBAR_UPPER_SHOW,
        'content': static_content(settings.SIDEBAR_UPPER_TEXT, settings.SIDEBAR_UPPER_RENDER_MODE),
        'wrap': not settings.SIDEBAR_UPPER_DONT_WRAP,
        'blockid': 'sidebar-upper',
        'view_user': user
    }

#@register.inclusion_tag('sidebar/recent_tags.html')
#def recent_tags():
   #return {'tags': Tag.active.order_by('-id')[:settings.RECENT_TAGS_SIZE]}

