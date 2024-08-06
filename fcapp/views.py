from django.shortcuts import render

def home(request):
    return render(request,'home.html')

def signup(request):
    
    try:
        if request.method == 'POST':
            Fname = request.POST['fname']
            Lname= request.POST['lname']
            usernam= request.POST['uname']
            Email = request.POST['E-mail']
            Address=request.POST['adds']
            paswd = request.POST['pswd']
        if paswd:
            if User.objects.filter(password = paswd).exists():
                print("This user name already exists")
                sweetify.error(request,"User name already exist")
                return redirect('signup')
            else:
                user = User.objects.create_user(username=usernam,first_name=Fname,
                            last_name=Lname,email=Email,password=paswd)
                user.save()
                custm = Employee( e_fname=Fname,
                                                e_lname=Lname,
                                                e_address=Address,
                                                 e_age=Age,
                                                e_email=Email,
                                                e_user=employee )
                custm.save()
                sweetify.success(request,"Your account has been registered successfully.Please use the Login credetianls to login ")
                return redirect('signup')
          
    except:
            sweetify.error(request,"Some details seems to be missing or wrong. Please check again that all detials are entered correctly")
            return redirect('signup')
    
    return render(request,'signup.html')

def login(request):
    if request.method== 'POST':
        global u_name
    u_name = request.POST['logname']
    pawd = request.POST['passw']
    log= auth.authenticate(username = u_name, password = pawd)
    if log is not None:
        if log.is_staff:
            auth.login(request,log)
            sweetify.success(request,'Login successful')
            return redirect('Eadmin')
        else:
            auth.login(request,log)
            sweetify.success(request,'Login successful')
            return redirect('Euser')
    else:
        sweetify.error(request,"User name or password does not match. Try again.")
        return redirect('loginpage')
    
    return render(request,'login.html')
