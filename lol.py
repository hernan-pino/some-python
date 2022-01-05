hosts_path_windows = r"C:\Windows\System32\drivers\etc\hosts"
hosts_path_unix = "/etc/hosts"
#host_dir = "hosts"
host_dir = hosts_path_windows

redirect = "127.0.0.1"

# list of websites to block
website_list = [
    'https://lan.leagueoflegends.com/es-mx/',
    'https://signup.las.leagueoflegends.com/es/signup/redownload',
    'https://na.leagueoflegends.com/es-es/',

]
with open(host_dir, 'r+') as file:
    content = file.read()
    for website in website_list:
        if website in content:
            pass
        else:
            file.write(redirect + " " + website + "\n")