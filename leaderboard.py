import urllib.request, json, sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

token = os.environ["GH_TOKEN"]
headers = {'Authorization': f'token {token}', 'User-Agent': 'monitor-agent'}
def get_json(url):
    req = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(req) as r:
        return json.loads(r.read())

# Get leaderboard issue
issue = get_json('https://api.github.com/repos/zhangjiayang6835-cyber/ai-research/issues/11')
comments = get_json('https://api.github.com/repos/zhangjiayang6835-cyber/ai-research/issues/11/comments')
print('Leaderboard body:')
print(issue['body'][:2000])
print()
print('Comments on leaderboard:')
for c in comments:
    print(f"  Comment {c['id']} by {c['user']['login']}: {c['body'][:400]}")
