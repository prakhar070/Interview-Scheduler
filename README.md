# Interview-Scheduler
Interview Schedule Software (InterviewBit SDE intern 2020 assignment)

## Demo Video -
  https://youtu.be/Y7PcSoTYPjs
  
## Approach

As the number of interviews to be taken increase in an organization, I developed a Interview Scheduler that eases the process.

Workflow of the application is that an admin who aims to schedule a new interview first logs in with a valid emailid and password. The admin is then redirected to the home page wherein all of his pending interviews are listed. The admin has the option to edit an  existing interview. The admin can also schedule new interviews.

Following Validations have been performed - 
  - The start time should be less than the end time for an interview
  - The minimum number of participants in an interview must be 2
  - The candidates being scheduled must not be busy in another interview for the same time slot


## Technology Stack

- Django (version = 2.0.5)
- PostgreSQL
- Bootstrap3

## Getting Started

To test, contribute or just see what we did follow few easy steps:
- clone the repository
- Install python3 and python3-pip on your machine
- then create a new virtual environment(env) to work with the current project
- run the virtual enviroment by source env/bin/activate
- install django 2.0.5 using the command 'pip3 install django==2.0.5'
- then we need to setup PostgreSQL to work django 
  Here is the link on how to setup PostgreSQL for django-
  https://www.digitalocean.com/community/tutorials/how-to-use-postgresql-with-your-django-application-on-centos-7
- Create a new database and a new user to handle that database
- Change the database settings in settings.py file - 
  for reference - 
  https://www.digitalocean.com/community/tutorials/how-to-use-postgresql-with-your-django-application-on-centos-7
- Create a new superuser that will act as admin - 
  python3 manage.py createsuperuser
- migrate all the changes to the database by the command-
  python3 manage.py makemigrations
  python3 manage.py migrate
- Now, your local development enviroment is set. To run the server , type python3 manage.py runserver. By default, the server
  will start on port 8000.


## Contributing

1. Fork it (<https://github.com/prakhar070/Interview-Scheduler>)
2. Create your feature branch (`git checkout -b feature/fooBar`)
3. Commit your changes (`git commit -am 'Add some fooBar'`)
4. Push to the branch (`git push origin feature/fooBar`)
5. Create a new Pull Request


