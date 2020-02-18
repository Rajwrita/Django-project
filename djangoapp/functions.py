def handle_uploaded_file(f):
    destination=open("djangoapp/static/uploads/"+f.name,"wb+")
    for c in f.chunks():
        destination.write(c)
    destination.close()