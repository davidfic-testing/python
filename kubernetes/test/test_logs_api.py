# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: v1.10.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import kubernetes.client
from kubernetes.client.rest import ApiException
from kubernetes.client.apis.logs_api import LogsApi


class TestLogsApi(unittest.TestCase):
    """ LogsApi unit test stubs """

    def setUp(self):
        self.api = kubernetes.client.apis.logs_api.LogsApi()

    def tearDown(self):
        pass

    def test_log_file_handler(self):
        """
        Test case for log_file_handler

        
        """
        pass

    def test_log_file_list_handler(self):
        """
        Test case for log_file_list_handler

        
        """
        pass


if __name__ == '__main__':
    unittest.main()
