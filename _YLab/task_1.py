
def domain_name(url):
    if 'http' in url:
        seq = url.split('//')[1]
        ans = seq[:seq.index('.')]
        return ans
    elif 'www' in url:
        seq = url.strip('www.')
        ans = seq[:seq.index('.')]
        return ans


assert domain_name("http://google.com") == "google"
assert domain_name("http://google.co.jp") == "google"
assert domain_name("www.xakep.ru") == "xakep"
assert domain_name("https://youtube.com") == "youtube"

print(domain_name("http://google.com"))
print(domain_name("http://google.co.jp"))
print(domain_name("www.xakep.ru"))
print(domain_name("https://youtube.com"))
