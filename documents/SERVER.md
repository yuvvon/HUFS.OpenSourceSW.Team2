# Server Structure

## Physical Structure
* Virtual Server Machine: Oracle Cloud Infrastructure Compute Instance
* Virtual Server Network: Accept TCP Port 80 Only

## Logical Structure
* Accept All Request by [Nginx](https://nginx.org/en/) 
* Flask Server Running by [PM2](https://pm2.keymetrics.io/)
* Request to "[hufsoss.rflxn.xyz](http://hufsoss.rflxn.xyz)" will be Pass to "localhost:5000" by Nginx Reverse Proxy
* Python Flask Handle Request from Nginx Reverse Proxy
