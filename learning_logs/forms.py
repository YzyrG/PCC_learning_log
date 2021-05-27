from django import forms

from .models import Topic, Entry

class TopicForm(forms.ModelForm):
	"""创建主题表单"""
	class Meta:
		"""创建主题表单以及包含字段"""
		model = Topic
		fields = ['text']
		labels = {'text': ''}

class EntryForm(forms.ModelForm):
	"""创建条目菜单"""
	class Meta:
		model = Entry
		fields = ['text']
		labels = {'text': ''}
		widgets = {'text': forms.Textarea(attrs={'cols': 80})}

