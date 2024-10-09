# P-DaiSy - Police Database and Identification System
A highly scalable facial recognition and information storage & retrieval system designed to enhance the efficiency of law enforcement in tracking and managing missing persons and individuals with criminal histories.
Made by [Saipranav M](https://github.com/AvGeeky) and [Ayushi Choudhary](https://github.com/ayushi16055) as part of their CBSE Class 12 Board Project.

## Table of Contents
- [Introduction](#introduction)
- [Objective and scope](#objective-and-scope)
- [System Design](#system-design)
- [Demo](#demo)
- [Python Modules used](#python-modules-used)
- [Challenges and Future Scope](#challenges-and-future-scope)
  
 ## Introduction
The Missing Person - Police Database and Identification System combines the aspects of a database system to store the details of missing people and a two-pronged searching system to access this database. The searching mechanism includes a MPIN-ID searching system which cross references a unique identification number assigned to each database element during creation to one entered by the user, as well as a face recognition system which takes any image of the missing persons’ face and cross references it with pre-existing reference images in a database to search for the person. Upon successful cross referencing, it returns all details of the missing person from the database. To keep the database system secure, a password and username based authentication system is in place. If the user forgets their credentials, a one-time password can be sent to their registered email address which will help them log them in.

## Objective and scope
With more than 15600 missing children and 17000 missing people in the state of Tamil Nādu; maintaining a system to store all details with a searching mechanism is a need of the hour. This is the objective of P-DaIsy, which can help to maintain a database for the above mentioned purpose, and hence help police and law enforcement officials in their search for finding missing people using images from CCTV feeds or other sources; or take one on the spot such as in the police station setting. The quickness of this program in searching for missing people can be a great asset for the state police.

## System Design
![My Image](https://raw.githubusercontent.com/AvGeeky/csproject-P-DaISy/refs/heads/main/sys-design.png)

## Demo 
### [Demo Screenshots of P-DaiSy](https://drive.google.com/file/d/1mGDRtvZr8T76_VHCbjpuyhtXWMiY1k6n/view)

## Python Modules used
 - Tkinter (tkinter,tkinter.font, tkinter.filedialog)
 - smtplib
 - random
 - PIL
 - os
 - face_recognition
 - cv2
 - csv
 - tkcalendar
 - tktimepicker
 - datetime

## Challenges and Future Scope
During the course of this project, understanding the different elements that come into the picture while considering all the aspects included in this for example image capturing, display, facial recognition, data inputting, editing and updating was a difficult task.
The code could have been much more efficient. The modules could have been used more efficiently than it currently is. The graphic interface could have been more aesthetic and user friendly. The implementation of the concept could have included a lot of other things considering the wide bracket this topic includes.
For the future, an edit option can be added for the user to edit the details already present in the database. Additionally, a button/key can be added to capture the image instead of the spacebar as is the case right now. It can also display the image uploaded while filing a new report when the rest of the information is being displayed for confirmation.
An administrator and a general public version of the program and interface can also be developed at a later stage.
