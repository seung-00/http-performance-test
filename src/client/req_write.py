import csv
import time
import requests
import matplotlib.pyplot as plt


def test(URL, req_num):
    try:
        print(f'\n{req_num} requst...')
        end_time = time.time()+1
        req_cnt = 0
        cnt = 0

        while time.time() < end_time:
            cnt += 1
            if req_cnt == req_num:
                break
            req = requests.get(URL)
            if req.status_code == 200:
                req_cnt += 1
        print(cnt)
        return req_cnt

    except Exception as e:
        print(e)


def write_tps(tps_list):
    with open(f'../data/{env}/{lang}/{rsc}.csv', 'w', encoding='utf-8', newline='') as f:
        wr = csv.writer(f)
        cnts = [i for i in range(1, len(tps_list)+1)]
        wr.writerows([cnts, tps_list])


if __name__ == '__main__':
    ip = input('type the server ip\n')
    while(True):
        rsc_key = int(input('type what you want to get =>\n  1: json 2: db\n'))
        if rsc_key == 1:
            rsc = 'json'
            break
        elif rsc_key == 2:
            rsc = 'db'
            break
        else:
            continue

    while(True):
        lang_key = int(input('  1: node 2:python 3: go \n'))
        if lang_key == 1:
            lang = 'node'
            break
        elif lang_key == 2:
            lang = 'python'
            break
        elif lang_key == 3:
            lang = 'go'
            break
        else:
            continue

    while(True):
        env_key = int(input('  1: native 2:vm 3: container \n'))
        if env_key == 1:
            env = 'native'
            break
        elif env_key == 2:
            env = 'vm'
            break
        elif env_key == 3:
            env = 'container'
            break
        else:
            continue

    URLS = {'node': f'http://{ip}:8081/{rsc}',
            'python': f'http://{ip}:8082/{rsc}', 'go': f'http://{ip}:8083/{rsc}'}

    max_req_num = int(input('put max request\n'))

    URL = URLS[lang]
    tps_list = []

    for req_num in range(1, max_req_num+1):
        result = test(URL, req_num)
        tps_list.append(result)

    print(tps_list)
    write_tps(tps_list)
