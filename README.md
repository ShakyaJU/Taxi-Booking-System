<h1 align="center">Taxi Booking System</h1>

<h3 style="text-align: justify;">This Python project demonstrates key principles of N-tier architecture, featuring a structured and user-friendly taxi booking and management system. The application starts with a Login and Registration Page, where customers, drivers, and admins can access their respective interfaces. Customers can book, update, and cancel trips, drivers can view assigned bookings, and admins manage the overall system, assigning drivers and monitoring records.

Developed in PyCharm IDE, the GUI was designed using Tkinter, following a prototype created in Balsamiq Wireframes. External libraries such as mysql-connector-python (for database connection), Pillow (for image handling), and tkcalendar (for date entry) were integrated to enhance functionality. The database was managed using phpMyAdmin (MySQL), with XAMPP used as the local server.
<pre>
The system follows a four-layer architecture:

Frontend Layer – Manages the GUI using Tkinter.
Business Layer – Handles core logic and validation.
Database Layer – Uses MySQL queries for data retrieval.
Models Layer – Defines getter and setter properties for system entities.
</pre></h3>


## Application Screenshots:

<p align="center">
  <img src="./TBS Diagrams/Picture1.png" alt="App screenshots" width="300">
  <img src="./TBS Diagrams/Picture2.png" alt="App screenshots" width="300">
  <img src="./TBS Diagrams/Picture3.png" alt="App screenshots" width="300">
  <img src="./TBS Diagrams/Picture4.png" alt="App screenshots" width="300">
  <img src="./TBS Diagrams/Picture5.png" alt="App screenshots" width="300">
  <img src="./TBS Diagrams/Picture6.png" alt="App screenshots" width="300">
  <img src="./TBS Diagrams/Picture7.png" alt="App screenshots" width="300">
  <img src="./TBS Diagrams/Picture8.png" alt="App screenshots" width="300">
  </p>

 ## Use Case Diagrams  

### Sea Level  
<p align="center">
  <img src="./TBS Diagrams/Use Case Diagram.jpg" alt="Use Case Diagram" width="900">
</p>  
<p align="justify">
  The <strong>Use Case Diagram</strong> outlines the core functionalities of the taxi booking system. Customers can <strong>book, view, update, and cancel bookings</strong> after registering and logging in. Similarly, taxi drivers must register to access assigned bookings. The <strong>admin</strong> oversees the system, managing bookings and assigning drivers.  
</p>  

---

### Fish Level  
<p align="center">
  <img src="./TBS Diagrams/Fish1.jpg" alt="Fish-Level Diagram" width="900">
</p>  
<p align="justify">
  All actors (<strong>Customer, Driver, and Admin</strong>) must log in using their <strong>email and password</strong> to access their respective dashboards.  
</p>  

<p align="center">
  <img src="./TBS Diagrams/Fish2-3.jpg" alt="Fish-Level Diagram 2" width="900">
</p>  
<p align="justify">
  Both <strong>customers and taxi drivers</strong> must complete their <strong>registration</strong> by providing the required details before accessing the system.  
</p>  

---

### Clam Level  
<p align="center">
  <img src="./TBS Diagrams/Clam.jpg" alt="Clam-Level Diagram" width="900">
</p>  
<p align="justify">
  - <strong>Customer Interface:</strong> Customers can <strong>book, view, update, and cancel bookings</strong>, and log out when needed.  
  - <strong>Driver Interface:</strong> Drivers can <strong>view assigned bookings</strong> and log out of the system.  
  - <strong>Admin Interface:</strong> Admins can <strong>manage customer and driver data, assign bookings, and oversee system operations</strong> before logging out.  
</p>


  ## ER Diagram
  <p align="center">
  <img src="./TBS Diagrams/ER Diagram.jpg" alt="ER-Diagram" width="1500">
   </p>

  ## Activity Diagram
  <p align="center">
  <img src="./TBS Diagrams/Activity Diagram.jpg" alt="A-Diagram" width="1500">
   </p>

<pre>P.S. Feel free to check the documentation if you want to know more about this project by clicking clicking👉<a href="https://drive.google.com/file/d/1v8e1hjOh4HFUHC5OnIVz-uDM-V4875j6/view?usp=sharing"> Here </a></pre>

