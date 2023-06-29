from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.template import loader

from .forms import ContactForm
from .models import Post


def homepage(request):
    template = loader.get_template('index_homepage.html')
    return HttpResponse(template.render())


def services(request):
    template = loader.get_template('services.html')
    return HttpResponse(template.render())


def contact(request):
    template = loader.get_template('contact.html')
    return HttpResponse(template.render())


def contact_form_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'success.html')
    form = ContactForm()
    context = {'form': form}
    return render(request, 'contact_form.html', context)


def confidentiality(request):
    template = loader.get_template('confidentiality.html')
    return HttpResponse(template.render())


def main(request):
    template = loader.get_template('main.html')
    return HttpResponse(template.render())


def blog(request):
    template = loader.get_template('blog.html')
    return HttpResponse(template.render())


def blog_post(request, title):
    article_title = Post.objects.get(title=title)
    author_name = request.GET.get('author')
    content = request.GET.get('content')
    return render(request, 'base.html', {
        'title': article_title,
        'author': author_name,
        'content': content
    })


def check_post(request):
    title = request.POST['title']
    author = request.POST['author_name']

    if Post.objects.filter(title=title).exists():
        return redirect('/' + title + '/?author=' + author)
    else:
        new_post = Post.objects.create(title=title)
        new_post.save()
        return redirect('/' + title + '/?author=' + author)


def add_post(request):
    title = request.POST['title']
    author = request.POST['author']
    content = request.POST['content']
    status = request.POST['status']

    new_post = Post.objects.create(author=author, title=title, content=content, status=status)
    new_post.save()
    return HttpResponse('Postat cu succes!')


def get_posts(request, title):
    article_title = Post.objects.get(title=title)
    blog_content = Post.objects.filter(content=article_title.id)
    return JsonResponse({"messages": list(blog_content.values())})
