from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.conf import settings
from django.core.mail import send_mail
import random,string
from newspaper import Article
from datetime import datetime, timedelta
from luffyluffy.tasks import send_reminder_email
# Create your views here.

from firebase_admin import firestore
from datetime import datetime, timedelta
  # Required if timestamps are in UTC

from django.utils import timezone
db=firestore.client()
def firstpage(request):
     
     return render(request, 'firstpage.html')

def mentor(request):
     if request.method == 'POST':
        # Get form data
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        country = request.POST.get('country')
        state = request.POST.get('state')
        city = request.POST.get('city')
        professional_title = request.POST.get('title')
        years_experience = request.POST.get('experience')
        password=request.POST.get('password')
        area=request.POST.get('expertise')
        # Create a dictionary to store the mentor data
        mentor_data = {
            'name': name,
            'email': email,
            'phone': phone,
            'country': country,
            'state': state,
            'city': city,
            'password':password,
            'professional_title': professional_title,
            'years_experience': years_experience,
            'area_of_expertise':area
        }

        # Store the mentor data inside Firestore
        db.collection('AvailableMentors').document(email).set(mentor_data)
        request.session['user']=email

        return render(request,'mentor_dashboard.html')
     else:
        return render(request, 'mentor.html')
def investor(request):
     if request.method == 'POST':
        # Get form data
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        country = request.POST.get('country')
        state = request.POST.get('state')
        city = request.POST.get('city')
       
        password=request.POST.get('password')
        
        # Create a dictionary to store the mentor data
        mentor_data = {
            'name': name,
            'email': email,
            'phone': phone,
            'country': country,
            'state': state,
            'city': city,
            'password':password,
            
        }

        # Store the mentor data inside Firestore
        db.collection('AvailableInvestors').document(email).set(mentor_data)
        request.session['user']=email

        return render(request,'investor_dashboard.html')
     else:
        return render(request, 'investor.html')
def redirectments(request):
   return redirect('mlogin')
def redirectinvests(request):
   return redirect('ilogin')
def redirectents(request):
     return redirect('entlogin')
def entrepreneur(request):
    
    if request.method == 'POST':
        print('Yes')
        full_name = request.POST.get('fullName')
        startup_name = request.POST.get('startupName')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        qualification = request.POST.get('qualification')
        description = request.POST.get('description')
        state = request.POST.get('state')
        city = request.POST.get('city')
        availability = request.POST.getlist('availability')
        languages = request.POST.getlist('languages')
        industry = request.POST.get('industry')
        team_size = request.POST.get('teamSize')
        password=request.POST.get('password')
        data = {
            'name': full_name,
            'startup_name': startup_name,
            'email': email,
            'phone': phone,
            'qualification': qualification,
            'description': description,
            'state': state,
            'city': city,
            'availability': availability,
            'languages': languages,
            'industry': industry,
            'team_size': team_size,
            'timestamp': datetime.now().isoformat(),
            'password':password
        }

        db.collection('AvailableEntrepreneurs').document(email).set(data)
        request.session['user']=email
        return render(request,'entrepreneur_dashboard.html')
    return render(request, 'index.html')  # Your form template
 
          
def home(request):
     print(timezone.now())

     return render(request, 'home.html')
def entrepreneur_signup(request):
    
     if (request.method=='POST'):
          print('welcome')
          name=request.POST.get('name')
          newemail=request.POST.get('email')
          password=request.POST.get('password')
          exist=False
          
          accounts=db.collection('AvailableEntrepreneurs').get()
          for i in accounts:
               print(i.to_dict()['email'])
               if i.to_dict()['email']==newemail:
                    exist=True
                    break

          if exist:
               return render(request,'entrepreneur_signup.html',{'message':'The email already exists '})
          else:
               return render(request,'index.html',{'name':name,'email':newemail,'password':password})       
     return render(request, 'entrepreneur_signup.html')


