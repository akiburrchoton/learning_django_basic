# Django Framework Basic Learning
After completing basic Python Programming, now I have started learning Django framework since I want to develop complex projects soon. 


<h3>Here are the links of the Python course completion certificate:</h3>
<ol>
  <li>Programming for Everybody (Getting Started with Python) - <a href="https://coursera.org/share/a671580c949fceced97b773e26ed41d1" target="_blank">View</a></li>
  <li>Python Data Structures - <a href="https://coursera.org/share/0dd25647d6b1f2fc4bb714117214c96a" target="_blank">View</a></li>
  <li>Using Databases with Python - <a href="https://coursera.org/share/bda801b6db32f13c8573fd28a963c96e" target="_blank">View</a></li>
  <li>Using Python to Access Web Data - <a href="https://coursera.org/share/aee8d83ed3caea398d2e8dd4a8b2df92" target="_blank">View</a></li>
</ol> 

<p>Before 11.07.2020 I have practiced how Models, makemigrations and migrate works. Moreover, I also learned what views.py does, how to make URLs dynamic etc. From here I will note everything down what I learn.</p>

<div>
    <h2>Date: 11.07.2020</h2>
    <ol>
        <li>Basic CRUD Feature</li>
    </ol>
</div>
<div>
    <h2>Date: 12.07.2020</h2>
    <ol>
        <li>Inline Formsets</li>
        <li>Filter Form Table Search</li>
    </ol>
</div>

<div>
    <h2>Date: 13.07.2020</h2>
    <ol>
        <li>User Regstration</li>   
        <ul>
          <li>Register new users through form</li>
          <li>Showing Error Messages</li>
          <li>Showing Success Message</li>
        </ul>
        <li>User Login Authentication</li>
        <ul>
          <li>Login to the system through form</li>
          <li>Showing Error Messages</li>
          <li>Showing Success Message</li>
        </ul>
        <li>Basic User Restrictions</li>
        <ul> 
          <li>If user is logged in they cannot see login, register page</li>
          <li>If user is not logged in they cannot see any other pages than login and register page.</li>
        </ul>
    </ol>
</div>

<div>
    <h2>Date: 15.07.2020</h2>
    <ol>
        <li>Restrict Users Based On Their Roles</li>   
        <ul>
          <li>Customers cannot see main dashboard page and some specific contents</li>
          <li>Only admins can see all pages(except login/signup if logged in)</li>
          <li>Restrict users by creating Decorators</li>
        </ul>
        <li>User Profile with One to One relationship</li>
        <ul>
          <li>Create extra model to hold extra information </li>
          <li>Based on this, now customer will be able to see their information in the User page</li>
          <li>if customer sign up, their role will be Customer automatically</li>
        </ul>
    </ol>
</div>
