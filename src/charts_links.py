from datetime import datetime


current_year = str(datetime.now().year)
current_decade = f'{str(current_year)[:-1]}0'
URLS = (
    f'https://www.discogs.com/search/?type=release&sort=hot%2Cdesc&ev=em_tr&decade={current_decade}'
    f'&genre_exact=Rock&format_exact=Album&year={current_year}',
    f'https://www.officialcharts.com/charts/rock-and-metal-albums-chart/',
)
