import re

from django import template
from django.utils.safestring import mark_safe

register = template.Library()


@register.filter
def highlight(text, query):
    if not query:
        return text
    query = query.strip()
    pattern = re.compile(re.escape(query), re.IGNORECASE)
    return mark_safe(pattern.sub(f"<mark>{query}</mark>", text))
