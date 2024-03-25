from django.shortcuts import redirect, render
from django.views.decorators.http import require_POST

from main.utils import get_tfidf_html_table


def index(request):
    return render(request, "index.html")


@require_POST
def tf_idf_table(request):
    file = request.FILES.get("file")
    if file:
        tf_idf_table = get_tfidf_html_table(file.read().decode("utf-8"))
        return render(request, "tf_idf_table.html", {"tf_idf_table": tf_idf_table})
    else:
        return redirect("index")
