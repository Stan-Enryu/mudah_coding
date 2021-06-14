from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.core.paginator import Paginator
from django.contrib.auth.models import Group
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import Course, Step_Course, Sub_Step_Course, Review
from users.models import Sub_Step_Done

import subprocess

from .forms import form_code

def course_view(request):
    courses = Course.objects.order_by('name')

    context = {
        'courses': courses
    }

    return render(request, "browse_course/course.html", context)

@login_required
def step_course(request, course_slug):
    courses = Course.objects.get(slug=course_slug)

    step_courses = Step_Course.objects.filter(course=courses.id).order_by('step_course_id')

    sub_step_courses = []
    sub_step_done = []

    for step_course in step_courses:
        sub_step_courses.append(Sub_Step_Course.objects.filter(step_course=step_course.id).order_by('sub_step_course_id'))
        sub_step_done.append(Sub_Step_Done.objects.filter(user_id=request.user.id, step_course=step_course).order_by('sub_step_course_id'))
        
    is_premium = Group.objects.get(name='Premium') in request.user.groups.all()

    step_done = []
    for i in range(len(sub_step_courses)):
        if(len(sub_step_courses[i]) == len(sub_step_done[i]) and len(sub_step_courses[i]) != 0):
            step_done.append(step_courses[i])
        else:
            step_done.append(0)


    sub_step_done = [j.sub_step_course for i in sub_step_done for j in i]
    len_sub_step_done = len(sub_step_done)
    len_sub_step = sum(len(x) for x in sub_step_courses)
    if len_sub_step_done == 0:
        percen_done = 0
    else:
        percen_done = (len_sub_step_done * 100 // len_sub_step)

    combine = zip(step_courses, sub_step_courses)


    free_course =[]
    if len(sub_step_courses) > 1:
        free_course.append(sub_step_courses[0][0])
        free_course.append(sub_step_courses[0][1])

    content = {
	    'courses': courses,
	    'sub_step_and_step_courses':combine,
        'is_premium': is_premium,
        'step_done': step_done,
        'sub_step_done': sub_step_done,
        'percen_done': percen_done,
        'free_course': free_course,
    }
    return render(request, 'browse_course/step_course.html', content)

@login_required
def sub_step_course(request, course_slug, step_slug, sub_step_id):

    course = Course.objects.get(slug=course_slug)
    step = Step_Course.objects.get(slug=step_slug)
    sub_step = Sub_Step_Course.objects.get(sub_step_course_id=sub_step_id,step_course=step)

    # ambil semua sub step
    all_sub_step = Sub_Step_Course.objects.filter(step_course=step).order_by("sub_step_course_id")

    # per page
    paginator = Paginator(all_sub_step, 1)
    page_now = sub_step_id
    sub_step_page = paginator.get_page(page_now)

    # banyak sub step
    len_all_sub_step = len(all_sub_step)

    output = ''
    color_output = '#231c14'

    if request.method == 'POST' and request.POST.get('compile_run') == "click":

        code_user = request.POST.get('code')
        form = form_code(initial={'code':code_user})
        
        path = "./Browse_Course/static/browse_course/file_compile/"

        file = open(path+"main.c","w")
        file.write(code_user)
        file.close()

        compile = subprocess.Popen(['gcc', path+"main.c", '-o', path+"main"], stdout=subprocess.PIPE, stderr=subprocess.PIPE,text=True)

        output, error = compile.communicate()

        if compile.returncode != 0:
            output = error
            color_output = 'red'
        else:
            run = subprocess.Popen([path+"main"], stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE, text=True, shell=True)

            output = run.communicate(input=sub_step.in_put)[0]

            if output == sub_step.output :
                color_output = 'green'

                try:
                    get_sub_step_done = Sub_Step_Done.objects.get(user=request.user, step_course=step, sub_step_course=sub_step)
                except Sub_Step_Done.DoesNotExist:
                    get_sub_step_done = None
                
                if get_sub_step_done is None:
                    Sub_Step_Done.objects.create(user=request.user, step_course=step, sub_step_course=sub_step)
                    messages.success(request,"Berhasil Menyelesaikan Sub Step Ini")
                else:
                    messages.success(request,"Sebelumnya Kamu Sudah Menyelesaikan Sub Step Ini")

            else:
                color_output = 'red'
                

    else:
        form = form_code(initial={'code':sub_step.code})

    content = {
        "course" : course,
        "step" : step,
        "sub_step" : sub_step,
        "form": form,
        "sub_step_page":sub_step_page,
        "len_all_sub_step":len_all_sub_step,
        "output":output,
        "color_output":color_output,
    }
    
    return render(request, "browse_course/sub_step_course.html", content)

@login_required
def review_view(request, course_slug):
    course = Course.objects.get(slug=course_slug)

    all_review = Review.objects.filter(course=course)
    print(all_review)

    content = {
        "all_review" : all_review,
        
    }
    return render(request, "browse_course/review_view.html",content)

@login_required
def review_create(request, course_slug):

    course = Course.objects.get(slug=course_slug)

    if request.method == 'POST':
        score=request.POST.get('rating')
        comment=request.POST.get('comment')
        if score and comment:
            Review.objects.create(user=request.user, course=course, description=comment,score=score)
            messages.success(request,"Komentar Berhasil diinput")
        else:
            messages.success(request,"Input Komentar gagal")

    return render(request, "browse_course/review_create.html")