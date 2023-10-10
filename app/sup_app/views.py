from django.shortcuts import render,redirect
import models
from datetime import date, timedelta
import datetime
from django.db.models import Q
from django.http import JsonResponse
# Create your views here.
def main_page(request):
    
    if models.Users.objects.filter(u_id=request.session['u_id']).exists():
        #отрисовка страницы с информацией о задачах
        person=models.Users.objects.get(u_id=request.session['u_id'])
        user={
            'id':person.u_id,
            'name':person.u_name,
            'secondName':person.u_second_name,
            'patronymic':person.u_patronymic,
            'phone':person.u_phone_number,
            'org':person.u_org_id.org_id,
              }
        users_rules=person.u_role_id
        posts=person.posts_set.all()
        rules={
                "can_see_organization_calendar":users_rules.can_see_organization_calendar,
                "can_create_task_from_lower_to_higher":users_rules.can_create_task_from_lower_to_higher,
                "can_create_task_for_not_connectet_posts":users_rules.can_create_task_for_not_connectet_posts,
                "can_change_user_rights":users_rules.can_change_user_rights,
                "can_create_related_posts":users_rules.can_create_related_posts,
                "can_change_related_posts":users_rules.can_change_related_posts,
                "can_delete_related_posts":users_rules.can_delete_related_posts,
                "can_create_any_posts":users_rules.can_create_any_posts,
                "can_change_any_posts":users_rules.can_change_any_posts,
                "can_delete_any_posts":users_rules.can_delete_any_posts,
                "can_invite_user":users_rules.can_invite_user,
                "can_delete_user":users_rules.can_delete_user,
                "can_see_other_posts_tasks":users_rules.can_see_other_posts_tasks,
                "can_change_other_posts_tasks":users_rules.can_change_other_posts_tasks,
                "can_delete_other_posts_tasks":users_rules.can_delete_other_posts_tasks,
                "have_personal_cal":users_rules.have_personal_cal,
                "can_create_multi_person_cal_event":users_rules.can_create_multi_person_cal_event,
                "can_see_knowledge_base":users_rules.can_see_knowledge_base,
                "can_see_organizations_chek_lists":users_rules.can_see_organizations_chek_lists,
                "can_change_organizations_chek_lists":users_rules.can_change_organizations_chek_lists,
                "can_add_organizations_chek_lists":users_rules.can_change_organizations_chek_lists,
                "can_delete_organizations_chek_lists":users_rules.can_delete_organizations_chek_lists,
                "can_see_sample_documents":users_rules.can_see_sample_documents,
                "can_change_sample_documents":users_rules.can_change_sample_documents,
                "can_add_sample_documents":users_rules.can_add_sample_documents,
                "can_delete_sample_documents":users_rules.can_delete_sample_documents,
                "can_see_reports":users_rules.can_see_reports,
        }
        for post in posts:
            post_rules=post.p_role_id
            if post_rules.can_see_organization_calendar:
                rules["can_see_organization_calendar"]=post_rules.can_see_organization_calendar
            if post_rules.can_create_task_from_lower_to_higher:
                rules["can_create_task_from_lower_to_higher"]=post_rules.can_create_task_from_lower_to_higher
            if post_rules.can_create_task_for_not_connectet_posts:
                rules["can_create_task_for_not_connectet_posts"]=post_rules.can_create_task_for_not_connectet_posts
            if post_rules.can_change_user_rights:
                rules["can_change_user_rights"]=post_rules.can_change_user_rights
            if post_rules.can_create_related_posts:
                rules["can_create_related_posts"]=post_rules.can_create_related_posts
            if post_rules.can_change_related_posts:
                rules["can_change_related_posts"]=post_rules.can_change_related_posts
            if post_rules.can_delete_related_posts:
                rules["can_delete_related_posts"]=post_rules.can_delete_related_posts
            if post_rules.can_create_any_posts:
                rules["can_create_any_posts"]=post_rules.can_create_any_posts
            if post_rules.can_change_any_posts:
                rules["can_change_any_posts"]=post_rules.can_change_any_posts
            if post_rules.can_delete_any_posts:
                rules["can_delete_any_posts"]=post_rules.can_delete_any_posts
            if post_rules.can_invite_user:
                rules["can_invite_user"]=post_rules.can_invite_user
            if post_rules.can_delete_user:
                rules["can_delete_user"]=post_rules.can_delete_user
            if post_rules.can_see_other_posts_tasks:
                rules["can_see_other_posts_tasks"]=post_rules.can_see_other_posts_tasks
            if post_rules.can_change_other_posts_tasks:
                rules["can_change_other_posts_tasks"]=post_rules.can_change_other_posts_tasks
            if post_rules.can_delete_other_posts_tasks:
                rules["can_delete_other_posts_tasks"]=post_rules.can_delete_other_posts_tasks
            if post_rules.have_personal_cal:
                rules["have_personal_cal"]=post_rules.have_personal_cal
            if post_rules.can_create_multi_person_cal_event:
                rules["can_create_multi_person_cal_event"]=post_rules.can_create_multi_person_cal_event
            if post_rules.can_see_knowledge_base:
                rules["can_see_knowledge_base"]:post_rules.can_see_knowledge_base
            if post_rules.can_see_organizations_chek_lists:
                rules["can_see_organizations_chek_lists"]=post_rules.can_see_organizations_chek_lists
            if post_rules.can_change_organizations_chek_lists:
                rules["can_change_organizations_chek_lists"]=post_rules.can_change_organizations_chek_lists
            if post_rules.can_delete_organizations_chek_lists:
                rules["can_delete_organizations_chek_lists"]=post_rules.can_delete_organizations_chek_lists
            if post_rules.can_see_sample_documents:
                rules["can_see_sample_documents"]=post_rules.can_see_sample_documents
            if post_rules.can_change_sample_documents:
                rules["can_change_sample_documents"]=post_rules.can_change_sample_documents
            if post_rules.can_add_sample_documents:
                rules["can_add_sample_documents"]=post_rules.can_add_sample_documents
            if post_rules.can_delete_sample_documents:
                rules["can_delete_sample_documents"]=post_rules.can_delete_sample_documents
            if post_rules.can_see_reports:
                rules["can_see_reports"]=post_rules.can_see_reports
        request.session['Rules']=rules
        request.session['u_id']=user['id']
        return render(request,'main.html',{'rules':rules,'user':user})
    else:
        return redirect('/login')
