# RSIR
**traffic generator**

執行generate_tms.py後會產生.pkl檔案，再執行iperf3_scripts.py會產生TM-00、TM-01....資料夾，
將這些資料夾放入23nodos供後面產生流量使用


**mininet**

geant.py為mininet檔案，開啟後會有4個選擇 CLI/CON/GEN/QUIT
* CLI
進入mininet介面
* CON
每個host先做一次ping操作，在拓樸建立完成時要先執行一次讓controller拿到相關資訊
* GEN
使用TM-XX(00、01.....)資料產生網路流量
* QUIT
離開mininet

**controller**

* OSPF_bwd / OSPF_delay / OSPF_loss  
使用 ryu-manager --observe-link ospf_proac.py 執行controller
* RSIR  
使用 ryu-manager --observe-link simple_monitor.py 執行controller  
執行RL_threading使用RL agent進行轉發路徑的學習
