from django.shortcuts import render, get_object_or_404
from .models import Resource

def resources_list(request):
    category = request.GET.get('category', '')

    if category:
        resources = Resource.objects.filter(category=category)
    else:
        resources = Resource.objects.all()

    emergency = Resource.objects.filter(is_emergency=True)

    context = {
        'resources': resources,
        'emergency': emergency,
        'selected_category': category,
        'categories': Resource.Category.choices,
    }
    return render(request, 'resources/resources.html', context)


def resource_detail(request, pk):
    resource = get_object_or_404(Resource, pk=pk)
    return render(request, 'resources/resource_detail.html', {'resource': resource})
