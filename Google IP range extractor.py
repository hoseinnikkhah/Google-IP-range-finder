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
