# Set creds and headers
era_user = "@@{era_creds.username}@@"
era_pass = "@@{era_creds.secret}@@"
headers = {"Content-Type": "application/json", "Accept": "application/json"}

# Get DB Server IP and ID
url = "https://@@{era_ip}@@/era/v0.9/databases/@@{DB_ENTITY_NAME}@@?value-type=name&detailed=true&load-dbserver-cluster=true"
resp = urlreq(
    url, verb="GET", auth="BASIC", user=era_user, passwd=era_pass, headers=headers
)

if resp.ok:
    print("DB_SERVER_IP={0}".format(json.loads(resp.content)["databaseNodes"][0]["dbserver"]["ipAddresses"]))
    print("DB_ID={0}".format(json.loads(resp.content)["id"]))
    print("DB_SERVER_ID={0}".format(json.loads(resp.content)["databaseNodes"][0]["dbserver"]["id"]))
else:
    print("Get DB info request failed", json.dumps(json.loads(resp.content), indent=4))
    exit(1)
