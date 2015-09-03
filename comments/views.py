from django.views.generic import View
from django.shortcuts import render, HttpResponseRedirect

from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

from .models import Comment
from .forms import AddCommentForm


class AddCommentView(View):
    comment_model = Comment
    comment_form_class = AddCommentForm
    template_name = 'base.html'

    @method_decorator(login_required)
    def post(self, request):

        comment_form = self.comment_form_class(request.POST, prefix='comment', auto_id=False)

        if comment_form.is_valid():

            comment = Comment()
            comment.message = comment_form.cleaned_data['message']

            comment.save()

            return HttpResponseRedirect('/thanks/')

        return render(request, self.template_name, comment_form)
