from jinja2 import Template

def testing_jinja():
    template = Template('<p>Hello {{ name }}!</p>')
    rendered_page = template.render(name='John Doe')  
    print(rendered_page)  

def testing_git():
    print("fggfdkjlgdfgkj")