#1- Просмотр всех задач должности + 3- просмотр событий календаря на этой неделе
def load_pers(request):
    person=models.Users.objects.get(u_id=request.session['u_id'])
    posts=person.posts_set.all()
    aktiv_tasks={}
    aktiv_tasks['aktiv']={}
    aktiv_tasks['watching']={}
    cal_events={}
    user={
            'id':person.u_id,
            'name':person.u_name,
            'secondName':person.u_second_name,
            'patronymic':person.u_patronymic,
            'phone':person.u_phone_number,
            'org':person.u_org_id.org_id,
              }
    postcal=1
    user['posts']={}
    for post in posts:
        user["posts"]["post"+postcal]=post.p_id
        postcal+=1
        aktasks=post.p_aktiv_tasks.all()
        indikator=1
        for task in aktasks:
            if task.t_status==False:
                aktiv_tasks['aktiv']["aktiv_task"+indikator]={"id":task.t_id,
                                                     "name":task.t_name,
                                                     "start":task.t_start,
                                                     "end":task.t_end,
                                                     "creator":task.t_creator_post_id,
                                                     "type":task.t_type,
                                                     }
                indikator+=1
        indikator=1
        aktasks=post.p_watching_tasks.all()
        for task in aktasks:
            if task.t_status==False:
                aktiv_tasks['watching']["watching_task"+indikator]={"id":task.t_id,
                                                     "name":task.t_name,
                                                     "start":task.t_start,
                                                     "end":task.t_end,
                                                     "creator":task.t_creator_post_id,
                                                     "type":task.t_type,
                                                     }
                indikator+=1
        calends=post.calendar_events_set.filter(c_e_date__gt=date.today()-timedelta(days=date.weekday(date.today())))&post.calendar_events_set.filter(c_e_date__lt=date.today()+timedelta(days=6-date.weekday(date.today())))
        indikator=1
        for cal in calends:
            if date.today()-timedelta(days=date.weekday(date.today()))>=cal.c_e_date_start and cal.c_e_date_start<date.today()+timedelta(days=6-date.weekday(date.today())):
                cal_events['event'+indikator]={
                        "c_e_id":cal.c_e_id,
                        "c_e_date_start":cal.c_e_date_start,
                        "c_e_time_start":cal.c_e_time_start,
                        "c_e_date_end":cal.c_e_date_end,
                        "c_e_time_end":cal.c_e_time_end,
                        "c_e_for_users":cal.c_e_for_users,
                        "c_e_for_org":cal.c_e_for_org,
                        }
                indikator+=1
    calends=person.calendar_events_set.filter(c_e_date__gt=date.today()-timedelta(days=date.weekday(date.today())))&person.calendar_events_set.filter(c_e_date__lt=date.today()+timedelta(days=6-date.weekday(date.today())))
    indikator=1
    for cal in calends:
        if date.today()-timedelta(days=date.weekday(date.today()))>=cal.c_e_date_start and cal.c_e_date_start<date.today()+timedelta(days=6-date.weekday(date.today())):
            cal_events['eventu'+indikator]={
                        "c_e_id":cal.c_e_id,
                        "c_e_date_start":cal.c_e_date_start,
                        "c_e_time_start":cal.c_e_time_start,
                        "c_e_date_end":cal.c_e_date_end,
                        "c_e_time_end":cal.c_e_time_end,
                        "c_e_for_users":cal.c_e_for_users,
                        "c_e_for_org":cal.c_e_for_org,
                        }
            indikator+=1
    if request.session['Rules']['can_see_organization_calendar']:
        indikator=1
        calends=models.Calendar_events.objects.filter(c_e_for_all=True)&models.Calendar_events.objects.filter(c_e_for_org=person.u_org_id.org_id)&models.Calendar_events.objects.filter(c_e_date_start__gt=date.today()-timedelta(days=date.weekday(date.today())))&models.Calendar_events.objects.filter(c_e_date_start__lt=date.today()+timedelta(days=6-date.weekday(date.today())))
        for cal in calends:
            cal_events['evento'+indikator]={
                        "c_e_id":cal.c_e_id,
                        "c_e_date_start":cal.c_e_date_start,
                        "c_e_time_start":cal.c_e_time_start,
                        "c_e_date_end":cal.c_e_date_end,
                        "c_e_time_end":cal.c_e_time_end,
                        "c_e_for_users":cal.c_e_for_users,
                        "c_e_for_org":cal.c_e_for_org,
            }
    person.u_status='online'
    person.save()
    request.session['Userinfo']=user
    return JsonResponse({'tasks':aktiv_tasks,'user':user,'cals':cal_events})
