from google.appengine.ext import ndb
import webapp2
import logging
import template
import function
from anagram import Anagram


class Add(webapp2.RequestHandler):
    def get(self):
        logging.debug("GET")
        self.response.headers['Content-Type'] = 'text/html'
        my_user = function.userKey()
        if function.userLoggedIn():
            if not function.userExist():
                function.newUser(function.currentUser())
                
            template.add(self, function.logoutUrl(self), my_user,
                       function.usersAnagrams(function.userKey()))

        else:
            template.login(self, function.loginUrl(self))

    def post(self):
        logging.debug("POST")
        self.response.headers['Content-Type'] = 'text/html'

        my_user = function.userKey()
        button = self.request.get('button')
        input_text = function.inputResult(self.request.get('value'))
        logging.debug(input_text)
        logging.debug(button)

        if button == 'Add':
            self.add(input_text, my_user)
            self.redirect('/add')


    def add(self, text, my_user):
        logging.debug('Add ' + text)      
        if text is not None or text != '':
            anagram_id = function.lexicographical_order(text)
            anagram_key = ndb.Key(Anagram, anagram_id)
            anagrams = anagram_key.get()
            if anagrams:
                function.add_anagram(my_user, text, anagram_key) 
            else:
                function.add_newAnagram(my_user, text, anagram_id, anagram_key)

