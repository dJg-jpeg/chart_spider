from aiohttp.web import Application, run_app
from src.routes import setup_routes
from jinja2 import PackageLoader
from aiohttp_jinja2 import setup


app = Application()
setup(app, loader=PackageLoader('src'))
setup_routes(app)


if __name__ == '__main__':
    run_app(app, host='localhost')
