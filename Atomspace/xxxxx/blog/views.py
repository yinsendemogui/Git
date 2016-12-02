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
	def inner(request):
		print (request.user.username)
		if request.user.is_authenticated():
			f(request)
		else:
			return redirect(to='login')
		return f(request)
	return inner



@Login_Check
def answer(request):
	context = {}
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
	'''
	context = {}
	answer_list = Answer.objects.all()
	errors = ''


	if request.method == 'GET':
		form = QuestionForm
	if request.method == 'POST':
		form = QuestionForm(request.POST)
		print (form.is_valid())
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
			return redirect(to='home')



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
	context = {}
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
				# print (request.POST["referer"])
				if request.POST["referer"] and 'login' not in request.POST["referer"] :
					return redirect(request.POST["referer"])
				else:
					return redirect(to='home')
	if "HTTP_REFERER" in request.META:
		context["referer"] = request.META["HTTP_REFERER"]
		# print (context["referer"])
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
