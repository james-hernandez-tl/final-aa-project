# KnowVerse

KnowVerse is a quizlet clone where users have full CRUD on sets and folders. They can create and use these sets to study.

check out [KnowVerse](https://knowverse.onrender.com)

## Index

[MVP Feature List ](https://github.com/ihavenoide/final-aa-project/wiki/MVP-Feature-List) | [Database Scheme](https://github.com/ihavenoide/final-aa-project/wiki/Database-Schema-and-Backend-Routes) | [User Stories](https://github.com/ihavenoide/final-aa-project/wiki/User-Stories) | [Wire Frames](https://github.com/ihavenoide/final-aa-project/wiki/Wireframes)

## Technologies Used

![JavaScript](https://img.shields.io/badge/javascript-%23323330.svg?style=for-the-badge&logo=javascript&logoColor=%23F7DF1E)
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![React](https://img.shields.io/badge/react-%2320232a.svg?style=for-the-badge&logo=react&logoColor=%2361DAFB)
![Redux](https://img.shields.io/badge/redux-%23593d88.svg?style=for-the-badge&logo=redux&logoColor=white)
![Flask](https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white)
![Postgres](https://img.shields.io/badge/postgres-%23316192.svg?style=for-the-badge&logo=postgresql&logoColor=white)

## Getting started

1. Clone this repository: https://github.com/ihavenoide/final-aa-project.git
2. Install denpendencies into the Backed and the Frontend by making a terminal for each one and then run the following:
   * backend (In base of directory):
       * ` Pipenv install `
   * frontend :
       * ` npm install `
3. Create a .env file using the .envexample provided

4. Set up your database with information from your .env and then run the following to create your database, migrate, and seed (base directory):
   * ` Pipenv shell `
   * ` flask db init `
   * ` flask db migrate `
   * ` flask db upgrade `
   * ` flask seed all `
5. Start the app for both backend and frontend using:
   * backend :
       * ` flask run `
   * fontend :
       * ` npm start `
## Amazon Web Services S3
   * For setting up your AWS refer to this [guide](https://github.com/jdrichardsappacad/aws-s3-pern-demo)


## Home Page

https://github.com/ihavenoide/final-aa-project/assets/104161335/cb8d39cc-5cbc-467d-98b7-be4fa8c6b668

## Sets

https://github.com/ihavenoide/final-aa-project/assets/104161335/e3bdcef6-61c2-49e5-a0a7-cc791b513f99

## Folders

https://github.com/ihavenoide/final-aa-project/assets/104161335/0418f2e7-20ab-4cd3-a888-8f6ade2b9d44


## Features
### Sets
   * Users can create a set
   * Users can read/view other Sets
   * Users can update their Sets
   * Users can delete their Sets
   * Users can rate Sets on a scale of 1-5
### Folders
   * Users can create a Folder
   * Users can read/view their own Folders
   * Users can update their Folders
   * Users can delete their Folders
### Search
   * In the nav bar users can search for public Sets filtered by name/description
   * When viewing their own Sets Users can filtered by name/description
   * When viewing their own Folders Users can filtered by name/description

## Future Features
   * Search for Users
   * Follow other Users
   * Ai chat to help users study sets
   * Achievements to track users progress
     