def mentor_signup(request):
     if (request.method=='POST'):
          name=request.POST.get('name')
          newemail=request.POST.get('email')
          password=request.POST.get('password')
          exist=False
          accounts=db.collection('AvailableMentors').get()
          for i in accounts:
               if i.to_dict()['email']==newemail:
                    exist=True
                    break
          if exist:
               return render(request,'mentor_signup.html',{'message':'The email already exists '})
          else:
              return  render(request,'mentor.html',{'name':name,'email':newemail,'password':password})       
     return render(request, 'mentor_signup.html')
          
def mentor_login(request):
     if request.method=='POST':
      mentors=db.collection('AvailableMentors').get()
      email=request.POST.get('email')
      password=request.POST.get('password')
      visited=False
      
      for i in mentors :
          
          if i.to_dict()['email']==email:
               
               if (i.to_dict()['password']==password):
                    visited=True
                    request.session['user']=email
                    
                    return render(request,'mentor_dashboard.html')
               else :
                    return render(request,'mentor_login.html',{'message':'The password is incorrect','email':email})
      if visited==False:
          return render(request, 'mentor_login.html',{'message':'The email or password is incorrect'})

     return render(request , 'mentor_login.html')
def  investor_login(request):
     if request.method=='POST':
      investors=db.collection('AvailableInvestors').get()
      email=request.POST.get('email')
      password=request.POST.get('password')
      visited=False
     
      for i in investors:
         
          if i.to_dict()['email']==email:
               
               if (i.to_dict()['password']==password):
                    visited=True
                    request.session['user']=email
                    
                    return render(request,'investor_dashboard.html')
               else :
                    return render(request,'investor_login.html',{'message':'The password is incorrect','email':email})
      if visited==False:
          return render(request, 'investor_login.html',{'message':'The email or password is incorrect'})

     return render(request , 'investor_login.html')
def investor_signup(request):
     if (request.method=='POST'):
          name=request.POST.get('name')
          newemail=request.POST.get('email')
          password=request.POST.get('password')
          exist=False
          accounts=db.collection('AvailableInvestors').get()
          for i in accounts:
               if i.to_dict()['email']==newemail:
                    exist=True
                    break
          if exist:
               return render(request,'investor_signup.html',{'message':'The email already exists '})
          else:
              return  render(request,'investor.html',{'name':name,'email':newemail,'password':password})       
     return render(request, 'investor_signup.html')
          

def entrepreneur_login(request):
     if request.method=='POST':
          ents=db.collection('AvailableEntrepreneurs').get()
          email=request.POST.get('email')
          password=request.POST.get('password')
          visited=False
          for i in ents:
               if (i.to_dict()['email']==email):
                    if (i.to_dict()['password']==password):
                         visited=True
                         request.session['user']=email
                         return render(request,'entrepreneur_dashboard.html')
                    else:
                         return render(request,'entrepreneur_login.html',{'message':'The password is incorrect','email':email})
          if visited==False:
               return render(request,'entrepreneur_login.html',{'message':'email or password incorrect','email':email} )  
     return render(request, 'entrepreneur_login.html')

def terms(request):
     return render(request,'terms.html')
def bookmentors(request):
     if request.method=="POST":
          
           
           currentemail=request.POST.get('mentoremail')
           detail={
                'mentoremail':currentemail,
                'entrepreneuremail':request.session['user'],
                'time':request.POST.get('time_1'),
                'date':request.POST.get('date_1'),
                'abstract':request.POST.get('idea_abstract')
           }
           db.collection('MentorBookings').add(detail)
           
           send_mail(
                    subject="Call request received",
                    message=f'''{request.session['user']} has requested a call at {request.POST.get('time_1')},{request.POST.get('date_1')} ''',
                    from_email="startupconnect8@gmail.com",
                    recipient_list=[currentemail],
                    fail_silently=False,
                )
           
           return render(request,'mentor-booking-success.html',{'details':detail})
           
                     
     
     mentorsdb=db.collection('AvailableMentors').get()
     mentors=[]
     for i in mentorsdb:
          mentors.append(i.to_dict())
     booked= db.collection('MentorBookings').get()
     wanted=[]
     reqmentos=[]
           
     for i in booked :
               
                if i.to_dict()['entrepreneuremail']==request.session['user']:
                     wanted.append(i.to_dict()['mentoremail'])
     
     for i in mentors :
                if i['email'] not in wanted:
                     print(i['email'])
                     reqmentos.append(i)
     
     return render(request,'mentor_booking.html',{'mentors':reqmentos})
     
