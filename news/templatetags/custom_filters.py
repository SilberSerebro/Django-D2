from django import template

register = template.Library()

black_list = ['редиска', 'кошка', 'собака']


# Регистрируем наш фильтр под именем currency, чтоб Django понимал,
# что это именно фильтр для шаблонов, а не простая функция.
@register.filter()
def censor(value):
    if not isinstance(value, str):
        raise ValueError
    for word in black_list:
        value = value.replace(word[1:], "*"*(len(word)-1))
    return value
# Возвращаемое функцией значение подставится в шаблон.
#value: значение, к которому нужно применить фильтр
