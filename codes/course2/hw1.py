names = "Alan, Bruce, Carlos, David, Emma"
name_list = names.split(",")
for name in name_list:
    name = name.strip()
    print("Hello, %s!" % name)
