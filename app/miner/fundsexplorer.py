from app.miner.common import Miner, CommonMiner, Reader


class CustomMiner(Miner):
    def dadoscheckna(self, page, marker_html='', clazz_name=''):
        lista = page.find_all(marker_html, {'class': clazz_name})
        for item in lista:
            it = item.text.replace(' ', '').replace('\n', '').replace('.', '') \
                .replace('R$', '').replace('R$ ', '').replace('%', '').replace(',', '.').strip()
            if (str('N/A').lower() in it.lower()):
                return True
        return False

    def checkna(self, page, limit_list=0, marker_html='', clazz_name=''):
        lista = page.find_all(marker_html, {'class': clazz_name})
        if len(lista) < limit_list:
            return True
        if 'n/a' in lista[1].text.replace(' ', '').replace('\n', '').replace('.', '') \
                .replace('R$', '').replace('R$ ', '').replace('%', '').replace(',', '.').lower():
            return True
        if float(lista[1].text.replace(' ', '').replace('\n', '').replace('.', '') \
                         .replace('R$', '').replace('R$ ', '').replace('%', '').replace(',', '.')) <= float(0.00):
            return True
        for item in lista:
            it = item.text.replace(' ', '').replace('\n', '').replace('.', '') \
                .replace('R$', '').replace('R$ ', '').replace('%', '').replace(',', '.')
            if (str('N/A').lower() in it.lower()):
                return True
        return False

    def get_num_estados(self, page):
        if page.find('span', {'class': 'fund-states'}):
            num_estados = int(page.find('span', {'class': 'fund-states'}).text.replace(' estados', '')
                              .replace(' estado', ''))
        elif page.find('div', {'id': 'fund-actives-chart-info-wrapper'}):
            num_estados = int(page.find('div', {'id': 'fund-actives-chart-info-wrapper'}).find_all('span')[1].text
                              .replace(' estados', '').replace(' estado', ''))
        else:
            num_estados = 0
        return num_estados

    def get_oscilacao_dia(self, page):
        osc = page.find('span', {'class': 'percentage'}).text. \
            replace(' ', '').replace('%', '').replace('.', '').replace(',', '.').replace('\n', '')
        return osc

    def get_num_cotas_emitidas(self, page):
        cot = page.find_all('span', {'class': 'description'})[2].text.replace('\n', '').replace('\n', ''). \
            replace('R$ ', '').replace('R$', '').replace(',', '.').replace(' ', '').replace('.', '')
        if (str('N/A').lower() in cot.lower()):
            return '0'
        return cot

    def get_yd_6(self, page):
        yd = page.find_all('td')[3].text.replace('R$ ', '').replace('.', '').replace(',', '.')
        if (str('N/A').lower() in yd.lower()):
            return '0'
        return yd

    def get_taxa_adm(self, page):
        tx = page.find_all('span', {'class': 'description'})[11].text.strip()
        if (str('N/A').lower() in tx.lower()):
            return '0'
        return tx

    def get_prazo_duracao(self, page):
        pra = page.find_all('span', {'class': 'description'})[10].text.replace('\n', '').replace('\n', ''). \
            replace('R$ ', '').replace('R$', '').replace(',', '.').replace('.', '').strip()
        return pra

    def get_liquidez(self, page):
        liq = page.find_all('span', {'class': 'indicator-value'})[0]
        it_format = liq.text.replace(' ', '').replace('\n', '').replace('.', '') \
            .replace('R$', '').replace('R$ ', '').replace('%', '').replace(',', '.')
        if (str('N/A').lower() in it_format.lower()):
            return '0'
        return it_format

    def get_yd_3_p(self, page):
        yd = page.find_all('td')[8].text.replace('R$ ', '').replace('.', '').replace(',', '.').replace('%', '')
        if (str('N/A').lower() in yd.lower()):
            return '0'
        return yd

    def get_yd_1_p(self, page):
        yd = page.find_all('td')[7].text.replace('R$ ', '').replace('.', '').replace(',', '.').replace('%', '')
        if (str('N/A').lower() in yd.lower()):
            return '0'
        return yd

    def get_nome(self, page):
        nome = page.find('h2', {'class': 'section-subtitle'}).text
        return nome

    def get_num_ativos(self, page):
        if page.find('span', {'class': 'fund-actives'}):
            num_estados = int(page.find('span', {'class': 'fund-actives'}).text.replace(' ativos', '')
                              .replace(' ativo', ''))
        elif page.find('div', {'id': 'fund-actives-chart-info-wrapper'}):
            num_estados = int(page.find('div', {'id': 'fund-actives-chart-info-wrapper'}).span.text
                              .replace(' ativos', '').replace(' ativo', ''))
        else:
            num_estados = 0
        return num_estados

    def get_dy(self, page):
        dy = page.find_all('span', {'class': 'indicator-value'})[2]
        it_format = dy.text.replace(' ', '').replace('\n', '').replace('.', '') \
            .replace('R$', '').replace('R$ ', '').replace('%', '').replace(',', '.')
        if (str('N/A').lower() in it_format.lower()):
            return '0'
        return it_format

    def get_yd_1(self, page):
        yd = page.find_all('td')[1].text.replace('R$ ', '').replace('.', '').replace(',', '.').replace('%', '')
        if (str('N/A').lower() in yd.lower()):
            return '0'
        return yd

    def get_segmento(self, page):
        seg = page.find_all('span', {'class': 'description'})[9].text.replace('\n', '').replace('\n', ''). \
            replace('R$ ', '').replace('R$', '').replace(',', '.').replace('.', '').strip()
        return seg

    def get_descricao(self, page):
        if page.find('div', {'id': 'description-content-description'}):
            desc = page.find('div', {'id': 'description-content-description'}).text
        else:
            desc = ''
        return desc

    def get_publico_alvo(self, page):
        pub = page.find_all('span', {'class': 'description'})[7].text.replace('\n', '').replace('\n', ''). \
            replace('R$ ', '').replace('R$', '').replace(',', '.').replace('.', '').strip()
        return pub

    def get_pl(self, page):
        pl = page.find_all('span', {'class': 'indicator-value'})[3]
        it_format = pl.text.replace(' ', '').replace('\n', '').replace('.', '') \
            .replace('R$', '').replace('R$ ', '').replace('%', '').replace(',', '.')
        return it_format

    def get_preco(self, page):
        preco = page.find('span', {'class': 'price'}).text. \
            replace(' ', '').replace('R$', '').replace('R$ ', ''). \
            replace('.', '').replace(',', '.').replace('\n', '')
        return preco

    def get_tipo_gestao(self, page):
        gestao = page.find_all('span', {'class': 'description'})[5].text.replace('\n', '').replace('\n', ''). \
            replace('R$ ', '').replace('R$', '').replace(',', '.').replace(' ', '').replace('.', '').strip()
        return gestao

    def get_mandato(self, page):
        pub = page.find_all('span', {'class': 'description'})[8].text.replace('\n', '').replace('\n', ''). \
            replace('R$ ', '').replace('R$', '').replace(',', '.').replace('.', '').strip()
        return pub

    def get_data_construcao_fundo(self, page):
        dat = page.find_all('span', {'class': 'description'})[1].text
        return dat.replace('\n', '').strip()

    def get_vi_cota(self, page):
        vi = page.find_all('span', {'class': 'description'})[4].text.replace('\n', ''). \
            replace('R$ ', '').replace('R$', '').replace('.', '').replace(',', '.').replace(' ', '')
        if (str('N/A').lower() in vi.lower()):
            return '0'
        return vi

    def get_ultimo_rendimento(self, page):
        ult = page.find_all('span', {'class': 'indicator-value'})[1]
        it_format = ult.text.replace(' ', '').replace('\n', '').replace('.', '') \
            .replace('R$', '').replace('R$ ', '').replace('%', '').replace(',', '.')
        return it_format

    def get_yd_6_p(self, page):
        yd = page.find_all('td')[9].text.replace('R$ ', '').replace('.', '').replace(',', '.').replace('%', '')
        if (str('N/A').lower() in yd.lower()):
            return '0'
        return yd

    def get_yd_3(self, page):
        yd = page.find_all('td')[2].text.replace('R$ ', '').replace('.', '').replace(',', '.').replace('%', '')
        if (str('N/A').lower() in yd.lower()):
            return '0'
        return yd

    def get_sigla(self, page):
        sigla = page.find('h1', {'class': 'section-title'}).text
        return sigla

    def get_yd_12(self, page):
        yd = page.find_all('td')[4].text.replace('R$ ', '').replace('.', '').replace(',', '.').replace('%', '')
        if (str('N/A').lower() in yd.lower()):
            return '0'
        return yd

    def get_yd_12_p(self, page):
        yd = page.find_all('td')[10].text.replace('R$ ', '').replace('.', '').replace(',', '.').replace('%', '')
        if (str('N/A').lower() in yd.lower()):
            return '0'
        return yd

    def get_rentabilidade_mes(self, page):
        rentab = page.find_all('span', {'class': 'indicator-value'})[5]
        it_format = rentab.text.replace(' ', '').replace('\n', '').replace('.', '') \
            .replace('R$', '').replace('R$ ', '').replace('%', '').replace(',', '.')
        return it_format


