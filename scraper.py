import scraperwiki       
import lxml.html           
import urllib2

for j in range(0,16):
    for i in range(0,100):
        if ((j*100)+i) >0:
            if ((j*100)+i) < 2:
                print "hello"
                html = scraperwiki.scrape("https://www.crunchbase.com/funding-rounds")
                root = lxml.html.fromstring(html)
                for tr in root.cssselect("div#col2_internal tr"):
                    print "in here"
                    tds = tr.cssselect("td")
                    print tds
                    if len(tds)==5:
                        data = {
                            'Date' : tds[0].text_content(),
                            'Name' : tds[1].text_content(), 
                            'Round' : tds[2].text_content(),
                            'Size' : tds[3].text_content(),
                            'Investors' : tds[4].text_content(),
                        }
                    scraperwiki.sqlite.save(unique_keys=['Date','Name','Round','Size','Investors'], data=data)
            
