import datetime
import re

import requests
from bs4 import BeautifulSoup
from django.db import IntegrityError
from jsbeautifier.unpackers import packer
from six import unichr
import random

from app.models import Episodio, LinkSerie, Temporada, Link, Url, Channel


def get_page_bs4(url):
    req = requests.get(url)
    if req.status_code == 200:
        page = BeautifulSoup(req.text, 'html.parser')
        return page
    return None


def get_episodios(page, temporada):
    section = page.find('section', {'class': 'temporadas-grid'})
    divs_episodios = section.select('div.item')
    print('total_episodios', len(divs_episodios))
    if len(divs_episodios) > 0:
        for div_ep in divs_episodios:
            atag_episodio = div_ep.find('a')
            href_episodio = atag_episodio['href']
            img_tag_episodio = atag_episodio.find('img')
            img_url_episodio = get_img_url(img_tag_episodio)
            array_episodio_temp = [text for text in atag_episodio.find('span', {
                'class': 'info'}).stripped_strings]
            if len(array_episodio_temp) == 2:
                type_episodio = array_episodio_temp[0]
                title_episodio = array_episodio_temp[1]
            else:
                type_episodio = array_episodio_temp[0]
                title_episodio = ''
            third_page = get_page_bs4(href_episodio)
            if third_page:
                div_links_epi = third_page.find_all('a', attrs={'class': 'cativ'})
                if div_links_epi:
                    atag_ep_link = div_links_epi
                    if len(atag_ep_link) > 0:
                        ids = []
                        for a_url_epi in atag_ep_link:
                            if a_url_epi.has_attr('data-id'):
                                data_id = str(a_url_epi['data-id'])
                                data_episodio = str(a_url_epi['data-episodio'])
                                data_player = str(a_url_epi['data-player'])
                                url_data_id = 'https://canaismax.com/embed/' + data_id + '/' + data_episodio + '/' + data_player
                                ids.append(url_data_id)
                        if len(ids) > 0:
                            save_episodio(ids, img_url_episodio, title_episodio, type_episodio, temporada)


def save_episodio(ids, img_url_episodio, title_episodio, type_episodio, temporada):
    episodio = Episodio()
    episodio.temporada = temporada
    episodio.img_url = img_url_episodio
    episodio.type = type_episodio
    episodio.title = title_episodio
    episodio.save()
    for id_url_epi in ids:
        save_url_serie_epi_canaismax(episodio, id_url_epi)


def get_img_url(img_tag):
    if img_tag.has_attr('src'):
        img_url = img_tag['src']
    elif img_tag.has_attr('data-src'):
        img_url = img_tag['data-src']
    else:
        img_url = ''
    return img_url


def get_url_temporada(url, i):
    if str(url).endswith('/'):
        return url + 'temporada/' + str(i)
    return str(url) + '/temporada/' + str(i)


def save_temporada(serie, num_seq):
    temporada_obj = Temporada()
    temporada_obj.num_seq = num_seq
    temporada_obj.serie = serie
    temporada_obj.save()
    return temporada_obj


def get_channel_id(string_script):
    api_url = 'https://canaismax.com/api/canal/'
    if api_url in string_script:
        ind = string_script.index(api_url) + len(api_url)
        ind_bar = ind + 24
        id = string_script[ind:ind_bar]
        return id
    return ''


def save_link_channel_aovivogratis(canal, href, m3u8):
    try:
        link = Link()
        link.url = href
        link.channel = canal
        link.m3u8 = get_m3u8_aovivogratis_by_eval(canal.url_site)
        link.save()
    except (Exception):
        print('erro ao salvar link')


def exists_m3u8_saved(m3u8):
    links = Channel.objects.filter(link__m3u8=m3u8)
    if len(links) > 0:
        return True
    return False