def mentor_view_requests(request):
     if request.method=='POST':
            # Get booking id from form
          action = request.POST.get('accorrej')         # Get accept/reject from form
          print(action)
        # Fetch the booking document
          bookings = db.collection('MentorBookings').get()
          selected=None
          selected_booking = None
          selected_booking_email= None
        
          for b in bookings:
            if b.to_dict()['entrepreneuremail']== request.POST.get('call_request_email') and b.to_dict()['mentoremail']==request.session['user']:
                selected=b
                selected_booking = b.to_dict()
                selected_booking_email= b.to_dict()['entrepreneuremail']
                break
          print(selected_booking)
          if selected_booking:
            
            if action == 'acc':
                # Move to AcceptedCalls
                selected_booking['room_name']='Room_' + ''.join(random.choices(string.ascii_letters + string.digits, k=8))
                db.collection('AcceptedCalls').add(selected_booking)
                
                # Send email
                send_mail(
                    subject="Mentor Booking Accepted",
                    message=f"Your booking was accepted by {selected_booking['mentoremail']}.",
                    from_email="startupconnect8@gmail.com",
                    recipient_list=[selected_booking['entrepreneuremail']],
                    fail_silently=False,
                )
                meeting_date=selected_booking['date']
                meeting_time=selected_booking['time']
                meeting_datetime= datetime.strptime(f"{meeting_date} {meeting_time}", "%Y-%m-%d %H:%M")
                reminder_time1 = meeting_datetime - timedelta(hours=1, minutes=0)
                reminder_time2 = meeting_datetime - timedelta(hours=0, minutes=10)
                entrepreneur_email=selected_booking['entrepreneuremail']
                mentor_email=selected_booking['mentoremail']
                

            elif action == 'rej':
                # Move to RejectedCalls
                db.collection('RejectedCalls').add(selected_booking)

                # Send email
                send_mail(
                    subject="Mentor Booking Rejected",
                    message=f"Your booking was rejected by {selected_booking['mentoremail']}.",
                    from_email="startupconnect8@gmail.com",
                    recipient_list=[selected_booking['entrepreneuremail']],
                    fail_silently=False,
                )
            
            # After moving to Accepted/Rejected, delete from MentorBookings
            db.collection('MentorBookings').document(selected.id).delete()
            
          

     allcalls = db.collection('MentorBookings').get()
     usercalls = [i.to_dict() for i in allcalls if i.to_dict()['mentoremail'] == request.session['user']]
    
     return render(request, 'call_requests.html', {'requests': usercalls})


from datetime import datetime, timedelta
from django.shortcuts import render, redirect
from django.utils.timezone import now, make_aware, is_naive
import logging

logger = logging.getLogger(__name__)

def bookedcallsforents(request):
    if 'user' not in request.session:
        return redirect('entrepreneur_login')

    user_email = request.session['user']
    bookings_all = db.collection('AcceptedCalls').stream()

    calls = []
    for booking in bookings_all:
        data = booking.to_dict()

        if data.get('entrepreneuremail') != user_email:
            continue

        # Fetch mentor name (with error handling)
        try:
            mentor_doc = db.collection('AvailableMentors').document(data['mentoremail']).get()
            data['name'] = mentor_doc.to_dict().get('name', 'Unknown')
        except:
            data['name'] = 'Unknown'

        try:
            # Ensure 'date' is a datetime.date, not a string
            if isinstance(data['date'], str):
                data['date'] = datetime.strptime(data['date'], '%Y-%m-%d').date()

            time_str = data.get('time', '')
            datetime_str = f"{data['date']} {time_str}"
            call_time = datetime.strptime(datetime_str, '%Y-%m-%d %H:%M')

            if is_naive(call_time):
                call_time = make_aware(call_time)

            if now() +timedelta(hours=5,minutes=30)- call_time > timedelta(hours=2):
                db.collection('AcceptedCalls').document(booking.id).delete()
                continue

        except Exception as e:
            logger.error(f"Error parsing time for booking {booking.id}: {e}")
            continue

        calls.append(data)

    return render(request, 'entscalls.html', {'calls': calls})