def login_page(request):
    if request.method== 'POST':

        person= models.Users.objects.filter(u_email=request.GET['email']) & models.Users.objects.filter(u_pass=request.GET['pass'])
        if person.exists():
            request.session['u_id']=person[0].u_id
            return redirect('')
        else:
            return render(request,'login.html',{'message':'Не верный адресс электронной почты или пароль'})
    else:
        return render(request,'login.html')
#2- Просмотр поставленных должностью задач
def load_sended_tasks(request):
    posts=request.session['Userinfo']['posts'].values()
    stasks={}
    for post in posts:
        tasks=models.Tasks.objects.filter(t_creator_post_id=models.Posts.objects.get(p_id=post))
        for task in tasks:
            stasks[task.t_id]= {"id":task.t_id,
                                "name":task.t_name,
                                "start":task.t_start,
                                "end":task.t_end,
                                "creator":task.t_creator_post_id,
                                "type":task.t_type,
                                }
    return JsonResponse({'stasks':stasks})
#5- просмотр подробной информации о задаче после клика
def task_full_info(request):
    if models.Users.objects.filter(u_id=request.session['Userinfo']['id']).exists():
        if request.GET.get('tid'):
            task=models.Tasks.objects.get(t_id=request.GET.get('tid'))
            info={}
            info['comments']={}
            info['cheklist']={}
            if request.session['Rules']['can_see_other_posts_tasks']==False:
                posts=request.session['Userinfo']['posts'].values()

                for post in posts:
                    rpost=models.Posts.objects.get(p_id=post)
                    if task in rpost.p_aktiv_tasks.all() or task in rpost.p_watching_tasks.all():
                        info['id']=task.t_id
                        info['name']=task.t_name
                        if task.t_full_text:
                            info['text']=task.t_full_text
                        if task.t_file:
                            info['file']=task.t_file
                        info['start']=task.t_start
                        if task.t_end:
                            info['end']=task.t_end
                        if task.t_fact_end_time:
                            info['fact_end']=task.t_fact_end_time
                        info['creator']=task.t_creator_post_id
                        info['closebyall']=task.t_close_by_all
                        info['status']=task.t_status
                        info['type']=task.t_type
                        comments=task.t_comments.all().order_by('c_send_time')
                        indikator=1
                        for comment in comments:
                            info['comments']['comment'+indikator]={}
                            info['comments']['comment'+indikator]['id']=comment.c_id
                            info['comments']['comment'+indikator]['time']=comment.c_send_time
                            info['comments']['comment'+indikator]['text']=comment.c_text
                            if comment.c_files:
                                info['comments']['comment'+indikator]['file']=comment.c_files
                            else:
                                info['comments']['comment'+indikator]['file']='none'
                            info['comments']['comment'+indikator]['sender']=comment.c_sended_by_user
                            indikator+=1
                        indikator=1
                        chekComs=models.Cheklist_component.objects.filter(c_c_ch_id=task.t_chek_list.ch_id).all()
                        for chekcom in chekComs:
                            info['cheklist']['ch_component'+indikator]={}
                            info['cheklist']['ch_component'+indikator]['id']=chekcom.c_c_id
                            info['cheklist']['ch_component'+indikator]['text']=chekcom.c_c_text
                            info['cheklist']['ch_component'+indikator]['cheker']=chekcom.c_c_closed
                            indikator+=1
                        return render(request,'taskifr.html',{'info':info})
            else:
                info['id']=task.t_id
                info['name']=task.t_name
                if task.t_full_text:
                    info['text']=task.t_full_text
                if task.t_file:
                    info['file']=task.t_file
                info['start']=task.t_start
                if task.t_end:
                    info['end']=task.t_end
                if task.t_fact_end_time:
                    info['fact_end']=task.t_fact_end_time
                info['creator']=task.t_creator_post_id
                info['closebyall']=task.t_close_by_all
                info['status']=task.t_status
                info['type']=task.t_type
                comments=task.t_comments.all().order_by('c_send_time')
                indikator=1
                for comment in comments:
                    info['comments']['comment'+indikator]={}
                    info['comments']['comment'+indikator]['id']=comment.c_id
                    info['comments']['comment'+indikator]['time']=comment.c_send_time
                    info['comments']['comment'+indikator]['text']=comment.c_text
                    if comment.c_files:
                        info['comments']['comment'+indikator]['file']=comment.c_files
                    else:
                        info['comments']['comment'+indikator]['file']='none'
                    info['comments']['comment'+indikator]['sender']=comment.c_sended_by_user
                    indikator+=1
                indikator=1
                chekComs=models.Cheklist_component.objects.filter(c_c_ch_id=task.t_chek_list.ch_id).all()
                for chekcom in chekComs:
                    info['cheklist']['ch_component'+indikator]={}
                    info['cheklist']['ch_component'+indikator]['id']=chekcom.c_c_id
                    info['cheklist']['ch_component'+indikator]['text']=chekcom.c_c_text
                    info['cheklist']['ch_component'+indikator]['cheker']=chekcom.c_c_closed
                    indikator+=1
                return render(request,'taskifr.html',{'info':info})
        else:
            return redirect('')
    else:
        return redirect('/login')
