from django.shortcuts import redirect, render
from django.views.generic import TemplateView, FormView, DetailView
from .models import Log, Collaborator
from .forms import CreateLogForm, ShareForm
from users.models import User

# Create your views here.
class LogListView(FormView, TemplateView):
    model = Log
    template_name = "journal/log_list.html"
    form_class = CreateLogForm
    
    def get_context_data(self, **kwargs):
        context = super(LogListView, self).get_context_data(**kwargs)

        logs = Log.objects.filter(user = self.request.user)
        context['logs'] = logs

        if 'create_log_form' not in context:
            context['create_log_form'] = CreateLogForm()

        if 'share_form' not in context:
            context['share_form'] = ShareForm()

        return context

    def post(self, request, *args, **kwargs):

        context = {}

        if 'create_log' in request.POST:
            create_log_form = CreateLogForm(request.POST)

            if create_log_form.is_valid():
                create_log_form.save(self.request.user)
            
            else:
                context['create_log_form'] = create_log_form
        
        if 'share_journal' in request.POST:
            share_form = ShareForm(request.POST)
            
            if share_form.is_valid():
                share_form.save(self.request.user)
            else:
                context['share_form'] = share_form

        return render(request, self.template_name, self.get_context_data(**context))
    
class ShareJournalView(DetailView):
    model = User
    template_name = "journal/shared_journal.html"

    def get_context_data(self, **kwargs):
        context = super(ShareJournalView, self).get_context_data(**kwargs)
        shared = Collaborator.objects.filter(doctor = self.request.user)
        journals = []
        mother = User.objects.filter(pk=self.kwargs['pk']).first()
        logs = Log.objects.filter(user =mother)
        for i in shared:
            journal = Log.objects.filter(user = i.mother)
            journals.append(journal)
        context['journals'] = journals
        context['shared'] = shared
        context['logs'] = logs
        return context
        

def redirectToJournalView(request):
    shared = Collaborator.objects.filter(doctor = request.user).first()
    return redirect('journal:shared_journal', pk=shared.mother.pk)