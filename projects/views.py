from django.views import generic
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.shortcuts import redirect, get_object_or_404
from .models import Project, Category, Review
from .forms import ReviewForm

class CategoryListView(generic.ListView):
    model = Category
    template_name = 'projects/category_list.html'
    context_object_name = 'categories'
    ordering = ['title']

class ProjectListView(generic.ListView):
    model = Project
    template_name = 'projects/project_list.html'
    context_object_name = 'projects'
    # paginate_by = 10  # Jei norite puslapiuoti

    def get_queryset(self):
        queryset = super().get_queryset()
        category_id = self.request.GET.get('category')
        if category_id:
            queryset = queryset.filter(category_id=category_id)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        context['selected_category'] = int(self.request.GET.get('category')) if self.request.GET.get('category') else None
        return context

class ProjectDetailView(generic.DetailView):
    model = Project
    template_name = 'projects/project_detail.html'
    context_object_name = 'project'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['related_projects'] = Project.objects.filter(category=self.object.category).exclude(id=self.object.id)[:5]
        context['previous_project'] = Project.objects.filter(id__lt=self.object.id).order_by('-id').first()
        context['next_project'] = Project.objects.filter(id__gt=self.object.id).order_by('id').first()
        context['reviews'] = Review.objects.filter(project=self.object)
        if self.request.user.is_authenticated:
            context['review_form'] = ReviewForm()
        return context

@method_decorator(login_required, name='dispatch')
class ReviewCreateView(generic.CreateView):
    model = Review
    form_class = ReviewForm

    def form_valid(self, form):
        project = get_object_or_404(Project, pk=self.kwargs['pk'])
        form.instance.user = self.request.user
        form.instance.project = project
        form.save()
        return redirect('projects:project_detail', pk=project.pk)

class AboutView(generic.TemplateView):
    template_name = 'projects/about.html'

class ContactView(generic.TemplateView):
    template_name = 'projects/contact.html'

    # def post(self, request, *args, **kwargs):
    #     form = ContactForm(request.POST)
    #     if form is_valid():
    #         # Formos apdorojimo logika
    #         form.save()
    #         return self.render_to_response(self.get_context_data(success=True))
    #     return self.render_to_response(self.get_context_data(form=form))
    #
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['form'] = ContactForm()
    #     return context
