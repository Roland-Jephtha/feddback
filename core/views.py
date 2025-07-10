
from django.shortcuts import render, redirect
from .models import Feedback
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from django.template.loader import render_to_string
from django.utils.html import strip_tags
import logging

logger = logging.getLogger(__name__)

def send_feedback_email(feedback):
    """Send email notification with feedback details"""
    subject = f"New Feedback Submission - {feedback.name}"

    # Create email content
    message = f"""
    New Feedback Submission Received
    ================================

    Submission Details:
    ------------------
    Name: {feedback.name}
    Address: {feedback.address or 'Not provided'}
    State: {feedback.state or 'Not provided'}
    Position: {feedback.position}
    Email: {feedback.email or 'Not provided'}

    Service Information:
    -------------------
    Services Requested: {feedback.services_requested or 'Not provided'}
    Department: {feedback.department or 'Not provided'}
    Staff Name: {feedback.staff_name or 'Not provided'}

    Feedback & Rating:
    -----------------
    Service Rating: {feedback.rating or 'Not provided'}
    Complaints: {feedback.complaint or 'None'}
    Suggestions: {feedback.suggestions or 'None'}
    Overall Satisfaction: {feedback.feedback_satisfaction or 'Not provided'}

    Submission Time: {feedback.submitted_at.strftime('%Y-%m-%d %H:%M:%S')}
    Feedback ID: {feedback.id}

    ---
    This is an automated message from PTI SERVICOM Unit Feedback System.
    """

    # Send email
    send_mail(
        subject=subject,
        message=message,
        from_email=settings.DEFAULT_FROM_EMAIL,
        recipient_list=['ochekwupius@yahoo.com'],
        fail_silently=False,
    )

def feedback_view(request):
    if request.method == 'POST':
        try:
            # Get form data
            name = request.POST.get('name', '').strip()
            address = request.POST.get('address', '').strip()
            state = request.POST.get('state', '').strip()
            position = request.POST.get('position', '').strip()
            services_requested = request.POST.get('services_requested', '').strip()
            rating = request.POST.get('rating', '').strip()
            complaint = request.POST.get('complaint', '').strip()
            department = request.POST.get('department', '').strip()
            staff_name = request.POST.get('staff_name', '').strip()
            suggestions = request.POST.get('suggestions', '').strip()
            email = request.POST.get('email', '').strip()
            feedback_satisfaction = request.POST.get('feedback_satisfaction', '').strip()

            # Validate required fields
            if not name:
                messages.error(request, 'Name is required.')
                return render(request, 'feedback.html')

            if not position:
                messages.error(request, 'Position is required.')
                return render(request, 'feedback.html')

            # Create feedback record
            feedback = Feedback.objects.create(
                name=name,
                address=address,
                state=state,
                position=position,
                services_requested=services_requested,
                rating=rating,
                complaint=complaint,
                department=department,
                staff_name=staff_name,
                suggestions=suggestions,
                email=email,
                feedback_satisfaction=feedback_satisfaction
            )

            logger.info(f"Feedback created successfully: ID {feedback.id}, Name: {name}")

            # Send email notification
            try:
                send_feedback_email(feedback)
                logger.info(f"Email notification sent for feedback ID {feedback.id}")
            except Exception as email_error:
                logger.error(f"Failed to send email for feedback ID {feedback.id}: {str(email_error)}")
                # Continue with redirect even if email fails

            return redirect('feedback_success')

        except Exception as e:
            logger.error(f"Error saving feedback: {str(e)}")
            messages.error(request, 'An error occurred while submitting your feedback. Please try again.')
            return render(request, 'feedback.html')

    return render(request, 'feedback.html')

def feedback_success(request):
    """Display success page after feedback submission"""
    return render(request, 'success.html')
