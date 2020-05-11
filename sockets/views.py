def index():
    with open ('template/index.html') as file:
        return file.read()

def blog():
    with open ('template/blog.html') as file:
        return file.read()

def error404():
    with open ('template/404.html') as file:
        return file.read()