from datetime import datetime, timedelta
from django.shortcuts import render
from django.utils.timezone import now
import logging
from django.utils.timezone import now, make_aware, is_naive

logger = logging.getLogger(__name__)

def bookedcallsforments(request):
    mentor_email = request.session.get('user')
    bookings_all = db.collection('AcceptedCalls').stream()

    calls = []
    for booking in bookings_all:
        data = booking.to_dict()
        if data.get('mentoremail') != mentor_email:
            continue

        try:
            # Ensure date is a date object
            if isinstance(data['date'], str):
                data['date'] = datetime.strptime(data['date'], '%Y-%m-%d').date()
            
            time_str = data.get('time', '')
            datetime_str = f"{data['date']} {time_str}"
            call_time = datetime.strptime(datetime_str, '%Y-%m-%d %H:%M')
            print(call_time)
            print(now())
            if is_naive(call_time):
                call_time = make_aware(call_time)
            if now() +timedelta(hours=5,minutes=30)- call_time > timedelta(hours=2):
                print('satisfied')
                db.collection('AcceptedCalls').document(booking.id).delete()
                continue

            # Fetch entrepreneur's name
            ent_doc = db.collection('AvailableEntrepreneurs').document(data['entrepreneuremail']).get()
            data['name'] = ent_doc.to_dict().get('name', 'Unknown')

            calls.append(data)

        except Exception as e:
            logger.error(f"Error processing booking {booking.id}: {e}")
            continue

    return render(request, 'mentscalls.html', {'calls': calls})

def bookedcallsforinvests(request):
    mentor_email = request.session.get('user')
    bookings_all = db.collection('AcceptedInvestorCalls').stream()

    calls = []
    for booking in bookings_all:
        data = booking.to_dict()
        if data.get('investoremail') != mentor_email:
            continue

        try:
            # Ensure date is a date object
            if isinstance(data['date'], str):
                data['date'] = datetime.strptime(data['date'], '%Y-%m-%d').date()
            
            time_str = data.get('time', '')
            datetime_str = f"{data['date']} {time_str}"
            call_time = datetime.strptime(datetime_str, '%Y-%m-%d %H:%M')
            print(call_time)
            print(now())
            if is_naive(call_time):
                call_time = make_aware(call_time)
            if now() +timedelta(hours=5,minutes=30)- call_time > timedelta(hours=2):
                print('satisfied')
                db.collection('AcceptedInvestorCalls').document(booking.id).delete()
                continue

            # Fetch entrepreneur's name
            ent_doc = db.collection('AvailableEntrepreneurs').document(data['entrepreneuremail']).get()
            data['name'] = ent_doc.to_dict().get('name', 'Unknown')

            calls.append(data)

        except Exception as e:
            logger.error(f"Error processing booking {booking.id}: {e}")
            continue

    return render(request, 'investscalls.html', {'calls': calls})



def video_meeting_for_ents(request, room_name):
    # Fetch the meeting details based on the room_name
    accepted_calls_ref = db.collection('AcceptedCalls')
    accepted_calls = accepted_calls_ref.stream()

    meeting = None
    for call in accepted_calls:
        call_data = call.to_dict()
        generated_room_name = call_data['room_name']
        if generated_room_name == room_name and call_data['entrepreneuremail']==request.session['user']:
            meeting = call_data
            break

    if meeting is None:
        return HttpResponse('meeting not found')

    # Get meeting date and time
    meeting_date = meeting['date']  # Format: YYYY-MM-DD
    meeting_time = meeting['time']  # Format: HH:MM

    # Combine date and time
    meeting_datetime_str = f"{meeting_date} {meeting_time}"
    meeting_datetime = datetime.strptime(meeting_datetime_str, "%Y-%m-%d %H:%M")

    # Get current time (timezone-aware)
    current_time = timezone.now()+timedelta(hours=5,minutes=30)
    
    if current_time < timezone.make_aware(meeting_datetime):
        return render(request, 'waiting_for_meeting_for_ents.html', {'message': 'Meeting has not started yet. Please wait.'})
     
    # If meeting time has arrived, render the meeting room
    return render(request, 'video_meeting_for_ents.html', {'room_name': room_name})