class CustomReader(Reader):
    def dadoscheckna(self, page, marker_html='', clazz_name=''):
        lista = page.find_all(marker_html, {'class': clazz_name})
        for item in lista:
            it = item.text.replace(' ', '').replace('\n', '').replace('.', '') \
                .replace('R$', '').replace('R$ ', '').replace('%', '').replace(',', '.').strip()
            if (str('N/A').lower() in it.lower()):
                return True
        return False

    def checkna(self, page, limit_list=0, marker_html='', clazz_name=''):
        lista = page.find_all(marker_html, {'class': clazz_name})
        if len(lista) < limit_list:
            return True
        if 'n/a' in lista[1].text.replace(' ', '').replace('\n', '').replace('.', '') \
                .replace('R$', '').replace('R$ ', '').replace('%', '').replace(',', '.').lower():
            return True
        if float(lista[1].text.replace(' ', '').replace('\n', '').replace('.', '') \
                         .replace('R$', '').replace('R$ ', '').replace('%', '').replace(',', '.')) <= float(0.00):
            return True
        for item in lista:
            it = item.text.replace(' ', '').replace('\n', '').replace('.', '') \
                .replace('R$', '').replace('R$ ', '').replace('%', '').replace(',', '.')
            if (str('N/A').lower() in it.lower()):
                return True
        return False

    def get_num_estados(self, page):
        if page.find('span', {'class': 'fund-states'}):
            num_estados = int(page.find('span', {'class': 'fund-states'}).text.replace(' estados', '')
                              .replace(' estado', ''))
        elif page.find('div', {'id': 'fund-actives-chart-info-wrapper'}):
            num_estados = int(page.find('div', {'id': 'fund-actives-chart-info-wrapper'}).find_all('span')[1].text
                              .replace(' estados', '').replace(' estado', ''))
        else:
            num_estados = 0
        return num_estados

    def get_oscilacao_dia(self, page):
        osc = page.find('span', {'class': 'percentage'}).text. \
            replace(' ', '').replace('%', '').replace('.', '').replace(',', '.').replace('\n', '')
        return osc

    def get_num_cotas_emitidas(self, page):
        cot = page.find_all('span', {'class': 'description'})[2].text.replace('\n', '').replace('\n', ''). \
            replace('R$ ', '').replace('R$', '').replace(',', '.').replace(' ', '').replace('.', '')
        if (str('N/A').lower() in cot.lower()):
            return '0'
        return cot

    def get_yd_6(self, page):
        yd = page.find_all('td')[3].text.replace('R$ ', '').replace('.', '').replace(',', '.')
        if (str('N/A').lower() in yd.lower()):
            return '0'
        return yd

    def get_taxa_adm(self, page):
        tx = page.find_all('span', {'class': 'description'})[11].text.strip()
        if (str('N/A').lower() in tx.lower()):
            return '0'
        return tx

    def get_prazo_duracao(self, page):
        pra = page.find_all('span', {'class': 'description'})[10].text.replace('\n', '').replace('\n', ''). \
            replace('R$ ', '').replace('R$', '').replace(',', '.').replace('.', '').strip()
        return pra

    def get_liquidez(self, page):
        liq = page.find_all('span', {'class': 'indicator-value'})[0]
        it_format = liq.text.replace(' ', '').replace('\n', '').replace('.', '') \
            .replace('R$', '').replace('R$ ', '').replace('%', '').replace(',', '.')
        if (str('N/A').lower() in it_format.lower()):
            return '0'
        return it_format

    def get_yd_3_p(self, page):
        yd = page.find_all('td')[8].text.replace('R$ ', '').replace('.', '').replace(',', '.').replace('%', '')
        if (str('N/A').lower() in yd.lower()):
            return '0'
        return yd

    def get_yd_1_p(self, page):
        yd = page.find_all('td')[7].text.replace('R$ ', '').replace('.', '').replace(',', '.').replace('%', '')
        if (str('N/A').lower() in yd.lower()):
            return '0'
        return yd

    def get_nome(self, page):
        nome = page.find('h2', {'class': 'section-subtitle'}).text
        return nome

    def get_num_ativos(self, page):
        if page.find('span', {'class': 'fund-actives'}):
            num_estados = int(page.find('span', {'class': 'fund-actives'}).text.replace(' ativos', '')
                              .replace(' ativo', ''))
        elif page.find('div', {'id': 'fund-actives-chart-info-wrapper'}):
            num_estados = int(page.find('div', {'id': 'fund-actives-chart-info-wrapper'}).span.text
                              .replace(' ativos', '').replace(' ativo', ''))
        else:
            num_estados = 0
        return num_estados

    def get_dy(self, page):
        dy = page.find_all('span', {'class': 'indicator-value'})[2]
        it_format = dy.text.replace(' ', '').replace('\n', '').replace('.', '') \
            .replace('R$', '').replace('R$ ', '').replace('%', '').replace(',', '.')
        if (str('N/A').lower() in it_format.lower()):
            return '0'
        return it_format

    def get_yd_1(self, page):
        yd = page.find_all('td')[1].text.replace('R$ ', '').replace('.', '').replace(',', '.').replace('%', '')
        if (str('N/A').lower() in yd.lower()):
            return '0'
        return yd

    def get_segmento(self, page):
        seg = page.find_all('span', {'class': 'description'})[9].text.replace('\n', '').replace('\n', ''). \
            replace('R$ ', '').replace('R$', '').replace(',', '.').replace('.', '').strip()
        return seg

    def get_descricao(self, page):
        if page.find('div', {'id': 'description-content-description'}):
            desc = page.find('div', {'id': 'description-content-description'}).text
        else:
            desc = ''
        return desc

    def get_publico_alvo(self, page):
        pub = page.find_all('span', {'class': 'description'})[7].text.replace('\n', '').replace('\n', ''). \
            replace('R$ ', '').replace('R$', '').replace(',', '.').replace('.', '').strip()
        return pub

    def get_pl(self, page):
        pl = page.find_all('span', {'class': 'indicator-value'})[3]
        it_format = pl.text.replace(' ', '').replace('\n', '').replace('.', '') \
            .replace('R$', '').replace('R$ ', '').replace('%', '').replace(',', '.')
        return it_format

    def get_preco(self, page):
        preco = page.find('span', {'class': 'price'}).text. \
            replace(' ', '').replace('R$', '').replace('R$ ', ''). \
            replace('.', '').replace(',', '.').replace('\n', '')
        return preco

    def get_tipo_gestao(self, page):
        gestao = page.find_all('span', {'class': 'description'})[5].text.replace('\n', '').replace('\n', ''). \
            replace('R$ ', '').replace('R$', '').replace(',', '.').replace(' ', '').replace('.', '').strip()
        return gestao

    def get_mandato(self, page):
        pub = page.find_all('span', {'class': 'description'})[8].text.replace('\n', '').replace('\n', ''). \
            replace('R$ ', '').replace('R$', '').replace(',', '.').replace('.', '').strip()
        return pub

    def get_data_construcao_fundo(self, page):
        dat = page.find_all('span', {'class': 'description'})[1].text
        return dat.replace('\n', '').strip()

    def get_vi_cota(self, page):
        vi = page.find_all('span', {'class': 'description'})[4].text.replace('\n', ''). \
            replace('R$ ', '').replace('R$', '').replace('.', '').replace(',', '.').replace(' ', '')
        if (str('N/A').lower() in vi.lower()):
            return '0'
        return vi

    def get_ultimo_rendimento(self, page):
        ult = page.find_all('span', {'class': 'indicator-value'})[1]
        it_format = ult.text.replace(' ', '').replace('\n', '').replace('.', '') \
            .replace('R$', '').replace('R$ ', '').replace('%', '').replace(',', '.')
        return it_format

    def get_yd_6_p(self, page):
        yd = page.find_all('td')[9].text.replace('R$ ', '').replace('.', '').replace(',', '.').replace('%', '')
        if (str('N/A').lower() in yd.lower()):
            return '0'
        return yd

    def get_yd_3(self, page):
        yd = page.find_all('td')[2].text.replace('R$ ', '').replace('.', '').replace(',', '.').replace('%', '')
        if (str('N/A').lower() in yd.lower()):
            return '0'
        return yd

    def get_sigla(self, page):
        sigla = page.find('h1', {'class': 'section-title'}).text
        return sigla

    def get_yd_12(self, page):
        yd = page.find_all('td')[4].text.replace('R$ ', '').replace('.', '').replace(',', '.').replace('%', '')
        if (str('N/A').lower() in yd.lower()):
            return '0'
        return yd

    def get_yd_12_p(self, page):
        yd = page.find_all('td')[10].text.replace('R$ ', '').replace('.', '').replace(',', '.').replace('%', '')
        if (str('N/A').lower() in yd.lower()):
            return '0'
        return yd
