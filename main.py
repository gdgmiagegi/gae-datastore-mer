import cgi
import urllib

import webapp2

from google.appengine.ext import ndb


class Contact(db.Model):

    # Basic info.
    name = db.StringProperty()
    birth_day = db.DateProperty()

    # Address info.
    address = db.PostalAddressProperty()

    # The original phone_number property has been replaced by
    # an implicitly created property called 'phone_numbers'.

    # Company info.
    company_title = db.StringProperty()
    company_name = db.StringProperty()
    company_description = db.StringProperty()
    company_address = db.PostalAddressProperty()


class PhoneNumber(db.Model):
    contact = db.ReferenceProperty(Contact,
                                   collection_name='phone_numbers')
    phone_type = db.StringProperty(
        choices=('home', 'work', 'fax', 'mobile', 'other'))
    number = db.PhoneNumberProperty()


class MainPage(webapp2.RequestHandler):
  def get(self):
    self.response.out.write("""
        <html><body>
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
