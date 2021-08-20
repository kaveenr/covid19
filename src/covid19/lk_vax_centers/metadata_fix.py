from covid19.lk_vax_centers.lk_vax_center_utils import round_x

FUZZY_KEY_TO_ALT_NAME = {
    'GMPHNTTMBWDHTHKNDRJMHVHRY': 'Dhathukanda Purana Rajamaha Viharaya',
    'GMPHNTTMBWNDGDVHRY': 'Bodhimalu Viharaya - Undugoda',
    'GMPHPLYGDGGBDCMMNTYHLL': 'PCAG Community Center',
    'TRNCMLPLMDDPLMDDBSHSPTL': 'Base Hospital - Pulmoddai',
    'NRDHPRTHNTHRMLTHNTHRMLRJMHVHRY': 'Tantirimale Rajamaha Viharaya',
    'BDLLLNGLLNGLHSPTL': 'District Hospital - Lunugala',
    'BDLLMHYNGNYMHYNGNYBSHSPTL': 'Base Hospital - Mahiyanganaya',
    'BDLLVPRNGMVPRNGMHSPTL': 'Divisional Hospital - Uva Paranagama',
    'BTTCLKLWNCHKDYKLWNCHKDYHSPTL': 'Base Hospital - Kaluwanchikudy',
    'BTTCLKLWNCHKDYMHFFCKLWNCHKDY': 'Medical Officer of Health Kaluwanchikudy',
    'CLMBGDYNMHFFCGDYN': 'MOH Egodauyana',
    'CLMBPDKKGHPDKK': 'Padukka Divisional Hospital',
    'HMBNTTTSSMHRMDBRWWPRSDNTSPRMRYSCHL': 'Debarawewa President\'s College',
    'KGLLMWNLLRNDWLMHVDYLY': 'Randiwala Maha Vidyalaya',
    'KLTRLTHGMLPTHTLNSRBLKMHVDYLY': 'Al Fasiyathul Nasriya'
    + ' Muslim Balika Navodaya School',
    'KLTRDDNGDMHFFCDDNGD': '6.540366199937832,80.03661033076219',
    'KLTRPNDRPNDRHSPTL': 'Base Hospital Panadura',
}

POLICE_INDEX = {
    'Agalawatta': {
        'ps_name_norm': 'Agalawatta',
        'ps_id': None,
        'ps_lat': round_x(6.54256638418913),
        'ps_lng': round_x(80.15717812090199),
    },
    'Adampan': {
        'ps_name_norm': 'Adampan',
        'ps_id': None,
        'ps_lat': round_x(8.93945137429449),
        'ps_lng': round_x(80.00205521277545),
    },
    'Imbulpe': {
        'ps_name_norm': 'Imbulpe',
        'ps_id': None,
        'ps_lat': round_x(6.688314278225411),
        'ps_lng': round_x(80.74377340378258),
    },
    'Panadura': {
        'ps_name_norm': 'Panadura North',
        'ps_id': None,
        'ps_lat': round_x(6.756308699534714),
        'ps_lng': round_x(79.89893946206159),
    },
    'Wadukkotte': {
        'ps_name_norm': 'Vaddukoddai',
        'ps_id': None,
        'ps_lat': round_x(9.728886232960443),
        'ps_lng': round_x(79.94777125510763),
    },
    'Pooneryn': {
        'ps_name_norm': 'Pooneryn',
        'ps_id': None,
        'ps_lat': round_x(9.505717334503101),
        'ps_lng': round_x(80.21101002627158),
    },
    'Karaitivu': {
        'ps_name_norm': 'Karaitivu',
        'ps_id': None,
        'ps_lat': round_x(9.744059134950323),
        'ps_lng': round_x(79.87058705168089),
    },
    'Haldummulla': {
        'ps_name_norm': 'Haldummulla',
        'ps_id': None,
        'ps_lat': round_x(6.7622160106687215),
        'ps_lng': round_x(80.88585605425267),
    },
}


def get_correct_district(district, police):
    if police in ['Kalutara South']:
        district = 'Kalutara'

    if police in ['Elpitiya']:
        district = 'Galle'
    if police in ['Weligama']:
        district = 'Matara'

    if police in ['Kotmale']:
        district = 'Nuwara Eliya'

    if police in ['Kotmale']:
        district = 'Nuwara Eliya'
    if police in ['Mullaitivu']:
        district = 'Mullaitivu'
    if police in ['Kilinochchi']:
        district = 'Kilinochchi'
    if police in ['Adampan']:
        district = 'Mannar'

    if police in ['Valachchenai', 'Kokkadichcholai', 'Kaluwanchikudy']:
        district = 'Batticaloa'

    if police in ['Kuliyapitiya', 'Nikaweratiya', 'Kurunegala']:
        district = 'Kurunegala'
    if police in ['Chilaw']:
        district = 'Puttalam'

    if police in ['Bibila']:
        district = 'Moneragala'

    return district
