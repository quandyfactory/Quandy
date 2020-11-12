# Quandy README

Quandy is a sweet, simple library to help you create web applications with Python.

It plays nice with web.py and sqlalchemy.

## Author

* Author: Ryan McGreal

* Email: [ryan@quandyfactory.com][1]

* Homepage: [http://quandyfactory.com/projects/quandy][2]

* Repository: [http://github.com/quandyfactory/Quandy][3]

## Licence

Released under the GNU General Public Licence, Version 2:

[http://www.gnu.org/licenses/old-licenses/gpl-2.0.html][4]

## This Version

* Version: 0.7

* Release Date: 2020-11-12

## Requirements and Recommendations

* Python 3 or Python 2.5+

* python-markdown [http://www.freewisdom.org/projects/python-markdown/][5]

* Web.py is a great simple web framework [http://webpy.org][6]

* SQLAlchemy is a fantastic ORM [http://www.sqlalchemy.org/][7]

## Things I Wish Quandy Had

### Packaging

At some point I need to tackle packaging this up either through PyPi or using
easy_install. In the meantime it's a file.

[1]: mailto:ryan@quandyfactory.com

[2]: http://quandyfactory.com/projects/quandy

[3]: http://github.com/quandyfactory/Quandy

[4]: http://www.gnu.org/licenses/old-licenses/gpl-2.0.html

[5]: http://www.freewisdom.org/projects/python-markdown/

[6]: http://webpy.org

[7]: http://www.sqlalchemy.org/

## Revision History

### Version 0.7

* Release Date: 2020-11-12

* Changes:

    *  Updated it to work with Python 3

### Version 0.68

* Release Date: 2014-11-21

* Changes:

    *  Fixed issue with checkbox input not accepting multiple values

### Version 0.67

* Release Date: 2014-11-21

* Changes:

    *  Removed Content-Style-Type from http meta-equiv - HTML5 validator doesn't like it

### Version 0.66

* Release Date: 2014-02-24

* Changes:

    * Just noticed it was still loading css files using @import, so switched to link

### Version 0.65

* Release Date: 2013-08-18

* Changes:

    * Updated formfield separator widget to new id, class conventions

### Version 0.64

* Release Date: 2013-08-18

* Changes:

    * Fixed misspelling `formconteiner` in replace function
    
### Version 0.63

* Release Date: 2013-08-18

* Changes:

    * Fixed bug in textarea twolines==False to remove unnecessary `</formitem>`

### Version 0.62

* Release Date: 2013-08-18

* Changes:

    * Fixed bug in checkbox, radio widgets where `</formitem>` is repeated after each option

### Version 0.61

* Release Date: 2013-08-18

* Changes:

    * Wrapped two-part non-table form widgets in `<formitem>` elements, removed formitem tags from table forms

### Version 0.60

* Release Date: 2013-08-18

* Changes:

    * Fixed minor classname issue in textarea widget 

### Version 0.59

* Release Date: 2013-08-18

* Changes:

    * Cleaned up formfield generation, made id, class etc. consistent across different widgets
    * Removed colspan attributes from non-table formfields

### Version 0.58

* Release Date: 2013-08-17

* Changes:

    * Added ability to structure form using custom form tags, not table

### Version 0.57

* Release Date: 2013-08-17

* Changes:

    * Fixed issue with radio formfield: it was displaying id instead of friendly name

### Version 0.56

* Release Date: 2013-06-03

* Changes:

    * Moved the stylesheet import to the top of the head in Html()
    * Added HTML5 doctype to Html()

### Version 0.55

* Release Date: 2013-04-16

* Changes:

    * Added checkbox/radio title class and ID attributes to hook styles
    * Fixed bug in label for attribute to match input ID

### Version 0.54

* Release Date: 2013-04-15

* Changes:

    * Added 'checkbox' widget to Formfields
    * Enabled accepting a list of checked values

### Version 0.53

* Release Date: 2013-01-05

* Changes:

    * Fixed bug in tools.unfriendly_name that created javascript-unfriendly element ids (%)

### Version 0.52

* Release Date: 2013-01-02

* Changes:

    * Changed `id='name-id` to `id=name_id` in radio ids
    * Fixed bug in tools.unfriendly_name that created javascript-unfriendly element ids

### Version 0.51

* Release Date: 2013-01-02

* Changes:

    * Changed `id='name-id` to `id=name_id` in radio ids
    * Added `id="for_id"` to radio button labels to hang event handlers

### Version 0.50

* Release Date: 2013-01-01

* Changes:

    * Added 'radio' widget to Formfields

### Version: 0.49

* Release Date: 2012-08-21

* Changes:

    * Replaced `str()` functions with `unicode()` functions.

### Version: 0.48

* Release Date: 2012-08-03

* Changes:

    * Added 'separator' widget type to Formfield.

### Version: 0.47

* Release Date: 2012-02-03

* Changes:

    * Fixed bug in Formfields() so that input, select, textarea container title attributes have any html stripped out of the title

### Version: 0.46

* Release Date: 2011-04-29

* Changes:

    * Fixed bug in tools.unfriendly_name that would cause it to choke on non-ASCII characters

### Version: 0.45

* Release Date: 2010-06-01

* Changes: 

    * Slightly refactored Tools.pcase().

### Version: 0.44

* Release Date: 2010-06-01

* Changes:

    * Slightly refactored Tools.pcase().

### Version: 0.44

* Release Date: 2010-06-01

* Changes:

    * Moved javascript file imports to the bottom of the HTML code, below the `body` tag.

### Version: 0.43

* Release Date: 2010-05-20

* Changes:

    * Added ability to specify on which weekday the week starts (default is Sunday)

### Version: 0.42

* Release Date: 2010-01-10

* Changes:

    * Fixed calendar colour when today is a weekend.

### Version: 0.41

* Release Date: 2010-01-07

* Changes:

    * Added td id and fixed div in Cal.write()

### Version: 0.4

* Release Date: 2010-01-06

* Changes:

    * Added Cal() calendar class.

### Version: 0.34

* Release Date: 2009-12-21

* Changes:

    * Fixed rss meta tag - only ends with ` />` if doctype = XHTML.

### Version: 0.33

* Release Date: 2009-12-17

* Changes:

    * Changed default nocache in Html.write() to `False`.
    * Added "rss" parameter to Html.write() to add an RSS autodiscovery meta-tag.

### Version: 0.32

* Release Date: 2009-12-03

* Changes:

    * Fixed bug in tools.validate_password that hard-coded response messages if passwords are too short or too long
    * Fixed typo in tools.validate_password that spells it "assword". Nice.
    * Added optional `strict` parameter to tools.validate_password (default is `False`) so it must contain at least three of four character groups.

### Version: 0.31

* Release Date: 2009-12-01

* Changes:

    * Fixed bug in tools.string_to_date() that unfairly failed valid date strings
    * Added tools.make_list_from_string() to make a list out of delimited (whitespace, comma, semicolon) strings

### Version: 0.3

* Release Date: 2009-11-22

* Changes:

    * Fixed bug in tools.sql_date() that was causing the default date to be 7 days ago
    * Fixed bug in tools.mark_it_up() and updated the html regex
    * Added tools.validate_email()
    * Added tools.validate_password()
    * Added tools.generate_random_password()

### Version: 0.23

* Release Date: 2009-10-23

* Changes:

    * Fixed bug in Tools.is_type()
    * Added Tools.sql_date(), which presents the date as a string in the form `YYYY/MM/DD` or `YYYY-MM-DD`.
    * Added Tools.string_to_date(), which takes a string in the form `YYYY/MM/DD` or `YYYY-MM-DD` and converts to a Python date.
    * Added Tools.compare_dates(), takes two dates and returns the difference, in days, between them.

### Version: 0.22

* Release Date: 2009-10-22

* Changes:

    * Added Tools.is_type(val, thetype), which returns True if `val` is of type `thetype`.
    * Changed Tools.friendly_date function to remove period after month.
    * Changed Tools.friendly_month to test whether date delimiter is '-' or '/'.
    * Changed Tools.friendly_month to test whether date has two parts (YYYY, MM).

### Version: 0.21

* Release Date: 2009-10-20

* Changes:

    * Fixed name (oops, no decimals in module names) from quandy0.2 to quandy02
    * Added Tools.single_or_plural(), which takes a value and returns either singular or plural suffix for a word (defaults are '' and 's').
    * Removed colon `:` and hyphen `-` from badchars list in Tools.unfriendly_name

### Version: 0.2

* Release Date: 2009-10-19

* Changes:

    * Converted all method names to lowercase_with_underscores to conform with [PEP 8](http://www.python.org/dev/peps/pep-0008/)
    * Changed file name to quandy0.2.py to maintain compatibility with apps using quandy.py versions < 0.2.
    * Modified Tools.friendly_date to take an optional monthname length parameter (default 3, i.e. January -> Jan).
    * Removed single quote `'` from badchars list in Tools.unfriendly_name
    * Added optional target parameter to Tools.mark_it_up (default is '')

### Version: 0.14

* Release Date: 2009-09-14

* Changes:

    * Fixed bug in Formfield.Write method, which compares value parameter to value in list of option to flag an option as `selected`. If option list was 2d (value, display), the value matching wasn't working.

### Version: 0.13

* Release Date: 2009-08-21

* Changes:

    * Added /static/ to the default file path values in the Html.Write method.

### Version: 0.12

* Release Date: 2009-08-21

* Changes:

    * Added missing lang attribute to <html> tag in Html.Write method.

### Version: 0.11

* Release Date: 2009-08-20

* Changes:

    * Fixed bug in Hml.Write method that didn't correctly display the version of Quandy
    * Fixed bug in Tools.Fix1252Codes that didn't properly import re
    * Enhanced the functionality of the Tools.PCase function to capitalize hyphenated words and optionally fix mixed-case names (like McGreal)

### Version: 0.1a

* Release Date: 2009-08-19

* Changes:

    * Unicode support works fine in web.py and SQLAlchemy. When using MySQL (via [mysql-python](http://sourceforge.net/projects/mysql-python/)), you must be sure to pass the `?charset=utf8` parameter as part of the db connection string.

### Version: 0.1

* Release Date: 2009-08-06

* Changes:

    * First Commit
