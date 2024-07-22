import store
from fastapi import FastAPI
from fastapi.responses import HTMLResponse


app = FastAPI()

@app.get('/')
def get_users():
    return [
        {'name': 'Cristian Orrego', 'username': 'codev', 'followers': 766},
        {'name': 'Allan Britos', 'username': 'calibre12', 'followers': 432},
        {'name': 'Elvert Galarga', 'username': 'elvert', 'followers': 677},
    ]


@app.get('/html', response_class=HTMLResponse)
def get_html_content():
    return """
    <html>
        <head>
            <title>Some HTML in here</title>
        </head>
        <body>
            <h1>Look ma! HTML!</h1>
        </body>
    </html>
    """


def run():
    store.get_store_categories()


if __name__ == '__main__':
    run()