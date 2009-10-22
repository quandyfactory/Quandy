"""
Quandy is a sweet, simple library to help you create web applications with Python. 
Quandy plays nice with Web.py and SQLAlchemy.
"""

__version__ = '0.22'
__releasedate__ = '2009-10-21'
__author__ = 'Ryan McGreal <ryan@quandyfactory.com>'
__homepage__ = 'http://quandyfactory.com/projects/5/quandy'
__repository__ = 'http://github.com/quandyfactory/Quandy'
__copyright__ = 'Copyright (C) 2009 by Ryan McGreal. Licenced under GPL version 2. http://www.gnu.org/licenses/gpl-2.0.html'

import datetime
date = datetime.date.today()
day = datetime.timedelta(days=1)

import hashlib # for password hash function
import re # for the fix_1252_codes function

class Html:
    """
    Summary:
    Methods to produce HTML, including an HTML page with all the header and footer boilerplate.
    """

    def __init__(self):
        #initialize values
        pass
        
    def write(self, body_content = '', site_domain='http://localhost/', site_name='Default Site Name', css_path='/static/styles/', css_files=[], css_extend=[], js_path='/static/scripts/', js_files=[], js_extend=[], page_title='Default Page Title', page_author='Default Page Author', doctype='html 4 strict', lang='en', charset='UTF-8', favicon_url='/static/favicon.ico', nocache=True):
        """
        Parameters:
        site_domain - web domain for your site
        site_name   - name of site or application (appears after page title in <title> element)
        css_path    - path to folder with css files
        css_files   - default list of css file names
        css_extend  - additional list of css file names for a given page
        js_path     - path to folder with js files
        js_files    - default list of js file names
        js_extend   - additional list of css file names for a given page
        page_title  - page title (appears in <title> element)
        page_author - page author
        doctype     - html doctype: 'html 4 strict' is the default
                    - also recognizes 'html 4 transitional', 'html 4 quirks', 'xhtml 1 strict', 'xhtml 1 transitional'
        lang        - page language (default is 'en')
        charset     - page character set (default is 'UTF-8')
        favicon_url - path to favicon file (default is /favicon.ico')
        nocache     - nocache meta tag (default is True)
        """
        output = []
        addline = output.append
        closetag = ''
        if doctype == 'html 4 transitional':
            addline('<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">')
            addline('<html lang="%s">' % (lang))
        elif doctype == 'html 4 quirks':
            addline('<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">')
            addline('<html lang="%s">' % (lang))
        elif doctype == 'xhtml 1 strict':
            addline('<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">')
            addline('<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="%s" lang="%s">' % (lang, lang))
            closetag = ' /'
        elif doctype == 'xhtml 1 transitional':
            addline('<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">')
            addline('<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="%s" lang="%s">' % (lang, lang))
            closetag = ' /'
        else: # default is HTML 4 strict
            addline('<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN" \n"http://www.w3.org/TR/html4/strict.dtd">')
            addline('<html lang="%s">' % (lang))
        addline('  <head>')
        addline('    <meta name="author" content="%s"%s>' % (page_author, closetag))
        addline('    <meta http-equiv="Content-Type" content="text/html; charset=%s"%s>' % (charset, closetag))
        addline('    <meta name="generator" content="Quandy %s; url=http://quandyfactory.com/projects/quandy"%s>' % (__version__, closetag))
        if nocache == True: addline('    <meta http-equiv="pragma" content="no-cache"%s>' % (closetag))
        addline('    <link rel="shortcut icon" href="%s"%s>' % (favicon_url, closetag))
        addline('    <title>%s - %s</title>' % (page_title, site_name))
        for file in css_files:
            addline('    <style type="text/css">@import "%s%s";</style>' % (css_path, file))
        for file in css_extend:
            addline('    <style type="text/css">@import "%s%s";</style>' % (css_path, file))
        for file in js_files:
            addline('    <script type="text/javascript" src="%s%s"></script>' % (js_path, file))
        for file in js_extend:
            addline('    <script type="text/javascript" src="%s%s"></script>' % (js_path, file))
        addline('  </head>\n  <body>')
        addline(body_content)
        addline('  </body>')
        addline('</html>')
        return '\n'.join(output)

    def tag(self, tagname='div', innertext = '', attributes = {}):
        """
        Summary:
        Produces an HTML element with opening and closing tags, attributes and inner text/HTML.

        Parameters:
        tagname - string
        innertext - string (optional - default = '')
        attributes - dictionary (optional - default = {})
        
        output:
        Returns an HTML element as a string.
        """
        output = ['<%s' % tagname]
        output.extend([' %s="%s"' % (k, v) for k, v in attributes.items()])
        output.append('>%s</%s>' % (innertext, tagname))
        return ''.join(output)

    def make_table_from_dictionary(self, collection = {}, caption = 'Dictionary', id = ''):
        """
        Summary:
        Converts a dictionary into an HTML table with key, value as th, td

        Parameters:
        collection - the dictionary of keys and values
        caption - optional caption (default is no caption)
        id - optional id (default is random_id)

        output:
        Returns an HTML table as a string
        """
        tools = Tools()
        if id == '':
            id = tools.random_id()
        output = ['<table id="%s">' % id]
        if caption != '':
            output.append('<caption>%s</caption>' % caption)
        for k, v in collection.items():
            output.append('  <tr>\n    <th>%s</th>\n    <td>%s</td>\n  </tr>' % (k, v))
        output.append('</table>')
        return '\n'.join(output)