#4- просмотр всех будующих событий календаря(исклячая прошедшие)
def full_cal(request):
    cal_events={}
    if models.Users.objects.filter(u_id=request.session['Userinfo']['id']).exists():
        person=models.Users.objects.get(u_id=request.session['Userinfo']['id'])
        if request.session['Rules']['can_see_organization_calendar']:
            indikator=1
            calends=models.Calendar_events.objects.filter(c_e_for_all=True)&models.Calendar_events.objects.filter(c_e_for_org=person.u_org_id.org_id)
            for cal in calends:
                cal_events['evento'+indikator]={
                        "c_e_id":cal.c_e_id,
                        "c_e_creator":cal.c_e_creator,
                        "c_e_date_start":cal.c_e_date_start,
                        "c_e_time_start":cal.c_e_time_start,
                        "c_e_date_end":cal.c_e_date_end,
                        "c_e_time_end":cal.c_e_time_end,
                        "c_e_for_users":cal.c_e_for_users,
                        "c_e_for_org":cal.c_e_for_org,
                }
                indikator+=1
        calends=person.calendar_events_set.filter(c_e_date__gte=date.today())
        indikator=1
        for cal in calends:
            cal_events['eventu'+indikator]={
                        "c_e_id":cal.c_e_id,
                        "c_e_creator":cal.c_e_creator,
                        "c_e_date_start":cal.c_e_date_start,
                        "c_e_time_start":cal.c_e_time_start,
                        "c_e_date_end":cal.c_e_date_end,
                        "c_e_time_end":cal.c_e_time_end,
                        "c_e_for_users":cal.c_e_for_users,
                        "c_e_for_org":cal.c_e_for_org,
                        }
            indikator+=1
        posts=person.posts_set.all()
        for post in posts:
            calends=post.calendar_events_set.filter(c_e_date__gte=date.today())
            indikator=1
            for cal in calends:
                cal_events['event'+indikator]={
                        "c_e_id":cal.c_e_id,
                        "c_e_creator":cal.c_e_creator,
                        "c_e_date_start":cal.c_e_date_start,
                        "c_e_time_start":cal.c_e_time_start,
                        "c_e_date_end":cal.c_e_date_end,
                        "c_e_time_end":cal.c_e_time_end,
                        "c_e_for_users":cal.c_e_for_users,
                        "c_e_for_org":cal.c_e_for_org,
                        }
                indikator+=1
        return render(request,'',{'cals':cal_events})
    else:
        return redirect('/login')
