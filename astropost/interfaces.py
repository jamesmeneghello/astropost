import mechanize
import logging
import sys
import re
import pprint
import urlparse

class Interface():
    urls = []
    field_ids = {}

    def post(self, url, post, debug=False):
        """
        Functional that should handle posting to most sites, so long as the provided
        data is correct. Hook at various points if necessary - newscorp is a good example
        of this, since whoever made their website fucked up and gave the comments textarea
        two name/id attributes, which browsers handle fine but beautifulsoup tends not to.

        :param url: URL to post the comment to
        :param post: Post object containing comment and author data
        """
        logging.info('[Interface] Loading page to post comment..')
        logger = logging.getLogger('mechanize')
        logger.addHandler(logging.StreamHandler(sys.stdout))

        br = mechanize.Browser()
        br.open(url)

        self.pre_fill(br)

        if self.field_ids['form_name'] != '':
            br.select_form(name=self.field_ids['form_name'])
        else:
            br.select_form(nr=self.field_ids['form_nr'])

        # could use find_control, but since we're printing debug output anyway..
        for control in br.form.controls:
            try:
                if control.id == self.field_ids['body']:
                    control.value = post.body
                elif control.id == self.field_ids['name']:
                    control.value = post.name
                elif control.id == self.field_ids['email']:
                    control.value = post.email
                elif control.id == self.field_ids['location']:
                    control.value = post.location
                logging.debug('[Interface] Control ' + pprint.pformat(control.id) + ' ' + pprint.pformat(
                    control.name) + ': ' + pprint.pformat(control.value))
            except:
                logging.warning('[Interface] Exception: ' + pprint.pformat(sys.exc_info()))

        self.post_fill(br)

        if debug:
            logging.debug('[Interface] Debug mode active, no data sent. Data that would be sent below: ')
            # only print debug output
            request = br.click()
            for k, v in urlparse.parse_qsl(request.get_data()):
                logging.debug(pprint.pformat(k + ' ' + v))
        else:
            resp = br.submit()
            logging.debug('[Interface] Post returned: ')
            logging.debug(resp.get_data())

    def pre_fill(self, browser):
        """
                Hook just prior to filling the forms with post data, useful
                if the HTML is broken, malformed or otherwise irritating
                :param browser: Mechanize browser instance containing the current response
                """
        pass

    def post_fill(self, browser):
        """
                Hook just after filling the form with post data.
                :param browser: Mechanize browser instance containing the current response
                """
        pass


class NewsLimited(Interface):
    urls = [
        '^http.*news\.com\.au.*story.*',
        '^http.*heraldsun\.com\.au.*story.*',
        '^http.*perthnow\.com\.au.*story.*',
    ]

    field_ids = {
        # no form name is specified on these pages, so we need to select by number instead
        # this being the second form on the page (the first is a search bar)
        'form_name': '',
        'form_nr': 1,
        'body': 'ccomments',
        'name': 'module-comment-add-fullName',
        'email': 'module-comment-add-email',
        'location': 'module-comment-add-location',
    }

    def pre_fill(self, browser):
        resp = browser.response()
        html = resp.get_data()
        html = re.sub('(name="comment" id="ccomments")', '', html)
        resp.set_data(html)
        browser.set_response(resp)

# SMH requires an actual login
# TODO: add SMH account support - fake facebook accounts?
class SMH(Interface):
    urls = [
        '^http:.*smh.com.au/.*'
    ]

# not many ABC articles actually allow comments, so this will have to wait
class ABC(Interface):
    urls = [
        '^http:.*abc.net.au/news/.*'
    ]

    field_ids = {

    }