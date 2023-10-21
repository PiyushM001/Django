from django.shortcuts import render

post = [
    {
        'author':'piyush',
        'title':'djangopm'
    },
    {
        'author':'piyush2',
        'title':'djangopm2'
    },{
        'author':'piyush3',
        'title':'djangopm3 '
    },
    {
        'author':'piyush',
        'title':'djangopm'
    },
    {
        'author':'piyush2',
        'title':'djangopm2'
    },{
        'author':'piyush3',
        'title':'djangopm3 '
    },{
        'author':'piyush',
        'title':'djangopm'
    },
    {
        'author':'piyush2',
        'title':'djangopm2'
    },{
        'author':'piyush3',
        'title':'djangopm3 '
    }
]

def home(request):
    context = {
        'posts':post
    }
    return render(request , 'blog/home.html', context)   
def about(request):
    return  render(request , 'blog/about.html')    