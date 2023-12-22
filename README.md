<h2>NoteBUDDY - Online Note Sharing Platform</h2>
NoteBUDDY is a Django-based web application that allows users to create, publish, and manage their notes online. Users can perform CRUD (Create, Read, Update, Delete) operations on their notes, and they have the option to publish notes for others to access on the Global Notes Zone. The project ensures user privacy through a robust user authentication system, allowing users exclusive access to their unpublished notes.

<h5>Features</h5>
<b>User Authentication:</b> Secure user accounts with authentication and authorization.<br>
<b>CRUD Operations:</b> Users can Create, Read, Update, and Delete their notes.<br>
<b>Privacy:</b> Unpublished notes are private to the user, ensuring data confidentiality.<br>
<b>Global Notes Zone:</b> Users can publish notes for others to access in the Global Notes Zone.

<h5>How to Run the Project</h5>
Follow these steps to run the NoteBUDDY project on your local machine:

<h5>Prerequisites</h5>
Python installed on your machine.
pip (Python package installer) installed.

<h5>Clone the Repository</h5>
--->   git clone https://github.com/your-username/NoteBUDDY.git
       cd NoteBUDDY

<h5>Create a Virtual Environment (Optional but recommended)</h5>
--->   python -m venv venv
       Activate the virtual environment:

<h5>For Windows:</h5>
--->   .\venv\Scripts\activate
<h5>For MacOS/Linux:</h5>
--->   source venv/bin/activate

<h5>Install Dependencies</h5>
--->   pip install -r requirements.txt

<h5>Apply Database Migrations</h5>
--->   python manage.py migrate

<h5>Create Superuser (Admin)</h5>
--->   python manage.py createsuperuser
    Follow the prompts to create a superuser account.

<h5>Run the Development Server</h5>
--->   python manage.py runserver

Visit http://127.0.0.1:8000/ in your browser to access the NoteBUDDY application.

Access Admin Panel
Visit http://127.0.0.1:8000/admin/ and log in with the superuser credentials created earlier.
