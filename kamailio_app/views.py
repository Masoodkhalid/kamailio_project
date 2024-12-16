from django.shortcuts import render, redirect, get_object_or_404
from .models import TrustedEntry
from django import forms

# TrustedEntry ModelForm for Insert and Update
class TrustedEntryForm(forms.ModelForm):
    class Meta:
        model = TrustedEntry
        fields = ['src_ip', 'proto', 'from_pattern', 'ruri_pattern', 'tag', 'priority']
        widgets = {
            'src_ip': forms.TextInput(attrs={'class': 'form-control'}),
            'proto': forms.TextInput(attrs={'class': 'form-control'}),
            'from_pattern': forms.TextInput(attrs={'class': 'form-control'}),
            'ruri_pattern': forms.TextInput(attrs={'class': 'form-control'}),
            'tag': forms.TextInput(attrs={'class': 'form-control'}),
            'priority': forms.NumberInput(attrs={'class': 'form-control'}),
        }

# Main View
def filter_and_crud(request):
    tag_filter = request.GET.get('tag', None)
    entries = TrustedEntry.objects.filter(tag=tag_filter) if tag_filter else TrustedEntry.objects.all()
    tags = TrustedEntry.objects.values_list('tag', flat=True).distinct()

    # Handle Insert Form
    if request.method == 'POST' and 'insert' in request.POST:
        form = TrustedEntryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('filter_and_crud')

    # Handle Update Form Submission
    if request.method == 'POST' and 'update_id' in request.POST:
        update_id = request.POST.get('update_id')
        entry_to_update = get_object_or_404(TrustedEntry, id=update_id)
        update_form = TrustedEntryForm(request.POST, instance=entry_to_update)
        if update_form.is_valid():
            update_form.save()
            return redirect('filter_and_crud')

    return render(request, 'kamailio_app/filter_and_modal.html', {
        'form': TrustedEntryForm(),  # Empty form for Insert
        'entries': entries,
        'tags': tags,
        'selected_tag': tag_filter,
    })
