import smtplib, ssl, sys, json
from email.mime.text import MIMEText

def send_notification(event_type, username, issue_num, details):
    ts = __import__("time").strftime("%Y-%m-%d %H:%M:%S")
    
    if event_type == "submission":
        subject = f"[AI Research] {username} submitted fix for #{issue_num}"
        body = f"""
<h2>New Code Submission</h2>
<p><b>User:</b> {username}</p>
<p><b>Task:</b> #{issue_num}</p>
<p><b>Time:</b> {ts}</p>
<p><b>Status:</b> Evaluating...</p>
"""
    elif event_type == "completed":
        subject = f"[AI Research] {username} completed #{issue_num} - {details.get("score", 0)} HONEY"
        cheat = details.get("cheat", False)
        status = "CHEAT DETECTED" if cheat else "CLEAN"
        body = f"""
<h2>Task Completed!</h2>
<p><b>User:</b> {username}</p>
<p><b>Task:</b> #{issue_num}</p>
<p><b>Time:</b> {ts}</p>
<p><b>Status:</b> {status}</p>
<p><b>Reward:</b> {details.get("score", 0)} HONEY</p>
"""
    else:
        return
    
    html = f"""<html><body style="font-family:Arial,sans-serif;">{body}
<hr>
<p style="color:#888;font-size:12px;">AI Research Monitor | {ts}</p>
</body></html>"""
    
    msg = MIMEText(html, "html", "utf-8")
    msg["Subject"] = subject
    msg["From"] = "2593697591@QQ.com"
    msg["To"] = "2593697591@QQ.com"
    
    ctx = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.qq.com", 465, context=ctx) as s:
        s.login("2593697591@QQ.com", "hwazivgrdiofebaj")
        s.sendmail("2593697591@QQ.com", "2593697591@QQ.com", msg.as_string())
    print(f"[EMAIL] {subject}")

if __name__ == "__main__":
    event = json.loads(sys.stdin.read())
    send_notification(event["type"], event["user"], event["issue"], event.get("details", {}))
