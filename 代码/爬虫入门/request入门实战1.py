import requests

content = input("请输入需要查找的内容：")
url = f"https://www.sogou.com/web?query={content}"

headers = {
    "User-Agent":
"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0"
}
resp = requests.get(url,headers = headers)
print(resp.text)