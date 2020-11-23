import time
import requests
import matplotlib.pyplot as plt

def test(URL, req_num):
    try:        
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

def draw_tps(max_req_num, tps_list):
    x = [i for i in range(1, max_req_num+1)]
    y = tps_list
    max_tps = max(tps_list)

    plt.figure()
    plt.plot(x, y)
    plt.grid(True)
    plt.axhline(y=max_tps, color='r', linewidth=1)
    plt.xlabel("request")
    plt.ylabel("TPS")
    plt.show()

if __name__ == "__main__":
    URLS = {1: "http://localhost:8081/node", 2: "http://localhost:8082/python", 3: "http://localhost:8083/go"}

    lang_key = int(input("1: node 2:python 3: go \n"))
    max_req_num = int(input("put max request\n"))

    URL = URLS[lang_key]
    tps_list = []

    for req_num in range(1, max_req_num+1):
        result = test(URL, req_num)
        tps_list.append(result)
    
    print(tps_list)
    print(max(tps_list))
    draw_tps(max_req_num, tps_list)