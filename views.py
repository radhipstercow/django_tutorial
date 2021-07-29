from django.shortcuts import render
from .forms import studyUserForm, part_1Form, part_2Form, part_3Form
from .models import studyUser, Session, part_1, part_2, part_3
# Create your views here.

# Login
def login(request):
    return render (request, 'login.html')

# Instructions
def instructions(request):
    if request.method == 'POST':
        # Creating the form
        form = studyUserForm(request.POST)
        if form.is_valid():
            # Put the sona ID from the form into a variable
            sona = form.cleaned_data['sonaID']
            # Check if sona user already exists
            if studyUser.objects.filter(sonaID = sona).exists():
                # If the user exists, the code will jump to line 41 and refresh the page
                print("User already exists")
            else:
                print("Creating new sona user")
                form.save()
            
            # Session creation 
            # Getting user sona and putting into variable
            study_User_Sesh = studyUser.objects.get(sonaID=sona)
            # Creating session based on the user sonaID
            sesh = Session.objects.create(sonaID = study_User_Sesh)

            # Calling sona and session from the database
            tmp = str(sesh.sessionID)
            request.session['sesh'] = tmp
            request.session['sona'] = sona

            context = {'sona': sona, 'sesh':tmp}
            return render (request, 'instructions.html')
        
        # If Sona ID already exists we refresh the page
        else:
            return render (request, 'login.html')

# Part 1
def part_1_View(request):
    # No functionality
    return render (request,'part_1.html')

# Part 2
def part_2_View(request):
    if request.method == 'POST':
        form_part_1 = part_1Form(request.POST)

        # Retrieeving the existing session tied to the sonaID
        seshID = request.session['sesh']
        ss = Session.objects.filter(sessionID=seshID)[:1].get()
        
        if form_part_1.is_valid():
            # Creating a new form and copying data from previous form
            tmpform_part_1 = form_part_1.save(commit=False)
            # Attaching existing session to new form
            tmpform_part_1.sessionID = ss
            # Saving new form
            tmpform_part_1.save()

            return render (request, 'part_2.html')

        # if the form is not valid, the page will go back to the previous view
        else:
            print('form_part_1 is NOT valid')
            return render (request, 'part_1.html')

# Part 3
def part_3_View(request):
    if request.method == 'POST':
        print("Got POST")
        form_part_2 = part_2Form(request.POST)

        # Retrieeving the existing session tied to the sonaID
        seshID = request.session['sesh']
        ss = Session.objects.filter(sessionID=seshID)[:1].get()
        
        if form_part_2.is_valid():
            # Creating a new form and copying data from previous form
            tmpform_part_2 = form_part_2.save(commit=False)
            # Attaching existing session to new form
            tmpform_part_2.sessionID = ss
            # Saving new form
            tmpform_part_2.save()
            return render (request, 'part_3.html')

        # if the form is not valid, the page will go back to the previous view
        else:
            print('form_part_2 is NOT valid')
            return render (request, 'part_2.html')

# Processing
def processing(request):
    if request.method == 'POST':
        print("Got POST")
        form_part_3 = part_3Form(request.POST)

        # Retrieeving the existing session tied to the sonaID
        seshID = request.session['sesh']
        ss = Session.objects.filter(sessionID=seshID)[:1].get()
        
        if form_part_3.is_valid():
            # Creating a new form and copying data from previous form
            tmpform_part_3 = form_part_3.save(commit=False)
            # Attaching existing session to new form
            tmpform_part_3.sessionID = ss
             # Saving new form
            tmpform_part_3.save()
            return render (request, 'processing.html')

        # if the form is not valid, the page will go back to the previous view
        else:
            print('form_part_3 iss NOT valid')
            return render (request, 'part_3.html')

# Results
def results(request):
    # Getting current session ID
    seshID = request.session['sesh']

    # Get Session table for current sessionID
    ss = Session.objects.filter(sessionID=seshID)[:1].get()
    # Get Part_1 table for current sessionID
    p1 = part_1.objects.filter(sessionID=seshID)[:1].get()
    # Get Part_2 table for current sessionID
    p2 = part_2.objects.filter(sessionID=seshID)[:1].get()
    # Get Part_3 table for current sessionID
    p3 = part_3.objects.filter(sessionID=seshID)[:1].get()

    context = {
        # Session fields
        'sona': ss.sonaID,
        'session': ss.sessionID,
        # Part_1 fields
        'p1_name': p1.name,
        'p1_age': p1.age,
        'p1_major': p1.major,
        # Part_2 fields
        'p2_degree': p2.advanced_degree,
        'p2_dream_Job': p2.dream_Job,
        # Part_3 fields
        'p3_os': p3.user_os,
        'p3_phone': p3.user_phone,
        'p3_sats': p3.phone_sat,
        

        }

    return render(request, 'results.html', context)

def all(request):
    user_list = studyUser.objects.all()

    context = {
        'users':user_list,
    }
    return render(request, 'all.html', context)
 