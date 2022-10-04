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


## Make mysql instance available to external computers
1. Config file
  - In GCP vm terminal, use "nano" to access config file
  - Once in the config file, find the port address and change it into "0.0.0.0"
  - Press ctrl + o to save, ctrl + x to exit config file
2. Opening ports via GCP
  - In search bar type "firewall"
  - Click "create firewall rule"
  - Give the firewall rule a name as required
  - Under "Targets", select "All instances in the network"
  - Under "Source IPv4 ranges", type "0.0.0.0/0"
  - Create firewall rule

## Uplode example dataset to mysql database
