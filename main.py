import requests,urllib.request
url = "https://api.chanify.net/v1/sender/CIDJ0YgGEiJBQUVCUjcySlk0UkZFQjUzTzVUTzZJTktHVExIQkRNQ0pVGhQtCe2ZSYlujMUeKq8OPSJeemOxNCIECAEQAQ.K6HCm8GeslfGtG2ipxgGte8OmQxpz29tVHNVfwHXSzI/"
msg = '推送测试9.47'
msg = urllib.parse.quote(msg)
response = urllib.request.urlopen(url+msg)
print(response.read().decode('utf8'))
