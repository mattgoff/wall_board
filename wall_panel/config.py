url = "http://www.goff.us/api/"
auth_token = "its_a_secret"
head = {'Authorization': 'token {}'.format(auth_token)}

data_dict ={
    'office_temperature': 0,
    'front_temperature': 0,
    'outside_patio_temperature': 0,
    'orb_color': [27, 148, 33],
    'office_color': [27, 148, 33],
    'front_color': [27, 148, 33],
    'patio_color': [27, 148, 33],
    'office_lst': [],
    'patio_lst': [],
    'front_lst': [],
}