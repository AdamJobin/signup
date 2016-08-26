
#
import webapp2, re
page_header="""
<!DOCTYPE html>
<html>
<head>
    <title>Signup</title>
    <style type="text/css">
        p.error {
            color: red;
        }
    </style>
</head>
<body>
"""

page_footer="""
</body>
</html>
"""

class MainHandler(webapp2.RequestHandler):
    def get(self):
        name_form="""
        <form action="/name" method="post">
            <label for="username">Username</label>
                <input name="name" type="text">
                <br>
            <label for="password">Password</label>
                <input name="password" type="password">
                <br>
            <label for="verify">Verify Password</label>
                <input name="verify" type="password">
                <br>
            <label for="email">Email(Optional)</label>
                <input name="email" type="email">
                <br>
                <input type="submit">
        </form>
        """
        self.response.write(page_header + name_form + page_footer)

class Response(webapp2.RequestHandler):
    def post(self):
        username= self.request.get("name")
        password1= self.request.get("password")
        verify1= self.request.get("verify")
        email1= self.request.get("email")

        if username == "":
            error1= "Please enter a username."
        elif not re.match("^[a-zA-Z0-9_-]{3,20}$", username):
            error1="Please enter a valid username"
        else:
            error1= ""
        if password1 != verify1:
            error2= "Passwords do not match"
        else:
            error2= ""

        name_form_response="""
        <form action= "/name" method= "post">
            <label for="username">Username</label>
                <input name="name" type="text">
                <br>
            <label for="password">Password</label>
                <input name="password" type="password">
                <br>
            <label for="verify">Verify Password</label>
                <input name="verify" type="password">
                <br>
            <label for="email">Email(Optional)</label>
                <input name="email" type="email">
                <br>
                <input type= "submit">
                <br>
                <p class="error">""" + error1 + error2 + """</p>
        </form>
        """
        self.response.write(page_header + name_form_response + page_footer)



app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/name', Response)
], debug=True)