def save_link_channel_multicanais(canal, id_url, select_server='tvfolha.com'):
    m3u8 = get_m3u8_multicanais(id_url, select_server=select_server)
    # if m3u8 and not exists_m3u8_saved(m3u8):
    if m3u8:
        try:
            link = Link()
            link.url = id_url
            link.channel = canal
            link.m3u8 = m3u8
            link.save()
        except (Exception,):
            print('erro ao salvar link')


def get_m3u8_filme_canaismax(uri):
    uri = str(uri)
    try:
        miner_req = get_page_bs4(uri)
        if miner_req:
            script = None
            for scr in miner_req.select('script'):
                if 'Clappr.Player' in str(scr):
                    script = scr
            content_script = str(script)
            string_source = 'source: "'
            string_m3u8 = '.m3u8'
            sources_indexes = [m.start() for m in
                               re.finditer(string_source, content_script)]
            m3u8_indexes = [m.start() for m in
                            re.finditer(string_m3u8, content_script)]
            strings = [
                content_script[(int(sources_indexes[i]) + len(string_source)):(int(m3u8_indexes[i]) + len(string_m3u8))]
                for i in range(len(sources_indexes))]
            if len(strings) > 0:
                return strings
    except (Exception,):
        print('nao tem source na uri, ', uri)
        return None


def get_m3u8_serie_epi_canaismax(uri):
    uri = str(uri)
    try:
        miner_req = get_page_bs4(uri)
        if miner_req:
            script = None
            for scr in miner_req.select('script'):
                if 'Clappr.Player' in str(scr):
                    script = scr
            content_script = str(script)
            string_source = 'source: "'
            string_m3u8 = '.m3u8'
            sources_indexes = [m.start() for m in
                               re.finditer(string_source, content_script)]
            m3u8_indexes = [m.start() for m in
                            re.finditer(string_m3u8, content_script)]
            strings = [
                content_script[(int(sources_indexes[i]) + len(string_source)):(int(m3u8_indexes[i]) + len(string_m3u8))]
                for i in range(len(sources_indexes))]
            if len(strings) > 0:
                return strings
    except (Exception,):
        print('nao tem source uri, ', uri)
        return None


def save_url_serie_epi_canaismax(episodio, id_url):
    m3u8_arr = get_m3u8_serie_epi_canaismax(id_url)
    for m3u8 in m3u8_arr:
        if m3u8:
            try:
                link = LinkSerie()
                link.url = id_url
                link.episodio = episodio
                link.m3u8 = m3u8
                link.save()
            except (Exception):
                print('erro ao salvar link do episodio da serie: ', episodio)


def save_url_filmes_canaismax(filme, id_url):
    m3u8_arr = get_m3u8_filme_canaismax(id_url)
    for m3u8 in m3u8_arr:
        if m3u8:
            try:
                link = Url()
                link.url = id_url
                link.filme = filme
                link.m3u8 = m3u8
                link.save()
            except (Exception):
                print('erro ao salvar link do filme')


def get_m3u8_topcanais(id_url, select_server=''):
    string_canal_id = '.php?canal='
    string_end_canal_id = '&pasta'
    uri = str(id_url)
    try:
        index_prefix = uri.index(string_canal_id)
        index_end_suffix = uri.index(string_end_canal_id)
        name_channel = uri[index_prefix + len(string_canal_id):index_end_suffix]
        miner_req = get_page_bs4(id_url)
        if miner_req:
            script = None
            for scr in miner_req.select('script'):
                if 'document.referrer' in str(scr):
                    script = scr
            content_script = str(script)
            string_source = 'source: "'
            string_m3u8 = '/video.m3u8'
            sources_indexes = [m.start() for m in
                               re.finditer(string_source, content_script)]
            m3u8_indexes = [m.start() for m in
                            re.finditer(string_m3u8, content_script)]
            strings = [
                content_script[(int(sources_indexes[i]) + len(string_source)):(int(m3u8_indexes[i]) + len(string_m3u8))]
                for i in range(len(sources_indexes))]
            if len(strings) > 0:
                if name_channel in strings[0]:
                    return strings[0]
                uri_m3u8 = str(strings[0]) + str(name_channel) + string_m3u8
                return uri_m3u8
            return None
    except (Exception,):
        print('nao tem nome na uri, ', id_url)
        return None


