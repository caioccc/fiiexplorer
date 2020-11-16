from django.core.management.base import BaseCommand, CommandError
from app.models import *
from django.contrib.auth.models import User


def create_manual_channels(category):
    arr_names = ['Studio Universal', 'HBO Plus', 'Nat Geo Kids', 'Disney Channel', 'HBO Family', 'Disney Junior',
                 'HBO', 'Fox Premium 2', 'HBO Pop', 'Disney XD', 'Sony', 'Paramount', 'HBO Xtreme',
                 'Telecine Cult', 'Off', 'HBO Mundi', 'Syfy', 'Animal Planet', 'Discovery Science', 'HBO Signature']

    arr_images = ['https://img1.gratispng.com/20180617/fvv/kisspng-universal-studios-hollywood-universal-pictures-uni-universal-studios-5b26dbd2cce012.5243627815292732988392.jpg',
                  'https://img2.gratispng.com/20180806/euw/kisspng-logo-product-design-brand-font-combate-ao-vivo-hd-online-kalentri-2018-5b68ae9e1ee8f5.6751575315335871021266.jpg',
                  'https://cdn.mitvstatic.com/channels/br_nat-geo-kids-hd_m.png',
                  'https://upload.wikimedia.org/wikipedia/commons/thumb/6/6c/2014_Disney_Channel_logo.svg/640px-2014_Disney_Channel_logo.svg.png',
                  'https://upload.wikimedia.org/wikipedia/commons/3/3a/HBO_Family_logo.png',
                  'https://imediatv.com/wp-content/uploads/2018/06/DISNEY-JR-USA.png',
                  'https://cdn.iconscout.com/icon/free/png-256/hbo-1-555167.png',
                  'https://eonteambrasil.com.br/SharedAssets/logo-canais/fox-premium-2.jpg',
                  'https://aovivo.gratis/wp-content/uploads/2020/05/hbopopb.png',
                  'https://aovivo.gratis/wp-content/uploads/2019/07/disneyxd.png',
                  'https://aovivo.gratis/wp-content/uploads/2019/07/sony.png',
                  'https://aovivo.gratis/wp-content/uploads/2019/07/paramount.png',
                  'https://aovivo.gratis/wp-content/uploads/2020/05/hboxtremeb.png',
                  'https://aovivo.gratis/wp-content/uploads/2019/07/tccult.png',
                  'https://aovivo.gratis/wp-content/uploads/2019/07/canaloff.png',
                  'https://aovivo.gratis/wp-content/uploads/2020/05/hbomundib.png',
                  'https://aovivo.gratis/wp-content/uploads/2019/07/syfy.png',
                  'https://aovivo.gratis/wp-content/uploads/2019/07/animalplanet.png',
                  'https://aovivo.gratis/wp-content/uploads/2019/07/discoveryscience.png',
                  'https://aovivo.gratis/wp-content/uploads/2019/07/hbosignature.png'
                  ]
    arr_m3u8 = [
        'https://edge-aws.aovivotv.xyz/hls/s:95.216.15.44:81/studiouniversal_8b4753ed_e9eb602a7c2d9ef490a1a2db36b7fa25e815f289/playlist.m3u8',
        'https://edge-aws.aovivotv.xyz/hls/s:88.198.163.51/hboplus_39dfc9ff_4f3a442ccedb3eccf12548df1aa0fb4189927f7a/playlist.m3u8',
        'https://edge-aws.aovivotv.xyz/hls/s:209.126.108.100:81/natgeokids_8746b7e5_2d130e8605b801b347635da6772949aa3df5a1f7/playlist.m3u8',
        'https://edge-aws.aovivotv.xyz/hls/s:88.198.239.170/disneychannel_a9334987_cdf5f1c7fe5d4ded59b58fccd8050e6a4e833c61/playlist.m3u8',
        'https://edge-aws.aovivotv.xyz/hls/s:209.126.108.100:81/hbofamily_536fb693_9ed27d164727601bc96c201b4c6055adf7f6be86/playlist.m3u8',
        'https://edge-aws.aovivotv.xyz/hls/s:209.126.108.100:81/disneyjunior_572e2073_714beb2651d51a645390357d22ab24d9b4cc325a/playlist.m3u8',
        'https://edge-aws.aovivotv.xyz/hls/s:209.126.108.100:81/hbo_63266754_cae4a2e13eb2ef5548c567d0ba9061338e7829ba/playlist.m3u8',
        'https://edge-aws.aovivotv.xyz/hls/s:209.126.108.100:81/foxpremium2_2456caf1_b9a14f1cc6d436afdefd12dfd288a0d6a7680195/playlist.m3u8',
        'https://edge-aws.aovivotv.xyz/hls/s:209.126.108.100:81/hbopop_ce09b127_0d9ca53c3490d560a8c9696d8d8d8dc36343992e/playlist.m3u8',
        'https://edge-aws.aovivotv.xyz/hls/s:88.198.239.170/disneyxd_d094700e_4a316f4740437f5a4519f86c3918528307a201f8/playlist.m3u8',
        'https://edge-aws.aovivotv.xyz/hls/s:78.46.240.155/sony_06349be7_d864dd817e69bbb26ca85cddd81ac0e26dd0e26e/playlist.m3u8',
        'https://edge-aws.aovivotv.xyz/hls/s:209.126.108.100:81/paramountchannel_efa260ad_99a82ed8195a8a62f8be48b148b950852cd874cd/playlist.m3u8',
        'https://edge-aws.aovivotv.xyz/hls/s:78.46.240.155/hboxtreme_9c676e00_5f893b270c204c093f16b393b718c9deee432886/playlist.m3u8',
        'https://edge-aws.aovivotv.xyz/hls/s:95.216.15.44:81/telecinecult_8d255e1e_9b361850c459966608e23178ba48afe7b6b7d6a1/playlist.m3u8',
        'https://edge-aws.aovivotv.xyz/hls/s:95.216.15.44:81/canaloff_12f0de3d_1ba2fd14b0b806c22388388990dcda91253d16eb/playlist.m3u8',
        'https://edge-aws.aovivotv.xyz/hls/s:78.47.27.206/hbomundi_9f682df2_1d7df5f0bc6fbaeb695805b2433d5f81cf5373e7/playlist.m3u8',
        'https://edge-aws.aovivotv.xyz/hls/s:95.216.15.44:81/syfy_097ccd4f_0572fe70ef473360f372fed61fc54fa276688663/playlist.m3u8',
        'https://edge-aws.aovivotv.xyz/hls/s:88.198.239.170/animalplanet_e114c448_692f0cf5c4614af4124a625b47129a72b22570e7/playlist.m3u8',
        'https://edge-aws.aovivotv.xyz/hls/s:209.126.108.100:81/discoveryscience_77c8184f_dde8708129550b69aa0dc05f4c04440f269613f5/playlist.m3u8',
        'https://edge-aws.aovivotv.xyz/hls/s:209.126.108.100:81/hbosignature_fa1a6512_1743726f691912d9d421fb2cd208f9daab7371d6/playlist.m3u8',
    ]

    for i in range(len(arr_names)):
        ch = Channel()
        ch.title = arr_names[i]
        ch.img_url = arr_images[i]
        ch.category = category
        ch.save()
        li = Link()
        li.m3u8 = arr_m3u8[i]
        li.channel = ch
        li.url = arr_m3u8
        li.save()


