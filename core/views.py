from django.shortcuts import render, redirect
from .forms import SchemeReportForm
from .models import SchemeReport, CounselingRequest
from django.core.mail import send_mail

def home(request):
    return render(request, 'core/home.html')

def report_scheme(request):
    if request.method == 'POST':
        form = SchemeReportForm(request.POST, request.FILES)
        if form.is_valid():
            report = form.save(commit=False)
            report.user = request.user if request.user.is_authenticated else None
            report.save()
            return redirect('report_status', tracking_id=report.tracking_id)
    else:
        form = SchemeReportForm()
    return render(request, 'core/report_scheme.html', {'form': form})

def report_status(request, tracking_id):
    report = SchemeReport.objects.get(tracking_id=tracking_id)
    return render(request, 'core/report_status.html', {'report': report})

def report_list(request):
    reports = SchemeReport.objects.all().order_by('-created_at')  # Order by most recent first
    return render(request, 'core/report_list.html', {'reports': reports})

def request_counseling(request):
    if request.method == 'POST':
        message = request.POST.get('message')
        CounselingRequest.objects.create(user=request.user, message=message)
        return render(request, 'core/counseling_success.html')
    return render(request, 'core/counseling.html')

def escalate_report(request, tracking_id):
    report = SchemeReport.objects.get(tracking_id=tracking_id)
    if report.status == 'verified':
        send_mail(
            'Sky Scheme Alert',
            f'Report {tracking_id}: {report.description}',
            'your-email@example.com',
            ['authority@example.com'],
            fail_silently=False,
        )
        return render(request, 'core/escalate_success.html')
    return render(request, 'core/escalate_failure.html')