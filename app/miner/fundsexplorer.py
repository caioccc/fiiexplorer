from app.miner.common import Miner, CommonMiner, Reader


class CustomMiner(Miner):
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
        return cot

    def get_yd_6(self, page):
        yd = page.find_all('td')[3].text.replace('R$ ', '').replace('.', '').replace(',', '.')
        return yd

    def get_taxa_adm(self, page):
        tx = page.find_all('span', {'class': 'description'})[11].text.strip()
        return tx

    def get_prazo_duracao(self, page):
        pra = page.find_all('span', {'class': 'description'})[10].text.replace('\n', '').replace('\n', ''). \
            replace('R$ ', '').replace('R$', '').replace(',', '.').replace('.', '').strip()
        return pra

    def get_liquidez(self, page):
        liq = page.find_all('span', {'class': 'indicator-value'})[0]
        it_format = liq.text.replace(' ', '').replace('\n', '').replace('.', '') \
            .replace('R$', '').replace('R$ ', '').replace('%', '').replace(',', '.')
        return it_format

    def get_yd_3_p(self, page):
        yd = page.find_all('td')[8].text.replace('R$ ', '').replace('.', '').replace(',', '.').replace('%', '')
        return yd

    def get_yd_1_p(self, page):
        yd = page.find_all('td')[7].text.replace('R$ ', '').replace('.', '').replace(',', '.').replace('%', '')
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
        return it_format

    def get_yd_1(self, page):
        yd = page.find_all('td')[1].text.replace('R$ ', '').replace('.', '').replace(',', '.').replace('%', '')
        return yd

    def get_segmento(self, page):
        seg = page.find_all('span', {'class': 'description'})[9].text.replace('\n', '').replace('\n', ''). \
            replace('R$ ', '').replace('R$', '').replace(',', '.').replace('.', '').strip()
        return seg

    def get_descricao(self, page):
        if  page.find('div', {'id': 'description-content-description'}):
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
            replace('R$ ', '').replace('R$', '').replace(',', '.').replace(' ', '')
        return vi

    def get_ultimo_rendimento(self, page):
        ult = page.find_all('span', {'class': 'indicator-value'})[1]
        it_format = ult.text.replace(' ', '').replace('\n', '').replace('.', '') \
            .replace('R$', '').replace('R$ ', '').replace('%', '').replace(',', '.')
        return it_format

    def get_yd_6_p(self, page):
        yd = page.find_all('td')[9].text.replace('R$ ', '').replace('.', '').replace(',', '.').replace('%', '')
        return yd

    def get_yd_3(self, page):
        yd = page.find_all('td')[2].text.replace('R$ ', '').replace('.', '').replace(',', '.').replace('%', '')
        return yd

    def get_sigla(self, page):
        sigla = page.find('h1', {'class': 'section-title'}).text
        return sigla

    def get_yd_12(self, page):
        yd = page.find_all('td')[4].text.replace('R$ ', '').replace('.', '').replace(',', '.').replace('%', '')
        return yd

    def get_yd_12_p(self, page):
        yd = page.find_all('td')[10].text.replace('R$ ', '').replace('.', '').replace(',', '.').replace('%', '')
        return yd

    def get_rentabilidade_mes(self, page):
        rentab = page.find_all('span', {'class': 'indicator-value'})[5]
        it_format = rentab.text.replace(' ', '').replace('\n', '').replace('.', '') \
            .replace('R$', '').replace('R$ ', '').replace('%', '').replace(',', '.')
        return it_format