class Command(BaseCommand):
    help = 'Script para inicializar Template Base'

    def handle(self, *args, **options):
        try:
            siteX = Site()
            siteX.name = 'multicanais'
            siteX.url = 'https://multicanais.com/'
            siteX.save()
            cat1X = CategoryChannel()
            cat1X.name = 'TV AO VIVO'
            cat1X.url = 'https://multicanais.com/aovivo/assistir-tv-online-gratis-hd-24h/'
            cat1X.path = 'aovivo/assistir-tv-online-gratis-hd-24h/'
            cat1X.site = siteX
            cat1X.pages = 3
            cat1X.save()

            site = Site()
            site.name = 'canaismax'
            site.url = 'https://canaismax.com/'
            site.save()
            cat1 = CategoryChannel()
            cat1.name = 'TV AO VIVO'
            cat1.url = 'https://canaismax.com/tvaovivo/'
            cat1.path = 'tvaovivo/'
            cat1.site = site
            cat1.save()

            site2 = Site()
            site2.name = 'topcanais'
            site2.url = 'https://topcanais.com/'
            site2.save()
            cat21 = CategoryChannel()
            cat21.name = 'Esportes'
            cat21.url = 'https://topcanais.com/esportes/'
            cat21.path = 'esportes/'
            cat21.site = site2
            cat21.pages = 2
            cat21.save()
            cat22 = CategoryChannel()
            cat22.name = 'Variedades'
            cat22.url = 'https://topcanais.com/variedades/'
            cat22.path = 'variedades/'
            cat22.site = site2
            cat22.save()
            cat23 = CategoryChannel()
            cat23.name = 'Documentarios'
            cat23.url = 'https://topcanais.com/documentarios/'
            cat23.path = 'documentarios/'
            cat23.site = site2
            cat23.pages = 2
            cat23.save()
            cat24 = CategoryChannel()
            cat24.name = 'Filmes e Series'
            cat24.url = 'https://topcanais.com/filmes-e-series/'
            cat24.path = 'filmes-e-series/'
            cat24.site = site2
            cat24.pages = 4
            cat24.save()

            site3 = Site()
            site3.name = 'filmes'
            site3.url = 'https://canaismax.com/'
            site3.save()
            cat31 = CategoryChannel()
            cat31.name = 'filmes'
            cat31.url = 'https://canaismax.com/filmes'
            cat31.path = 'filmes/'
            cat31.site = site3
            cat31.pages = 48
            cat31.save()

            site4 = Site()
            site4.name = 'series'
            site4.url = 'https://canaismax.com/'
            site4.save()
            cat41 = CategoryChannel()
            cat41.name = 'series'
            cat41.url = 'https://canaismax.com/series'
            cat41.path = 'series/'
            cat41.site = site4
            cat41.pages = 26
            cat41.save()

            siteXI = Site()
            siteXI.name = 'aovivogratis'
            siteXI.url = 'https://aovivo.gratis/'
            siteXI.save()
            cat1XI = CategoryChannel()
            cat1XI.name = 'Canais'
            cat1XI.url = 'https://aovivo.gratis/'
            cat1XI.path = '/'
            cat1XI.site = siteXI
            cat1XI.pages = 1
            cat1XI.save()

            create_manual_channels(cat1XI)

        except (Exception,):
            raise CommandError('Erro ao inicializar Models')
        self.stdout.write(self.style.SUCCESS('Successfully created sites and categories'))
