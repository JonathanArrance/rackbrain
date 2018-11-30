import subprocess

#random utilities and tools
def get_location():
    l = subprocess.Popen(["curl", "ipinfo.io"], stdout=subprocess.PIPE)
    return l.communicate()