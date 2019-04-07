import jinja2
import os
import function

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__) + "/templates"),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)


def login(self, url):
    template_values = {'url': url}

    template = JINJA_ENVIRONMENT.get_template('login.html')
    self.response.write(template.render(template_values))


def main(self, url, my_user, anagrams):
    template_values = {
        'url': url,
        'user': function.currentUser(),
        'my_user': my_user,
        'anagrams': anagrams,
    }

    template = JINJA_ENVIRONMENT.get_template('main.html')
    self.response.write(template.render(template_values))

def add(self, url, my_user, anagrams):
    template_values = {
        'url': url,
        'user': function.currentUser(),
        'my_user': my_user,
        'anagrams': anagrams,
    }

    template = JINJA_ENVIRONMENT.get_template('add.html')
    self.response.write(template.render(template_values))


def searchtext(self, url, my_user, value, input_text, anagrams):
    template_values = {
        'url': url,
        'user': function.currentUser(),
        'my_user': my_user,
        'value': value,
        'input_text': input_text,
        'anagrams': anagrams,
    }

    template = JINJA_ENVIRONMENT.get_template('search.html')
    self.response.write(template.render(template_values))

def upload(self, url, my_user, anagrams):
    template_values = {
        'url': url,
        'user': function.currentUser(),
        'my_user': my_user,
        'anagrams': anagrams,
    }

    template = JINJA_ENVIRONMENT.get_template('fileupload.html')
    self.response.write(template.render(template_values))

def subanagram(self, url, my_user, value, anagrams):
    template_values = {
        'url': url,
        'user': function.currentUser(),
        'my_user': my_user,
        'value': value,
        'anagrams': anagrams,
    }

    template = JINJA_ENVIRONMENT.get_template('subanagram.html')
    self.response.write(template.render(template_values))