class CustomReader(Reader):
    def get_num_estados(self, page):
        try:
            num_estados = int(str(page.find('span', {'class': 'fund-states'}).text).replace(' estado', ''))
            return num_estados
        except (Exception,):
            return ''

    def get_oscilacao_dia(self, page):
        try:
            osc = str(page.find('span', {'class': 'percentage'}).text). \
                replace(' ', '').replace('%', '').replace('.', '').replace(',', '.').replace('\n', '')
            return osc
        except (Exception,):
            return ''

    def get_num_cotas_emitidas(self, page):
        try:
            cot = str(page.find_all('span', {'class': 'description'})[2].text).replace('\n', '').replace('\n', ''). \
                replace('R$ ', '').replace('R$', '').replace(',', '.').replace(' ', '').replace('.', '')
            return cot
        except (Exception,):
            return ''

    def get_yd_6(self, page):
        try:
            yd = str(page.find_all('td')[3].text).replace('R$ ', '').replace('.', '').replace(',', '.')
            return yd
        except (Exception,):
            return ''

    def get_taxa_adm(self, page):
        try:
            tx = page.find_all('span', {'class': 'description'})[11].text.strip()
            return tx
        except (Exception,):
            return ''

    def get_prazo_duracao(self, page):
        try:
            pra = str(page.find_all('span', {'class': 'description'})[10].text).replace('\n', '').replace('\n', ''). \
                replace('R$ ', '').replace('R$', '').replace(',', '.').replace('.', '').strip()
            return pra
        except (Exception,):
            return ''

    def get_liquidez(self, page):
        try:
            liq = page.find_all('span', {'class': 'indicator-value'})[0]
            it_format = str(liq.text).replace(' ', '').replace('\n', '').replace('.', '') \
                .replace('R$', '').replace('R$ ', '').replace('%', '').replace(',', '.')
            return it_format
        except (Exception,):
            return ''

    def get_yd_3_p(self, page):
        try:
            yd = str(page.find_all('td')[8].text).replace('R$ ', '').replace('.', '').replace(',', '.').replace('%', '')
            return yd
        except (Exception,):
            return ''

    def get_yd_1_p(self, page):
        try:
            yd = str(page.find_all('td')[7].text).replace('R$ ', '').replace('.', '').replace(',', '.').replace('%', '')
            return yd
        except (Exception,):
            return ''

    def get_url_no_bars_last(self, url):
        return CommonMiner.get_url_no_bars_last(self, url)

    def get_nome(self, page):
        try:
            nome = page.find('h2', {'class': 'section-subtitle'}).text
            return nome
        except (Exception,):
            return ''

    def get_num_ativos(self, page):
        try:
            num_estados = int(str(page.find('span', {'class': 'fund-actives'}).text).replace(' ativo', ''))
            return num_estados
        except (Exception,):
            return ''

    def get_dy(self, page):
        try:
            dy = page.find_all('span', {'class': 'indicator-value'})[2]
            it_format = str(dy.text).replace(' ', '').replace('\n', '').replace('.', '') \
                .replace('R$', '').replace('R$ ', '').replace('%', '').replace(',', '.')
            return it_format
        except (Exception,):
            return ''

    def get_yd_1(self, page):
        try:
            yd = str(page.find_all('td')[1].text).replace('R$ ', '').replace('.', '').replace(',', '.').replace('%', '')
            return yd
        except (Exception,):
            return ''

    def get_segmento(self, page):
        try:
            seg = str(page.find_all('span', {'class': 'description'})[9].text).replace('\n', '').replace('\n', ''). \
                replace('R$ ', '').replace('R$', '').replace(',', '.').replace('.', '').strip()
            return seg
        except (Exception,):
            return ''

    def get_descricao(self, page):
        try:
            desc = page.find('div', {'id': 'description-content-description'}).text
            return desc
        except (Exception,):
            return ''

    def get_publico_alvo(self, page):
        try:
            pub = str(page.find_all('span', {'class': 'description'})[7].text).replace('\n', '').replace('\n', ''). \
                replace('R$ ', '').replace('R$', '').replace(',', '.').replace('.', '').strip()
            return pub
        except (Exception,):
            return ''

    def get_pl(self, page):
        try:
            pl = page.find_all('span', {'class': 'indicator-value'})[3]
            it_format = str(pl.text).replace(' ', '').replace('\n', '').replace('.', '') \
                .replace('R$', '').replace('R$ ', '').replace('%', '').replace(',', '.')
            return it_format
        except (Exception,):
            return ''

    def get_preco(self, page):
        try:
            preco = str(page.find('span', {'class': 'price'}).text). \
                replace(' ', '').replace('R$', '').replace('R$ ', ''). \
                replace('.', '').replace(',', '.').replace('\n', '')
            return preco
        except (Exception,):
            return ''

    def get_tipo_gestao(self, page):
        try:
            gestao = str(page.find_all('span', {'class': 'description'})[5].text).replace('\n', '').replace('\n', ''). \
                replace('R$ ', '').replace('R$', '').replace(',', '.').replace(' ', '').replace('.', '').strip()
            return gestao
        except (Exception,):
            return ''

    def get_mandato(self, page):
        try:
            pub = str(page.find_all('span', {'class': 'description'})[8].text).replace('\n', '').replace('\n', ''). \
                replace('R$ ', '').replace('R$', '').replace(',', '.').replace('.', '').strip()
            return pub
        except (Exception,):
            return ''

    def get_data_construcao_fundo(self, page):
        try:
            dat = page.find_all('span', {'class': 'description'})[1].text
            return str(dat).replace('\n', '').strip()
        except (Exception,):
            return ''

    def get_vi_cota(self, page):
        try:
            vi = str(page.find_all('span', {'class': 'description'})[4].text).replace('\n', ''). \
                replace('R$ ', '').replace('R$', '').replace(',', '.').replace(' ', '')
            return vi
        except (Exception,):
            return ''

    def get_ultimo_rendimento(self, page):
        try:
            ult = page.find_all('span', {'class': 'indicator-value'})[1]
            it_format = str(ult.text).replace(' ', '').replace('\n', '').replace('.', '') \
                .replace('R$', '').replace('R$ ', '').replace('%', '').replace(',', '.')
            return it_format
        except (Exception,):
            return ''

    def get_yd_6_p(self, page):
        try:
            yd = str(page.find_all('td')[9].text).replace('R$ ', '').replace('.', '').replace(',', '.').replace('%', '')
            return yd
        except (Exception,):
            return ''

    def get_yd_3(self, page):
        try:
            yd = str(page.find_all('td')[2].text).replace('R$ ', '').replace('.', '').replace(',', '.').replace('%', '')
            return yd
        except (Exception,):
            return ''

    def get_sigla(self, page):
        try:
            sigla = page.find('h1', {'class': 'section-title'}).text
            return sigla
        except (Exception,):
            return ''

    def get_yd_12(self, page):
        try:
            yd = str(page.find_all('td')[4].text).replace('R$ ', '').replace('.', '').replace(',', '.').replace('%', '')
            return yd
        except (Exception,):
            return ''

    def get_yd_12_p(self, page):
        try:
            yd = str(page.find_all('td')[10].text).replace('R$ ', '').replace('.', '').replace(',', '.').replace('%',
                                                                                                                 '')
            return yd
        except (Exception,):
            return ''

    def get_rentabilidade_mes(self, page):
        try:
            rentab = page.find_all('span', {'class': 'indicator-value'})[5]
            it_format = str(rentab.text).replace(' ', '').replace('\n', '').replace('.', '') \
                .replace('R$', '').replace('R$ ', '').replace('%', '').replace(',', '.')
            return it_format
        except (Exception,):
            return ''
