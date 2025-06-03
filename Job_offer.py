machio@DESKTOP-68BKMSN:~$ pwd
/home/machio
machio@DESKTOP-68BKMSN:~$ ls
'#Prepostfix.java#'       Main1.2.java~                   machio1.2.py~
'#facebook_users.py#'     Main1_2.class                   machio1.3.py~
'#firstEmac.py#'          Main1_2.java~                   my_projects
'#for_extended.py'\''#'   Prepostfix.java~                rangefunc1.0,py
 Break_statements1.py     break_continue.py~              rangefunc1.0.py~
 For_extended.py~         facebook_users.py~              snap
 Machio.class             macchio_FOR_statement_1.3.py~
 Machio.java~             machio.py~
machio@DESKTOP-68BKMSN:~$ python3 Break_statement1.py
python3: can't open file '/home/machio/Break_statement1.py': [Errno 2] No such file or directory
machio@DESKTOP-68BKMSN:~$ python3 Break_statements1.py
6 is equals to 3 * 2
8 is equals to 4 * 2
9 is equals to 3 * 3
10 is equals to 5 * 2
machio@DESKTOP-68BKMSN:~$ python3 facebook_users.py
python3: can't open file '/home/machio/facebook_users.py': [Errno 2] No such file or directory
machio@DESKTOP-68BKMSN:~$ python3 facebook_users.py~
  File "/home/machio/facebook_users.py~", line 2
    users = {'Machio':'online','Peter':'offline':,'Derric':'online',
                                                ^
SyntaxError: invalid syntax
machio@DESKTOP-68BKMSN:~$ python3 Break_statements1.py
6 is equals to 3 * 2
8 is equals to 4 * 2
9 is equals to 3 * 3
10 is equals to 5 * 2
2 is an even number
3 is an odd number
4 is an even number
5 is an odd number
6 is an even number
7 is an odd number
8 is an even number
9 is an odd number
10 is an even number
11 is an odd number
12 is an even number
13 is an odd number
14 is an even number
15 is an odd number
16 is an even number
17 is an odd number
18 is an even number
19 is an odd number
machio@DESKTOP-68BKMSN:~pwd
/home/machio
machio@DESKTOP-68BKMSN:~$ ls
'#Break_statements1.py#'   Machio.class                    machio.py~
'#Prepostfix.java#'        Machio.java~                    machio1.2.py~
'#facebook_users.py#'      Main1.2.java~                   machio1.3.py~
'#firstEmac.py#'           Main1_2.class                   my_projects
'#for_extended.py'\''#'    Main1_2.java~                   rangefunc1.0,py
 Break_statements1.py      Prepostfix.java~                rangefunc1.0.py~
 Break_statements1.py~     break_continue.py~              snap
 For_extended.py~          facebook_users.py~
 Job_offers.py             macchio_FOR_statement_1.3.py~
machio@DESKTOP-68BKMSN:~$ python3 Job_offers.py
  File "/home/machio/Job_offers.py", line 7
    {'Name':'Angela','submitted_resume':False,'Accepted_other_offer':True}
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
SyntaxError: invalid syntax. Perhaps you forgot a comma?
machio@DESKTOP-68BKMSN:~$ python3 Job_offers.py
  File "/home/machio/Job_offers.py", line 16
    print(f'skipping{applicant['Name']} no resume submitted')
                                ^^^^
SyntaxError: f-string: unmatched '['
machio@DESKTOP-68BKMSN:~$ python3 Job_offers.py
  File "/home/machio/Job_offers.py", line 16
    print(f"skipping {applicant["Name"]} no resume submitted")
                                 ^^^^
SyntaxError: f-string: unmatched '['
machio@DESKTOP-68BKMSN:~$ python3 Job_offers.py
  File "/home/machio/Job_offers.py", line 21
    print(f"Interviewing {applicant['Name']...")
                                               ^
SyntaxError: f-string: expecting '}'
machio@DESKTOP-68BKMSN:~$ python3 Job_offers.py
Traceback (most recent call last):
  File "/home/machio/Job_offers.py", line 15, in <module>
    if not applicant['submited_resume']:
KeyError: 'submited_resume'
machio@DESKTOP-68BKMSN:~$ 