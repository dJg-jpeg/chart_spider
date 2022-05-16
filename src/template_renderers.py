from aiohttp_jinja2 import template
from src.spider import get_top_albums


@template('index.html')
async def index(request):
    top_albums = await get_top_albums()
    return {
        'title': 'Most popular rock and metal albums from Discogs and official charts',
        'discogs': top_albums[0],
        'charts': top_albums[1],
    }
