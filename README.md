<h2>NoteBUDDY - Online Note Sharing Platform</h2>
NoteBUDDY is a Django-based web application that allows users to create, publish, and manage their notes online. Users can perform CRUD (Create, Read, Update, Delete) operations on their notes, and they have the option to publish notes for others to access on the Global Notes Zone. The project ensures user privacy through a robust user authentication system, allowing users exclusive access to their unpublished notes.

<h6>Features</h6>
<b>User Authentication:</b> Secure user accounts with authentication and authorization.
<b>CRUD Operations:</b> Users can Create, Read, Update, and Delete their notes.
<b>Privacy:</b> Unpublished notes are private to the user, ensuring data confidentiality.
<b>Global Notes Zone:</b> Users can publish notes for others to access in the Global Notes Zone.

<h6>How to Run the Project</h6>
Follow these steps to run the NoteBUDDY project on your local machine:

<h6>Prerequisites</h6>
Python installed on your machine.
pip (Python package installer) installed.

<h6>Clone the Repository</h6>
--->   git clone https://github.com/your-username/NoteBUDDY.git
       cd NoteBUDDY

<h6>Create a Virtual Environment (Optional but recommended)</h6>
--->   python -m venv venv
       Activate the virtual environment:

<h6>For Windows:</h6>
--->   .\venv\Scripts\activate
<h6>For MacOS/Linux:</h6>
--->   source venv/bin/activate

<h6>Install Dependencies</h6>
--->   pip install -r requirements.txt

<h6>Apply Database Migrations</h6>
--->   python manage.py migrate

<h6>Create Superuser (Admin)</h6>
--->   python manage.py createsuperuser
    Follow the prompts to create a superuser account.

<h6>Run the Development Server</h6>
--->   python manage.py runserver

Visit http://127.0.0.1:8000/ in your browser to access the NoteBUDDY application.

Access Admin Panel
Visit http://127.0.0.1:8000/admin/ and log in with the superuser credentials created earlier.
