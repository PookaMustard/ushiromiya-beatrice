import requests, requests.utils
import time
import discord
from discord.ext import commands
import json

class PyBingException(Exception):
    pass

class PyBingSearch(object):
    """
    Shell class for the individual searches
    """
    def __init__(self, api_key, query, query_base, safe=False):
        self.api_key = api_key
        self.safe = safe
        self.current_offset = 0
        self.query = query
        self.QUERY_URL = query_base

    def search(self, limit=50, format='json', searchsafe='Off'):
        ''' Returns the result list, and also the uri for next page (returned_list, next_uri) '''
        return self._search(limit, format, searchsafe)

    def search_all(self, limit=50, format='json'):
        ''' Returns a single list containing up to 'limit' Result objects'''
        desired_limit = limit
        results = self._search(limit, format)
        limit = limit - len(results)
        while len(results) < desired_limit:
            more_results = self._search(limit, format)
            if not more_results:
                break
            results += more_results
            limit = limit - len(more_results)
            time.sleep(1)
        return results
        
        
class PyBingImageException(Exception):
    pass

class PyBingImageSearch(PyBingSearch):

    IMAGE_QUERY_BASE = 'https://api.datamarket.azure.com/Bing/Search/Image' \
                 + '?Query={}&$top={}&$skip={}&$format={}&ImageFilters={}&Adult={}'

    def __init__(self, api_key, query, image_filters='', safe=False, custom_params=''):
        """
        :param image_filters: Array of strings that filter the response the API sends based on size, aspect,
        color, style, face or any combination thereof.

        Valid values are:
         - Size:Small, Size:Medium, Size:Large, Size:Width:[Width], Size:Height:[Height]
         - Aspect:Square, Aspect:Wide, Aspect:Tall
         - Color:Color, Color:Monochrome
         - Style:Photo, Style:Graphics, Face:Face, Face:Portrait, Face:Other

        Value like: Size:Small+Aspect:Square
        """
        PyBingSearch.__init__(self, api_key, query, self.IMAGE_QUERY_BASE + custom_params, safe=safe)
        self.image_filters = image_filters

    def _search(self, limit, format, searchsafe):
        '''
        Returns a list of result objects, with the url for the next page bing search url.
        '''
        searchsafe = "'" + searchsafe + "'"
        filters = requests.utils.quote("'{}'".format(self.image_filters))
        url = self.QUERY_URL.format(requests.utils.quote("'{}'".format(self.query)), min(50, limit), self.current_offset, format, filters, searchsafe)
        print (url)
        r = requests.get(url, auth=("", self.api_key))
        try:
            json_results = r.json()
        except ValueError as vE:
            if not self.safe:
                raise PyBingImageException("Request returned with code %s, error msg: %s" % (r.status_code, r.text))
            else:
                print ("[ERROR] Request returned with code %s, error msg: %s. \nContinuing in 5 seconds." % (r.status_code, r.text))
                time.sleep(5)
        packaged_results = [ImageResult(single_result_json) for single_result_json in json_results['d']['results']]
        self.current_offset += min(50, limit, len(packaged_results))
        return packaged_results

class ImageResult(object):
    '''
    The class represents a single image search result.
    Each result will come with the following:

    #For the actual image results#
    self.id: id of the result
    self.title: title of the resulting image
    self.media_url: url to the full size image
    self.source_url: url of the website that contains the source image
    self.width: width of the image
    self.height: height of the image
    self.file_size: size of the image (in bytes) if available
    self.content_type the MIME type of the image if available
    self.meta: meta info

    #Meta info#:
    meta.uri: the search uri for bing
    meta.type: for the most part ImageResult
    '''

    class _Meta(object):
        '''
        Holds the meta info for the result.
        '''
        def __init__(self, meta):
            self.type = meta['type']
            self.uri = meta['uri']

    def __init__(self, result):

        self.id = result['ID']
        self.title = result['Title']
        self.media_url = result['MediaUrl']
        self.source_url = result['SourceUrl']
        self.display_url = result['DisplayUrl']
        self.width = result['Width']
        self.height = result['Height']
        self.file_size = result['FileSize']
        self.content_type = result['ContentType']
        self.meta = self._Meta(result['__metadata'])
        
class bingimagebot:
    """Fetches an image from Bing"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def bing(self, *text):
        """Fetches an image from Bing"""

        #Your code will go here
        text = " ".join(text)
        bing_image = PyBingImageSearch('WdlwygeDRR0NsUzUZEF4Yql4OLomvvZfp3moFgLl9Zg', text)
        result= bing_image.search(limit=1, format='json', searchsafe='Off') #1-50
        bottext = result[0].media_url
        return self.bot.say(bottext)

def setup(bot):
bot.add_cog(echo(bot))