def save_link_channel_topcanais(canal, id_url):
    m3u8 = get_m3u8_topcanais(id_url)
    headers = {'origin': 'https://topcanais.com', 'referer': 'https://topcanais.com/'}
    if check_m3u8_req(m3u8, headers=headers):
        try:
            link = Link()
            link.url = id_url
            link.channel = canal
            link.m3u8 = m3u8
            link.save()
        except (Exception):
            print('erro ao salvar link')


def save_link_channel(canal, id_url):
    m3u8, swarmId = get_m3u8_and_swarmid(id_url)
    headers = {'origin': 'https://canaismax.com', 'referer': 'https://canaismax.com/',
               'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36}'}
    if check_m3u8_req(m3u8, headers):
        try:
            link = Link()
            link.url = id_url
            link.channel = canal
            link.m3u8 = m3u8
            link.swarmId = swarmId
            link.save()
        except (Exception,):
            print('erro ao salvar link')


def contain_http(uri):
    if str(uri).startswith('http'):
        return True
    return False


def from_char_code(*args):
    return ''.join(map(unichr, args))


def get_m3u8_aovivogratis_by_eval(url):
    source = get_source_script_aovivogratis(url)
    index_init = source.index('player.src({src:') + len('player.src({src:')
    index_end = source.index(',type:')
    item = source[index_init:index_end]
    replaced_item = item.replace('String.fromCharCode(', 'from_char_code(')
    string = 'https:' + str(eval(replaced_item))
    return string


def get_source_script_aovivogratis(uri):
    headers = {'referer': 'https://www.tibiadown.com/', 'authority': 'player.aovivotv.xyz'}
    req = requests.get(uri, headers=headers)
    if req.status_code == 200:
        page = BeautifulSoup(req.text, 'html.parser')
        scripts = [scr for scr in page.select('script') if 'eval(function(' in str(scr)]
        if len(scripts) > 0:
            script = str(scripts[0].string)
            if packer.detect(script):
                unpacked = packer.unpack(script)
                return unpacked
    return ''

def get_uri_stream_multicanais(string):
    md5_pos = string.index('md5')
    new_str = string[:md5_pos]+'&'+string[md5_pos:]
    return new_str

def get_token_multicanais(canal):
    headers = {'origin': 'https://esporteone.com', 'referer': 'https://esporteone.com'}
    req = requests.post('https://esporteone.com/get_token.php', {'canal': canal}, headers=headers)
    # req = requests.post('https://esporteone.com/app/stream/get_token.php', {'canal': canal}, headers=headers)
    if req.status_code == 200:
        return get_uri_stream_multicanais(req.json()['stream'])
    else:
        return None


def get_m3u8_multicanais(id_url, select_server='tvfolha.com'):
    # arr_sites = ['assistirbbb.com', 'multicanais.org', 'mundobbb.com']
    arr_sites = ['esporteone.com', 'multicanais.com', ]
    string_canal_id = '.php?canal='
    string_referer = 'player.php?id='
    uri = str(id_url)
    try:
        index_prefix = uri.index(string_canal_id)
        index_referer = uri.index(string_referer)
        if index_prefix > -1:
            name_channel = uri[index_prefix + len(string_canal_id):len(id_url)]
            referer = uri[index_referer + len(string_referer):]
            headers = {'origin': 'https://esporteone.com', 'referer': str(referer),
                       'accept': 'application/json',
                       "accept-language": "pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7",
                       "content-type": "application/x-www-form-urlencoded", "sec-fetch-dest": "empty",
                       "sec-fetch-mode": "cors", "sec-fetch-site": "cross-site",
                       'Host': 'cdn.esporteone.com',
                       'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'}
            select_server = random.choice(arr_sites)
            m3u8_uri = get_token_multicanais(name_channel)
            # token = get_token_multicanais(name_channel)
            # m3u8_uri = "https://live." + str(select_server) + "/" + name_channel + "/video.m3u8?token=" + str(token)
            # m3u8_uri = "http://cdn." + str(select_server) + "/" + name_channel + "/video.m3u8"
            # i = 0
            # while i < 3:
            #     if check_m3u8_req(m3u8_uri, headers=headers):
            #         break
            #     else:
            #         select_server = random.choice(arr_sites)
            #         m3u8_uri = "https://cdn." + str(select_server) + "/" + name_channel + "/video.m3u8"
            #         i = i + 1
            if check_m3u8_req(m3u8_uri, headers=headers):
                return m3u8_uri
            else:
                return ''
        else:
            return ''
    except (ValueError,):
        pass


