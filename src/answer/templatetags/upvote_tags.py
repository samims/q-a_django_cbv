from django import template

register = template.Library()


@register.filter()
def has_upvoted(user, answer):
    return user.id in answer.upvote_set.all().values_list("user", flat=True)
