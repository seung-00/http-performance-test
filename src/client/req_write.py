import csv
import time
import requests
import matplotlib.pyplot as plt


def test(URL, req_num):
    try:
        print(f"{req_num} requst...")
        end_time = time.time()+1
        req_cnt = 0

        while time.time() < end_time:
            if req_cnt == req_num:
                break
            req = requests.get(URL)
            if req.status_code == 200:
                req_cnt += 1

        # print(f"TPS: {req_cnt}")
        return req_cnt

    except Exception as e:
        print(e)


def write_tps(tps_list):
    with open('../data/new.csv', 'w', encoding='utf-8', newline='') as f:
        wr = csv.writer(f)
        cnts = [i for i in range(1, len(tps_list)+1)]
        wr.writerows([cnts, tps_list])


if __name__ == "__main__":
    ip = input("type the server ip\n")
    rsc = input("type what you want to get => json or db\n")
    URLS = {1: f"http://{ip}:8081/{rsc}",
            2: f"http://{ip}:8082/{rsc}", 3: f"http://{ip}:8083/{rsc}"}
    print(URLS)
    lang_key = int(input("1: node 2:python 3: go \n"))
    max_req_num = int(input("put max request\n"))

    URL = URLS[lang_key]
    tps_list = []

    for req_num in range(1, max_req_num+1):
        result = test(URL, req_num)
        tps_list.append(result)

    print(tps_list)
    write_tps(tps_list)
