import cgi
import urllib

import webapp2

from google.appengine.ext import ndb


class Contact(ndb.Model):

    # Basic info.
    name = ndb.StringProperty()
    birth_day = ndb.DateProperty()

    # Address info.
    address = ndb.PostalAddressProperty()

    # The original phone_number property has been replaced by
    # an implicitly created property called 'phone_numbers'.

    # Company info.
    company_title = ndb.StringProperty()
    company_name = ndb.StringProperty()
    company_description = ndb.StringProperty()
    company_address = ndb.PostalAddressProperty()


class PhoneNumber(ndb.Model):
    contact = ndb.ReferenceProperty(Contact,
                                   collection_name='phone_numbers')
    phone_type = ndb.StringProperty(
        choices=('home', 'work', 'fax', 'mobile', 'other'))
    number = ndb.PhoneNumberProperty()


class MainPage(webapp2.RequestHandler):
  def get(self):
    self.response.out.write("""
      <html>
        <body>
          <form action="/save" method="post">
            <div>Name: <input type="text" /></div>
            <div>Name: <input type="text" /></div>
            <div>Name: <input type="text" /></div>
            <h3>Company</h3>
            <div>Name: <input type="text" /></div>
            <div>Name: <input type="text" /></div>
            <div>
                <select name="type">
                    <option>home</option>
                    <option>work</option>
                    <option>mobile</option>
                </select>
            </div>
            <div><input type="submit" value="Sign Guestbook"></div>
          </form>
        </body>
      </html>""")


class SubmitForm(webapp2.RequestHandler):
  def post(self):
      print "toto"


app = webapp2.WSGIApplication([
  ('/', MainPage),
  ('/save', SubmitForm)
])

