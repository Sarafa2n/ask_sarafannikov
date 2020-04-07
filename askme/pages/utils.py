from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def pagination(objects, request):
    page_count = request.GET.get('page')
    pages = Paginator(objects, 3)

    try:
        content = pages.page(page_count)
    except PageNotAnInteger:
        content = pages.page(1)
    except EmptyPage:
        content = pages.page(pages.num_pages)

    return content