def entrepreneurdashboard(request):
     return render (request,'entrepreneur_dashboard.html')
def redirectentrepreneurstocallbooking(request):
     return redirect ('bookmentors')
def redirectentstoviewcalls(request):
     return redirect('bookedcallsents')
def mentordashboard(request):
     return render(request,'mentor_dashboard.html')
def redirectmentstobookedcalls(request):
     return redirect('bookedcallsments')
def redirectinveststobookedcalls(request):
     return redirect('bookedcallsinvests')
def redirectmentstocallrequest(request):
     return redirect('view_requests')
def video_meeting_for_ments(request, room_name):
    # Fetch the meeting details based on the room_name
    accepted_calls_ref = db.collection('AcceptedCalls')
    accepted_calls = accepted_calls_ref.stream()

    meeting = None
    for call in accepted_calls:
        call_data = call.to_dict()
        generated_room_name = call_data['room_name']
        if generated_room_name == room_name and call_data['mentoremail']==request.session['user']:
            meeting = call_data
            break

    if meeting is None:
        return HttpResponse('meeting not found')

    # Get meeting date and time
    meeting_date = meeting['date']  # Format: YYYY-MM-DD
    meeting_time = meeting['time']  # Format: HH:MM

    # Combine date and time
    meeting_datetime_str = f"{meeting_date} {meeting_time}"
    meeting_datetime = datetime.strptime(meeting_datetime_str, "%Y-%m-%d %H:%M")

    # Get current time (timezone-aware)
    current_time = timezone.now()+timedelta(hours=5,minutes=30)
    print(current_time)
    
    if current_time < timezone.make_aware(meeting_datetime):
        return render(request, 'waiting_for_meeting_for_ments.html', {'message': 'Meeting has not started yet. Please wait.'})
     
    # If meeting time has arrived, render the meeting room
    return render(request, 'video_meeting_for_ments.html', {'room_name': room_name})

def failures_list(request):
    failures_ref = db.collection('entrepreneur_stories')
    docs = failures_ref.stream()

    failures = []
    for doc in docs:
        print(doc.to_dict())
        data = doc.to_dict()
        failures.append({
           
            "startup_name": data.get('startup_name', ''),
            "industry": data.get('industry', ''),
            "funding_stage": data.get('funding_stage', ''),
            "mistake": data.get('mistake', '')
        })

    return render(request,'stories.html',{'failure_stories':failures})

def investordashboard(request):
     return render(request,'investor_dashboard.html')


def submit_failure(request):
    if request.method=='POST':
     startup_name = request.POST.get('startup')
     industry = request.POST.get('industry')
     funding_stage = request.POST.get('stage')
     mistake = request.POST.get('mistake')

     data = {
        'startup_name': startup_name,
        'industry': industry,
        'funding_stage': funding_stage,
        'mistake': mistake,
    }

     db.collection('entrepreneur_stories').add(data)
     return redirect('main')
    return render(request,'post.html')
def main(request):
    return render(request,'main.html')
def browse(request):
    return render(request,'browse.html')
def redirectentrepreneurstofailurevault(request):
     return redirect('main')
def start(request):
     return render(request,'start.html')
