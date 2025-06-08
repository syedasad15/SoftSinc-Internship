
import datetime

def log_role_action(role: str, user: str, action: str):
    log_file = f"{role.lower()}.log"
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    entry = f"[{timestamp}] {user}: {action}\n"

    try:
        with open(log_file, "a", encoding="utf-8") as file:
            file.write(entry)
    except Exception as e:
        print(f"Failed to write log for {user}: {e}")
