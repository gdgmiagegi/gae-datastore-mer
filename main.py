import cgi
import urllib

import webapp2

from google.appengine.ext import db


class Contact(db.Model):

    # Basic info.
    name = db.StringProperty()
    birthday = db.StringProperty()

    # Address info.
    address = db.StringProperty()

    # The original phone_number property has been replaced by
    # an implicitly created property called 'phone_numbers'.

    # Company info.
    company_title = db.StringProperty()
    company_name = db.StringProperty()
    company_description = db.StringProperty()
    company_address = db.StringProperty()


class PhoneNumber(db.Model):
    contact = db.ReferenceProperty(Contact,
                                   collection_name='phone_numbers')
    phone_type = db.StringProperty(
        choices=('home', 'work', 'fax', 'mobile', 'other'))
    number = db.PhoneNumberProperty()


class MainPage(webapp2.RequestHandler):
  def get(self):
    self.response.out.write("""
      <html>
        <head>
            <script type="text/javascript">
                function addNumber(){
                }
            </script>
        </head>
        <body>
          <form action="/save" method="post">
            <div>Name: <input type="text" name="cont_name"/></div>
            <div>Birthday: <input type="text" name="birthday" /></div>
            <h3>Company</h3>
            <div>Title: <input type="text" name="company_title" /></div>
            <div>Name: <input type="text" name="company_name" /></div>
            <div>Description: <input type="text" name="company_desc" /></div>
            <div>
                Type
                <select name="type">
                    <option>home</option>
                    <option>work</option>
                    <option>mobile</option>
                </select>
            </div>
            <div><input type="submit" value="Save"></div>
          </form>
        </body>
      </html>""")

class ContactListPage(webapp2.RequestHandler):
  def get(self):
      self.response.out.write("<html><body>Liste de contact<ul>")
      contact_list = Contact.all()
      for contact in contact_list:
          self.response.out.write("<li>")
          self.response.out.write("%s -- %s"%(contact.name, contact.birthday))
          #self.response.out.write(" - ")
          #self.response.out.write(contact.birthday)
          self.response.out.write("</li>")
      self.response.out.write("</ul></body></html>")

class SubmitForm(webapp2.RequestHandler):
  def post(self):
      cont = Contact(name=self.request.get('cont_name'), birthday=self.request.get('birthday'))
      cont.put()
      self.redirect('/list')


app = webapp2.WSGIApplication([
  ('/', MainPage),
  ('/list', ContactListPage),
  ('/save', SubmitForm)
])