cp_1252_chars = {
    # from http://www.microsoft.com/typography/unicode/1252.htm
    u"\x80": u"\u20AC", # EURO SIGN
    u"\x82": u"\u201A", # SINGLE LOW-9 QUOTATION MARK
    u"\x83": u"\u0192", # LATIN SMALL LETTER F WITH HOOK
    u"\x84": u"\u201E", # DOUBLE LOW-9 QUOTATION MARK
    u"\x85": u"\u2026", # HORIZONTAL ELLIPSIS
    u"\x86": u"\u2020", # DAGGER
    u"\x87": u"\u2021", # DOUBLE DAGGER
    u"\x88": u"\u02C6", # MODIFIER LETTER CIRCUMFLEX ACCENT
    u"\x89": u"\u2030", # PER MILLE SIGN
    u"\x8A": u"\u0160", # LATIN CAPITAL LETTER S WITH CARON
    u"\x8B": u"\u2039", # SINGLE LEFT-POINTING ANGLE QUOTATION MARK
    u"\x8C": u"\u0152", # LATIN CAPITAL LIGATURE OE
    u"\x8E": u"\u017D", # LATIN CAPITAL LETTER Z WITH CARON
    u"\x91": u"\u2018", # LEFT SINGLE QUOTATION MARK
    u"\x92": u"\u2019", # RIGHT SINGLE QUOTATION MARK
    u"\x93": u"\u201C", # LEFT DOUBLE QUOTATION MARK
    u"\x94": u"\u201D", # RIGHT DOUBLE QUOTATION MARK
    u"\x95": u"\u2022", # BULLET
    u"\x96": u"\u2013", # EN DASH
    u"\x97": u"\u2014", # EM DASH
    u"\x98": u"\u02DC", # SMALL TILDE
    u"\x99": u"\u2122", # TRADE MARK SIGN
    u"\x9A": u"\u0161", # LATIN SMALL LETTER S WITH CARON
    u"\x9B": u"\u203A", # SINGLE RIGHT-POINTING ANGLE QUOTATION MARK
    u"\x9C": u"\u0153", # LATIN SMALL LIGATURE OE
    u"\x9E": u"\u017E", # LATIN SMALL LETTER Z WITH CARON
    u"\x9F": u"\u0178", # LATIN CAPITAL LETTER Y WITH DIAERESIS
}        
    
