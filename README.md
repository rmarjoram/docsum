# DocSum Application
DocSum is designed to simplify the work of policymakers and those in decision-making roles by providing summaries of document text such as reports, research, and meeting notes. It is meant to help alleviate information overload and make processes requiring decisions more efficient by reducing delays that might occur from having to sift through large amoutns of relevant information.

DocSum is a simple application that uses OpenAI generative AI for providing summaries of document text. This demonstrates basic assistant functionality using GPT 3.5.

## How to use
The app is configured to run with Flask. If you have Python and Flask, you can clone this repository and run it using `flask run`. If you are using a Mac, you can use the following command in your terminal to run the application:

> `python3 -m flask --app docsum.py run`

Once the application is running, you can access it locally by opening a browser and navigating to http://127.0.0.1:5000/ or localhost:5000 (this is operating system-dependant).

The app takes user input and runs the result using OpenAI's Chat API. The system is configured using the following query:

> 'You are a virtual assistant that provides summaries for text that users input. Your output summaries should be less than 500 words and should be provided in bullet points. The summary should include language and terms used within the text that was submitted by the user.'

The site then writes ChatGPT's response in the space below the button.

## Files

### Front-end
The application's front-end is the file index.html. It displays three input boxes: one for the user's name, one for the user's email address, and one for the document text input. The front-end also provides basic user instructions including the purpose of the application and what the intended output is. 
The static folder contains the Doc Sum robot image (DocSum2.png), which is rendered on the user input page and the icon is displayed in the browser tab. 
The static folder also contains main.css, which defines the visual elements of the input page, including fonts, colours, margins, padding, form input box sizes, and more. 

### docsum.py
This is the back-end python file that runs the who application. It specifies the database connection, the methods for inputting and returning outputs (GET and POST methods), the OpenAI model (GPT-3.5-turbo), and the prompt the model uses. This is also where the pathway to save input to the database is specified.

### Database
User inputs are stored in a database created by the schema.sql file. There are two tables: user and document. 
The user table stores the user name and user email address as entered into the front-end form. The database automatically generates a user ID and a timestamp for the record creation. 
The document table stores the document text input into the front-end form as well as the response generated by the GPT model. The document table is connected to the user table through the auto-generated userID foreign key. 

### Database files
database.db is the locally-housed database for all inputs and responses returned by the AI model. It can be accessed through the terminal/command prompt or through a graphical user interface.
db_test.py tests the database connection to make sure the app is connected to database.db and will prompt it to return results from the tables "user" and "document".
init_db.py initializes the database using the schema.sql file and executes commands to input data into database.db.

### Additional files
License: see [License](#license) for more details; specifies who can use or modify this app and under what circumstances.
README.md: hi, you're already here. I hope this file was valuable!
requirements.txt: minimum environment requirements for running this web application. Use this during installation as specified above.
gitignore: specifies which files will be ignored when updating git or pushing changes to a repository. This mainly includes the __pycache__ and .env files; 
.env: contains the OpenAI API key, and SHOULD NOT be pushed to a public repository.

## Contributing
If you'd like to be a part of this project, consider creating a new branch in the repository and making your changes. Push your branch and create a pull request and we'll implement your changes if they align with the goals of this application. Please be clear in your title and description of changes to reduce confusion and make it easy on us to implement your changes.

## License
This project is licensed under the [MIT License](LICENSE).