def get_m3u8_and_swarmid(id_url):
    try:
        miner_req = get_page_bs4(id_url)
        if miner_req:
            script = None
            for scr in miner_req.select('script'):
                if 'document.referrer' in str(scr):
                    script = scr
            content_script = str(script)
            string_source = 'source: "'
            string_m3u8 = '.m3u8'
            string_swarmid = "swarmId: '"
            options_end_swarm = ["max'", "mycdn'"]
            string_end_swarm = options_end_swarm[0]
            swarm_indexes = [m.start() for m in
                             re.finditer(string_swarmid, content_script)]
            swarm_end_indexes = []
            for opt in options_end_swarm:
                aux = [m.start() for m in
                       re.finditer(opt, content_script)]
                if len(aux) > 0:
                    string_end_swarm = opt
                    swarm_end_indexes = aux
            sources_indexes = [m.start() for m in
                               re.finditer(string_source, content_script)]
            m3u8_indexes = [m.start() for m in
                            re.finditer(string_m3u8, content_script)]
            strings = [
                content_script[(int(sources_indexes[i]) + len(string_source)):(int(m3u8_indexes[i]) + len(string_m3u8))]
                for i in range(len(sources_indexes))]
            swarm_id = None
            if len(swarm_end_indexes) > 0:
                swarm_id = [content_script[
                            (int(swarm_indexes[ind]) + len(string_swarmid)):(
                                    int(swarm_end_indexes[ind]) + (len(string_end_swarm) - 1))] for ind in
                            range(len(swarm_end_indexes))]
            if len(strings) > 0:
                if swarm_id:
                    if len(swarm_id) > 0:
                        return strings[0], swarm_id[0]
                return strings[0], ''
            return '', ''
    except (Exception,):
        return '', ''


def make_ids_topcanais(atags):
    ids = []
    for a in atags:
        if a.has_attr('data-id'):
            data_id = str(a['data-id'])
            data_pasta = str(a['data-pasta'])
            url_id = 'https://topcanais.com/player/aovivo.php?canal=' + data_id + '&pasta=' + data_pasta
            if url_id:
                ids.append(url_id)
    return ids


def make_ids_multicanais(atags):
    ids = []
    for a in atags:
        if a.has_attr('data-id'):
            data_id = str(a['data-id'])
            if 'http' in data_id:
                url_id = 'https://multicanais.com/player.php?id=' + data_id
                ids.append(url_id)
    return ids


def make_ids(atags):
    ids = []
    for a in atags:
        if a.has_attr('data-link'):
            data_id = str(a['data-link'])
            if 'op=' in data_id:
                third_page_temp = get_page_bs4(data_id)
                if third_page_temp:
                    div_buttons = third_page_temp.find('div',
                                                       attrs={
                                                           'class': 'buttons-quality'})
                    if div_buttons:
                        novos_links = div_buttons.find_all('a')
                        if len(novos_links) > 0:
                            for alinks_temp in novos_links:
                                if alinks_temp.has_attr('href'):
                                    alink_temp_url = str(alinks_temp['href'])
                                    ids.append(alink_temp_url)
            else:
                ids.append(data_id)
    return ids


