
# Set up your search query
The search query determines the condition for triggering the alert. For instance, suppose you're searching for logs with a status field that can either be Green or Red:

```
index="your_index" source="your_source" | search status="Green" OR status="Red"
```

```
Job - $result.status$
```

```
{"time": "2024-12-13 03:40:17,501", "level": "INFO", "func": "run_robot_script", "mes": "CII Robot Automation2 -  {"status": "FAILED", "message": "Script failed with return code 1"}"}
```

```
your_search_query
| rex field=mes "\"status\":\s*\"(?<status>[^\"]+)\""
| table time level func status
```