def event_info(request):
    if models.Users.objects.filter(u_id=request.session['Userinfo']['id']).exists():
        event_inf={}
        if request.GET.get('ceid'):
            if models.Calendar_events.objects.filter(c_e_id=request.GET.get('ceid')).exists():
                event=models.Calendar_events.objects.get(c_e_id=request.GET.get('ceid'))
                if event.c_e_for_all:
                    if request.session['Rules']['can_see_organization_calendar'] and request.session['Userinfo]']['org']==event.c_e_for_org.org_id:
                        event_inf['exist']=True
                        event_inf['event_id']=event.c_e_id
                        event_inf['event_creator']=event.c_e_creator
                        event_inf['event_name']=event.c_e_name
                        event_inf['event_date_start']=event.c_e_date_start
                        event_inf['event_time_start']=event.c_e_time_start
                        event_inf['event_date_end']=event.c_e_date_end
                        event_inf['event_time_end']=event.c_e_time_end
                        event_inf['event_place']=event.c_e_place
                        event_inf['event_for_all']=event.c_e_for_all
                        event_inf['event_for_user']=event.c_e_for_users
                        event_inf['event_for_org']=event.c_e_for_org
                    else:
                        event_inf['exist']=False
                else:
                    user=models.Users.objects.get(u_id=request.session['Userinfo']['id'])
                    if event.c_e_for_users:
                        if user in event.c_e_invited_users:
                            event_inf['exist']=True
                            event_inf['event_id']=event.c_e_id
                            event_inf['event_creator']=event.c_e_creator
                            event_inf['event_name']=event.c_e_name
                            event_inf['event_date_start']=event.c_e_date_start
                            event_inf['event_time_start']=event.c_e_time_start
                            event_inf['event_date_end']=event.c_e_date_end
                            event_inf['event_time_end']=event.c_e_time_end
                            event_inf['event_place']=event.c_e_place
                            event_inf['event_for_all']=event.c_e_for_all
                            event_inf['event_for_user']=event.c_e_for_users
                            event_inf['event_invited']={}
                            if event.c_e_for_users:
                                users=event.c_e_invited_users.all()
                                indikator=1
                                for user in users:
                                    event_inf['event_invited'][indikator]={
                                        "name":user.u_name,
                                        "second_name":user.u_second_name,
                                        "patronymic":user.u_patronymic,
                                        "profile_photo":user.u_profile_photo,
                                        "id":user.u_id
                                    }
                                    indikator+=1
                        else:
                            event_inf['exist']=False
                    else:
                        posts=user.posts_set
                        existflag=0
                        for post in posts:
                            if post in event.c_e_invited_posts:
                                existflag+=1
                        if existflag>0:
                            event_inf['exist']=True
                            event_inf['event_id']=event.c_e_id
                            event_inf['event_creator']=event.c_e_creator
                            event_inf['event_name']=event.c_e_name
                            event_inf['event_date_start']=event.c_e_date_start
                            event_inf['event_time_start']=event.c_e_time_start
                            event_inf['event_date_end']=event.c_e_date_end
                            event_inf['event_time_end']=event.c_e_time_end
                            event_inf['event_place']=event.c_e_place
                            event_inf['event_for_all']=event.c_e_for_all
                            event_inf['event_for_user']=event.c_e_for_users
                            event_inf['event_invited']={}
                            posts=event.c_e_invited_posts.all()
                            for post in posts:
                                event_inf['event_invited'][indikator]={
                                    "name":post.p_name,
                                    "id":post.p_id
                                }
                                indikator+=1
                        else:
                            event_inf['exist']=False
            else:
                event_inf['exist']=False
            return render(request,'eventinf.html',{'event_ind':event_inf})
        else:
            return redirect('/full_cal')
    else:
        return redirect('/login')
