from django.views.generic import TemplateView

# Create your views here.
class HomepageView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['my_statement'] = 'Nice to see you, This is the get context method from homepage views.'
        context['next_statement'] = 'Snowbarding lets go!'
        context['playing_around'] = 'Here is some stuff to play with. '
        return context

    def say_bye(self):
        return 'Goodbye!'
    
