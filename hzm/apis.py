from django.http import JsonResponse, HttpResponse, FileResponse, HttpResponseRedirect
from django.urls import reverse
from hzm.models import *
import requests
import json
import os
from django.utils import timezone
from django.shortcuts import render,redirect
from django.views.decorators.csrf import csrf_exempt
from django.contrib import auth
from django.contrib.auth.models import User
from django.core.files.storage import default_storage #파일 저장 경로
from django.conf import settings
from django.db.models import Q
from .serializers import *
import time
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage

master_passwd = "ssdsmh"
club_passwd ="hzm"

def id_check_btn (request) :
	player_name = request.GET.get('player_name')
	print("id_check_btn")
	print(player_name)
	try :
		check_id = Player.objects.get(player_name=player_name)
		print(check_id)
		if check_id is not None :
			return HttpResponse("fail")
		else :
			return HttpResponse("good") 

	except Exception as e :
		return HttpResponse("good")


def id_check (request) :
	player_name = request.GET.get('player_id')

	try :
		check_id = Player.objects.get(player_name=player_name)
		return HttpResponse("fail")
	except Exception as e :
		return HttpResponse("good")

def edit_mypage_info(request) :
	pk = request.session.get('pk')
	name=request.POST.get('player_name')
	password_now=request.POST.get('password_now')
	password_change=request.POST.get('password_change')

	club_name=request.POST.get('club_name')

	if Player.objects.filter(player_name=name).exclude(pk=pk) :
		return HttpResponse("sameId")

	try:
		player=Player.objects.get(pk=pk)
		print(player)
		print(password_now)
		print(player.passwd)
		if player.passwd == password_now :
			print("sss")
			player.player_name = name
			player.passwd = password_change
			player.club_name=club_name
			player.save()
			request.session['player_name'] = name
			print("Ddddd")	
			return HttpResponse("good")
		else :
			return HttpResponse("passwordfail")
	except Exception as e :
		return HttpResponse("fail")

def sign_in(request) :
	player_name = request.POST.get('player_name')
	player_passwd = request.POST.get('player_passwd')
	try :
		if request.method == 'POST' :
			print('POST')
			print(player_name)
			print(player_passwd)

			player = Player.objects.get(Q(player_name=player_name) & Q(passwd=player_passwd))
			data = {}
			print(player.pk)
			if player is not None:
				print('login')
				#data['pk'] = player_pk
				request.session['pk'] = player.pk
				request.session['player_name'] = player.player_name
				return redirect('/')
			else :
				print('NONE')
				return HttpResponse('login_fail1')
		else :
			return HttpResponse('login_fail2')
	except Exception as e :
		return HttpResponse("login_fail3")


def sign_up(request) :
	player_name = request.POST.get('player_id')
	player_passwd = request.POST.get('player_passwd')
	club_name = request.POST.get('player_club')
	try :
		if request.method == 'POST' :
			print('POST')
			print(player_id)
			print(player_passwd)

			player = Player(player_name=player_name, passwd=player_passwd, club_name=club_name)
			player.save()

			player = Player.objects.get(player_name=player_name)
			request.session['pk'] = player.pk
			request.session['player_name'] = player.player_name

			if player is not None:
				print('create id')
				return redirect('/')
			else:
				print('NONE')
				return HttpResponse('아이디 생성실패1')
		else :
			return HttpResponse('good')
	except Exception as e : 
		print(e)
		print('create id error')
		return HttpResponse(e)

def logout(request) :
	request.session.clear()
	return redirect('/')


def add_fmatch(request) :
	post_writer = request.POST.get('post_writer');
	club_name = request.POST.get('club_name');
	match_date = request.POST.get('match_date');
	match_time_start = request.POST.get('match_time_start');
	match_time_end = request.POST.get('match_time_end');
	player_num = request.POST.get('player_num');
	passwd = request.POST.get('passwd');
	blue_goga_avg = request.POST.get('blue_goga_avg')
	date = request.POST.get('date')
	p1 = request.POST.get('p1')
	p2 = request.POST.get('p2')
	p3 = request.POST.get('p3')
	p4 = request.POST.get('p4')



	print(date)
	
	post = Post_list(post_writer=post_writer, club_name=club_name, \
		match_date=match_date, match_time_start=match_time_start, match_time_end=match_time_end,\
		passwd=passwd,blue_goga_avg=blue_goga_avg,date=date,\
		blue_p1_name=p1,blue_p2_name=p2,blue_p3_name=p3,blue_p4_name=p4)
	post.save()

	return HttpResponse("good")

