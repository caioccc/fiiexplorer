# coding=utf-8
import logging
import requests
from bs4 import BeautifulSoup

from app.models import Fundo, Historico

sync_urls_delay = 30
check_new_minig_requests_delay = 86400

logger = logging.getLogger(__name__)


def dict_gen(curs):
    ''' From Python Essential Reference by David Beazley
    '''
    import itertools
    field_names = [d[0].lower() for d in curs.description]
    while True:
        rows = curs.fetchmany()
        if not rows: return
        for row in rows:
            yield dict(itertools.izip(field_names, row))


def safe_unicode(obj, *args):
    """ return the unicode representation of obj """
    try:
        return unicode(obj, *args)
    except UnicodeDecodeError:
        # obj is byte string
        ascii_text = str(obj).encode('string_escape')
        return unicode(ascii_text)


def safe_str(obj):
    """ return the byte string representation of obj """
    try:
        return str(obj)
    except UnicodeEncodeError:
        # obj is unicode
        return unicode(obj).encode('unicode_escape')


class CommonMiner():
    def dadoscheckna(self, page, marker_html='', clazz_name=''):
        return False

    def checkna(self, page, limit_list=0, marker_html='', clazz_name=''):
        return False

    def get_url_no_bars_last(self, url):
        if url[len(url) - 1] == '/':
            url = url[:-1]
        return url

    def get_page_bs4(self, url):
        req = requests.get(url)
        if req.status_code == 200:
            page = BeautifulSoup(req.text, 'html.parser')
            return page
        return None

    def get_funds(self, page):
        lista = page.find_all('span', {'class': 'symbol'})
        l_funds = []
        if len(lista) > 0:
            for item in lista:
                l_funds.append(item.text)
        print(len(l_funds))
        return l_funds

    def get_sigla(self, page):
        return ''

    def get_nome(self, page):
        return ''

    def get_preco(self, page):
        return ''

    def get_oscilacao_dia(self, page):
        return ''

    def get_liquidez(self, page):
        return ''

    def get_ultimo_rendimento(self, page):
        return ''

    def get_dy(self, page):
        return ''

    def get_pl(self, page):
        return ''

    def get_rentabilidade_mes(self, page):
        return ''

    def get_descricao(self, page):
        return ''

    def get_data_construcao_fundo(self, page):
        return ''

    def get_num_cotas_emitidas(self, page):
        return ''

    def get_vi_cota(self, page):
        return ''

    def get_tipo_gestao(self, page):
        return ''

    def get_publico_alvo(self, page):
        return ''

    def get_mandato(self, page):
        return ''

    def get_segmento(self, page):
        return ''

    def get_prazo_duracao(self, page):
        return ''

    def get_taxa_adm(self, page):
        return ''

    def get_yd_1(self, page):
        return ''

    def get_yd_3(self, page):
        return ''

    def get_yd_6(self, page):
        return ''

    def get_yd_12(self, page):
        return ''

    def get_yd_1_p(self, page):
        return ''

    def get_yd_3_p(self, page):
        return ''

    def get_yd_6_p(self, page):
        return ''

    def get_yd_12_p(self, page):
        return ''

    def get_num_ativos(self, page):
        return ''

    def get_num_estados(self, page):
        return ''