def investor_view_requests(request):
     if request.method=='POST':
            # Get booking id from form
          action = request.POST.get('accorrej')         # Get accept/reject from form
          print(action)
        # Fetch the booking document
          bookings = db.collection('InvestorBookings').get()
          selected=None
          selected_booking = None
          selected_booking_email= None
        
          for b in bookings:
            if b.to_dict()['entrepreneuremail']== request.POST.get('call_request_email') and b.to_dict()['investoremail']==request.session['user']:
                selected=b
                selected_booking = b.to_dict()
                selected_booking_email= b.to_dict()['entrepreneuremail']
                break
          print(selected_booking)
          if selected_booking:
            
            if action == 'acc':
                # Move to AcceptedCalls
                selected_booking['room_name']='Room_' + ''.join(random.choices(string.ascii_letters + string.digits, k=8))
                db.collection('AcceptedInvestorCalls').add(selected_booking)
                
                # Send email
                send_mail(
                    subject="Investor Booking Accepted",
                    message=f"Your booking was accepted by {selected_booking['investoremail']}.",
                    from_email="startupconnect8@gmail.com",
                    recipient_list=[selected_booking['entrepreneuremail']],
                    fail_silently=False,
                )
                meeting_date=selected_booking['date']
                meeting_time=selected_booking['time']
                meeting_datetime= datetime.strptime(f"{meeting_date} {meeting_time}", "%Y-%m-%d %H:%M")
                reminder_time1 = meeting_datetime - timedelta(hours=1, minutes=0)
                reminder_time2 = meeting_datetime - timedelta(hours=0, minutes=10)
                entrepreneur_email=selected_booking['entrepreneuremail']
                mentor_email=selected_booking['investoremail']
                

            elif action == 'rej':
                # Move to RejectedCalls
                db.collection('RejectedInvestorCalls').add(selected_booking)

                # Send email
                send_mail(
                    subject="Investor Booking Rejected",
                    message=f"Your booking was rejected by {selected_booking['investoremail']}.",
                    from_email="startupconnect8@gmail.com",
                    recipient_list=[selected_booking['entrepreneuremail']],
                    fail_silently=False,
                )
            
            # After moving to Accepted/Rejected, delete from MentorBookings
            db.collection('InvestorBookings').document(selected.id).delete()
            
          

     allcalls = db.collection('InvestorBookings').get()
     usercalls = [i.to_dict() for i in allcalls if i.to_dict()['investoremail'] == request.session['user']]
    
     return render(request, 'call_requests_investors.html', {'requests': usercalls})

def redirectinveststocallrequest(request):
    return redirect('view_requests_invest')
def bookinvestors(request):
     if request.method=="POST":
           
           currentemail=request.POST.get('investoremail')
           detail={
                'investoremail':currentemail,
                'entrepreneuremail':request.session['user'],
                'time':request.POST.get('time_1'),
                'date':request.POST.get('date_1'),
                'abstract':request.POST.get('idea_abstract')
           }
           db.collection('InvestorBookings').add(detail)

           send_mail(
                    subject="Call request received",
                    message=f'''{request.session['user']} has requested a call at {request.POST.get('time_1')},{request.POST.get('date_1')} ''',
                    from_email="startupconnect8@gmail.com",
                    recipient_list=[currentemail],
                    fail_silently=False,
                )
           
           return render(request,'investor-booking-success.html',{'details':detail})
           
                     

     mentorsdb=db.collection('AvailableInvestors').get()
     mentors=[]
     for i in mentorsdb:
          mentors.append(i.to_dict())
     booked= db.collection('InvestorBookings').get()
     wanted=[]
     req=[]   
     for i in booked :
               
                if i.to_dict()['entrepreneuremail']==request.session['user']:
                     wanted.append(i.to_dict()['investoremail'])
     for i in mentors :
                if i['email'] not in wanted:
                    req.append(i)
     return render(request,'investor_booking.html',{'mentors':req})
def redirectentrepreneurstoinvestorbookings(request):
     return redirect('investorbooking')
def video_meeting_for_invests(request,room_name):
    
    accepted_calls_ref = db.collection('AcceptedInvestorCalls')
    accepted_calls = accepted_calls_ref.stream()

    meeting = None
    for call in accepted_calls:
        call_data = call.to_dict()
        generated_room_name = call_data['room_name']
        if generated_room_name == room_name and call_data['investoremail']==request.session['user']:
            meeting = call_data
            break

    if meeting is None:
        return HttpResponse('meeting not found')

    # Get meeting date and time
    meeting_date = meeting['date']  # Format: YYYY-MM-DD
    meeting_time = meeting['time']  # Format: HH:MM

    # Combine date and time
    meeting_datetime_str = f"{meeting_date} {meeting_time}"
    meeting_datetime = datetime.strptime(meeting_datetime_str, "%Y-%m-%d %H:%M")

    # Get current time (timezone-aware)
    current_time = timezone.now()+timedelta(hours=5,minutes=30)
    print(current_time)
    
    if current_time < timezone.make_aware(meeting_datetime):
        return render(request, 'waiting_for_meeting_for_invests.html', {'message': 'Meeting has not started yet. Please wait.'})
     
    # If meeting time has arrived, render the meeting room
    return render(request, 'video_meeting_for_invests.html', {'room_name': room_name})

