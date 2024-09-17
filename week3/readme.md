# WEEK3: TASK 2: CREATE A VPC NETWORK
 - Navigate to Create VPC Network    
![1](task2/1.png)
1. Create VPC Network with default settings and appropriate CIDR     
2. Create a Subnet        
![2](task2/2.png)
3. Create 5 more Subnets     
![3](task2/3.png)
4. Assign Public IP's to the public subnet      
![4](task2/4.png)
5. create 2 Routing Tables one for Public and one for Private Subnets       
6. assign public Subnets to routing table      
![2](task2/6.png) 
8. create an internet gateway      
![2](task2/5.png)
9. Create a NAT Gateway       
![2](task2/7.png)
10. associate the edge device to the public Subnet        
![2](task2/8.png)         

Subnets associated to internet gateway are public subnets and those not connected are private subnets.

## ALTERNATIVE
1. Select VPC and more option  in Create VPC Networks        
![0](alternative/0.png)
2. Select 3 Availability Zones        
![1](alternative/1.png)
3. Select 3 Public and 3 Private Subnets        
![2](alternative/2.png)
4. Set 1 NAT Gateway        
![3](alternative/3.png)
5. Select S3 Gateway       
7. Create VPC        
![4](alternative/map.png)

# WEEK3: TASK 4: HOST A EC2 INSTANCE IN PUBLIC SUBNET
1. Navigate to Launch an EC2 instance     
2. Name the Instance      
![1](task3/1.png)
3. Select the OS Image (Amazon Linux for free tier with ssd)      
4. Select the Instance Type (T2.micro for free tier)      
![2](task3/2.png)
5. Select the new VPC network created       
![3](task3/3.png)
6. Select any public subnet      
7. Configure Security Group       
![1](task3/4.png)
8. Remove all ip address settings and create firewall rule to only allow self-ip to connect.       
9. Create Instance        
![1](task3/5.png)      
