from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
# from django.views.generic.detail import DetailView

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect

from .models import Presentation, Slide
from .forms import PresentationForm, SlideForm


class PresentationCreate(CreateView):
    model = Presentation
    template_name = 'presentations/index.html'
    fields = ['title', 'description']

    def get_context_data(self):
        presentations = Presentation.objects.filter(author=self.request.user).order_by('date_creation')
        form = PresentationForm
        context = {'presentations': presentations,'form': form,}
        return context
    
    def form_valid(self, form):
        presentation = form.save(commit=False)
        presentation.author = self.request.user
        presentation.save()
        return HttpResponseRedirect(self.request.path_info)


class PresentationUpdate(UpdateView):
    form_class = PresentationForm
    template_name = 'presentations/update.html'
    success_url = reverse_lazy('presentation-new')

    def get_object(self):
        return get_object_or_404(Presentation, pk=self.kwargs.get(self.pk_url_kwarg))


class PresentationDelete(DeleteView):
    model = Presentation
    success_url = reverse_lazy('presentation-new')
    template_name = 'presentations/delete.html'


def presentation_view(request, pk):
    slides = Slide.objects.filter(presentation=pk)
    return render(request, 'presentations/view.html', {'slides': slides})

def slide_preview(request, pk):
    slide = Slide.objects.get(pk=pk)
    return render(request, 'presentations/preview.html', {'slide': slide})

class SlideCreate(CreateView):
    model = Slide
    template_name = 'presentations/create-slide.html'
    fields = ['content']

    def get_context_data(self, **kwargs):
        form = SlideForm
        presentation = get_object_or_404(Presentation, pk=self.kwargs.get(self.pk_url_kwarg))
        slides_list = Slide.objects.filter(presentation=self.kwargs.get(self.pk_url_kwarg))
        page = self.request.GET.get('page', 1)
        paginator = Paginator(slides_list, 1)

        try:
            slides = paginator.page(page)
        except PageNotAnInteger:
            slides = paginator.page(1)
        except EmptyPage:
            slides = paginator.page(paginator.num_pages)

        context = {'presentation': presentation, 'form': form, 'slides': slides,}
        return context


    def form_valid(self, form):
        slide = form.save(commit=False)
        presentation = get_object_or_404(Presentation, pk=self.kwargs.get(self.pk_url_kwarg))
        slide.presentation = presentation
        slide.save()
        return HttpResponseRedirect(self.request.path_info)


class SlideUpdate(UpdateView):
    form_class = SlideForm
    template_name = 'presentations/update-slide.html'

    def get_object(self):
        return get_object_or_404(Slide, pk=self.kwargs.get(self.pk_url_kwarg))
    
    def get_success_url(self):
        slide = get_object_or_404(Slide, pk=self.kwargs.get(self.pk_url_kwarg))
        self.success_url = reverse_lazy('slides-view', kwargs={'pk': slide.presentation.id})
        return str(self.success_url)


class SlideDelete(DeleteView):
    model = Slide
    success_url = reverse_lazy('presentation-new')
    template_name = 'presentations/delete-slide.html'

