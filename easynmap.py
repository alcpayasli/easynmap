# -*- coding: utf-8 -*-
from pr_modules.easynmap_cls import EasyNmap
from pr_modules.print_colored import PrintStyle
from pyfiglet import Figlet
my_text = Figlet().renderText("EASY NMAP")
print(PrintStyle.CYELLOW + my_text + PrintStyle.CYELLOW)
print(PrintStyle.CRED + 28*"*"+"""BY ALI CAN PAYASLI""" + 28*"*"+PrintStyle.CRED)



while True:
    print(PrintStyle.CYELLOW + """
    OPERATIONS:
    1-INTENSE SCAN
    2-INTENSE SCAN (PLUS UDP)
    3-INTENSE SCAN (ALL TCP PORTS)
    4-PING SCAN
    5-QUICK SCAN
    6-QUICK SCAN (PLUS)
    7-VERSION AND OS SCAN
    0-QUIT
    """ + PrintStyle.CYELLOW)
    operations = raw_input("Choose operation:")
    print("\n")
    if operations == "1":
        while True:
            print(PrintStyle.CRED + "PRESS 0 FOR RETURN TO MAIN MENU" + PrintStyle.CRED)
            targets = raw_input(PrintStyle.CYELLOW +"Input targets " + PrintStyle.CYELLOW +  PrintStyle.CBEIGE +
                                "(EXAMPLE: 192.168.1.26 OR 192.168.1.25 192.168.1.16 OR example.com):" + PrintStyle.CBEIGE)
            print("\n")

            if targets == "0":
                break
            else:
                my_object = EasyNmap(targets)
                try:
                    print(
                                PrintStyle.CRED + "*" * 15 + " STARTING SCAN BE PATIENT AND WAIT " + "*" * 15 + PrintStyle.CRED)
                    print(PrintStyle.CBEIGE)

                    my_object.intense_scan()
                    print(PrintStyle.CRED + "*" * 15 + " FINISH SCAN " + "*" * 15 + PrintStyle.CRED)
                    print("\n")
                except:
                    print(PrintStyle.CRED + "Error" + PrintStyle.CRED)
    ##############################################################################################################################
    elif operations == "2":
        while True:
            print(PrintStyle.CRED + "PRESS 0 FOR RETURN TO MAIN MENU" + PrintStyle.CRED)
            targets = raw_input(PrintStyle.CYELLOW +"Input targets " + PrintStyle.CYELLOW +  PrintStyle.CBEIGE +
                                "(EXAMPLE: 192.168.1.26 OR 192.168.1.25 192.168.1.16 OR example.com):" + PrintStyle.CBEIGE)
            print("\n")

            if targets == "0":
                break
            else:
                my_object = EasyNmap(targets)
                try:
                    print(
                                PrintStyle.CRED + "*" * 15 + " STARTING SCAN BE PATIENT AND WAIT " + "*" * 15 + PrintStyle.CRED)
                    print(PrintStyle.CBEIGE)

                    my_object.intense_scan_plus_udp()
                    print(PrintStyle.CRED + "*" * 15 + " FINISH SCAN " + "*" * 15 + PrintStyle.CRED)
                    print("\n")
                except:
                    print(PrintStyle.CRED + "Error" + PrintStyle.CRED)
    ################################################################################################################################
    elif operations == "3":
        while True:
            print(PrintStyle.CRED + "PRESS 0 FOR RETURN TO MAIN MENU" + PrintStyle.CRED)
            targets = raw_input(PrintStyle.CYELLOW +"Input targets " + PrintStyle.CYELLOW +  PrintStyle.CBEIGE +
                                "(EXAMPLE: 192.168.1.26 OR 192.168.1.25 192.168.1.16 OR example.com):" + PrintStyle.CBEIGE)
            print("\n")

            if targets == "0":
                break
            else:
                my_object = EasyNmap(targets)
                try:
                    print(
                                PrintStyle.CRED + "*" * 15 + " STARTING SCAN BE PATIENT AND WAIT " + "*" * 15 + PrintStyle.CRED)
                    print(PrintStyle.CBEIGE)

                    my_object.intense_scan_all_tcpports()
                    print(PrintStyle.CRED + "*" * 15 + " FINISH SCAN " + "*" * 15 + PrintStyle.CRED)
                    print("\n")
                except:
                    print(PrintStyle.CRED + "Error" + PrintStyle.CRED)
    ###############################################################################################################################
    elif operations == "4":
        while True:
            print(PrintStyle.CRED + "PRESS 0 FOR RETURN TO MAIN MENU" + PrintStyle.CRED)
            targets = raw_input(PrintStyle.CYELLOW +"Input targets " + PrintStyle.CYELLOW +  PrintStyle.CBEIGE +
                                "(EXAMPLE: 192.168.1.26 OR 192.168.1.25 192.168.1.16 OR example.com):" + PrintStyle.CBEIGE)
            print("\n")

            if targets == "0":
                break
            else:
                my_object = EasyNmap(targets)
                try:
                    print(
                                PrintStyle.CRED + "*" * 15 + " STARTING SCAN BE PATIENT AND WAIT " + "*" * 15 + PrintStyle.CRED)
                    print(PrintStyle.CBEIGE)

                    my_object.ping_scan()
                    print(PrintStyle.CRED + "*" * 15 + " FINISH SCAN " + "*" * 15 + PrintStyle.CRED)
                    print("\n")
                except:
                    print(PrintStyle.CRED + "Error" + PrintStyle.CRED)
    ###############################################################################################################################
    elif operations == "5":
        while True:
            print(PrintStyle.CRED + "PRESS 0 FOR RETURN TO MAIN MENU" + PrintStyle.CRED)
            targets = raw_input(PrintStyle.CYELLOW +"Input targets " + PrintStyle.CYELLOW +  PrintStyle.CBEIGE +
                                "(EXAMPLE: 192.168.1.26 OR 192.168.1.25 192.168.1.16 OR example.com):" + PrintStyle.CBEIGE)
            print("\n")

            if targets == "0":
                break
            else:
                my_object = EasyNmap(targets)
                try:
                    print(
                                PrintStyle.CRED + "*" * 15 + " STARTING SCAN BE PATIENT AND WAIT " + "*" * 15 + PrintStyle.CRED)
                    print(PrintStyle.CBEIGE)

                    my_object.quick_scan()
                    print(PrintStyle.CRED + "*" * 15 + " FINISH SCAN " + "*" * 15 + PrintStyle.CRED)
                    print("\n")
                except:
                    print(PrintStyle.CRED + "Error" + PrintStyle.CRED)
    ##################################################################################################################################
    elif operations == "6":
        while True:
            print(PrintStyle.CRED + "PRESS 0 FOR RETURN TO MAIN MENU" + PrintStyle.CRED)
            targets = raw_input(PrintStyle.CYELLOW +"Input targets " + PrintStyle.CYELLOW +  PrintStyle.CBEIGE +
                                "(EXAMPLE: 192.168.1.26 OR 192.168.1.25 192.168.1.16 OR example.com):" + PrintStyle.CBEIGE)
            print("\n")

            if targets == "0":
                break
            else:
                my_object = EasyNmap(targets)
                try:
                    print(
                                PrintStyle.CRED + "*" * 15 + " STARTING SCAN BE PATIENT AND WAIT " + "*" * 15 + PrintStyle.CRED)
                    print(PrintStyle.CBEIGE)

                    my_object.quick_scan_plus()
                    print(PrintStyle.CRED + "*" * 15 + " FINISH SCAN " + "*" * 15 + PrintStyle.CRED)
                    print("\n")
                except:
                    print(PrintStyle.CRED + "Error" + PrintStyle.CRED)
    ################################################################################################################################
    elif operations == "7":
        while True:
            print(PrintStyle.CRED + "PRESS 0 FOR RETURN TO MAIN MENU" + PrintStyle.CRED)
            targets = raw_input(PrintStyle.CYELLOW +"Input targets " + PrintStyle.CYELLOW +  PrintStyle.CBEIGE +
                                "(EXAMPLE: 192.168.1.26 OR 192.168.1.25 192.168.1.16 OR example.com):" + PrintStyle.CBEIGE)
            print("\n")

            if targets == "0":
                break
            else:
                my_object = EasyNmap(targets)
                try:
                    print(
                                PrintStyle.CRED + "*" * 15 + " STARTING SCAN BE PATIENT AND WAIT " + "*" * 15 + PrintStyle.CRED)
                    print(PrintStyle.CBEIGE)

                    my_object.version_and_os_scan()
                    print(PrintStyle.CRED + "*" * 15 + " FINISH SCAN " + "*" * 15 + PrintStyle.CRED)
                    print("\n")
                except:
                    print(PrintStyle.CRED + "Error" + PrintStyle.CRED)

    elif operations == "0":
        break
    else:
        print(PrintStyle.CRED + "Invalid Operations" + PrintStyle.CRED)