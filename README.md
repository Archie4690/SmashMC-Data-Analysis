# SmashMC-Data-Analysis
Python and SQL scripts to parse Minecraft Proxy logs into player-retention and chat-categorisation datasets. 

## Why this exists?
I wanted hands-on experience with working on large, muddy datasets before moving into my masters degree and SmashMC's resources provided me with a large, messy, real-world dataset to apply my learning to. This allowed me to feed statistically-informed findings back to the rest of the management team. 

## Current Pipeline

### classifyLogs.py
This script parses gzipped log files, extracts all chat messages and uses a small local AI model to classify them into different categories. Once categorized, it outputs to a CSV file containing user, message and label.

### /VelocityRetention/main.py
This script parses through gzipped velocity logs with regex in order to identify connected|disconnected events across the whole server. These events were logged into a large CSV file with log-in time, log out time and total duration saved.  

### /VelocityRetention/analysis.py
This script allows for CSV files to be opened in a SQLite server, ready for querying. 

## Roadmap

### 

### 

## Setup
