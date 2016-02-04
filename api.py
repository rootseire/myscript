#MESSAGE
import urllib2
import json
locu_api = '747dcc58845f36c6a49ab9ff3e8c42a92c2b1a7f';




def locu_search(query):
        api_key = locu_api
        url = 'https://api.locu.com/v1_0/venue/search/?api_key=' + api_key
        locality = query.replace(' ', '%20')
        final_url = url + "&locality=" + locality + "&category=restaurant"
        json_obj = urllib2.urlopen(final_url)
        data = json.load(json_obj)

        for item in data['objects']:
            #print "item is :" + str(item)
            print item['name'], item['phone']
