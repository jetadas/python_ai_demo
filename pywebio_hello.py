from pywebio.input import input, FLOAT
from pywebio.output import put_text, put_markdown, put_html
from pywebio import start_server

def hello_pywebio():
    put_markdown("# Hello from PyWebIO!")
    put_text("This is a simple PyWebIO application.")

    name = input("What's your name?", type='text')
    if name:
        put_html(f"<h3>Nice to meet you, {name}!</h3>")

if __name__ == '__main__':
    start_server(hello_pywebio, port=8080, debug=True)
