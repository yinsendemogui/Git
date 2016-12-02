from django.shortcuts import render,redirect,HttpResponse
from blog.models import UserProfile,Question,Topic,Answer,Ticket
from blog.forms import LoginForm,RegisterForm,QuestionForm
from django.contrib.auth import authenticate,login
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist



# Create your views here.


def Login_Check(f):
	'''
	装饰器用于用户登录状态监控
	author：陈思齐
	:param func:对象
	:return:对象
	'''
	def inner(request,*args,**kwargs):
		# print (request.user.username)
		if request.user.is_authenticated():
			return  f(request,*args,**kwargs)
		else:
			return redirect(to='login')
		# return f(request)
	return inner



@Login_Check
def answer(request,tag = 'False',id = 'False'):
	'''
	回答页逻辑实现
	author：陈思齐
	:param request:
	:param tag:
	:param id:
	:return:
	'''
	context = {}

	if request.method == 'POST' :
		try:
			tag = request.POST['tagg']
		except:
			pass
		try:
			tag = request.POST['tag']
		except:
			pass
		try:
			id = request.POST['id']
		except:
			pass
		try:
			question_id = request.POST['detail']
			return redirect(to='detail',question_id=question_id)
		except:
			pass
	print(id)
	topic_list = Topic.objects.all()
	if len(topic_list) < 16:
		context['topic_list'] = topic_list
	elif tag == 'False':
		context['topic_list'] = topic_list[:16]
	else:
		context['topic_list'] = topic_list


	context['tag'] = tag

	if id == 'False':
		context['id'] = topic_list[0].id
		question_list = Question.objects.filter(answer_counts='0',topics = topic_list[0])
	else:
		context['id'] = int(id)
		topic_name = Topic.objects.get(id = int(id))
		question_list = Question.objects.filter(answer_counts='0', topics = topic_name)
	print(id)
	context['question_list'] = question_list
	print(question_list)
	return render(request, "answer.html", context)



@Login_Check
def detail(request, question_id):
	context = {}
	return render(request, "detail.html", context)



@Login_Check
def home(request):
	'''
	提问页逻辑实现
	author：陈思齐
	:param request:
	:return:

	home页逻辑实现
	author：徐毅
	:param request:
	:return:
	'''
	context = {}
	answer_list = Answer.objects.all()
	errors = ''
	if request.method == 'GET':
		form = QuestionForm
	if request.method == 'POST':
		form = QuestionForm(request.POST)
		# print (form.is_valid())
		if form.is_valid():
			title = form.cleaned_data['title']
			desc = form.cleaned_data['desc']
			topic = form.cleaned_data['topic']
			try:
				f_userprofile = UserProfile.objects.get(belong_to = request.user)
			except:
				raise ValidationError(u'UserProfile的用户资料没有找到！')
			f_topic = Topic(name = topic)
			f_topic.save()
			f_question = Question(title = title,desc = desc,author = f_userprofile)
			f_question.save()
			# if request.POST["referer"]:
			# 	return redirect(request.POST["referer"])
			# else:
			# 	return redirect(to='home')
			# print (f_question.id)
			return redirect(to='detail',question_id=f_question.id)


	if "HTTP_REFERER" in request.META:
		context["referer"] = request.META["HTTP_REFERER"]
	else:
		context["referer"] = ""
	context['form'] = form
	context['errors'] = errors
	context["answer_list"] = answer_list
	return render(request, "home.html", context)




def Login(request):
	'''
	用户登录界面逻辑实现
	author：陈思齐
	:param request:
	:return:
	'''
	context = {}
	errors = ''
	if request.method == "GET":
		form = LoginForm
	if request.method == "POST":
		form = LoginForm(request.POST)
		if form.is_valid():
			email = form.cleaned_data['email']
			password = form.cleaned_data['password']
			user = authenticate(username = email,password = password)
			if user and user.is_active:
				login(request,user)
				if request.POST["referer"] and 'register' not in request.POST["referer"] :
					return redirect(request.POST["referer"])
				else:
					return redirect(to='home')

	if "HTTP_REFERER" in request.META:
		context["referer"] = request.META["HTTP_REFERER"]
	else:
		context["referer"] = ""
	context['form'] = form
	context['errors'] = errors
	return render(request, "login.html", context)

@Login_Check
def profile(request):
	'''
	个人中心页逻辑实现
	author：C梦君（bbjoe）
	:param request:
	:return:
	'''
	context = {}
	# 如果用户登录了的话
	try:
		user_profile = UserProfile.objects.filter(belong_to=request.user)
		print(user_profile)

		# 获取登录的用户Use对应的UserProfile里的name
		user_name = user_profile.values("name").first()['name']  # 需要查询特定的某一个或几个属性时，这个时候可以用到values或values_list
		print(user_name)
		# 提出的问题
		question_list = Question.objects.filter(author__name__contains=user_name).order_by('-createtime')
		question_count = question_list.count()
		# 回答的问题
		answer_list = Answer.objects.filter(author__name__contains=user_name).order_by('-createtime')
		answer_count = answer_list.count()
		context['question_list'] = question_list
		context['question_count'] = question_count
		context['answer_list'] = answer_list
		context['answer_count'] = answer_count
		context['user_profile'] = user_profile
	except:
		raise ValidationError(u'当前登录用户的个人资料有错！请通知管理员！')
	return render(request, "profile.html", context)




def register(request):
	'''
	用户注册界面逻辑实现
	author：陈思齐
	:param request:
	:return:
	'''
	context = {}
	errors = ''
	if request.method == "GET":
		form = RegisterForm
	if request.method == "POST":
		form = RegisterForm(request.POST)
		if form.is_valid():
			name = form.cleaned_data['name']
			password = form.cleaned_data['password']
			email = form.cleaned_data['email']
			user = User.objects.create_user(username = email,password = password,email = email)
			if user:
				user.is_staff = True
				user.save()
				c = UserProfile(name=name, email=email, belong_to=user)
				c.save()
				login(request, user)
				print (request.POST["referer"])
				if request.POST["referer"] and 'login' not in request.POST["referer"] :
					return redirect(request.POST["referer"])
				else:
					return redirect(to='home')
	if "HTTP_REFERER" in request.META:
		context["referer"] = request.META["HTTP_REFERER"]
		print (context["referer"])
	else:
		context["referer"] = ""
	context['form'] = form
	context['errors'] = errors
	return render(request, "register.html", context)



@Login_Check
def search(request):
	context = {}
	return render(request, "search.html", context)


def vote(request,id):
	'''
	投票功能实现
	author：徐毅
	:param request:
	:param id:
	:return:
	'''
	if request.user.is_authenticated():
		voter_id = request.user.id
		try:
			user_ticket_for_this_answer = Ticket.objects.get(voter_id = voter_id,answer_tickets_id=id)
			user_ticket_for_this_answer.choice = request.POST["vote"]
			user_ticket_for_this_answer.save()
		except ObjectDoesNotExist:
			new_ticket = Ticket(voter_id = voter_id,answer_tickets_id = id, choice = request.POST['vote'])
			new_ticket.save()
		if request.POST["vote"] == "like":
			answer = Answer.objects.get(id=id)
			answer.like_counts += 1
			answer.save()
	return redirect(to="home")