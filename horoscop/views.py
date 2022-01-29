from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from django.urls import reverse
from django.template.loader import render_to_string

# Create your views here.


zodiac = {"aries": "Овен - первый знак зодиака, планета Марс (с 21 марта по 20 апреля)",
          "taurus": "Телец - второй знак зодиака, планета Венера (с 21 апреля по 21 мая) Вероника",
          "gemini": "Близнецы - третий знак зодиака, планета Меркурий (с 22 мая по 21 июня)",
          "cancer": "Рак - четвёртый знак зодиака, Луна (с 22 июня по 22 июля)",
          "leo": "Лев - пятый знак зодиака, солнце (с 23 июля по 21 августа)",
          "virgo": "Дева - шестой знак зодиака, планета Меркурий (с 22 августа по 23 сентября)",
          "libra": "Весы - седьмой знак зодиака, планета Венера (с 24 сентября по 23 октября)",
          "scorpio": "Скорпион - восьмой знак зодиака, планета Марс (с 24 октября по 22 ноября)",
          "sagittarius": "Стрелец - девятый знак зодиака, планета Юпитер (с 23 ноября по 22 декабря)",
          "capricorn": "Козерог - десятый знак зодиака, планета Сатурн (с 23 декабря по 20 января",
          "aquarius": "Водолей - одиннадцатый знак зодиака, планеты Уран и Сатурн (с 21 января по 19 февраля)",
          "pisces": "Рыбы - двенадцатый знак зодиака, планеты Юпитер (с 20 февраля по 20 марта)"
          }


def get_html(request):
    foo = render_to_string('horoscop/info.html')
    return HttpResponse(foo)


def index(request):
    z=list(zodiac)
    li_elements = ''
    for sign in zodiac:
        redirect_pa = reverse('horoscope-name', args=[sign])
        li_elements += f'<li><a href= "{redirect_pa}">{sign.title()}</a></li>'
        response = f"""
        <ol>
            {li_elements}
        </ol>
        """

    return HttpResponse(response)


def get_push_zodiac(request, a):
    description = zodiac.get(a, None)
    if description:
        return HttpResponse(description)
    else:
        return HttpResponseNotFound(f'Не известный знак задиака- {a}')


def get_push_zodiac_number(request, a):
    if a < 13 and a > 0:
        return HttpResponse(zodiac[((list(zodiac))[a - 1])])
    else:
        return HttpResponseNotFound(f'Не известный знак задиака- {a}')




