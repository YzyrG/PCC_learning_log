from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Topic(models.Model):
	"""用户学习的主题"""
	text = models.CharField(max_length=200)
	# 在每个主题旁放置时间戳
	date_added = models.DateTimeField(auto_now_add=True)
	# ower建立到模型User的外键关系
	owner = models.ForeignKey(User, on_delete=models.CASCADE)
	def __str__(self):
		"""返回模型的字符串表示"""
		return self.text

class Entry(models.Model):
	"""有关某个主题的具体知识"""
	# 与主题关联
	topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
	text = models.TextField()
	date_added = models.DateTimeField(auto_now_add=True)

	class Meta:
		"""
		需要时使用entries表示多个条目
		没有此类，django用Entrys表示多个条目
		"""
		verbose_name_plural = 'entries'

	def __str__(self):
		"""呈现条目时显示的信息"""
		# 显示前50个字符
		if len(self.text) > 50:
			return f"{self.text[:50]}..."
		else:
			return self.text


