# My-Gallery
## Author 
>[Vivian-Gichuki]
# Description 
This is a Django application for my personal gallery where a user can upload images for other to see and be able to search for images according to their category.
##  Live Link 
 Click [View Site](galleryapp21.herokuapp.com/)  to visit the site
## User Story 
* View different photos that interest them
* Click a single image to expand it and view the details of that photo
* Search for different categories
* Copy a link to the photo to share with my friends.
* View photos based on the location they were taken.
## Setup and Installation 
To get the project .......
##### Cloning the repository: 
 ```bash
https://github.com/VGichuki/gallery-app
```
##### Navigate into the folder and install requirements 
 ```bash
cd Picture-Globe pip install -r requirements.txt
```
##### Install and activate Virtual 
 ```bash
- python3 -m venv virtual - source virtual/bin/activate
```
##### Install Dependencies 
 ```bash
 pip install -r requirements.txt
```
##### Setup Database 
  SetUp your database User,Password, Host then make migrate
 ```bash
python manage.py makemigrations pictures
 ```
 Now Migrate
 ```bash
 python manage.py migrate
```
##### Run the application 
 ```bash
 python manage.py runserver
```
##### Running the application 
 ```bash
 python manage.py server
```
##### Testing the application 
 ```bash
 python manage.py test
```
Open the application on your browser `127.0.0.1:8000`.
## Technology used 
* [Python3.8]
* [Django]
* [Heroku]
## Known Bugs
* There are no known bugs currently but pull requests are allowed incase you spot a bug
## License
* *MIT License:*
* Copyright (c) 2021 **Vivian Gichuki**
Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.