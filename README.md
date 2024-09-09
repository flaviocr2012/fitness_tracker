# **Fitness Tracker API**

## **Overview**

This is a project for a RESTful API to track physical activities, developed in Python using the Flask framework. 
The goal is to allow users to register and monitor their physical activities, such as running, cycling, swimming, among others.

## **Technologies Used**

* **Python** 3.12: The main programming language of the project.
* **Flask**: Web framework used for API development.
* **SQLAlchemy**: ORM (Object-Relational Mapping) used for database interaction with SQLite.
* **SQLite**: Relational database used to store user information and their activities.
* **Postman**: Tool used to test the API and simulate HTTP requests.

## **Developed Features**

**User Registration**: Allows creating new users.
**Activity Registration**: Allows adding physical activities associated with a user.
**Activity Query**: Allows querying all activities of a specific user.

## **Available Endpoints**

* ```POST /add_user```: Adds a new user.
* ```POST /add_activity```: Adds a new activity for an existing user.
* ```GET /user/<username>/activities```: Returns all activities of a user.

![Screenshot from 2024-09-09 17-09-48](https://github.com/user-attachments/assets/fb2734e2-c112-4e3b-90fc-41c689aeabff)

![Screenshot from 2024-09-09 17-09-24](https://github.com/user-attachments/assets/b661f978-2773-4f87-bc4e-a3d6e1d04426)


## **Next Steps**

* Implement user authentication and authorization.
* Develop a web interface to facilitate API usage.
* Add more activity metrics (distance, type of exercise, etc.).
* Write unit and integration tests.

## **Project Status**

**🚧Under construction🚧**

This project is still under development, and new features and improvements are being continuously added.
