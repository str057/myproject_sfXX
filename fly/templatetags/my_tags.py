# Правильный импорт Django-шаблонов
from django import template

# Создание объекта Library
register = template.Library()


@register.filter(name="media_filter")  # Рекомендуется явно указать имя фильтра
def media_filter(path):
    """
    Фильтр для формирования полного пути к медиафайлам
    """
    if path:
        return f"/media/{path}"
    return "#"
