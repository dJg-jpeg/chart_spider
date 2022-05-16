from src.template_renderers import index


def setup_routes(app):
    app.router.add_route('GET', '/', index, name='index')
