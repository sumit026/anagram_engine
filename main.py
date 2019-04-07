from google.appengine.ext import ndb
import webapp2
import logging
import template
import function
from anagram import Anagram
from add import Add
from search import Search
from upload import Upload
from subanagram import SubAnagram


class MainPage(webapp2.RequestHandler):
    def get(self):
        logging.debug("GET")
        self.response.headers['Content-Type'] = 'text/html'
        my_user = function.userKey()
        
        if function.userLoggedIn():
            if not function.userExist():
                function.newUser(function.currentUser())

            template.main(self, function.logoutUrl(self), my_user,
                                 function.usersAnagrams(function.userKey()))

        else:
            template.login(self, function.loginUrl(self))



app = webapp2.WSGIApplication(
    [
        ('/', MainPage),
        ('/add', Add),
        ('/search', Search),
        ('/upload', Upload),
        ('/subanagram', SubAnagram),
    ], debug=True)
