# SmashMC-Data-Analysis
Python and SQL scripts to parse Minecraft Proxy logs into player-retention and chat-categorisation datasets. 

## Why this exists
I wanted hands-on experience with working on large, muddy datasets before moving into my masters degree and SmashMC's resources provided me with a large, messy, real-world dataset to apply my learning to. This allowed me to feed statistically-informed findings back to the rest of the management team. 

## Current Pipeline

### classifyLogs.py
This script parses gzipped log files, extracts all chat messages and uses a small local AI model to classify them into different categories. Once categorized, it outputs to a CSV file containing user, message and label.

### /VelocityRetention/main.py
This script parses through gzipped velocity logs with regex in order to identify connected and disconnected events across the whole server. These events are logged into a large CSV file with log-in time, log out time and total duration saved.  

### /VelocityRetention/analysis.py
This script allows for CSV files to be opened in a SQLite database, ready for querying. 

## Roadmap

### Finishing analysis.py
Currently I have not included any SQL queries to run against the analysis. I plan to change this and include a thorough analysis into playtime data and retention analytics.

### Data Visualisation
I plan on learning matplotlib/seaborn to be able to visually demonstrate some of the data I find. 

### Attach playtime data to other variables
Playtime is a useful metric, but only covers a portion of what makes each player important. Connecting this data to in-game behaviour, microtransactions, chatting habits etc would result in more well-rounded analysis. 

## Setup
Full instructions to setup will appear later, here is a list for now:
- Python 3.6+
- pandas
- requests
- Ollama Running on localhost:11434
- qwen2.5:3b
- Minecraft Chat Logs and Velocity logs (You can't have mine)
