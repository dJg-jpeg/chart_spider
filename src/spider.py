from aiohttp import ClientSession
from src.charts_links import URLS


async def get_top_albums():
    top_albums = []
    async with ClientSession() as session:

        async with session.get(URLS[0], ssl=False) as discogs:
            top_albums.append(await parse_discogs(await discogs.text()))

        async with session.get(URLS[1], ssl=False) as charts:
            top_albums.append(await parse_charts(await charts.text()))

    return top_albums


async def parse_discogs(html):
    main_content = html.split('<div class="cards cards_layout_large" id="search_results">')[1]
    main_content = main_content.split('<div class="pagination bottom ">')[0]
    top_albums = main_content.split('''<div
        class="card card_large float_fix
        
        shortcut_navigable"''')[1:11]
    for album in top_albums:
        top_albums[top_albums.index(album)] = album.split('alt="')[1].split('" />')[0]
    return top_albums


async def parse_charts(html):
    top_albums = []
    main_content = html.split('<th class="h-weeks"><abbr title="Weeks on Chart">WoC</abbr></th>')[1]
    main_content = main_content.split('</table>')[0]
    unprepared_albums = main_content.split('<div class="title-artist">')[1:11]
    for album in unprepared_albums:
        album = album.split('<div class="label-cat"><span class="label">')[0]
        title, artist = album.split('<a href="')[1:]
        title = title.split('">')[1].split('</a>')[0]
        artist = artist.split('">')[1].split('</a>')[0]
        top_albums.append(f'{artist} - {title}')
    return top_albums
