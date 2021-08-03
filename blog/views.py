from django.shortcuts import render

posts = [
    {
        'author': 'Dylan Peter',
        'title': 'Blog post 1',
        'content': 'First post content',
        'date_posted': 'Jule 9, 2021',
    },
    {
        'author': 'Jordon Kristopher',
        'title': 'Blog post 2',
        'content': 'Second post content',
        'date_posted': 'Jule 10, 2021',
    },
]


def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
