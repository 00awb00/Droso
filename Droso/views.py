from django.contrib.auth import login, logout, authenticate

from django.shortcuts import render, redirect


def loginUser(request):
    if request.method == "POST":
        # GET AND AUTHENTICATE USERNAME AND PASSWORD
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username, password)

        user = authenticate(username=username, password=password)

        if user is not None:
            # IF LOGIN CREDENTIALS ARE CORRECT.
            login(request, user)
            return redirect("/")

        else:
            # IF LOGIN CREDENTIALS ARE WRONG.
            return render(request, 'user/login.html', {'note': 'Wrong Login credentials detected.'})

    return render(request, 'user/login.html', {'note2': 'Enter username and password to continue...'})


def logoutUser(request):
    # LOGOUT USER
    logout(request)

    return render(request, 'user/logout.html')


def __find_userpath(request):
    # GET USERNAME AMD FIND ITS PATH
    pass


def main(request):
    # IF THE USER TRIES TO ACCESS ANY PAGE WITH URL WITHOUT SIGNING IN. REDIRECT TO LOGIN PAGE.
    if request.user.is_anonymous:
        return redirect("/login")
    return render(request, 'index.html', {'head': 'Drosometer | DOW-UIT'})


def wingdimen(request):
    # IF THE USER TRIES TO ACCESS ANY PAGE WITH URL WITHOUT SIGNING IN. REDIRECT TO LOGIN PAGE.
    if request.user.is_anonymous:
        return redirect("/login")

    return render(request, 'wings/dimensions/w_dimen.html', {'head': 'Drosometer | Wings'})


def wingdimen2(request):
    # IF THE USER TRIES TO ACCESS ANY PAGE WITH URL WITHOUT SIGNING IN. REDIRECT TO LOGIN PAGE.
    if request.user.is_anonymous:
        return redirect("/login")

    if request.method == 'POST':
        return render(request, 'wings/dimensions/w_dimen2.html',
                      {'head': 'Drosometer | Wings', 'img_path': '../static/images/perfect.png',
                       'img_name': 'Like this: '})
    return render(request, 'wings/dimensions/w_dimen2.html',
                  {'head': 'Drosometer | Wings', 'img_path': '../static/images/perfect.png',
                   'img_name': 'Like this: '})


def wingshape(request):
    # IF THE USER TRIES TO ACCESS ANY PAGE WITH URL WITHOUT SIGNING IN. REDIRECT TO LOGIN PAGE.
    if request.user.is_anonymous:
        return redirect("/login")

    return render(request, 'wings/shape/w_shape.html', {'head': 'Drosometer | Wings'})


def __reader(obj):
    # FUNCTION TO READ IMAGES
    pass


def __upload_file_to_userdir(request, file, file_format, flag=True):
    # ASSIGNS NAME AND PATH TO THE FILE
    # SAVE FILE ONLY IF FLAG IS TRUE
    pass


def wingshape2(request):
    # IF THE USER TRIES TO ACCESS ANY PAGE WITH URL WITHOUT SIGNING IN. REDIRECT TO LOGIN PAGE.
    if request.user.is_anonymous:
        return redirect("/login")

    if request.method == 'POST':

        return render(request, 'wings/shape/w_shape2.html',
                      {'head': 'Drosometer | Wings', 'ans': 'Oregan', 'out': 'class.', 'prob_oreg': 0.1,
                       'prob_mut': 0.9, 'img_path': '../static/images/perfect.png', 'img_name': 'Uploaded Image: '})

    else:
        return render(request, 'wings/shape/w_shape2.html',
                      {'head': 'Drosometer | Wings', 'img_path': '../static/images/perfect.png',
                       'img_name': 'Like this: '})


def wingbristles(request):
    # IF THE USER TRIES TO ACCESS ANY PAGE WITH URL WITHOUT SIGNING IN. REDIRECT TO LOGIN PAGE.
    if request.user.is_anonymous:
        return redirect("/login")

    return render(request, 'wings/bristles/w_bristles.html', {'head': 'Drosometer | Wings'})


def wingbristles2(request):
    # IF THE USER TRIES TO ACCESS ANY PAGE WITH URL WITHOUT SIGNING IN. REDIRECT TO LOGIN PAGE.
    if request.user.is_anonymous:
        return redirect("/login")

    return render(request, 'wings/bristles/w_bristles2.html',
                  {'head': 'Drosometer | Wings', 'img_path': '../static/images/perfect.png',
                   'img_name': 'Like this: '})


def c_us(request):
    # IF THE USER TRIES TO ACCESS ANY PAGE WITH URL WITHOUT SIGNING IN. REDIRECT TO LOGIN PAGE.
    if request.user.is_anonymous:
        return redirect("/login")

    return render(request, 'others/contactus.html', {'head': 'Drosometer | Contact Us'})


def a_us(request):
    # IF THE USER TRIES TO ACCESS ANY PAGE WITH URL WITHOUT SIGNING IN. REDIRECT TO LOGIN PAGE.
    if request.user.is_anonymous:
        return redirect("/login")

    return render(request, 'others/aboutus.html', {'head': 'Drosometer | About Us'})


def f_b(request):
    # IF THE USER TRIES TO ACCESS ANY PAGE WITH URL WITHOUT SIGNING IN. REDIRECT TO LOGIN PAGE.
    if request.user.is_anonymous:
        return redirect("/login")

    return render(request, 'others/feedback.html', {'head': 'Drosometer | Give Feedback'})


def wing_f(request):
    # IF THE USER TRIES TO ACCESS ANY PAGE WITH URL WITHOUT SIGNING IN. REDIRECT TO LOGIN PAGE.
    if request.user.is_anonymous:
        return redirect("/login")
    return render(request, 'f_w.html', {'head': 'Drosometer | Wings'})


def eye_f(request):
    # IF THE USER TRIES TO ACCESS ANY PAGE WITH URL WITHOUT SIGNING IN. REDIRECT TO LOGIN PAGE.
    if request.user.is_anonymous:
        return redirect("/login")

    return render(request, 'f_e.html', {'head': 'Drosometer | Eyes'})


def thorax_f(request):
    if request.user.is_anonymous:
        return redirect("/login")
    return render(request, 'f_t.html', {'head': 'Drosometer | Thorax'})


def w_option(request):
    # IF THE USER TRIES TO ACCESS ANY PAGE WITH URL WITHOUT SIGNING IN. REDIRECT TO LOGIN PAGE.
    if request.user.is_anonymous:
        return redirect("/login")

    return render(request, 'wings/dimensions/opt.html', {'head': 'Drosometer | Wings'})


def w_bar(request):
    if request.user.is_anonymous:
        return redirect("/login")

    return render(request, 'wings/dimensions/bar.html',
                  {'head': 'Drosometer | Wings', 'img_path': '../static/images/perfect.png' , 'img_name': 'Uploaded Image'})