def add_schedule(request) :
	pk = request.session['pk']
	player = Player.objects.get(pk=pk)
	title = request.POST.get('title')
	date_start = request.POST.get('date_start')
	date_end =request.POST.get('date_end')

	print(date_start)
	print(date_end)
	print(title)

	schedule = Schedule(player_id=pk,date_start=date_start,date_end=date_end,title=title)
	schedule.save();

	data = {
		'title' : schedule.title,
		'date_end' : schedule.date_end,
		'date_start' : schedule.date_start,
		'pk' : schedule.pk,
	}

	return JsonResponse(data)

def get_my_schedules(request) :

	pk = request.session['pk']
	schedules = Schedule.objects.filter(player_id=pk)
	serialized_schedules = ScheduleSerializer(schedules,many=True)

	return HttpResponse(json.dumps(serialized_schedules.data))

def create_my_schedule_table(request) :

	now = time.localtime()

	mon = str(now.tm_mon)
	day = str(now.tm_mday)
	hour=str(now.tm_hour)
	mins=str(now.tm_min)
	sec=str(now.tm_sec)


	if now.tm_mon < 10 :
		mon= str('0')+str(now.tm_mon)
		print(mon)
	if now.tm_mday < 10 :
		day= str('0')+str(now.tm_mday)
		print(day)
	if now.tm_hour < 10 :
		hour= str('0')+str(now.tm_hour)
		print(hour)
	if now.tm_min < 10 :
		hour= str('0')+str(now.tm_min)
		print(mins)
	if now.tm_sec < 10 :
		sec= str('0')+str(now.tm_sec)
		print(sec)


	date_now = str(now.tm_year)+'-'+mon\
	+'-'+day+'T'+hour+':'+mins+':'+sec

	print(date_now)
	pk = request.session['pk']
	schedules = Schedule.objects.filter(Q(player_id=pk) & Q(date_start__gte=date_now)).order_by('date_start')
	serialized_schedules = ScheduleSerializer(schedules,many=True)

	return HttpResponse(json.dumps(serialized_schedules.data))



def get_all_schedules(request) :
	pk = request.session['pk']
	schedules = Schedule.objects.exclude(player_id=pk)
	serialized_schedules = ScheduleSerializer(schedules,many=True)

	return HttpResponse(json.dumps(serialized_schedules.data))

def delete_my_schedule(request) :
	try :
		pk = request.POST.get('pk')
		schedule = Schedule.objects.filter(pk=pk)
		schedule.delete()
		return HttpResponse("삭제되었습니다!")
	except Exception as e :
		return HttpResponse("delete schedule failed") 

def edit_my_schedule(request) :
	pk = int(request.POST.get('pk'))
	print("pk")
	print(pk)
	date_start = request.POST.get('date_start')
	date_end = request.POST.get('date_end')

		
	print(1)
	schedule = Schedule.objects.get(pk=pk)
	schedule.date_start=date_start
	schedule.date_end=date_end
	schedule.save()
	print(schedule)
	
	data = {
		'pk' : schedule.pk,
		'title' : schedule.title,
		'date_start' : schedule.date_start,
		'date_end' : schedule.date_end,
		}
	print(4)
	return JsonResponse(data)

def create_post_list(request) :
	posts=Post_list.objects.all().order_by('-pk')
	serialized_posts = PostSerializer(posts,many=True)

	pages = request.GET.get('page',0)
	return HttpResponse(json.dumps(serialized_posts.data))

def delete_match_info(request,post_pk) :

	pk=request.session.get('pk')
	player_name = request.GET.get('player_name')

	if pk is None :
			return redirect('/')

	try :
		post=Post_list.objects.get(pk=post_pk)
		post.delete();
		posts = Post_list.objects.all().filter(state=True).order_by('-pk')
		count = posts.count()
		
		paginator = Paginator(posts, 10)
		pages = request.GET.get('page',1)
		posts = paginator.get_page(pages)

	except PageNotAnInteger :
		posts = paginator.page(1)
	except EmptyPage :
		posts = paginator.page(paginator.num_pages)
		return HttpResponse("end")
	except Exception as e :
		return HttpResponse("게시물이 존재하지 않습니다")

	return render(request, 'hzm/match.html',{'posts' : posts, 'count':count, 'pk':pk, 'player_name':player_name})