class Tools:
    """
    Various tools for easing the creation of web pages.
    """
    def __init__(self):
        #INITIALIZE VALUES
        pass

    def fix_1252_codes(self, text):
        """
        Replace non-standard Microsoft character codes from the Windows-1252 character set in a unicode string with proper unicode codes.
        Code originally from: http://effbot.org/zone/unicode-gremlins.htm
        """
        if re.search(u"[\x80-\x9f]", text):
            def fixup(m):
                s = m.group(0)
                return cp_1252_chars.get(s, s)
            if isinstance(text, type("")):
                text = unicode(text, "iso-8859-1")
            text = re.sub(u"[\x80-\x9f]", fixup, text)
        return text 
 
    def single_or_plural(self, value, single_string='', plural_string='s'):
        """
        Takes a value and an optional single_string (default '') and plural_string (default 's'). 
        Returns the single_string if the value = 1 or the plural_string if the value != 1.
        """
        if value == 1:
            return single_string
        else:
            return plural_string
 
    def make_hash(self, password, salt='saltydog', type='md4'):
        """
        Takes a plain text password and returns a salted hash.
        """
        fullpassword = password+salt
        return hashlib.new(type, fullpassword.encode('utf-16le')).hexdigest().upper() 
        
    def weekday_name(self, adate):
        """
        Takes a date and returns the weekday name for that date.
        """
        wkdays = 'Monday Tuesday Wednesday Thursday Friday Saturday Sunday'.split()
        return wkdays[adate.weekday()]

    def mark_it_up(self, plaintext, target=""):
        """
        Converts URLs and Email addresses to hyperlinks
        """
        def make_link(match, target):
            return '<a href="%s" target="%s">%s</a>' % (match.group(1), match.group(1), target)
        def make_email(match):
            return '<a href="mailto:%s">%s</a>' % (match.group(1), match.group(1))
        rx = re.compile(r'(http://([w.]+/?)S*)')
        output = rx.sub(make_link, plaintext)
        rx = re.compile(r'([a-zA-Z_0-9.-]+@[a-zA-Z_0-9.-]+.w+)')
        output = rx.sub(make_email, output)
        return output

    def friendly_date(self, uglydate, monthchars=3):
        """
        Takes a YYYY/MM/DD date and returns the date string in MMM D, YYYY format
        """
        months = ' January February March April May June July August September October November December'.split(' ')
        if '-' in uglydate:
            delimiter = '-'
        elif '/' in uglydate:
            delimiter = '/'
        else:
            delimiter = '/'
        ud = uglydate.split(delimiter)
        if len(ud) == 3:
            if monthchars != 0:
                thismonth = months[int(ud[1])][:monthchars]
            else:
                thismonth = months[int(ud[1])]
            
            return '%s %s, %s' % (months[int(ud[1])], ud[2], ud[0])
        else:
            return str(uglydate)

    def friendly_month(self, uglymonth):
        """
        Takes a YYYY/MM date and returns it in MMM, YYYY format
        """
        if '-' in uglymonth:
            delimiter = '-'
        elif '/' in uglymonth:
            delimiter = '/'
        else:
            delimiter = '/'
        months = ' January February March April May June July August September October November December'.split(' ')
        dt = uglymonth.split(delimiter)
        if len(dt) == 2:
            return '%s, %s' % (months[int(dt[1])], dt[0])
        else:
            return str(uglymonth)

    def pcase(self, text, names=False):
        """
        Takes a string and returns it in proper case (initial caps)
        """
        text = text.lower()
        text = ' '.join(self.capitalize(i) for i in text.split(' '))
        text = '-'.join(self.capitalize(i) for i in text.split('-'))
        text = '"'.join(self.capitalize(i) for i in text.split('"'))
        text = "'".join(self.capitalize(i) for i in text.split("'"))
        text = text.replace("'S ", "'s ") # fix incorrect capitalize on possessive s
        if names==True:
            text = 'Mc'.join(self.Capitalize(i) for i in text.split('Mc'))
            text = 'Mac'.join(self.Capitalize(i) for i in text.split('Mac'))
        return text.strip()
        
    def capitalize(self, text):
        """
        Capitalizes a word
        """
        outstr = '' #initialize outstr
        if len(text) > 0:
            outstr = text[0].capitalize()
            if len(text) > 1:
                for c in text[1:]: 
                    outstr = outstr + c
        return outstr
        
    def friendly_name(self, uname):
        """
        Takes a lowercase string with underscores _ between words and returns a string of capitalized words with spaces.
        """
        uname = self.pcase(str(uname).replace('_',' '))
        
        if len(uname) != 0:
            finalname=[]
            finalname.append(uname[0].upper())
            for char in range(1,len(uname)):
                if uname[char-1]==' ' or uname[char-1]=='-':
                    finalname.append(uname[char].upper())
                else:
                    finalname.append(uname[char])
            return ''.join(finalname)
        else:
            return uname
        
    def unfriendly_name(self, uname):
        """
        Takes a tring of capitalized words with spaces and returns a lowercase string with underscores between words.
        """
        uname = str(uname).replace(' ','_').lower()
        uname = uname.replace('&#39;','')
        badchars = ".,!?;/"
        outname = ''.join([c for c in uname if c not in badchars])
        while '__' in outname: 
            outname = outname.replace('__','_')
        return outname

    def random_id(self):
        """
        Returns a randomized id in the form 'form id_#######' for use in HTML elements that require a distinct id for DOM manipulation.
        """
        import random
        return 'id_' + str(random.random()).replace('.','')


