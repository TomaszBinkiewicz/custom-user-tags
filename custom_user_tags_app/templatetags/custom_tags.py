from django import template

register = template.Library()


@register.simple_tag
def pg_13(user: object) -> str:
    if user.age > 13:
        return "allowed"
    return "blocked"


@register.simple_tag
def bizz_fuzz(user: object):
    if user.random_number % 15 == 0:
        return "BizzFuzz"
    elif user.random_number % 5 == 0:
        return "Fuzz"
    elif user.random_number % 3 == 0:
        return "Bizz"
    else:
        return user.random_number
