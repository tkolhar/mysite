from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.http import Http404
from django.template import loader
from django.shortcuts import render
from django.http import HttpResponseRedirect

from .forms import LoginForm
from .forms import AlertForm

from .models import RescueSpecialist, PatientRecord, Vital_Signs



def index(request):
    rescuespecialist = RescueSpecialist.objects.get(id=1)
    template = loader.get_template('PCR/index.html')
    context = {
        'rescuespecialist': rescuespecialist,
    }
    return HttpResponse(template.render(context, request))

def get_name(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = LoginForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/PCR/patientaccesscenter/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = LoginForm()

    return render(request, 'PCR/login.html', {'form': form})

def patient_access_center(request):
    template = loader.get_template('PCR/PatientAccessCenter.html')
    return HttpResponse(template.render(request))

def search(request):
    template = loader.get_template('PCR/search.html')
    return HttpResponse(template.render(request))


def search_history(request):
    results=""
    if request.GET.get('sar_no'):
        search = request.GET.get('sar_no')
        results = PatientRecord.objects.get(pk=search)

    return render(request, 'PCR/past_history.html',{
        'results': results,
    })

def tracking(request):
    results=""
    res = ""
    if request.GET.get('sar_no'):
        search_no = request.GET.get('sar_no')
        results = Vital_Signs.objects.create(pt_sar_inc_no_id=12)
        res = PatientRecord.objects.get(pk=search_no)
        res.pt_sar_inc_no = search_no
        res.save()
        results.bpdate = request.GET.get('myDate')
        results.systolic = request.GET.get('systolic')
        results.diastolic = request.GET.get('diastolic')
        results.save()
    return render(request, 'PCR/tracking.html',{
        'results': results,
    })

def logout(request):
    template = loader.get_template('PCR/logout.html')
    return HttpResponse(template.render(request))


def add(request):
    template = loader.get_template('PCR/add.html')
    return HttpResponse(template.render(request))

def update(request):
    template = loader.get_template('PCR/update.html')
    return HttpResponse(template.render(request))

def alert(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = AlertForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            results = ""
            if request.POST.get('sar_no'):
                search = request.POST.get('sar_no')
                results = PatientRecord.objects.get(pk=search)
                results.medications = request.POST.get('med')
                results.alertupdate=1;
                results.save()
            return HttpResponseRedirect('/PCR/update/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = AlertForm()

    return render(request, 'PCR/alert.html', {'form': form})

def alertlist(request):
    list = []
    for results in PatientRecord.objects.all():
        if results.alertupdate == 0:
           list.append((results.given_name,results.surname,results.SAR_incident_no))
    return render(request, 'PCR/alertlist.html', {
        'results': list,
    })

def linechart(request):
    # instantiate a drawing object
    import mycharts
    d = mycharts.MyLineChartDrawing()

    # extract the request params of interest.
    # I suggest having a default for everything.

    d.height = 500
    d.chart.height = 500

    d.width = 1000
    d.chart.width = 1000

    d.title._text = "Blood Pressure"#request.session.get('Some custom title')

    d.XLabel._text = "Systolic" #request.session.get('X Axis Labell')
    d.YLabel._text = "Diastolic" #request.session.get('Y Axis Label')

    results = Vital_Signs.objects.all()
    length = results.__len__()
    list = []
    for e in Vital_Signs.objects.all():
        print type(e.diastolic)
        list.append((int(e.systolic),int(e.diastolic)))
    d.chart.data =  [(list)] #, (3, 3), (4, 5)), ((1, 2), (2, 3), (2.5, 2), (3.5, 5), (4, 6))]

    labels = ["Systolic"]
    if labels:
        # set colors in the legend
        d.Legend.colorNamePairs = []
        for cnt, label in enumerate(labels):
            d.Legend.colorNamePairs.append((d.chart.lines[cnt].strokeColor, label))

    # get a GIF (or PNG, JPG, or whatever)
    binaryStuff = d.asString('gif')
    return HttpResponse(binaryStuff, 'image/gif')