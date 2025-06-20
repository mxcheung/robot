
Great — if you want each file in a folder to become its own test case without using a preprocessing script, you can simulate dynamic test cases using Robot Framework’s built-in FOR loop inside a single test case or define multiple keywords with a template-style approach. But true dynamic test generation without preprocessing requires a custom Python library.

However, here's a clean compromise: use the built-in OperatingSystem library and create a single test case that loops through all files, logging the content as separate Robot keywords, and let Robot log show each file clearly.

