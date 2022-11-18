from django import template


register = template.Library()


# Регистрируем наш фильтр под именем currency, чтоб Django понимал,
# что это именно фильтр для шаблонов, а не простая функция.

CUR_SUMBOLS = {
    'rub': '₽',
    'usd': '$',
    'eur': '€',
}

curse_words = ['dolor', 'Lorem', 'редиска', '"редиска"']

@register.filter()
def censor(text):
    text = text.split(" ")
    for i, word in enumerate(text):
        if word in curse_words:
            text[i] = f"{text[i][:1]}{'*'*(len(word)-1)}"
    
    return " ".join(text)

# @register.filter()
# def censor(text):
#     text = text.split("")
#     if curse_words in text:
