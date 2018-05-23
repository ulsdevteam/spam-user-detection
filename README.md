# spam-user-detection

This application helps in detection of spam users in Drupal, by analyzing the dataset and doing feature selection and finally ending with a decision tree.

## Getting started.

This is an application which can either be run on a jupyter notebook or for feasibility, you could download this as a cgi application on your server.

### Requirements
* Apache Web Server
* Python 3.6

### Installation

1) You need to copy the 'spam_trap.py', 'actual_words.csv', 'spamwords.csv','term_frequency.csv' files to your cgi-bin folder.

2) Also create a folder 'uni' in your public directory '/var/www/html'. Setting the access for this folder to 777.

3) Change the 'Timeout value to 400' in your web server conf file.

4) Now go to your python3.6 location, make sure the location is '/usr/local/bin/python3.6' or you can also have it any location and change the 'spam_trap.py' script to start with the 'shebang' of the desired location , there will be a pip file out here. You would need to run the following commands to install the dependencies for this project.

```bash
$ pip install numpy
$ pip install pandas
$ pip install csv
$ pip install unicodecsv
$ pip install re
$ pip install multiprocessing
$ pip install time
$ pip install datetime
$ pip install cgitb
$ pip install cgi
```

Some of these modules will already be pre installed, but it is always nice to recheck.


5) You would need to provide a csv file with the following mysql query, 

```
SELECT 
    users.*,
    COALESCE(user_settings.setting_value) AS biography,
    COALESCE(signs.setting_value) AS signature
FROM
    users
        LEFT OUTER JOIN
    user_settings ON (users.user_id = user_settings.user_id
        AND user_settings.setting_name = 'biography')
        LEFT OUTER JOIN
    user_settings AS signs ON (users.user_id = signs.user_id
        AND signs.setting_name = 'signature')
GROUP BY users.user_id
```

6) Upload the file, wait for two minutes/ 40000 users. Click on the download link, it will provide you a corresponding csv file with only the spam user names.






