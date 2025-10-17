from .models import Category

def memu_links(request):
    links = Category.objects.all()
    return dict(links=links)