class Miner(CommonMiner):
    def check_fundo_exists(self, fund):
        fundos = Fundo.objects.filter(sigla=fund)
        if len(fundos) > 0:
            return True
        return False

    def mine(self):
        url_init = 'https://www.fundsexplorer.com.br/funds'
        site_initial = self.get_page_bs4(url_init)
        if site_initial:
            funds = self.get_funds(site_initial)
            print('Total of Funds: ' + str(len(funds)))
            for fund in funds:
                if self.check_fundo_exists(fund):
                    print('Fundo ja existe: ', fund)
                    continue
                fund_url = url_init + '/' + fund
                page_fund = self.get_page_bs4(fund_url)
                if page_fund:
                    print('Fundo: ', fund)
                    if self.checkna(page_fund, 7, 'span', 'indicator-value'):
                        continue
                    nome = self.get_nome(page_fund)
                    sigla = self.get_sigla(page_fund)
                    preco = self.get_preco(page_fund)
                    oscilacao_dia = self.get_oscilacao_dia(page_fund)
                    liquidez = self.get_liquidez(page_fund)
                    ultimo_rendimento = self.get_ultimo_rendimento(page_fund)
                    dy = self.get_dy(page_fund)
                    pl = self.get_pl(page_fund)
                    rentabilidade_mes = self.get_rentabilidade_mes(page_fund)
                    descricao = self.get_descricao(page_fund)
                    data_construcao_fundo = self.get_data_construcao_fundo(page_fund)
                    num_cotas_emitidas = self.get_num_cotas_emitidas(page_fund)
                    vi_cota = self.get_vi_cota(page_fund)
                    tipo_gestao = self.get_tipo_gestao(page_fund)
                    publico_alvo = self.get_publico_alvo(page_fund)
                    mandato = self.get_mandato(page_fund)
                    segmento = self.get_segmento(page_fund)
                    prazo_duracao = self.get_prazo_duracao(page_fund)
                    taxa_adm = self.get_taxa_adm(page_fund)
                    yd_1 = self.get_yd_1(page_fund)
                    yd_3 = self.get_yd_3(page_fund)
                    yd_6 = self.get_yd_6(page_fund)
                    yd_12 = self.get_yd_12(page_fund)
                    yd_1_p = self.get_yd_1_p(page_fund)
                    yd_3_p = self.get_yd_3_p(page_fund)
                    yd_6_p = self.get_yd_6_p(page_fund)
                    yd_12_p = self.get_yd_12_p(page_fund)
                    num_ativos = self.get_num_ativos(page_fund)
                    num_estados = self.get_num_estados(page_fund)
                    print('Minerado: ', sigla)
                    fundo = Fundo(nome=nome, sigla=sigla, preco=preco, oscilacao_dia=oscilacao_dia, liquidez=liquidez,
                                  ultimo_rendimento=ultimo_rendimento, dy=dy, pl=pl,
                                  rentabilidade_mes=rentabilidade_mes, descricao=descricao,
                                  data_construcao_fundo=data_construcao_fundo, num_cotas_emitidas=num_cotas_emitidas,
                                  vi_cota=vi_cota, tipo_gestao=tipo_gestao, publico_alvo=publico_alvo,
                                  mandato=mandato, segmento=segmento, prazo_duracao=prazo_duracao, taxa_adm=taxa_adm,
                                  yd_1=yd_1, yd_3=yd_3, yd_6=yd_6, yd_12=yd_12, yd_1_p=yd_1_p, yd_3_p=yd_3_p,
                                  yd_6_p=yd_6_p, yd_12_p=yd_12_p, num_ativos=num_ativos, num_estados=num_estados,
                                  url=fund_url)
                    fundo.save()
                else:
                    print('Nao foi possivel abrir a page do fundo: ', str(fund_url))
            return True
        else:
            print('Nao foi possivel abrir a page site: ', str(url_init))
            return False


