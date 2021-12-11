## product name - automated attendance system


### what is this?
a face recognition based attendance system for students in my department

### why am i making it?
curiosity. I had just started learning openCV from sentdex and techwithtim and what better way to put it to the test. I got to research existing biometric based attendance systems, and found a afaster way to streamline the entire workflow for my department.

![gif of working prototype](https://media3.giphy.com/media/2vogqNpFQywWC0z0j5/giphy.gif)
<center style=color:grey;>sitting duck</center>

### want to use it?
you probably can if you want to but you'll need to tweak the code and setup your email provider to work with smtplib and the google sheets API so you do not get flagged. this should not be hard to do, just look it up

### how it works
using your primary camera or webcam, the facerec program will identify and recognise faces available in the "known_faces" dir. recognised faces will trigger the "sheets.py" program to mark the student as present in the specified google spreadsheet, and at the end of the day the full attendance list will be sent to the lecturer's email.

#### technologies
this was built entirely with love on an eventful day with:

- python
- smtplib
- google sheets api
- ❤️

### what's coming next
probably nothing. I am pretty satisfied with how it turned out. maybe working with other departments to replace their existing paper based attendance system

### want to help make this better?
you are a massive nerd if you think this is cool and want to contribute to it😂, i love you still. just make a pr with any changes you have or shoot me a dm on twitter

[//]: # (So depending on use case, you may want to keep the documentation short. in that case you may not need to include the last two sections or you can)
