from django import template

register = template.Library()


@register.filter()
def check_text(text):
    """
    text:
    """
    text1 = f'{text[0]}'
    for i in text[1:]:
        if i.isupper():
            text1 = text1 + '*'
        else:
            text1 = text1 + i

    return f'{text1}'


@register.filter()
def check_head(head):
    """
    head:
    """
    head1 = f'{head[0]}'
    for i in head[1:]:
        if i.isupper():
            head1 = head1 + '*'
        else:
            head1 = head1 + i

    return f'{head1}'