class Form:
    """
    Summary:
    Produces an HTML form.
    
    Parameters:
    
    Id - form id attribute (default is random id)
    Name - form name attribute (default is id)
    Class - form class attribute
    Title - optional form title displayed as an H3 element above the form
    Method - form method attribute ('post' or 'get')
    Action - form action (destination URL) attribute
    Enctype - form enctype attribute (default is 'application/x-www-form-urlencoded'; use 'multipart/form-data' for file uploads
    """

    def __init__(self):
        #INITIALIZE VALUES
        pass

    def get_form_dates(self, days = 7, start = 0, order = -1):
        """
        Summary:
        Generates a list of dates to use as the options for a form select object.

        Parameters:
        Takes a dictionary with three optional keys:
        
        days - number of days (default = 7)
        start - start date # days before today (default = 0)
        order - 1 = asc, -1 = desc (default = -1)
        """
        if order == -1:
            end = start + days
            fudge = 0
        else:
            start = start + days
            end = start
            fudge = -1
        options = []; x = start
        while x != end:
            options.append(str(date - (day*(x+fudge))))
            x += order*-1
        return options    

    def write(self, formfields = [], id='', name='', classname='', title='', method='post', action='', enctype='application/x-www-form-urlencoded'):
        atts = {}
        output = []
        addline = output.append
        tools = Tools()
        
        if id == '': id = tools.random_id()
        atts['id'] = id
        
        if name == '': name = id
        atts['name'] = name
        
        if method == '': method = 'post'
        atts['method'] = method
        
        if enctype == '': enctype = 'application/x-www-form-urlencoded'
        atts['enctype'] = enctype

        if classname != '': atts['class'] = classname
        if action != '': atts['action'] = action
        
        attlist = []
        for k, v in atts.items():
            attlist.append(' %s="%s"' % (k, v))
        
        attstring = ''.join(attlist)
        addline('<form%s>' % attstring)

        addline('<table>')
        if title <> '':
             addline('<caption id="%s_caption">%s</caption>\n' % (id, title))
        addline('<tbody id="%s_tbody">' % id)
        
        # form fields
        addline('\n'.join([f for f in formfields]))
        
        addline('</tbody>')
        addline('</table>')
        addline('</form>')
        return '\n'.join(output)
        return '\n'.join(output)


