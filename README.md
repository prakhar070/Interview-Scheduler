# Interview-Scheduler
Interview Schedule Software (InterviewBit SDE intern 2020 assignment)

## Demo Video (https://youtu.be/kEOYu0fHAEo)
[Watch the video here](https://youtu.be/kEOYu0fHAEo)

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
- cd to the directory with the repository
- run `yarn install` (or `npm install` if you don't use yarn)
- Go to Nexmo website (<https://www.nexmo.com>), signup there and get your API key and secret
- Make .env file and insert details there regarding API_KEY,API_SECRET for making connection to nexmo api and details of your e-mail and password required to send mail using nodemailer api.
- run the app using `yarn start` (or `npm start`)
- now, open (<http://localhost:3000>) & enjoy!


## Contributing

1. Fork it (<https://github.com/prakhar070/Interview-Scheduler>)
2. Create your feature branch (`git checkout -b feature/fooBar`)
3. Commit your changes (`git commit -am 'Add some fooBar'`)
4. Push to the branch (`git push origin feature/fooBar`)
5. Create a new Pull Request


