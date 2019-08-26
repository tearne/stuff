
* 'ping' obviously
* `nmap -p 80 google.com`

Starting Nmap 7.60 ( https://nmap.org ) at 2019-08-26 07:09 UTC
Nmap scan report for google.com (172.217.169.14)
Host is up (0.0035s latency).
Other addresses for google.com (not scanned): 2a00:1450:4009:816::200e
rDNS record for 172.217.169.14: lhr25s26-in-f14.1e100.net

PORT   STATE SERVICE
80/tcp open  http

Nmap done: 1 IP address (1 host up) scanned in 0.76 seconds


https://www.professormesser.com/nmap/hacking-nmap-using-nmap-to-calculate-network-response-time/6/
`nmap -p80 --oX - www.google.com`

* `curl -w %{time_connect}\\n -o /dev/null -s https://dynamodb.eu-west-2.amazonaws.com/`