def redirectentstoviewinvestorcalls(request):
     return redirect('bookedinvestorcallsents')
def bookedinvestorcallsforents(request):
    if 'user' not in request.session:
        return redirect('entrepreneur_login')

    user_email = request.session['user']
    bookings_all = db.collection('AcceptedInvestorCalls').stream()

    calls = []
    for booking in bookings_all:
        data = booking.to_dict()

        if data.get('entrepreneuremail') != user_email:
            continue

        # Fetch mentor name (with error handling)
        try:
            mentor_doc = db.collection('AvailableInvestors').document(data['investoremail']).get()
            data['name'] = mentor_doc.to_dict().get('name', 'Unknown')
        except:
            data['name'] = 'Unknown'

        try:
            # Ensure 'date' is a datetime.date, not a string
            if isinstance(data['date'], str):
                data['date'] = datetime.strptime(data['date'], '%Y-%m-%d').date()

            time_str = data.get('time', '')
            datetime_str = f"{data['date']} {time_str}"
            call_time = datetime.strptime(datetime_str, '%Y-%m-%d %H:%M')
            print(call_time)
            print(now())
            if is_naive(call_time):
                call_time = make_aware(call_time)

            if now()+timedelta(hours=5,minutes=30) - call_time > timedelta(hours=2):
                db.collection('AcceptedInvestorCalls').document(booking.id).delete()
                continue

        except Exception as e:
            logger.error(f"Error parsing time for booking {booking.id}: {e}")
            continue

        calls.append(data)

    return render(request, 'entsinvestorcalls.html', {'calls': calls})
def video_meeting_for_ents_investors(request,room_name):
     # Fetch the meeting details based on the room_name
    accepted_calls_ref = db.collection('AcceptedInvestorCalls')
    accepted_calls = accepted_calls_ref.stream()

    meeting = None
    for call in accepted_calls:
        call_data = call.to_dict()
        generated_room_name = call_data['room_name']
        if generated_room_name == room_name and call_data['entrepreneuremail']==request.session['user']:
            meeting = call_data
            break

    if meeting is None:
        return HttpResponse('meeting not found')

    # Get meeting date and time
    meeting_date = meeting['date']  # Format: YYYY-MM-DD
    meeting_time = meeting['time']  # Format: HH:MM

    # Combine date and time
    meeting_datetime_str = f"{meeting_date} {meeting_time}"
    meeting_datetime = datetime.strptime(meeting_datetime_str, "%Y-%m-%d %H:%M")

    # Get current time (timezone-aware)
    current_time = timezone.now()+timedelta(hours=5,minutes=30)
    
    if current_time < timezone.make_aware(meeting_datetime):
        return render(request, 'waiting_for_meeting_for_ents_investors.html', {'message': 'Meeting has not started yet. Please wait.'})
     
    # If meeting time has arrived, render the meeting room
    return render(request, 'video_meeting_for_ents_investors.html', {'room_name': room_name})
def entprofile(request):
    return render(request,'profiles_ents.html',{'details':db.collection('AvailableEntrepreneurs').document(request.session['user']).get().to_dict()})
def editentprofile(request):
    if request.method=='POST':
        data={
            'name':request.POST.get('name'),
            'email':request.POST.get('email'),
            'password':db.collection('AvailableEntrepreneurs').document(request.session['user']).get().to_dict()['password'],
            
            'description':request.POST.get('desc'),
            'city':request.POST.get('city'),
            'state':request.POST.get('state'),
            'industry':request.POST.get('industry'),
            'team_size':request.POST.get('teamsize'),
            'startup_name':request.POST.get('stname'),
            'phone':request.POST.get('phone')
        }
        db.collection('AvailableEntrepreneurs').document(request.session['user']).update(data)
        return redirect('entprofile')
    return HttpResponse('You can now edit your profile details')
