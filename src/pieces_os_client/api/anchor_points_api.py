# coding: utf-8

"""
    Pieces Isomorphic OpenAPI

    Endpoints for Assets, Formats, Users, Asset, Format, User.

    The version of the OpenAPI document: 1.0
    Contact: tsavo@pieces.app
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import re  # noqa: F401
import io
import warnings

from pydantic import validate_arguments, ValidationError

from typing_extensions import Annotated
from pydantic import Field, StrictBool, StrictStr

from typing import Optional

from openapi_client.models.anchor_point import AnchorPoint
from openapi_client.models.anchor_points import AnchorPoints
from openapi_client.models.seeded_anchor_point import SeededAnchorPoint

from openapi_client.api_client import ApiClient
from openapi_client.api_response import ApiResponse
from openapi_client.exceptions import (  # noqa: F401
    ApiTypeError,
    ApiValueError
)


class AnchorPointsApi:
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None) -> None:
        if api_client is None:
            api_client = ApiClient.get_default()
        self.api_client = api_client

    @validate_arguments
    def anchor_points_create_new_anchor_point(self, transferables : Annotated[Optional[StrictBool], Field(description="This is a boolean that will decided if we are want to return the transferable data (default) or not(performance enhancement)")] = None, seeded_anchor_point : Optional[SeededAnchorPoint] = None, **kwargs) -> AnchorPoint:  # noqa: E501
        """/anchor_points/create [POST]  # noqa: E501

        This will create a anchorPoint.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.anchor_points_create_new_anchor_point(transferables, seeded_anchor_point, async_req=True)
        >>> result = thread.get()

        :param transferables: This is a boolean that will decided if we are want to return the transferable data (default) or not(performance enhancement)
        :type transferables: bool
        :param seeded_anchor_point:
        :type seeded_anchor_point: SeededAnchorPoint
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request.
               If one number provided, it will be total request
               timeout. It can also be a pair (tuple) of
               (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: AnchorPoint
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            message = "Error! Please call the anchor_points_create_new_anchor_point_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"  # noqa: E501
            raise ValueError(message)
        return self.anchor_points_create_new_anchor_point_with_http_info(transferables, seeded_anchor_point, **kwargs)  # noqa: E501

    @validate_arguments
    def anchor_points_create_new_anchor_point_with_http_info(self, transferables : Annotated[Optional[StrictBool], Field(description="This is a boolean that will decided if we are want to return the transferable data (default) or not(performance enhancement)")] = None, seeded_anchor_point : Optional[SeededAnchorPoint] = None, **kwargs) -> ApiResponse:  # noqa: E501
        """/anchor_points/create [POST]  # noqa: E501

        This will create a anchorPoint.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.anchor_points_create_new_anchor_point_with_http_info(transferables, seeded_anchor_point, async_req=True)
        >>> result = thread.get()

        :param transferables: This is a boolean that will decided if we are want to return the transferable data (default) or not(performance enhancement)
        :type transferables: bool
        :param seeded_anchor_point:
        :type seeded_anchor_point: SeededAnchorPoint
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the ApiResponse.data will
                                 be set to none and raw_data will store the
                                 HTTP response body without reading/decoding.
                                 Default is True.
        :type _preload_content: bool, optional
        :param _return_http_data_only: response data instead of ApiResponse
                                       object with status code, headers, etc
        :type _return_http_data_only: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(AnchorPoint, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'transferables',
            'seeded_anchor_point'
        ]
        _all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers'
            ]
        )

        # validate the arguments
        for _key, _val in _params['kwargs'].items():
            if _key not in _all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method anchor_points_create_new_anchor_point" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}

        # process the query parameters
        _query_params = []
        if _params.get('transferables') is not None:  # noqa: E501
            _query_params.append(('transferables', _params['transferables']))

        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        if _params['seeded_anchor_point'] is not None:
            _body_params = _params['seeded_anchor_point']

        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # set the HTTP header `Content-Type`
        _content_types_list = _params.get('_content_type',
            self.api_client.select_header_content_type(
                ['application/json']))
        if _content_types_list:
                _header_params['Content-Type'] = _content_types_list

        # authentication setting
        _auth_settings = []  # noqa: E501

        _response_types_map = {
            '200': "AnchorPoint",
            '500': "str",
        }

        return self.api_client.call_api(
            '/anchor_points/create', 'POST',
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            async_req=_params.get('async_req'),
            _return_http_data_only=_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=_params.get('_preload_content', True),
            _request_timeout=_params.get('_request_timeout'),
            collection_formats=_collection_formats,
            _request_auth=_params.get('_request_auth'))

    @validate_arguments
    def anchor_points_delete_specific_anchor_point(self, anchor_point : Annotated[StrictStr, Field(..., description="This is the specific uuid of an anchor_point.")], **kwargs) -> None:  # noqa: E501
        """/anchor_points/{anchor_point}/delete [POST]  # noqa: E501

        This will delete a specific anchorPoint!  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.anchor_points_delete_specific_anchor_point(anchor_point, async_req=True)
        >>> result = thread.get()

        :param anchor_point: This is the specific uuid of an anchor_point. (required)
        :type anchor_point: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request.
               If one number provided, it will be total request
               timeout. It can also be a pair (tuple) of
               (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: None
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            message = "Error! Please call the anchor_points_delete_specific_anchor_point_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"  # noqa: E501
            raise ValueError(message)
        return self.anchor_points_delete_specific_anchor_point_with_http_info(anchor_point, **kwargs)  # noqa: E501

    @validate_arguments
    def anchor_points_delete_specific_anchor_point_with_http_info(self, anchor_point : Annotated[StrictStr, Field(..., description="This is the specific uuid of an anchor_point.")], **kwargs) -> ApiResponse:  # noqa: E501
        """/anchor_points/{anchor_point}/delete [POST]  # noqa: E501

        This will delete a specific anchorPoint!  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.anchor_points_delete_specific_anchor_point_with_http_info(anchor_point, async_req=True)
        >>> result = thread.get()

        :param anchor_point: This is the specific uuid of an anchor_point. (required)
        :type anchor_point: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the ApiResponse.data will
                                 be set to none and raw_data will store the
                                 HTTP response body without reading/decoding.
                                 Default is True.
        :type _preload_content: bool, optional
        :param _return_http_data_only: response data instead of ApiResponse
                                       object with status code, headers, etc
        :type _return_http_data_only: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: None
        """

        _params = locals()

        _all_params = [
            'anchor_point'
        ]
        _all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers'
            ]
        )

        # validate the arguments
        for _key, _val in _params['kwargs'].items():
            if _key not in _all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method anchor_points_delete_specific_anchor_point" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params['anchor_point']:
            _path_params['anchor_point'] = _params['anchor_point']


        # process the query parameters
        _query_params = []
        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # authentication setting
        _auth_settings = []  # noqa: E501

        _response_types_map = {}

        return self.api_client.call_api(
            '/anchor_points/{anchor_point}/delete', 'POST',
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            async_req=_params.get('async_req'),
            _return_http_data_only=_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=_params.get('_preload_content', True),
            _request_timeout=_params.get('_request_timeout'),
            collection_formats=_collection_formats,
            _request_auth=_params.get('_request_auth'))

    @validate_arguments
    def anchor_points_snapshot(self, transferables : Annotated[Optional[StrictBool], Field(description="This is a boolean that will decided if we are want to return the transferable data (default) or not(performance enhancement)")] = None, **kwargs) -> AnchorPoints:  # noqa: E501
        """/anchor_points [GET]  # noqa: E501

        This will get a snapshot of all your anchorPoints.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.anchor_points_snapshot(transferables, async_req=True)
        >>> result = thread.get()

        :param transferables: This is a boolean that will decided if we are want to return the transferable data (default) or not(performance enhancement)
        :type transferables: bool
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request.
               If one number provided, it will be total request
               timeout. It can also be a pair (tuple) of
               (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: AnchorPoints
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            message = "Error! Please call the anchor_points_snapshot_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"  # noqa: E501
            raise ValueError(message)
        return self.anchor_points_snapshot_with_http_info(transferables, **kwargs)  # noqa: E501

    @validate_arguments
    def anchor_points_snapshot_with_http_info(self, transferables : Annotated[Optional[StrictBool], Field(description="This is a boolean that will decided if we are want to return the transferable data (default) or not(performance enhancement)")] = None, **kwargs) -> ApiResponse:  # noqa: E501
        """/anchor_points [GET]  # noqa: E501

        This will get a snapshot of all your anchorPoints.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.anchor_points_snapshot_with_http_info(transferables, async_req=True)
        >>> result = thread.get()

        :param transferables: This is a boolean that will decided if we are want to return the transferable data (default) or not(performance enhancement)
        :type transferables: bool
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the ApiResponse.data will
                                 be set to none and raw_data will store the
                                 HTTP response body without reading/decoding.
                                 Default is True.
        :type _preload_content: bool, optional
        :param _return_http_data_only: response data instead of ApiResponse
                                       object with status code, headers, etc
        :type _return_http_data_only: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(AnchorPoints, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'transferables'
        ]
        _all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers'
            ]
        )

        # validate the arguments
        for _key, _val in _params['kwargs'].items():
            if _key not in _all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method anchor_points_snapshot" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}

        # process the query parameters
        _query_params = []
        if _params.get('transferables') is not None:  # noqa: E501
            _query_params.append(('transferables', _params['transferables']))

        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # authentication setting
        _auth_settings = []  # noqa: E501

        _response_types_map = {
            '200': "AnchorPoints",
            '500': "str",
        }

        return self.api_client.call_api(
            '/anchor_points', 'GET',
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            async_req=_params.get('async_req'),
            _return_http_data_only=_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=_params.get('_preload_content', True),
            _request_timeout=_params.get('_request_timeout'),
            collection_formats=_collection_formats,
            _request_auth=_params.get('_request_auth'))
