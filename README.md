# Google-IP-range-finder
This script will easily get all IPv4 ranges from official JSON file

> Support with your ⭐

# How to use

Fisrt of all you need a JSON file otherwise this code won't work properly, in [Amazon IP range finder](https://github.com/hoseinnikkhah/Amazon-IP-range-finder) and [Gcore IP range finder](https://github.com/hoseinnikkhah/Gcore-IP-range-finder) I used direct link to read the file while in Google it was not possible due to sanctions. so I decided to read JSON file localy, In order to do so you need to download official file provided by google, Open [this](https://www.gstatic.com/ipranges/cloud.json) link and download the JSON file.
change it's name to *cloud.json* if it is not this name.

Download this script and save it in any folder you like, in order to make the code run you need to place *cloud.json* file in same directory.

If you don't have python installed, install it from [Python](https://www.python.org/downloads/) website.

Here's the code if you like to copy and paste

```
import json

def eafp(data: dict):
    """Easier to Ask Forgiveness than Permission"""
    ipv4s = []

    for prefix in data["prefixes"]:
        try:
            ipv4s.append(prefix["ipv4Prefix"])
        except KeyError:
            # This happens when "ipv4Prefix" is not in prefix
            pass

    return ipv4s


def get_data(path) -> dict:
    with open(path) as f:
        return json.load(f)


if __name__ == "__main__":
    data = get_data("cloud.json")
    #print(eafp(data))
    f_path = (r"ip.txt")
    with open (f_path ,'w') as d:
        for lang in eafp(data):
            d.write("{}\n".format(lang))
```
