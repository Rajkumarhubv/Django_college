from django.shortcuts import render

def home(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def academics(request):
    return render(request, 'academics.html')

def branch_detail(request, branch_name):
    branches = {
        'CSE': 'Computer Science and Engineering focuses on programming, AI, and machine learning.',
        'AIDS': 'Artificial Intelligence and Data Science covers advanced AI and data techniques.',
        'MECH': 'Mechanical Engineering emphasizes manufacturing and mechanical systems.',
        'IT': 'Information Technology focuses on software development and IT systems.',
        'CSML': 'Cyber Security and Machine Learning focuses on secure systems and ML.',
    }
    branch_info = branches.get(branch_name, 'Branch not found.')
    return render(request, 'branch_detail.html', {'branch_name': branch_name, 'branch_info': branch_info})