from django.http import JsonResponse
def fetch_article(request):
    url = request.GET.get('url')
    if not url:
        return JsonResponse({'error': 'URL required'}, status=400)
    try:
        article = Article(url)
        article.download()
        article.parse()
        return JsonResponse({'text': article.text})
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)
def surveyform(request):
    return render(request,'survey1.html')
def surveyform1(request):
    if request.method=='POST':
        name=request.POST.get('title')
        city=request.POST.get('targetCity')
        url=request.POST.get('googleFormUrl')
        mentors=db.collection('AvailableMentors').get()
        entrepreneurs=db.collection('AvailableEntrepreneurs').get()
        investors=db.collection('AvailableInvestors').get()
        mentorsmail=[i.to_dict()['email'] for  i in mentors if i.to_dict()['city'].upper()==city.upper()]
        entsmail=[i.to_dict()['email'] for  i in entrepreneurs if i.to_dict()['city'].upper()==city.upper()]
        investorsmail=[i.to_dict()['email'] for  i in investors if i.to_dict()['city'].upper()==city.upper()]
        req=[]
        req = mentorsmail + entsmail + investorsmail
        req=list(set(req))
        subject = f"Survey Form Request - {name}"
        message = f"""
Dear Participant,

An entrepreneur from your city ({city}) has shared a survey form and would appreciate your response.

Form Title: {name}
Submitted By: {request.session['user']}

Please take a moment to fill it out: {url}

Thank you for your valuable time and input.

Best regards,
StartUp Connect Team
"""
        send_mail(
            subject,
            message,
            'startupconnect8@gmail.com',  # sender (configured in your Django settings)
            req,  # list of recipient emails
            fail_silently=False,
        )

        return render(request, 'success.html')


    return render(request,'survey2.html')
def mentorrating(request,room_name):
    print(room_name)    
    if request.method == 'POST':
        startup = request.POST.get('startup_idea')
        creativity = request.POST.get('creativity')
        hardsoft = request.POST.get('security_hw')
        realtime = request.POST.get('security_sw')
        summary = request.POST.get('description')
        suggestions = request.POST.get('desc')
        call=db.collection('AcceptedCalls').get()

        req=[]
        for i in call:
             if i.to_dict()['room_name']==room_name:
                 id=i.id
                 req.append(i.to_dict())
        call=req[0]
        mentor_data = {
            'startup_idea': startup,
            'creativity': creativity,
            'security_hw': hardsoft,
            'security_sw': realtime,
            'description': summary,
            'decs': suggestions,
            'entrepreneuremail':call['entrepreneuremail'],
            'mentoremail':call['mentoremail'],
            'date':call['date'],
            'time':call['time'],
            'abstract':call['abstract'],
            'room_name':room_name,
            'end_time':timezone.now()
        }
        db.collection('mentorresult').document(room_name).set(mentor_data)
        db.collection('AcceptedCalls').document(id).delete()
        return HttpResponse('successfully submitted')
        
    return render(request,'review-mentor.html')
def nomentorrating(request,room_name):
    call=db.collection('AcceptedCalls').get()
    req=[]
    for i in call:
             if i.to_dict()['room_name']==room_name:
                 id=i.id
                 req.append(i.to_dict())
    call=req[0]
    mentor_data = {
            'startup_idea':'No Rating',
            'creativity': 'No Rating',
            'security_hw': 'No Rating',
            'security_sw': 'No Rating',
            'description': 'No summary',
            'decs': 'No suggestions',
            'entrepreneuremail':call['entrepreneuremail'],
            'mentoremail':call['mentoremail'],
            'date':call['date'],
            'time':call['time'],
            'abstract':call['abstract'],
            'room_name':room_name,
            'end_time':timezone.now()
        }
    db.collection('mentorresult').document(room_name).set(mentor_data)
    db.collection('AcceptedCalls').document(id).delete()
    return redirect('bookedcallsments')
        
    
def callhistorywithmentors(request):
    calls=db.collection('mentorresult').get()
    req=[i.to_dict() for i in calls if i.to_dict()['entrepreneuremail']==request.session['user']]
    return render(request,'entscallhistorywithmentors.html',{'calls':req})