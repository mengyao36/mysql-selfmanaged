# mysql-selfmanaged

## Cloud Enviornment
- GCP

## Set up VM via GCP
1. Select "Create a VM" on the homepage of GCP
2. Name the vm
3. Under "Machine type", select "e2-medium (2 vCPU, 4 GB memory)" to meet the minimun requirement of mysql
4. Under "Boot disk", select "change"
    - Under "Operating system", select "Ubuntu"
    - Under "Version", select "Ubuntu 18.04 LTS x86/64, amd64 bionic image built on 2022-09-01, supports Shielded VM features"
    - Click "select"
5. Under "Firewall", check both "Allow HTTP traffic" and "Allow HTTPS traffic"
6. Click "create" at the bottom to create vm
 
## Set up OS image
1. Update OS command
    - `sudo apt-get update`
2. Install mysql command
    - `sudo apt install mysql-server mysql-client`
3. Login to mysql command 
    - `sudo mysql`

## Make mysql instance available to external computers
1. Config file (allow inbound connection to mysql)
    - In GCP vm terminal, use "nano" to access config file
        - `sudo nano /etc/mysql/mysql.conf.d/mysqld.cnf`
    - Once enter the config file, find the "bind-address" and change it into "0.0.0.0"
    - Press "ctrl + o" to save, "ctrl + x" to exit config file
    - restart mysql (the two commands below work the same, use either)
        - `sudo nano service mysql restart`
        - `sudo /etc/init.d/myql restart`
2. Opening ports via GCP (enable inbound connection)
    - In the searching bar, type "firewall"
    - Select "create firewall rule" (associated with our created vm)
    - Give the firewall rule a name as required
    - Under "Protocols and ports", select "Specified protocols and ports", then select "TCP", type "3306" under "Ports"
    - Under "Direction of traffic", select "Ingress"
    - Under "Action on match", select "Allow", then
        - Under "Targets", select "All instances in the network"
        - Under "Source IPv4 ranges", type "0.0.0.0/0"
    - Create firewall rule

## Uplode example dataset to mysql database
Following commmands used in python file
Screenshot added to show dataset uploded successfully
    - Under database called "hmy", a new table added called "new_table"
