from google.appengine.ext import ndb
import webapp2
import logging
import template
import function
from anagram import Anagram


class SubAnagram(webapp2.RequestHandler):
    def get(self):
        logging.debug("GET")
        self.response.headers['Content-Type'] = 'text/html'
        my_user = function.userKey()
        if function.userLoggedIn():
            if not function.userExist():
                function.newUser(function.currentUser())
                
            template.subanagram(self, function.logoutUrl(self), my_user,
                                       self.request.get('name'),
                                       function.usersAnagrams(function.userKey()))

        else:
            template.login(self, function.loginUrl(self))

