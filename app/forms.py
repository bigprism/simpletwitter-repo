from django import forms

from .models import Post

from .models import Comment


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['content']

    def clean_content(self):
        content = self.cleaned_data['content']
        if len(content) > 255:
            raise forms.ValidationError("Content cannot be longer than 255 characters.")
        return content


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']

    def clean_content(self):
        content = self.cleaned_data['content']
        if len(content) > 255:
            raise forms.ValidationError("Comment cannot be longer than 255 characters.")
        return content