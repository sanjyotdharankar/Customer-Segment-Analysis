from django.shortcuts import render
from .forms import ModelUploadForm
import pickle

def home(request):
    return render(request, 'home.html')

def upload_model(request):
    form = ModelUploadForm()
    if request.method == 'POST':
        form = ModelUploadForm(request.POST)
        if form.is_valid():
            # Get the form data
            recency = form.cleaned_data['recency']
            total_expenses = form.cleaned_data['total_expenses']
            income = form.cleaned_data['income']
            total_acc_cmp = form.cleaned_data['total_acc_cmp']
            total_purchases = form.cleaned_data['total_purchases']
            
            
            # Load the trained model using pickle
            model = pickle.load(open('dest1.pkl','rb'))
            
            # Create input data for prediction
            data = [[recency, total_expenses, income, total_acc_cmp, total_purchases]]
            
            # Make predictions using the loaded model
            predictions = model.predict(data)
            
            # Render the results template with the predictions
            return render(request, 'results.html', {'predictions': predictions})

    return render(request, 'upload.html', {'form': form})
