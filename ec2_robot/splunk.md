
# Set up your search query
The search query determines the condition for triggering the alert. For instance, suppose you're searching for logs with a status field that can either be Green or Red:

```
index="your_index" source="your_source" | search status="Green" OR status="Red"
```

```
Job - $result.status$
```
