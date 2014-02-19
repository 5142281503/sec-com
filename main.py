#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
#import webapp2
from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
import sys      # sys.version
import string   # string.rjust
import os


linestring1 = open('Freedom.html').read()

def printDiggButton(self):
    self.response.out.write("""
    <script type="text/javascript">
    (function() {
    var s = document.createElement('SCRIPT'), s1 = document.getElementsByTagName('SCRIPT')[0];
    s.type = 'text/javascript';
    s.async = true;
    s.src = 'https://widgets.digg.com/buttons.js';
    s1.parentNode.insertBefore(s, s1);
    })();
    </script>
    <!-- Compact Button -->
    <a class="DiggThisButton DiggCompact"></a>
    """)

def printSlashdotButton(self):
    self.response.out.write("""
    <script type="text/javascript">
    slashdot_title="Communicate with anyone anywhere for free";
    </script>
    <script src="https://slashdot.org/slashdot-it.js" type="text/javascript"></script>
    """)
    
# browser complains, see http://stackoverflow.com/questions/3485897/google-ads-doesnt-support-https-what-alternatives-are-there
def printGoogleAd(self):
    self.response.out.write("""
		<script type="text/javascript"><!--
		google_ad_client = "ca-pub-9346123304509336";
		/* 728x90, created 6/16/08 */
		google_ad_slot = "8609601531";
		google_ad_width = 728;
		google_ad_height = 90;
		//-->
		</script>
		<script type="text/javascript"
		src="http://pagead2.googlesyndication.com/pagead/show_ads.js">
		</script>""")


def printPayPalDonateButton(self):
    self.response.out.write("""<FORM action=https://www.paypal.com/cgi-bin/webscr method=post target="_blank">
        <INPUT type=hidden value=_s-xclick name=cmd> <INPUT type=image alt="PayPal - The safer, easier way to pay online!"
        src="https://www.paypal.com/en_US/i/btn/btn_donate_LG.gif" border=0 name=submit> <IMG height=1 alt=""
        src="https://www.paypal.com/en_US/i/scr/pixel.gif" width=1 border=0> <INPUT type=hidden value="-----\
BEGIN PKCS7-----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-----END PKCS7-----&#13;&#10;" name=encrypted> </FORM>
        """)

def printHtmlPageHeader(self):
    self.response.out.write('<html><HEAD><TITLE>~~~Sec-Com~~~(Beta)</TITLE></HEAD><body bgcolor="#D38811">')

def printHtmlPageFooter(self):    
    self.response.out.write('</body></html>')

def printEmailLinks(self):
    self.response.out.write('<a href="mailto:sec-com@superconfigure.com?subject=sec-com&body=http://sec-com.appspot.com/">Email Me Questions, Bugs, Or Feature Requests</a>')

def printTweetButton(self):
    self.response.out.write("""<a href="http://twitter.com/share" class="twitter-share-button" data-count="horizontal" data-via="0utlaw">Tweet</a><script type="text/javascript" src="https://platform.twitter.com/widgets.js"></script>""")

# =" _blank" Opens new page in a new browser window 
def printWebLinks(self):    
    self.response.out.write('<br/><a href="files/faq.html" target="_self" >F.A.Q.</a>')    
    self.response.out.write('<br/><a href="http://superconfigure.wordpress.com/" target="_blank" >My blog</a>')
    self.response.out.write('<br/><a href="http://twitter.com/#!/0utlaw" target="_blank" >Twitter</a>')
    self.response.out.write('<br/><a href="http://www.superconfigure.com/" target="_blank" >Other Windows PC tools of mine</a>')



class MainHandler(webapp.RequestHandler):
    def get(self):
        printHtmlPageHeader(self)
        self.response.out.write('<br/><br/><font size="24" face="Georgia, Arial" color="maroon">~~~Sec-Com~~~</font><br/><br/>')
        self.response.out.write("""
              <form action="/Freedom" method="post">
                <div><input type="submit" value="Click to begin"></div>
              </form>
            """)
        self.response.out.write('<br/><br/><font size="5" face="Georgia, Arial" color="maroon">1- Secure Group Chat (peer2peer(s)).</font><br/>')
        self.response.out.write('<br/><font size="5" face="Georgia, Arial" color="maroon">2- Runs on ANY platform and ANY device that supports Flash 10.1.</font><br/>')
        self.response.out.write('<br/><font size="5" face="Georgia, Arial" color="maroon">3- Anywhere in the world, any time of the day.</font><br/>')
        self.response.out.write('<br/><font size="5" face="Georgia, Arial" color="maroon">4- It is FAST.</font><br/>')
        self.response.out.write('<br/><font size="5" face="Georgia, Arial" color="maroon">5- It is FREE.</font><br/>')
        self.response.out.write('<br/><font size="5" face="Georgia, Arial" color="maroon">6- Nothing to install.</font><br/>')
        self.response.out.write('<br/><br/><br/>This app requires Flash 10.1 at a minimum, and UDP traffic<br/><br/><br/><br/>')
        self.response.out.write('<font size="1"> Python:' + sys.version + '</font><br/>');
        printEmailLinks(self)
        printWebLinks(self)
        self.response.out.write('<br/>')
        printTweetButton(self)
        printDiggButton(self)
        printSlashdotButton(self)
        printPayPalDonateButton(self)        
        printGoogleAd(self)
        printHtmlPageFooter(self)

class Freedom(webapp.RequestHandler):
    def post(self):
        self.response.out.write(linestring1)


app = webapp.WSGIApplication([('/', MainHandler), 
                               ('/Freedom', Freedom)],
                              debug=False)
def main():
    run_wsgi_app(app)

if __name__ == "__main__":
    main()
