# mysql-selfmanaged

## Cloud Enviornment
- GCP

## Set up VM via GCP
- select "Create a VM" on the homepage of GCP
- name the vm
- under "Machine type", select "e2-medium (2 vCPU, 4 GB memory)" to meet the minimun requirement of mysql
- under "Boot disk", select "change"
  - under "Operating system", select "Ubuntu"
  - under "Version", select "Ubuntu 18.04 LTS x86/64, amd64 bionic image built on 2022-09-01, supports Shielded VM features"
  - click "select"
- under "Firewall", check both "Allow HTTP traffic" and "Allow HTTPS traffic"
- click "create" at the bottom to create vm
 
## Set up OS image


## Make mysql instance available to external computers
- config file
  - in GCP vm terminal, use "nano" to access config file
  - once in the config file, find the port address and change it into "0.0.0.0"
  - press ctrl + o to save, ctrl + x to exit config file
- opening ports via GCP
  - in search bar type "firewall"
  - click "create firewall rule"
  - give the firewall rule a name as required
  - under "Targets", select "All instances in the network"
  - under "Source IPv4 ranges", type "0.0.0.0/0"
  - create firewall rule

## Uplode example dataset to mysql database