def get_date_now():
    now = datetime.datetime.now()
    month = str("0") + str(now.month) if now.month < 10 else now.month
    day = str("0") + str(now.day) if now.day < 10 else now.day
    return '%s-%s-%s' % (now.year, month, day)


def request_json():
    api_url = 'https://canaismax.com/api/programacao'
    req = requests.get(api_url)
    if req.status_code == 200:
        json = req.json()
        return json
    return None


def check_m3u8_req(uri, headers):
    try:
        req = requests.get(uri, headers=headers, timeout=2, verify=False)
        if req.status_code == 200:
            return True
        return False
    except (Exception,):
        print('BREAK m3u8')
        return False


def remove_iv(array_uri):
    for i in range(len(array_uri)):
        if '",IV' in str(array_uri[i]):
            index_iv = str(array_uri[i]).index('",IV=')
            if index_iv >= 0:
                array_uri[i] = str(array_uri[i])[:index_iv]
    return array_uri


def get_text_type(link):
    uri = str(link.m3u8)
    if 'sd/' in uri:
        return 'SD'
    elif 'hd/' in uri:
        return 'HD'
    else:
        return None


def clean_title(channel):
    title = str(channel.title)
    if 'assistir ' in title.lower():
        if ' ao ' in title.lower():
            title = title[(title.lower().index('assistir ') + len('assistir ')):title.lower().index(' ao ')]
        else:
            title = title[(title.lower().index('assistir ') + len('assistir ')):]
    if ' ao' in title.lower():
        title = title[:title.lower().index(' ao ')]
    if ' online' in title.lower():
        title = title[:title.lower().index(' online')]
    return title


def films_get_playfilms():
    uri = 'https://filmplay.biz/filmes/page/1'  # iter page
    req = requests.get(uri)
    page = BeautifulSoup(req.text, 'html.parser')
    tag_movies = page.select('.movies')
    movies = [tag.select('div.poster>a')[0]['href'] for tag in tag_movies]
    for link_movie in movies:
        req = requests.get(link_movie)
        page = BeautifulSoup(req.text, 'html.parser')
        link_id_movie = str(page.select('link[rel="shortlink"]')[0]['href'])
        id_movie = link_id_movie[link_id_movie.index('p=') + len('p='):]
        req = requests.get('https://filmplay.biz/wp-json/dooplayer/v1/post/' + id_movie + '?type=movie&source=1')
        json = req.json()
        req = requests.get(json['embed_url'])
        page = BeautifulSoup(req.text, 'html.parser')
        iframe = page.find('iframe')
        url_iframe = iframe['src']
        req = requests.get(url_iframe)
        page = BeautifulSoup(req.text, 'html.parser')
        string_init = "addiframe"
        string_end = "Now"
        script = [scr for scr in page.select('script') if string_init in str(scr)][0]
        script = str(script).replace('\n', '').replace('\t', '').replace('\r', '')
        init_index = [m.start() for m in re.finditer(string_init, script)]
        end_index = [m.start() for m in re.finditer(string_end, script)]
        strings = [script[(int(init_index[i]) + len(string_init)):int(end_index[i])] for i in range(len(init_index))]
        link_regex = re.compile('((https?):((//)|(\\\\))+([\w\d:#@%/;$()~_?\+-=\\\.&](#!)?)*)', re.DOTALL)
        p = [re.findall(link_regex, st) for st in strings]
        links_video = [arr[0][0] for arr in p[:len(p) - 1]]
        for link_video in links_video:
            req = requests.get(link_video)
            page = BeautifulSoup(req.text, 'html.parser')
            iframe_video = page.find('iframe')
            url_iframe_video = iframe_video['src']
            req = requests.get(url_iframe_video)
            page = BeautifulSoup(req.text, 'html.parser')
