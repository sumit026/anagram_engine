from google.appengine.ext import ndb
import webapp2
import logging
import template
import function
import re
from anagram import Anagram
from add import Add
from myuser import MyUser
from itertools import combinations


class Upload(webapp2.RequestHandler):
    def get(self):
        logging.debug("GET")
        self.response.headers['Content-Type'] = 'text/html'
        my_user = function.userKey()
        if function.userLoggedIn():
            if not function.userExist():
                function.newUser(function.currentUser())

            template.upload(self, function.logoutUrl(self), my_user,
                                 function.usersAnagrams(function.userKey()))

        else:
            template.login(self, function.loginUrl(self))


    def post(self):
        logging.debug("POST")
        self.response.headers['Content-Type'] = 'text/html'

        my_user = function.userKey()
        button = self.request.get('button')
        file = self.request.get('file')
        result = []
        output = []
        with open(file, 'r') as file:
            wordlist = "%s" %(file.read())
            for r in wordlist:
                if r == '\n':
                    result.append(''.join(output))
                    output = []
                else:
                    output.append(r)
            else:
                if output:
                    result.append(''.join(output))
        print(result)
        for i in result:
            wordlist = i
            
            value = function.inputResult(wordlist)
            logging.debug(value)
            logging.debug(button)

            if button == 'Upload':
                self.add(value, my_user)
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