class Reader(CommonMiner):
    def sync(self, fundo):
        url = fundo.url
        try:
            page = self.get_page_bs4(url)
            if page:
                novo_preco = self.get_preco(page)
                oscilacao_dia = self.get_oscilacao_dia(page)
                liquidez = self.get_liquidez(page)
                ultimo_rendimento = self.get_ultimo_rendimento(page)
                dy = self.get_dy(page)
                pl = self.get_pl(page)
                rentabilidade_mes = self.get_rentabilidade_mes(page)
                yd_1 = self.get_yd_1(page)
                yd_3 = self.get_yd_3(page)
                yd_6 = self.get_yd_6(page)
                yd_12 = self.get_yd_12(page)
                yd_1_p = self.get_yd_1_p(page)
                yd_3_p = self.get_yd_3_p(page)
                yd_6_p = self.get_yd_6_p(page)
                yd_12_p = self.get_yd_12_p(page)
                num_ativos = self.get_num_ativos(page)
                num_estados = self.get_num_estados(page)
                print('ID: ', fundo.id, ', Fundo: ', fundo.sigla, ' URL: ', url)
                preco_fundo_db = fundo.preco
                if fundo.historico_set.count() == 0:
                    first_hist = Historico(fund=fundo,
                                           preco=novo_preco,
                                           oscilacao_dia=oscilacao_dia,
                                           liquidez=liquidez,
                                           ultimo_rendimento=ultimo_rendimento,
                                           dy=dy,
                                           pl=fundo.pl,
                                           rentabilidade_mes=rentabilidade_mes,
                                           yd_1=yd_1,
                                           yd_3=yd_3,
                                           yd_6=yd_6,
                                           yd_12=yd_12,
                                           yd_1_p=yd_1_p,
                                           yd_3_p=yd_3_p,
                                           yd_6_p=yd_6_p,
                                           yd_12_p=yd_12_p,
                                           num_ativos=num_ativos,
                                           num_estados=num_estados
                                           )
                    first_hist.save()
                try:
                    if float(novo_preco) > float(preco_fundo_db) or float(novo_preco) < float(preco_fundo_db):
                        fundo.preco = float(novo_preco)
                        fundo.oscilacao_dia = float(oscilacao_dia)
                        fundo.liquidez = int(liquidez)
                        fundo.ultimo_rendimento = float(ultimo_rendimento)
                        fundo.dy = float(dy)
                        fundo.pl = str(pl)
                        fundo.rentabilidade_mes = float(rentabilidade_mes)
                        fundo.yd_1 = float(yd_1)
                        fundo.yd_3 = float(yd_3)
                        fundo.yd_6 = float(yd_6)
                        fundo.yd_12 = float(yd_12)
                        fundo.yd_1_p = float(yd_1_p)
                        fundo.yd_3_p = float(yd_3_p)
                        fundo.yd_6_p = float(yd_6_p)
                        fundo.yd_12_p = float(yd_12_p)
                        fundo.num_ativos = int(num_ativos)
                        fundo.num_estados = int(num_estados)
                        fundo.save()
                        print('CHANGED PRICE: ', fundo.sigla, fundo.preco)
                        hist = Historico(fund=fundo,
                                         preco=novo_preco,
                                         oscilacao_dia=oscilacao_dia,
                                         liquidez=liquidez,
                                         ultimo_rendimento=ultimo_rendimento,
                                         dy=dy,
                                         pl=fundo.pl,
                                         rentabilidade_mes=rentabilidade_mes,
                                         yd_1=yd_1,
                                         yd_3=yd_3,
                                         yd_6=yd_6,
                                         yd_12=yd_12,
                                         yd_1_p=yd_1_p,
                                         yd_3_p=yd_3_p,
                                         yd_6_p=yd_6_p,
                                         yd_12_p=yd_12_p,
                                         num_ativos=num_ativos,
                                         num_estados=num_estados
                                         )
                        hist.save()
                    elif float(ultimo_rendimento) > float(fundo.ultimo_rendimento) or \
                            float(ultimo_rendimento) < float(fundo.ultimo_rendimento):
                        fundo.preco = novo_preco
                        fundo.oscilacao_dia = oscilacao_dia
                        fundo.liquidez = liquidez
                        fundo.ultimo_rendimento = ultimo_rendimento
                        fundo.dy = dy
                        fundo.pl = pl
                        fundo.rentabilidade_mes = rentabilidade_mes
                        fundo.yd_1 = yd_1
                        fundo.yd_3 = yd_3
                        fundo.yd_6 = yd_6
                        fundo.yd_12 = yd_12
                        fundo.yd_1_p = yd_1_p
                        fundo.yd_3_p = yd_3_p
                        fundo.yd_6_p = yd_6_p
                        fundo.yd_12_p = yd_12_p
                        fundo.num_ativos = num_ativos
                        fundo.num_estados = num_estados
                        fundo.save()
                        print('CHANGED PRICE: ', fundo.sigla, fundo.preco)
                        hist = Historico(fund=fundo,
                                         preco=novo_preco,
                                         oscilacao_dia=oscilacao_dia,
                                         liquidez=liquidez,
                                         ultimo_rendimento=ultimo_rendimento,
                                         dy=dy,
                                         pl=fundo.pl,
                                         rentabilidade_mes=rentabilidade_mes,
                                         yd_1=yd_1,
                                         yd_3=yd_3,
                                         yd_6=yd_6,
                                         yd_12=yd_12,
                                         yd_1_p=yd_1_p,
                                         yd_3_p=yd_3_p,
                                         yd_6_p=yd_6_p,
                                         yd_12_p=yd_12_p,
                                         num_ativos=num_ativos,
                                         num_estados=num_estados
                                         )
                        hist.save()
                except:
                    logger.debug(
                        'Erro ao tentar checar novo preco do Fundo: ' + fundo.sigla)
        except:
            logger.info('PAGE NOT EXISTS: ' + fundo.url)

        """
        to = 'caiomarinho8@gmail.com'
        gmail_user = 'caiomarinho8@gmail.com'
        gmail_pwd = 'izszygyncvtfwicz'
        smtpserver = smtplib.SMTP("smtp.gmail.com",587)
        smtpserver.ehlo()
        smtpserver.starttls()
        smtpserver.ehlo
        smtpserver.login(gmail_user, gmail_pwd)
        header = 'To:' + to + '\n' + 'From: ' + gmail_user + '\n' + 'Subject:'+label+' - '+safe_str(title)+' \n'
        msg = header + '\n Price changed from '+str(dbprice)+' to '+str(price)+' \n\n'
        msg = msg + '\n\n '+url+' \n\n'
        smtpserver.sendmail(gmail_user, to, msg)
        smtpserver.close()"""
