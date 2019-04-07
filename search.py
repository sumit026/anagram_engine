from google.appengine.ext import ndb
import webapp2
import logging
import template
import function
from anagram import Anagram


class Search(webapp2.RequestHandler):
    def get(self):
        logging.debug("GET")
        self.response.headers['Content-Type'] = 'text/html'
        my_user = function.userKey()
        if function.userLoggedIn():
            if not function.userExist():
                function.newUser(function.currentUser())
                
            template.searchtext(self, function.logoutUrl(self), my_user,
                                       function.lexicographical_order(self.request.get('value')),
                                       function.inputResult(self.request.get('value')),
                                       function.usersAnagrams(function.userKey()))
        else:
            template.login(self, function.loginUrl(self))