def create_task_form(request):
    if models.Users.objects.filter(u_id=request.session['Userinfo']['id']).exists():
        person=models.Users.objects.get(u_id=request.session['Userinfo']['id'])
        posts=person.posts_set.all()
        posts_name={}
        indikator=1
        for post in posts:
            posts_name['post'+indikator]={}
            posts_name['post'+indikator]['id']=post.p_id
            posts_name['post'+indikator]['name']=post.p_name
            indikator+=1
        return render(request,'taskcreate.html',{'posts':posts_name})
    else:
        return redirect('/login')
def create_task_req(request):
    try:
        newtask=models.Tasks()
        newtask.t_name=request.GET.get('name')
        newtask.t_full_text=request.GET.get('text')
        if request.GET.get('start'):
            newtask.t_start=request.GET.get('start')
        else:
            newtask.t_start=date.today()
        if request.GET.get('end'):
            newtask.t_end=request.GET.get('end')
        newtask.t_creator_post_id=request.GET.get('cid')
        if request.GET.get('byall') and request.GET.get('byall')=='True':
            newtask.t_close_by_all=True
        npost=models.Posts.objects.get(p_id=request.GET.get('fid'))
        if request.GET.get('wid'):
            wpost=models.Posts.objects.get(p_id=request.GET.get('wid'))
        newtask.t_type=request.GET.get('type')
        newchecklist=models.Cheklist()
        newchecklist.ch_name='tch'
        newchecklist.save()
        i=1
        while i<=int(request.GET.get('cout')):
            newchcom=models.Cheklist_component()
            newchcom.c_c_ch_id=newchecklist
            newchcom.c_c_text=request.GET.get('ch'+i)
            i+=1
        i=1
        newtask.t_chek_list=newchecklist
        newtask.save()
        npost.p_aktiv_tasks.add(newtask)
        if request.GET.get('wid'):
            npost.p_watching_tasks.add(newtask)
        return JsonResponse({'result':'success','id':newtask.t_id})
    except Exception as err:
        return JsonResponse({'result':'error; '+err})