class Formfield:
    """
    Summary:
    Produces an HTML form element.
    
    Parameters:
    widget        - type of form element (e.g. input, select, textarea)
    id            - id attribute (default is random id)
    name          - name attribute (default is id)
    classname     - formfield class attribute
    title         - optional formfield title (default is formatted id)
    disabled      - formfield disabled attribute (default is false)
    retainstate   - retain value on submit (default is true)
    options       - list of select formfield options
                    an option can be a list: option[0] is the value and option[1] is the text
    leadingoption - first select option is blank (default is false)
    value         - default formfield value
    multiple      - allows multiple option selection (default is false)
    type          - type attribute for input formfield (default is 'text')
    options       - list of select formfield option values
    rows          - number of rows for a textarea
    cols          - number of cols for a textarea
    """

    def __init__(self):
        pass

    def write(self, widget='input', id='', name='', classname='', title='', disabled='', retainstate='true', options = [], leadingoption='', value='', multiple='', type='text', visible='', rows=10, cols=40, twolines=False):
        output = []
        addline = output.append
        atts = {}
        tools = Tools()
        
        if id == '': id = tools.random_id()
        atts['id'] = id
        
        if name == '': name = id
        atts['name'] = name
        
        if title == '': title = tools.friendly_name(id)

        if disabled != '': atts['disabled'] = 'disabled'
        if classname != '': atts['class'] = classname

        # SELECT widget
        if widget == 'select':
            if multiple != '':
                atts['Multiple'] = 'multiple'
            ats = "".join([' %s="%s"' % (k, v) for k, v in atts.items()])
            addline('  <tr id="%s_tablerow" class="%s_tablerow">' % (id, classname))
            addline('    <th title="%s">%s</th>' % (title, title))
            addline('    <td title="%s">' % (title))
            addline('      <select%s>' % (ats))
    
            if leadingoption != '':
                addline('        <option value="">--</option>')
            for option in options:
                selected = ''
                if option.__class__() == []:
                    if retainstate != '' and str(option[0]) == str(value):
                        selected = ' selected'
                    addline('        <option value="%s"%s>%s</option>' % (option[0], selected, option[1]))
                else:
                    if retainstate != '' and str(option) == str(value):
                        selected = ' selected'
                    addline('        <option value="%s"%s>%s</option>' % (option, selected, option))
            addline('      </select>\n    </td>\n  </tr>')

        # INPUT widget
        elif widget == 'input':
            if value != '':
                atts['value'] = value
            if type != '':
                atts['type'] = type
            ats = "".join([' %s="%s"' % (k, v) for k, v in atts.items()])
            if type == 'hidden' and visible == '':
                addline(' <tr style="display: none"><td><input%s></td></tr>' % (ats))
            else:
                addline('  <tr id="%s_tablerow" class="%s_tablerow">' % (id, classname))
                if type != 'submit':
                    addline('    <th title="%s">%s</th>\n    <td title="%s">' % (title, title, title))
                else:
                    addline('    <td colspan="2" title = "%s" class="form_button">' % (title))
                addline('      <input%s>' % (ats))
                if type == 'hidden' and visible != '': addline(value)
                addline('    </td>')
                addline('  </tr>')
        
        # TEXTAREA widget
        elif widget == 'textarea':
            if rows > 0:
                atts['rows'] = rows
            if cols > 0:
                atts['cols'] = cols
            ats = "".join([' %s="%s"' % (k, v) for k, v in atts.items()])
            addline('  <tr id="%s_tablerow" class="%s_tablerow">' % (id, classname))
            if twolines == False:
                addline('    <th title="%s">%s</th>\n    <td title="%s">' % (title, title, title))
            else:
                addline('    <th colspan="2" title="%s">%s</th>\n  </tr>\n  <tr>' % (title, title))
                addline('    <td colspan="2" title = "%s" class="form_textarea">' % (title))
            addline('      <textarea%s>%s</textarea>' % (ats, value))
            addline('    </td>')
            addline('  </tr>')
        return '\n'.join(output)
        

class Handler:
    """
    Summary:
    Generic class for handling URL requests
    """

    def __init__(self):
        pass
        
    def get_path_list(self, path):
        html = Html()
        output = []
        addline = output.append
        addline(html.tag('ul','\n'.join([html.tag('li','%s' % p) for p in path])))
        return '\n'.join(output)
          
    def default(self, path, formfields):
        handler = Handler()
        html = Html()
        output = []
        addline = output.append
        page_title = 'Default Page'
        addline(html.tag('h1','%s' % page_title))
        addline(html.tag('p','Default page (base URL). To customize this, create a class in quandy_handlers.py based on this class, and define your custom handlers (including a custom error handler) there.'))
        addline(html.tag('h2','Path:'))
        addline(handler.get_path_list(path))
        page = html.write(
            page_title = page_title,
            body_content='\n'.join(output),
            )
        return page
    
    def error(self, path, formfields):
        handler = Handler()
        html = Html()
        output = []
        addline = output.append
        page_title = 'Error: Page Not Found'
        addline(html.tag('h1','%s' % page_title))
        addline(html.tag('p','Default error page (page not found). To customize this, create a class in quandy_handlers.py based on this class, and define your custom handlers (including a custom error handler) there.'))
        addline(html.tag('h2','Path:'))
        addline(handler.GetPathList(path))
        page = html.write(
            page_title = page_title,
            body_content='\n'.join(output),
            )
        return page

