
from django.shortcuts import render, redirect
from .models import Feedback
from django.contrib import messages
import logging

logger = logging.getLogger(__name__)

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
            return redirect('feedback_success')

        except Exception as e:
            logger.error(f"Error saving feedback: {str(e)}")
            messages.error(request, 'An error occurred while submitting your feedback. Please try again.')
            return render(request, 'feedback.html')

    return render(request, 'feedback.html')

def feedback_success(request):
    """Display success page after feedback submission"""
    return render(request, 'success.html')