def close_task(request):
    try:
        if request.GET.get('tid') and models.Tasks.objects.filter(t_id=request.GET.get('tid')).exists():
            ctask=models.Tasks.objects.get(t_id=request.GET.get('tid'))
            cuser=models.Users.objects.get(u_id=request.GET.get('uid'))
            posts=cuser.posts_set.all()
            scheto=0
            for post in posts:
                if post.p_aktiv_tasks.filter(t_id=ctask.t_id).exists():
                    post.p_aktiv_tasks.remove(ctask)
                    post.p_past_tasks.add(ctask)
                    scheto+=1
            if scheto>0:
                if ctask.t_close_by_all:
                    posts=ctask.posts_set.all()
                    schet=0
                    for post in posts:
                        if post.p_aktiv_tasks.filter(t_id=ctask.t_id).exists():
                            schet+=1
                    if schet==0:
                        ctask.t_status=True
                        ctask.save(update_fields=['t_status'])
                else:
                    posts=ctask.posts_set.all()
                    for post in posts:
                        if post.p_aktiv_tasks.filter(t_id=ctask.t_id).exists():
                            post.p_aktiv_tasks.remove(ctask)
                            post.p_past_tasks.add(ctask)
                        if post.p_watching_tasks.filter(t_id=ctask.t_id).exists():
                            post.p_watching_tasks.remove(ctask)
                            post.p_past_tasks.add(ctask)
                    ctask.t_status=True
                    ctask.t_fact_end_time=datetime.datetime.now()
                    ctask.save(update_fields=['t_status','t_fact_end_time'])
                    return JsonResponse({'result':'success'})
            else:
                return JsonResponse({'result':'can not be closed'})
        else:
            return JsonResponse({'result':'task is not exist'})
    except Exception as err:
        return JsonResponse({'result':'error; '+err})
def close_check_point(requuest):
    try:
        if requuest.GET.get('ccid') and models.Cheklist_component.objects.filter(c_c_id=requuest.GET.get('ccid')).exists():
            ccpoint=models.Cheklist_component.objects.get(c_c_id=requuest.GET.get('ccid'))
            ccpoint.c_c_closed=True
            ccpoint.save(update_fields=['c_c_closed'])
            return JsonResponse({'result':'success'})
        else:
            return JsonResponse({'result':'not exist'})
    except Exception as err:
        return JsonResponse({'result':'error;'+err})
def create_event_form(request):
    if models.Users.objects.filter(u_id=request.session['Userinfo']['id']).exists():
        org=models.Organizations.objects.get(org_id=request.session['Iserinfo']['org'])
        persons_in_org=models.Users.objects.filter(u_org_id=org).all()
        posts_in_org=models.Posts.objects.filter(p_org_id=org).all()
        posts={}
        users={}
        indik=1
        for post in posts_in_org:
            posts[indik]={}
            posts[indik]['id']=post.p_id
            posts[indik]['name']=post.p_name
            indik+=1
        indik+=1
        for user in persons_in_org:
            users[indik]={}
            users[indik]['id']=user.u_id
            users[indik]['name']=user.u_name
            users[indik]['sec']=user.u_second_name
            users[indik]['pat']=user.u_patronymic
        return render(request,'eventcreate.html',{'posts':posts,'users':users})
    else:
        return redirect('/login')
