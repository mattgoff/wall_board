import requests


url = "http://www.goff.us/api/pistats/1/"
auth_token = "its_a_secret"
head = {'Authorization': 'token {}'.format(auth_token)}

body_data = {}

def send_info():
    response = requests.put(url, headers=head, data=body_data)
    data = response.json()
    print(data)

def pi_hole_stats():
    pi_hole_server = "172.16.12.9"
    r = requests.get('http://' + pi_hole_server + '/admin/api.php')
    output_info = r.json()
    body_data.update({'pi_hole_stats_24hr_block': output_info['ads_blocked_today']})
    body_data.update({'pi_hole_status_24hr_DNS_queries': output_info['dns_queries_today']})

def cpu_temp():
    with open('/sys/class/thermal/thermal_zone2/temp', 'r') as f:
        temp_c = float(f.readline().strip('\n')) / 1000
        temp_f = temp_c * (9.0 / 5.0) + 32
        body_data.update({'pi_hole_cpu_temperature': temp_f,})
        print("temp_c = {}  temp_f = {:.2f}".format(temp_c, temp_f))

pi_hole_stats()
cpu_temp()
send_info()

