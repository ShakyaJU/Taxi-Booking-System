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

<table>
  <tr>
    <td align="center" colspan="4">
      <b>Sea Level - Use Case Diagram</b><br><br>
      <img src="./TBS Diagrams/Use Case Diagram.jpg" alt="Use Case Diagram" width="800"><br>
      <p align="justify">
        The <strong>Use Case Diagram</strong> outlines the core functionalities of the taxi booking system. Customers can <strong>book, view, update, and cancel bookings</strong> after registering and logging in. Similarly, taxi drivers must register to access assigned bookings. The <strong>admin</strong> oversees the system, managing bookings and assigning drivers.
      </p>
    </td>
  </tr>
  <tr>
    <td align="center">
      <b>Fish Level - Login Process</b><br><br>
      <img src="./TBS Diagrams/Fish1.jpg" alt="Fish-Level Diagram" width="500"><br>
      <p align="justify">
        All actors (<strong>Customer, Driver, and Admin</strong>) must log in using their <strong>email and password</strong> to access their respective dashboards.
      </p>
    </td>
    <td align="center">
      <b>Fish Level - Registration</b><br><br>
      <img src="./TBS Diagrams/Fish2-3.jpg" alt="Fish-Level Diagram 2" width="500"><br>
      <p align="justify">
        Both <strong>customers and taxi drivers</strong> must complete their <strong>registration</strong> by providing the required details before accessing the system.
      </p>
    </td>
  </tr>
  <tr>
    <td align="center" colspan="2">
      <b>Clam Level - User Interfaces</b><br><br>
      <img src="./TBS Diagrams/Clam.jpg" alt="Clam-Level Diagram" width="800"><br>
      <p align="justify">
        <strong>Customer:</strong> Book, view, update, cancel bookings, and log out.<br>
        <strong>Driver:</strong> View assigned bookings and log out.<br>
        <strong>Admin:</strong> Manage users, assign bookings, oversee operations, and log out.
      </p>
    </td>
  </tr>
</table>


 


 ## Activity Diagrams

<table>
  <tr>
    <td align="center">
      <img src="./TBS Diagrams/Customer Activity.jpg" alt="Customer Activity Diagram" width="400">
      <br><b>For Customer</b>
      <p align="justify">
        The customer starts by logging in or registering if they don’t have an account. Once authenticated, they can book a ride, view bookings, update details, or cancel a reservation.
      </p>
    </td>
    <td align="center">
      <img src="./TBS Diagrams/Driver Activity.jpg" alt="Driver Activity Diagram" width="400">
      <br><b>For Driver</b>
      <p align="justify">
        The driver logs in using valid credentials. After authentication, they can view and manage customer bookings assigned to them, ensuring smooth ride operations.
      </p>
    </td>
    <td align="center">
      <img src="./TBS Diagrams/Admin Activity.jpg" alt="Admin Activity Diagram" width="400">
      <br><b>For Admin</b>
      <p align="justify">
        The admin logs in with authorized credentials to access the dashboard. They can view all bookings, assign rides to drivers, and manage registered users, including customers and drivers.
      </p>
    </td>
  </tr>
</table>

 ## ER Diagram
  <p align="center">
  <img src="./TBS Diagrams/ER Diagram.jpg" alt="ER-Diagram" width="1000">
   </p>

<pre>P.S. Feel free to check the documentation if you want to know more about this project by clicking👉<a href="https://drive.google.com/file/d/1DRTYLUQJeab6pC57TT5rg5prtH6tPQxI/view?usp=sharing"> Here </a></pre>