def delete_before_match_info(request,post_pk) :
	try :
		pk=request.session.get('pk')
		player_name = request.GET.get('player_name')
		
		if pk is None :
			return redirect('/')

		post=Post_list.objects.get(pk=post_pk)
		post.delete();
		posts = Post_list.objects.all().filter(state=False).order_by('-pk')
		count = posts.count()
		paginator = Paginator(posts, 10)
		pages = request.GET.get('page',1)
		posts = paginator.get_page(pages)
	except PageNotAnInteger :
		posts = paginator.page(1)
	except EmptyPage :
		posts = paginator.page(paginator.num_pages)
		return HttpResponse("end")
	except Exception as e :
		return HttpResponse("게시물이 존재하지 않습니다.")

	return render(request, 'hzm/match_before.html',{'posts' : posts, 'count':count, 'pk':pk, 'player_name':player_name})

def accpet_match_info(request,post_pk) :
	pk=request.session.get('pk')
	player_name=request.session.get('player_name')
	if pk is None :
		return redirect('/')

	try :
		print(post_pk)
		post=Post_list.objects.get(pk=post_pk)
		print(post)
		post.state=True
		post.save()
		print(1)
		posts = Post_list.objects.all().filter(state=True).order_by('-pk')
		print(2)
		count = posts.count()
		paginator = Paginator(posts, 10)
		pages = request.GET.get('page',1)
		posts = paginator.get_page(pages)
		print(3)
	except PageNotAnInteger :
		posts = paginator.page(1)
	except EmptyPage :
		posts = paginator.page(paginator.num_pages)
		return HttpResponse("end")

	except Exception as e :
		return HttpResponse("게시물이 존재하지 않습니다.")

	return render(request, 'hzm/match.html',{'posts' : posts, 'count':count, 'pk':pk, 'player_name':player_name})

def check_post_passwd(request) :
	passwd=request.POST.get('post_passwd')
	pk = request.POST.get('pk')
	print(passwd)
	post=Post_list.objects.get(pk=pk)
	
	if passwd == post.passwd :
		data={'team':'blue'}
		return JsonResponse(data)
	elif passwd == club_passwd :
		data={'team':'red'}
		return JsonResponse(data)
	elif passwd == master_passwd :
		data={'team':'all'}
		return JsonResponse(data)
	else :
		data={'team':"fail"}
	return JsonResponse(data)

def save_match_info(request) :
	pk=request.POST.get('post_pk')

	print(pk)

	post=Post_list.objects.get(pk=pk)

	red_p1_name=request.POST.get('red_p1_name')
	red_p2_name=request.POST.get('red_p2_name')
	red_p3_name=request.POST.get('red_p3_name')
	red_p4_name=request.POST.get('red_p4_name')
	blue_p1_name=request.POST.get('blue_p1_name')
	blue_p2_name=request.POST.get('blue_p2_name')
	blue_p3_name=request.POST.get('blue_p3_name')
	blue_p4_name=request.POST.get('blue_p4_name')
	match_data=request.POST.get('match_data')
	match_time_start=request.POST.get('time_start')
	match_time_end=request.POST.get('time_end')
	red_goga_avg=request.POST.get('red_goga_avg')
	blue_goga_avg=request.POST.get('blue_goga_avg')
	player_num=request.POST.get('player_num')


	post.red_p1_name=red_p1_name
	post.red_p2_name=red_p2_name
	post.red_p3_name=red_p3_name
	post.red_p4_name=red_p4_name
	post.blue_p1_name=blue_p1_name
	post.blue_p2_name=blue_p2_name
	post.blue_p3_name=blue_p3_name
	post.blue_p4_name=blue_p4_name
	post.match_data=match_data
	post.match_time_start=match_time_start
	post.match_time_end=match_time_end
	post.red_goga_avg=red_goga_avg
	post.blue_goga_avg=blue_goga_avg
	post.player_num=player_num
	post.save()		
	return HttpResponse("good")

 	


