import pygeoip
import datetime
import os
import ipinfo
import pprint
import re
import os

# https://ipinfo.io/account -----> better script by ip info api

access_token = '' #create account in ipinfo.com and get a free token
handler = ipinfo.getHandler(access_token)
sorted_ip = {}
string_raw_ip = open('raw_ips.txt', 'r').read()
index_starting_pos = 0


def ip_filter(ip):
    global sorted_ip
    global string_raw_ip
    global index_starting_pos
    if ip != '127.0.0.1' and ip != '0.0.0.0':
        if re.match(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$", ip):

            ip_position = string_raw_ip.find(
                ip, index_starting_pos, -1)

            third_bracket_pos = string_raw_ip.find(
                "[", ip_position)

            third_bracket_ending_pos = string_raw_ip.find(
                "]", third_bracket_pos)

            application_name = string_raw_ip[third_bracket_pos +
                                             1:third_bracket_ending_pos]

            sorted_ip[ip] = {'application_name': application_name}

            index_starting_pos = ip_position


def sorter():
    global sorted_ip
    global string_raw_ip
    global index_starting_pos
    with open('raw_ips.txt', 'r') as irf:
        lines = irf.readlines()
        for l in lines:
            splited_list = l.split(' ')
            splited_list = list(dict.fromkeys(splited_list))
            if len(splited_list) == 6:
                semi_colon_pos = splited_list[3].find(':')
                ip = splited_list[3][:semi_colon_pos]
                ip_filter(ip)  # calling ip_filter to filter ip by need

    print('done---------Sorting--------------->')


def ip_info_get():
    now = datetime.datetime.now()

    with open('ip_informations.txt', 'a') as ipf:
        ipf.write('\n')
        ipf.write('\n')
        ipf.write('\n')
        ipf.write('\n')
        ipf.write(
            f'Time------>{now} {now.strftime("%p")} Ip search -->{len(sorted_ip)}<--------------')
        for ip, application in sorted_ip.items():

            ipf.write('\n')
            ipf.write('\n')
            ipf.write('\n')
            ipf.write('\n')
            ipf.write('\n')
            ipf.write('\n')
            ipf.write('\n')
            ipf.write(
                f"Ip is : {ip}                application: "+application['application_name']+" \n")
            details = handler.getDetails(ip)
            for key, val in details.all.items():

                ipf.write('%s : %s' % (key, val))
                ipf.write('\n')

    print('done-----------finding ip information ------------->')


if __name__ == "__main__":

    sorter()
    ip_info_get()
