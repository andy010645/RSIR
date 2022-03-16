# RSIR
## Controller

### ryu controller install

使用python 3.7

先去[ryu controller github](https://github.com/faucetsdn/ryu) 下載code
載完後進入ryu資料夾，執行pip3 install .

在此ryu版本裡會缺少我們需要的一些function  [ryu controller fix code](https://github.com/muzixing/ryu/blob/master/ryu/topology/switches.py)  
所以我們需要自己對此做出修改

1. 進入ryu/ryu/topology/switches.py
2. class PortData 裡的init多加一個self.delay = 0  
![](https://i.imgur.com/E9RPmRz.png)
3. 在lldp_packet_in_handler開頭先新增一行code : recv_timestamp = time.time()
4. 將fix版本code的714行後的get the lldp delay code 複製  
![image](https://user-images.githubusercontent.com/69691891/145552471-a11fbc18-a494-4e34-982c-6e88a861a27a.png)
5. 將剛剛複製好的code貼到791行
6. 上述動作執行完成後，回到ryu資料夾並執行python3 setup.py install

### ryu controller usage

建議將mininet主機以及controller主機分開

* OSPF_bwd / OSPF_delay / OSPF_loss  / OSPF_all  
使用 ryu-manager --observe-link ospf_proac.py 執行controller
* RSIR / DRSIR  
使用 ryu-manager --observe-link simple_monitor.py 執行controller  
執行RL_threading使用RL agent進行轉發路徑的學習




