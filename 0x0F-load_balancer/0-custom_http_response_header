#!/usr/bin/env bash
#this bash script adds a custom header to a web server's response
sudo apt update
sudo apt install nginx -y
cutsom_header = "add_header X-S	erved-By \$hostname;"
sudo sed -i "/^http {/a \ \ \ \ $custom_header_conf" /etc/nginx/nginx.conf
sudo systemctl restart nginx
