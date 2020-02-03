import numpy as np

responses = {
    'welcome': [
        'Oi',
        'olá',
    ],
    'good_morning': [
        'Bom dia'
    ],
    'attendance_support': [
        'OK, estamos lhe transferido para o suporte',
        'BLZ, chamando alguem do suporte para atender vc'
    ],
    'attendance_financeiro': [
        'Certo, jaja alguem do financeiro vai lhe atender',
        '1 min, estamos lhe transferindo para alguem do financeiro'
    ],
    'baixar_boleto': [
        'OK, em instantes lhe enviaremos sua fatura atualizada'
        'Aguarde um momento, estamos processando seu download'
    ],
    'information': [
        'Aguarde 1 min, estamos verificando essa informação'
    ]
}

def get_random_response(intent):
    response_list = responses[intent]

    return response_list[0]
