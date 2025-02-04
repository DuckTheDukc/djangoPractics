from django.views.generic import CreateView
from ..models import EntryPassword

from ..forms.entry_password_form import EntryPasswordForm

from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView, UpdateView, DeleteView,FormView
from passwordManager.forms.search_forms import SearchWebSiteForm
from passwordManager.views.mixins import MixinFormValidTemplate
class HomeView(ListView):
    template_name = 'home.html'
    model=EntryPassword
    context_object_name = 'websites'
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context['websites'] = EntryPassword.objects.all()
        return context
    
class WebSiteDataDetailView(DetailView):
    template_name="website_data_detail.html"
    model=EntryPassword
    context='website'
    
class WebSiteDataCreateView(MixinFormValidTemplate, CreateView):
    template_name="website_form_create.html"
    model=EntryPassword
    form_class=EntryPasswordForm
    success_url='/'
    def form_valid(self, form):
        response= super().form_valid(form)
        return render(self.request, "website_data_detail.html", context={'website': self.object})


class WebSiteDataUpdateView(UpdateView):
    template_name="website_form_update.html"
    model=EntryPassword
    form_class=EntryPasswordForm
    context_object_name='website'
    success_url='/'
    def form_valid(self, form):
        response= super().form_valid(form)
        return render(self.request, "website_data_detail.html", context={'website': self.object})
    
class WebsiteDataDeleteView(DeleteView):
    model=EntryPassword
    success_url='/'
    
class WebsiteSearchView(FormView):
    template_name="website_form_search.django"
    form_class = SearchWebSiteForm
    
    def form_valid(self, form):
        response = super().form_valid(form)
        website=response.get('website')
        
        EntryPassword.objects.get(website__contains=website)
        
        return render(self.request, 'website_data_detail.html', context={
            'website':self.object
        })