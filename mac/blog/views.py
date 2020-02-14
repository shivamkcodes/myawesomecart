from django.shortcuts import render
from django.http import HttpResponse
from.models import Blogpost
def index(request):
    mypost=Blogpost.objects.all()
    print(mypost)
    return render(request,'blog/index.html',
                  {'mypost':mypost})
    # return HttpResponse("<h1>index blog home")

# Create your views here.
def blogpage(request,id):
    post= Blogpost.objects.filter(post_id=id)[0]
    print(post)
    return render(request,'blog/blogpage.html',
                  {'post':post})


#
# def writeblog(request):
#     if request.method == "POST":
#         writer_name = request.POST.get('writer_name', '')
#         email = request.POST.get('email', '')
#         title = request.POST.get('title', '')
#         head0 = request.POST.get('head0','')
#         chead0 = request.POST.get('chead0','')
#         head1 = request.POST.get('head1','')
#         chead1 = request.POST.get('chead1','')
#         head2 = request.POST.get('head2','')
#         chead2 = request.POST.get('chead2','')
#
#         blog = Writeblog(writer_name=writer_name, email=email, title=title, head0=head0, chead0=chead0, chead1=chead1,
#                           chead2=chead2, head2=head2,head1=head1)
#         blog.save()
#         print(email,title)
#     return render(request, 'blog/writeblog.html')


