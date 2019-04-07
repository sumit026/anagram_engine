from google.appengine.ext import ndb
from google.appengine.api import users
from myuser import MyUser
from anagram import Anagram
import logging
import re
from itertools import combinations

def loginUrl(main_page):
    return users.create_login_url(main_page.request.uri)


def logoutUrl(main_page):
    return users.create_logout_url(main_page.request.uri)

def currentUser():
    return users.get_current_user()


def userKey():
    user = currentUser()
    if user:
        my_user_key = ndb.Key(MyUser, user.user_id())
        return my_user_key.get()


def userLoggedIn():
    return True if currentUser() else False


def userExist():
    return True if userKey() else False


def newUser(user):
    MyUser(id=user.user_id()).put()


def usersAnagrams(my_user):
    if my_user:
        logging.debug(my_user.anagrams)
        result = []

        for anagram in my_user.anagrams:
            anagrams = anagram.get()
            result.append(anagrams)

        return result


def add_newAnagram(my_user, text, anagram_id, anagram_key):
    if text:
        anagram = Anagram(id=anagram_id)
        anagram.words.append(text)
        anagram.sorted_word = lexicographical_order(text)
        anagramList = list(text)
        anagram.sub_anagram = generateSubAnagrams(anagramList)
        anagram.length = len(text)
        anagram.user_id = my_user.key.id()
        anagram.put()
        
        my_user.anagrams.append(anagram_key)
        if anagram.sorted_word is not None:
            my_user.anagram_count += 1
        my_user.anagram_count
        if anagram.words is not None:
            my_user.words_count += 1
        my_user.words_count
        my_user.put()


def add_anagram(my_user, text, anagram_key):
    anagram = anagram_key.get()
    if text not in anagram.words:
        if text:
            anagram.words.append(text)
            anagramList = list(text)
            anagram.sub_anagram = generateSubAnagrams(anagramList)
            anagram.put()

            if anagram.words is not None:
                my_user.words_count += 1
            my_user.words_count
            my_user.put()
            

def lexicographical_order(text):
    key = text.lower()
    return ''.join(sorted(key))


def inputResult(input_text):
    result = input_text.lower()
    result = re.sub('[^a-z]+', '', result)
    return result

def generateSubAnagrams(anagramList):
    sub_anagram = []
    anagram_len = len(anagramList)
    length = anagram_len -1
    while length > 2:
        for c in combinations(anagramList, length):
            sub_anagram.append(''.join(c))
        length -= 1
    return sub_anagram
