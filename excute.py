'''import pyfiglet as pflt
import subprocess as sbpc
from Color import *
screenput=pflt.figlet_format("Vidit Shringi" , font = "isometric1")
print(screenput)'''
k=int(input("[+]\t1.)for IP And domian Name request:\n[+]\t2.)For CPU Information:\n[+]\t3.)For IFCONFIG:\n=:=:=:=:=:=:=:=:=:=:=:=>"))
if k == 1:
    PING=pflt.figlet_format("WebsitePing")
    print(Formatting.Bold,PING, Formatting.Reset)
    print("[+] Enter IP Address OR website name(Domain name):\t")
    i=input()
    sbpc.call("ping "+i,shell=True)
elif k== 2:
    LSCPU=pflt.figet_format("C_P_U...Infomation",font='5lineoblique')
    print(LSCPU)
    sbpc.call("lscpu")
    print("""<----!This Function Not available YET !---->""")
elif k==3:
    IFF=pflt.figlet_format("IFCONFIG",font="dot")
    print(IFF)
    sbpc.call("ifconfig")
else:
    print("<---M!$$!0N_A80RT--->")
    quit()


'''
print("Base:")
print(Base.FAIL,"This is a test!", Base.END)

print("ANSI_Compatible:")
print(ANSI_Compatible.Color(120),"This is a test!", ANSI_Compatible.END)

print("Formatting:")


print("GColor:") # Gnome terminal supported
print(GColor.RGB(204,100,145),"This is a test!", GColor.END)

print("Color:")
print(Color.F_Cyan,"This is a test!",Color.F_Default)
'''

"""
from pyfiglet import Figlet
f = Figlet(font='5lineoblique')
print (f.renderText('hello'))
"""
