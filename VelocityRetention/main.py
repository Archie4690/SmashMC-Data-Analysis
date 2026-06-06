import gzip 
import re
import glob
from datetime import datetime
import csv

active_sessions = {}
completed_sessions = []
files = glob.glob("/home/archie/smc/dataAnalytics/VelocityRetention/VelocityLogs/*.log.gz")

def add_session(username, connection_time, date):
    full_datetime = date + " " + connection_time
    active_sessions[username] = datetime.strptime(full_datetime, "%Y-%m-%d %H:%M:%S")

def end_session(username, disconnection_time, date):
    full_datetime = date + " " + disconnection_time
    if username in active_sessions:
        start_time = active_sessions[username]
        completed_sessions.append({
            "player": username,
            "start_time": start_time,
            "end_time": datetime.strptime(full_datetime, "%Y-%m-%d %H:%M:%S"),
            "duration": datetime.strptime(full_datetime, "%Y-%m-%d %H:%M:%S") - start_time
            })
        del active_sessions[username]


for filename in sorted(files):
    date = re.search(r"(\d{4}-\d{2}-\d{2})", filename).group(1)
    with gzip.open(filename, "rt") as f:
        for line in f:
            match = re.search(r"\[(\d{2}:\d{2}:\d{2})\].*\[connected player\] (\w{3,16}).*has (connected|disconnected)", line)
            if match:
                if "connected" == match.group(3):
                    add_session(match.group(2), match.group(1), date)
                if "disconnected" == match.group(3):
                    end_session(match.group(2), match.group(1), date)
    print(f"File date: {date} completed.")

with open("written_sessions.csv", "w", newline="") as written_sessions:
    writer = csv.DictWriter(written_sessions, fieldnames=["player", "start_time", "end_time", "duration"])
    writer.writeheader()
    for session in completed_sessions:
        writer.writerow(session)

print(len(active_sessions))

# [20:31:31] [Netty epoll Worker #11/INFO] [com.velocitypowered.proxy.connection.client.AuthSessionHandler]: [connected player] BigKenji81 (/177.115.31.237:51642) has connected
# [20:34:19] [Netty epoll Worker #11/INFO] [com.velocitypowered.proxy.connection.MinecraftConnection]: [connected player] BigKenji81 (/177.115.31.237:51642) has disconnected
