import requests

url = "https://domain-availability.whoisxmlapi.com/api/v1?apiKey=at_68yGO5A1y78Ww7qJVcFQqn1UZH1o3&domainName=schulb.com&credits=DA"

querystring = {"domainname":"example.com","outputFormat":"JSON","mode":"DNS_ONLY"}

headers = {
	"x-rapidapi-key": "Sign Up for Key",
	"x-rapidapi-host": "whoisapi-domain-availability-v1.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

print(response.json())