def create_event_req(request):
    try:
        newevent=models.Calendar_events()
        newevent.c_e_creator=request.session['Userinfo']['id']
        newevent.c_e_name=request.GET.get('ename')
        newevent.c_e_date_start=datetime.date.strftime(request.GET.get('dstart'),'%Y-%m-%d')
        if request.GET.get('allday')=='y':
            newevent.c_e_date_end=datetime.date.strftime(request.GET.get('dend'),'%Y-%m-%d')
        else:
            newevent.c_e_time_start=datetime.time.strftime(request.GET.get('tstart'),"%H:%M:%S.%f")
            newevent.c_e_time_end=datetime.time.strftime(request.GET.get('tend'),"%H:%M")
        if request.GET.get('place'):
            newevent.c_e_place=request.GET.get('place')
        if request.GET.get('fall') and request.GET.get('fall')=='y':
            newevent.c_e_for_all=True
        elif request.GET.get('fus')=='y':
            newevent.c_e_for_users=True
            i=1
            while i<=int(request.GET.get('icount')):
                if models.Users.objects.filter(u_id=request.GET.get('i'+i)).exists():
                    newevent.c_e_invited_users.add(models.Users.objects.get(u_id=request.GET.get('i'+i)))
                i+=1
        else:
            newevent.c_e_for_users=False
            i=1
            while i<=int(request.GET.get('icount')):
                if models.Posts.objects.filter(p_id=request.GET.get('i'+i)).exists():
                    newevent.c_e_invited_posts.add(models.Posts.objects.get(p_id=request.GET.get('i'+i)))
                i+=1
        return JsonResponse({'result':'success','id':newevent.c_e_id})
    except Exception as err:
        return JsonResponse({'result':'error; '+err})
def task_edit(request):
    try:
        if models.Tasks.objects.filter(t_id=request.GET.get('tid')).exists():
            task=models.Tasks.objects.get(t_id=request.GET.get('tid'))
            edit=[]
            if request.GET.get('name'):
                edit.append('t_name')
                task.t_name=request.GET.get('name')
            if request.GET.get('text'):
                edit.append('t_full_text')
                task.t_full_text=request.GET.get('text')
            if request.GET.get('end'):
                edit.append('t_end')
                task.t_end=request.GET.get('t_end')
            if request.GET.get('tforc'):
                aposts=models.Posts.objects.filter(p_aktiv_tasks__t_id=task.t_id)
                for post in aposts:
                    post.p_aktiv_tasks.remove(task)
                i=1
                while i<=int(request.GET.get('tforc')):
                    if models.Posts.objects.filter(p_id=request.GET.get('tfor'+i)).exists():
                        npost=models.Posts.objects.get(p_id=request.GET.get('tfor'+i))
                        npost.p_aktiv_tasks.add(task)
                    i+=1
            if request.GET.get('cba'):
                if request.GET.get('cba')=="y":
                    task.t_close_by_all=True
                if request.GET.get('cba')=='n':
                    task.t_close_by_all=False
                edit.append('t_close_by_all')
            if request.GET.get('chcсount'):
                j=1
                while j<=int(request.GET.get('chcount')):
                    if models.Cheklist_component.objects.filte(c_c_id=request.GET.get('chcid'+j)).exists():
                        if request.GET.get("chct"+j):
                            component=models.Cheklist_component.objects.get(c_c_id=request.GET.get('chcid'+j))
                            component.c_c_text=request.GET.get("chct"+j)
                            component.save(update_fields=['c_c_text'])
                    j+=1
            
    except Exception as err:
        return JsonResponse({'result':'error; '+err})
