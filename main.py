import conf

from trello import TrelloClient

TITLE_COLOR = '${color 5294e2}'
TEXT_COLOR = '${color e3e3e3}'

client = TrelloClient(
    api_key = conf.api_key,
    token = conf.token
)

#method to print all the cards in a list
def print_list(title, card_list):
    print(TITLE_COLOR, '', title)

    for i, card in enumerate(card_list.list_cards(), start = 1):
        card_format = '{}{}. {}'.format(TEXT_COLOR, '', card.name)
        print(card_format)

    print('')

#Get the boards and the list we want from each board
#INCIDENTES DE CIBERSEGURIDAD
incidentes_ciberseguridad = client.get_board(conf.incidentes_ciberseguridad)
incidentes_ciberseguridad_list = incidentes_ciberseguridad.get_list(conf.incidentes_ciberseguridad_list)

#PUESTA EN PRODUCCIÓN SEGURA
puesta_produccion_segura = client.get_board(conf.puesta_produccion_segura)
puesta_produccion_segura_list = puesta_produccion_segura.get_list(conf.puesta_produccion_segura_list)

#NORMATIVA DE CIBERSEGURIDAD
normativa_ciberseguridad = client.get_board(conf.normativa_ciberseguridad)
normativa_ciberseguridad_list = normativa_ciberseguridad.get_list(conf.normativa_ciberseguridad_list)

print_list("INCIDENTES DE CIBERSEGURIDAD", incidentes_ciberseguridad_list)
print_list("PUESTA EN PRODUCCIÓN SEGURA", puesta_produccion_segura_list)
print_list("NORMATIVA DE CIBERSEGURIDAD", normativa_ciberseguridad_list)


