# coding: utf-8

"""
    Wheel Fitment API

    The Wheel Fitment API allows for programmatic access to the database of www.wheel-size.com and its services. Use this API to retrieve information about vehicle fitment database for rims and tires, including OE and option fitments, and plus/minus sizing fitment information. A variety of country and language specific options are available. The coverage of fitment data for vehicles manufactured since 2000 is nearly 100%.  The information about fitment data is updated on a daily basis.  # noqa: E501

    OpenAPI spec version: v1
    Contact: info@wheel-size.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from ws_api_client.api_client import ApiClient


class MakesApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def makes_list(self, **kwargs):  # noqa: E501
        """Returns a list of manufacturers  # noqa: E501

        Get a list of all manufacturers  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronoushronous HTTP request, please pass asynchronous=True
        >>> thread = api.makes_list(asynchronous=True)
        >>> result = thread.get()

        :param asynchronous bool
        :param str lang: Use this parameter anywhere in the API to get *`name`* field translation of the following objects: **`Make`**, **`Model`**, **`Market`**. Across the *`name`* this objects will have *`name_en`* field with original english name. By default `en` language is used.  Available languages: `en,de,ru,es,pt,fr,ja,zh-cn,zh-tw`. Currently translation works for chinese `zh-cn` language only
        :param str brands: Show information only for specified manufacturers. Use _**`GET /makes/`**_ method to get the full list. (e.g. `mitsubishi,nissan,toyota`)
        :param str brands_exclude: Don't show information for specified manufacturers. Use _**`GET /makes/`**_ method to get the full list. (e.g. `geely,great-wall`)
        :param str countries: Show information for local manufacturers from specified countries only. Use _**`GET /countries/`**_ method to get the full list of countries. (e.g. `us,gb,jp`)
        :param str countries_exclude: Don't show information for local manufacturers from specified countries. Use _**`GET /countries/`**_ method to get the full list of countries. (e.g. `ru,ua`)
        :return: list[Make]
                 If the method is called asynchronoushronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('asynchronous'):
            return self.makes_list_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.makes_list_with_http_info(**kwargs)  # noqa: E501
            return data

    def makes_list_with_http_info(self, **kwargs):  # noqa: E501
        """Returns a list of manufacturers  # noqa: E501

        Get a list of all manufacturers  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronoushronous HTTP request, please pass asynchronous=True
        >>> thread = api.makes_list_with_http_info(asynchronous=True)
        >>> result = thread.get()

        :param asynchronous bool
        :param str lang: Use this parameter anywhere in the API to get *`name`* field translation of the following objects: **`Make`**, **`Model`**, **`Market`**. Across the *`name`* this objects will have *`name_en`* field with original english name. By default `en` language is used.  Available languages: `en,de,ru,es,pt,fr,ja,zh-cn,zh-tw`. Currently translation works for chinese `zh-cn` language only
        :param str brands: Show information only for specified manufacturers. Use _**`GET /makes/`**_ method to get the full list. (e.g. `mitsubishi,nissan,toyota`)
        :param str brands_exclude: Don't show information for specified manufacturers. Use _**`GET /makes/`**_ method to get the full list. (e.g. `geely,great-wall`)
        :param str countries: Show information for local manufacturers from specified countries only. Use _**`GET /countries/`**_ method to get the full list of countries. (e.g. `us,gb,jp`)
        :param str countries_exclude: Don't show information for local manufacturers from specified countries. Use _**`GET /countries/`**_ method to get the full list of countries. (e.g. `ru,ua`)
        :return: list[Make]
                 If the method is called asynchronoushronously,
                 returns the request thread.
        """

        all_params = ['lang', 'brands', 'brands_exclude', 'countries', 'countries_exclude']  # noqa: E501
        all_params.append('asynchronous')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method makes_list" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'lang' in params:
            query_params.append(('lang', params['lang']))  # noqa: E501
        if 'brands' in params:
            query_params.append(('brands', params['brands']))  # noqa: E501
        if 'brands_exclude' in params:
            query_params.append(('brands_exclude', params['brands_exclude']))  # noqa: E501
        if 'countries' in params:
            query_params.append(('countries', params['countries']))  # noqa: E501
        if 'countries_exclude' in params:
            query_params.append(('countries_exclude', params['countries_exclude']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['user_key']  # noqa: E501

        return self.api_client.call_api(
            '/makes/', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[Make]',  # noqa: E501
            auth_settings=auth_settings,
            asynchronous=params.get('asynchronous'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
