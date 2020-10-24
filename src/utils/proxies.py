def get_proxy():
    url = "https://free-proxy-list.net/"
    # формируем объект sp, получив ответ http
    sp = bs(requests.get(url).content, "html.parser")
    proxy = []
    for row in sp.find("table", attrs={"id": "proxylisttable"}).find_all("tr")[1:]:
        tds = row.find_all("td")
        try:
            ip = tds[0].text.strip()
            port = tds[1].text.strip()
            host = f"{ip}:{port}"
            proxy.append(host)
        except IndexError:
            continue
    return proxy