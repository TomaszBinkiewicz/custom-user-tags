from django import template

register = template.Library()


@register.simple_tag
def pg_13(user: object) -> str:
    if user.age > 13:
        return "allowed"
    return "blocked"
