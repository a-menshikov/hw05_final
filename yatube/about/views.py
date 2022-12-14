from django.views.generic.base import TemplateView


class AboutAuthorView(TemplateView):
    """Страница об авторе"""
    template_name = 'about/author.html'


class AboutTechView(TemplateView):
    """Страница стека технологий"""
    template_name = 'about/tech.html'
