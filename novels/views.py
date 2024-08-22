from django.shortcuts import render
from .models import Novel

def novel_list(request):
    novels = Novel.objects.all()
    return render(request, 'novels/novel_list.html', {'novels': novels})

from django.shortcuts import render, get_object_or_404, redirect
from .models import Novel
from .forms import NovelForm  # We'll create this form later

def novel_list(request):
    novels = Novel.objects.all()
    return render(request, 'novels/novel_list.html', {'novels': novels})

def novel_detail(request, pk):
    novel = get_object_or_404(Novel, pk=pk)
    return render(request, 'novels/novel_detail.html', {'novel': novel})

def novel_create(request):
    if request.method == "POST":
        form = NovelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('novel_list')
    else:
        form = NovelForm()
    return render(request, 'novels/novel_form.html', {'form': form})

def novel_edit(request, pk):
    novel = get_object_or_404(Novel, pk=pk)
    if request.method == "POST":
        form = NovelForm(request.POST, instance=novel)
        if form.is_valid():
            form.save()
            return redirect('novel_detail', pk=novel.pk)
    else:
        form = NovelForm(instance=novel)
    return render(request, 'novels/novel_form.html', {'form': form})

def novel_delete(request, pk):
    novel = get_object_or_404(Novel, pk=pk)
    novel.delete()
    return redirect('novel_list')
