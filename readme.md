Add something like this to your `.bash_profile`:
`python /Users/Jesse/Dropbox/reminder/reminder.py &`

---

How to make it stop:

```
$ ps aux | grep reminder
Jesse            53094   0.0  0.0  4277992    728 s000  R+    1:38PM   0:00.00 grep reminder
Jesse            53027   0.0  0.1  4298992   5332 s000  S     1:38PM   0:00.07 /usr/local/Cellar/python@2/2.7.15/Frameworks/Python.framework/Versions/2.7/Resources/Python.app/Contents/MacOS/Python reminder.py

$ kill 53027
```
