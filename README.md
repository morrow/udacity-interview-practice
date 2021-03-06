# Interview Practice


## Job Description
https://careers.simplecast.com/Front-End-Developer

Front-End Developer


Audios Inc is seeking a Front-End Developer to join the Simplecast team; a self-motivated individual with a passion for clean, succinct, reusable code, who isn’t afraid to experiment.

We’re reengineering Simplecast from the ground up. Everything. And nothing is sacred. You’ll be working directly with our Head of Platform and interfacing with our design, backend, and infrastructure teams. You’ll be writing UI code for our best-in-class admin tools, user sharing tools, analytics dashboard, and more. Experience in SaaS is a huge bonus.

We’re looking for people who:

3+ years of demonstrated development experience.
Expertise in JavaScript (with a concentration in Vue.js or React), HTML, CSS, and Node.js tooling.
Expertise working with RESTful APIs and single-page apps.
Familiarity with at least one backend language, eg. PHP, Ruby, Python, GoLang... Our backend is written in Elixir. If you’ve got Elixir experience, massive bonus points!
Familiarity with Git/Gitlab.
Extremely self-motivated and manages time well, both with a team and remotely.
Excellent problem solver with a knack for building industry-innovating tools, thinks beyond current trends.
Bonus: Loves podcasts, and has the drive to innovate the industry.

Nice to haves:

Experience with UX design.
Experience with various 3rd party integrations, eg. Mapbox, Stripe.
Familiarity with AWS.
CI/CD Workflow experience.

Role, Location, Benefits:

Full-time opportunity.
Ideally NYC or Albany-based, but work from anywhere if you’re the right fit.
Medical, dental, and vision benefits coverage. Generous benefit stipend. Generous PTO. 401K. A shiny, new Mac. Tiered budget for continued learning.

If interested, please email your GitHub link, LinkedIn profile, and/or code samples, plus a cover letter, to work@simplecast.com.



## Interview Questions
**1. What is the most influential book or blog post you’ve read regarding web development?**

Paul Graham's essay entitled "Holding A Program In One's Head". In this Essay, Paul discusses his approach to programming in a way that enables you to understand the problem you are solving by keeping the program in your head. One approach to achieve this is to do what's called "bottom-up programming", where you write your program in multiple reusable layers, with each layer enabling a clean abstraction layer for the layer above it, thus only requiring you to keep the top-level layer in your head in order to reason about how your program works. He also suggests using succint languages where possible and keeping your program short so it is easier to keep in your head as well.

**2. Tell me about a web application you have built. Why did you choose to build it? What did you learn? What challenges did you face and how did you overcome them?**

I built a web application using Ruby on Rails which featured a shared code editor for the purpose of pair programming. I built it using Rails 5 and Rails 5's ActionCable interface, which enables websocket connections in addition to the traditional RESTful interface rails uses. This enabled some useful features, such as seamlessly shared editing, where if I type something on screen A, my partner sees on screen B. As well as a simple JavaScript API powered chat system to go alongside the editor. The challenges I faced were that I had never used websockets before, and so implementing it was a challenge that required a lot of research and iterations to work.

**3. Write a function in Python that takes a list of strings and returns a single string that is an HTML unordered list (\<ul>...\</ul>) of those strings. You should include a brief explanation of your code. Then, what would you have to consider if the original list was provided by user input?**

**Initial Version:**

    def getUnorderedList(l):
      return "<ul>%s</ul>" % ''.join(map(lambda x: "<li>%s</li>" % x, l))

  The code uses string interpolation and the 'map' function to surround each list item with list item HTML tags and then surrounds the entire tagged list with the unordered list HTML tag.

**User Input Version:**

    import cgi
    def getUnorderedList(l):
      return "<ul>%s</ul>" % ''.join(map(lambda x: "<li>%s</li>" % cgi.escape(x), l))

This version is the same as above, except it uses a library called 'cgi' to escape each list item. I chose to use a library instead of regex or some similar simple form of sanitizing input because sanitizing input is complicated and important to get right.


**4. List 2-3 attacks that web applications are vulnerable to. How do these attacks work? How can we prevent those attacks?**
  **XSRF or CSRF - Cross-Site-Request-Forgery**
  These attacks work by surreptitiously submitting requests to a website that the user has some kind of credentials with and that the application trusts.
  Example: An attacker uses an IMG tag to send a GET request to 'https://website.com/change-password?newpassword=attackerpass', which triggers website.com to change the user's password.
  We can prevent these attacks by generating tokens and providing them to the user for each page they visit, and disallow requests with an invalid token.

  **XSS - Cross-Site-Scripting**
  XSS is a vulnerability whereby an attacker injects client-side scripts into a user's web page. This is often seen when webpages use HTTP queries or other user inputted data when rendering a page, and do not properly sanitize this input.
  Example: A website has user profiles without sanitized input. An attacker modifies their profile to include the following:
  "This is my profile! \<script>
  We can prevent this by properly sanitizing user input both when it goes into our database and when it is rendered in the browser.

  **SQLi - SQL Injection**
  SQL Injection is a vulnerability similar to XSS whereby an attacker can gain access to a higher level of access to the back-end database than they are supposed to have. This can mean the attacker can run queries, exposing the structure of your database, and in some cases can lead to total compromiization of user data.
  We can prevent this eliminating any direct user input into the database, instead opting for prepared statements or paramaterized queries, which will sanitize the input and disallow an injection attack.


**5. Here is some starter code for a Flask Web Application. Expand on that and include a route that simulates rolling two dice and returns the result in JSON. You should include a brief explanation of your code.**

  **Original Version**

    from flask import Flask
    app = Flask(__name__)

    import json
    import random

    @app.route('/')
    def hello_world():
     return 'Hello World!'

    if __name__ == '__main__':
     app.debug = True
     app.run()

  **Modified Version**

    import random
    from flask import Flask, jsonify

    app = Flask(__name__)

    @app.route('/')
    def hello_world():
     return 'Hello World!'

    @app.route('/roll')
    def roll_dice():
      a = random.randint(1,6)
      b = random.randint(1,6)
      return jsonify([a,b])

    if __name__ == '__main__':
     app.debug = True
     app.run()

   This version adds a route at '/roll' that uses the 'random' library's 'randint' method to generate two psuedorandom integers within a given range (1-6 since we are simulating dice). The response is served as a JSON array using flask's jsonify method.


**6. If you were to start your full-stack developer position today, what would be your goals a year from now?**

I would like to be solving difficult problems and building innovative software which helps users accomplish their goals. I would like to have contributed toward larger organizational projects, and if appropriate, lead development of a project or codebase. As I am new to Elixir, I would have it as a goal to be proficient and comfortable in it as well.