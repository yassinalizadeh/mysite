from django import forms
from blog.models import Post, Comment


class PostForm(forms.ModelForm):
    # todo meta chie
    class Meta:
        model = Post
        fields = ('author', 'title', 'text')

        widgets = {
            # todo textinputclass va postcontent chie
            'title': forms.TextInput(attrs={'class': 'textinputclass'}),
            'text': forms.Textarea(attrs={'class': 'editable medium-editor-textarea postcontent'}),
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('author', 'text')

        widgets = {
            # todo textinputclass va postcontent chie
            'author': forms.TextInput(attrs={'class': 'textinputclass'}),
            'text': forms.Textarea(attrs={'class': 'editable medium-editor-textarea'}),
        }



