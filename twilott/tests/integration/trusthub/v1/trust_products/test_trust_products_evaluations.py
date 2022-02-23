# coding=utf-8
r"""
This code was generated by
\ / _    _  _|   _  _
 | (_)\/(_)(_|\/| |(/_  v1.0.0
      /       /
"""

from tests import IntegrationTestCase
from tests.holodeck import Request
from twilio.base.exceptions import TwilioException
from twilio.http.response import Response


class TrustProductsEvaluationsTestCase(IntegrationTestCase):

    def test_create_request(self):
        self.holodeck.mock(Response(500, ''))

        with self.assertRaises(TwilioException):
            self.client.trusthub.v1.trust_products("BUXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                   .trust_products_evaluations.create(policy_sid="RNXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")

        values = {'PolicySid': "RNXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX", }

        self.holodeck.assert_has_request(Request(
            'post',
            'https://trusthub.twilio.com/v1/TrustProducts/BUXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/Evaluations',
            data=values,
        ))

    def test_create_response(self):
        self.holodeck.mock(Response(
            201,
            '''
            {
                "sid": "ELaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "policy_sid": "RNaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "trust_product_sid": "BUaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "status": "noncompliant",
                "date_created": "2020-04-28T18:14:01Z",
                "url": "https://trusthub.twilio.com/v1/TrustProducts/BUaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Evaluations/ELaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "results": [
                    {
                        "friendly_name": "Business",
                        "object_type": "business",
                        "passed": false,
                        "failure_reason": "A Business End-User is missing. Please add one to the regulatory bundle.",
                        "error_code": 22214,
                        "valid": [],
                        "invalid": [
                            {
                                "friendly_name": "Business Name",
                                "object_field": "business_name",
                                "failure_reason": "The Business Name is missing. Please enter in a Business Name on the Business information.",
                                "error_code": 22215
                            },
                            {
                                "friendly_name": "Business Registration Number",
                                "object_field": "business_registration_number",
                                "failure_reason": "The Business Registration Number is missing. Please enter in a Business Registration Number on the Business information.",
                                "error_code": 22215
                            },
                            {
                                "friendly_name": "First Name",
                                "object_field": "first_name",
                                "failure_reason": "The First Name is missing. Please enter in a First Name on the Business information.",
                                "error_code": 22215
                            },
                            {
                                "friendly_name": "Last Name",
                                "object_field": "last_name",
                                "failure_reason": "The Last Name is missing. Please enter in a Last Name on the Business information.",
                                "error_code": 22215
                            }
                        ],
                        "requirement_friendly_name": "Business",
                        "requirement_name": "business_info"
                    },
                    {
                        "friendly_name": "Excerpt from the commercial register (Extrait K-bis) showing name of Authorized Representative",
                        "object_type": "commercial_registrar_excerpt",
                        "passed": false,
                        "failure_reason": "An Excerpt from the commercial register (Extrait K-bis) showing name of Authorized Representative is missing. Please add one to the regulatory bundle.",
                        "error_code": 22216,
                        "valid": [],
                        "invalid": [
                            {
                                "friendly_name": "Business Name",
                                "object_field": "business_name",
                                "failure_reason": "The Business Name is missing. Or, it does not match the Business Name you entered within Business information. Please enter in the Business Name shown on the Excerpt from the commercial register (Extrait K-bis) showing name of Authorized Representative or make sure both Business Name fields use the same exact inputs.",
                                "error_code": 22217
                            }
                        ],
                        "requirement_friendly_name": "Business Name",
                        "requirement_name": "business_name_info"
                    },
                    {
                        "friendly_name": "Excerpt from the commercial register showing French address",
                        "object_type": "commercial_registrar_excerpt",
                        "passed": false,
                        "failure_reason": "An Excerpt from the commercial register showing French address is missing. Please add one to the regulatory bundle.",
                        "error_code": 22216,
                        "valid": [],
                        "invalid": [
                            {
                                "friendly_name": "Address sid(s)",
                                "object_field": "address_sids",
                                "failure_reason": "The Address is missing. Please enter in the address shown on the Excerpt from the commercial register showing French address.",
                                "error_code": 22219
                            }
                        ],
                        "requirement_friendly_name": "Business Address (Proof of Address)",
                        "requirement_name": "business_address_proof_info"
                    },
                    {
                        "friendly_name": "Excerpt from the commercial register (Extrait K-bis)",
                        "object_type": "commercial_registrar_excerpt",
                        "passed": false,
                        "failure_reason": "An Excerpt from the commercial register (Extrait K-bis) is missing. Please add one to the regulatory bundle.",
                        "error_code": 22216,
                        "valid": [],
                        "invalid": [
                            {
                                "friendly_name": "Document Number",
                                "object_field": "document_number",
                                "failure_reason": "The Document Number is missing. Please enter in the Document Number shown on the Excerpt from the commercial register (Extrait K-bis).",
                                "error_code": 22217
                            }
                        ],
                        "requirement_friendly_name": "Business Registration Number",
                        "requirement_name": "business_reg_no_info"
                    },
                    {
                        "friendly_name": "Government-issued ID",
                        "object_type": "government_issued_document",
                        "passed": false,
                        "failure_reason": "A Government-issued ID is missing. Please add one to the regulatory bundle.",
                        "error_code": 22216,
                        "valid": [],
                        "invalid": [
                            {
                                "friendly_name": "First Name",
                                "object_field": "first_name",
                                "failure_reason": "The First Name is missing. Or, it does not match the First Name you entered within Business information. Please enter in the First Name shown on the Government-issued ID or make sure both First Name fields use the same exact inputs.",
                                "error_code": 22217
                            },
                            {
                                "friendly_name": "Last Name",
                                "object_field": "last_name",
                                "failure_reason": "The Last Name is missing. Or, it does not match the Last Name you entered within Business information. Please enter in the Last Name shown on the Government-issued ID or make sure both Last Name fields use the same exact inputs.",
                                "error_code": 22217
                            }
                        ],
                        "requirement_friendly_name": "Name of Authorized Representative",
                        "requirement_name": "name_of_auth_rep_info"
                    },
                    {
                        "friendly_name": "Executed Copy of Power of Attorney",
                        "object_type": "power_of_attorney",
                        "passed": false,
                        "failure_reason": "An Executed Copy of Power of Attorney is missing. Please add one to the regulatory bundle.",
                        "error_code": 22216,
                        "valid": [],
                        "invalid": [],
                        "requirement_friendly_name": "Power of Attorney",
                        "requirement_name": "power_of_attorney_info"
                    },
                    {
                        "friendly_name": "Government-issued ID",
                        "object_type": "government_issued_document",
                        "passed": false,
                        "failure_reason": "A Government-issued ID is missing. Please add one to the regulatory bundle.",
                        "error_code": 22216,
                        "valid": [],
                        "invalid": [
                            {
                                "friendly_name": "First Name",
                                "object_field": "first_name",
                                "failure_reason": "The First Name is missing on the Governnment-Issued ID.",
                                "error_code": 22217
                            },
                            {
                                "friendly_name": "Last Name",
                                "object_field": "last_name",
                                "failure_reason": "The Last Name is missing on the Government-issued ID",
                                "error_code": 22217
                            }
                        ],
                        "requirement_friendly_name": "Name of Person granted the Power of Attorney",
                        "requirement_name": "name_in_power_of_attorney_info"
                    }
                ]
            }
            '''
        ))

        actual = self.client.trusthub.v1.trust_products("BUXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                        .trust_products_evaluations.create(policy_sid="RNXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")

        self.assertIsNotNone(actual)

    def test_list_request(self):
        self.holodeck.mock(Response(500, ''))

        with self.assertRaises(TwilioException):
            self.client.trusthub.v1.trust_products("BUXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                   .trust_products_evaluations.list()

        self.holodeck.assert_has_request(Request(
            'get',
            'https://trusthub.twilio.com/v1/TrustProducts/BUXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/Evaluations',
        ))

    def test_read_empty_response(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "results": [],
                "meta": {
                    "page": 0,
                    "page_size": 50,
                    "first_page_url": "https://trusthub.twilio.com/v1/TrustProducts/BUaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Evaluations?PageSize=50&Page=0",
                    "previous_page_url": null,
                    "url": "https://trusthub.twilio.com/v1/TrustProducts/BUaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Evaluations?PageSize=50&Page=0",
                    "next_page_url": null,
                    "key": "results"
                }
            }
            '''
        ))

        actual = self.client.trusthub.v1.trust_products("BUXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                        .trust_products_evaluations.list()

        self.assertIsNotNone(actual)

    def test_read_full_response(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "results": [
                    {
                        "sid": "ELaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "policy_sid": "RNaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "trust_product_sid": "BUaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "status": "noncompliant",
                        "date_created": "2020-04-28T18:14:01Z",
                        "url": "https://trusthub.twilio.com/v1/TrustProducts/BUaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Evaluations/ELaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "results": [
                            {
                                "friendly_name": "Business",
                                "object_type": "business",
                                "passed": false,
                                "failure_reason": "A Business End-User is missing. Please add one to the regulatory bundle.",
                                "error_code": 22214,
                                "valid": [],
                                "invalid": [
                                    {
                                        "friendly_name": "Business Name",
                                        "object_field": "business_name",
                                        "failure_reason": "The Business Name is missing. Please enter in a Business Name on the Business information.",
                                        "error_code": 22215
                                    },
                                    {
                                        "friendly_name": "Business Registration Number",
                                        "object_field": "business_registration_number",
                                        "failure_reason": "The Business Registration Number is missing. Please enter in a Business Registration Number on the Business information.",
                                        "error_code": 22215
                                    },
                                    {
                                        "friendly_name": "First Name",
                                        "object_field": "first_name",
                                        "failure_reason": "The First Name is missing. Please enter in a First Name on the Business information.",
                                        "error_code": 22215
                                    },
                                    {
                                        "friendly_name": "Last Name",
                                        "object_field": "last_name",
                                        "failure_reason": "The Last Name is missing. Please enter in a Last Name on the Business information.",
                                        "error_code": 22215
                                    }
                                ],
                                "requirement_friendly_name": "Business",
                                "requirement_name": "business_info"
                            },
                            {
                                "friendly_name": "Excerpt from the commercial register (Extrait K-bis) showing name of Authorized Representative",
                                "object_type": "commercial_registrar_excerpt",
                                "passed": false,
                                "failure_reason": "An Excerpt from the commercial register (Extrait K-bis) showing name of Authorized Representative is missing. Please add one to the regulatory bundle.",
                                "error_code": 22216,
                                "valid": [],
                                "invalid": [
                                    {
                                        "friendly_name": "Business Name",
                                        "object_field": "business_name",
                                        "failure_reason": "The Business Name is missing. Or, it does not match the Business Name you entered within Business information. Please enter in the Business Name shown on the Excerpt from the commercial register (Extrait K-bis) showing name of Authorized Representative or make sure both Business Name fields use the same exact inputs.",
                                        "error_code": 22217
                                    }
                                ],
                                "requirement_friendly_name": "Business Name",
                                "requirement_name": "business_name_info"
                            },
                            {
                                "friendly_name": "Excerpt from the commercial register showing French address",
                                "object_type": "commercial_registrar_excerpt",
                                "passed": false,
                                "failure_reason": "An Excerpt from the commercial register showing French address is missing. Please add one to the regulatory bundle.",
                                "error_code": 22216,
                                "valid": [],
                                "invalid": [
                                    {
                                        "friendly_name": "Address sid(s)",
                                        "object_field": "address_sids",
                                        "failure_reason": "The Address is missing. Please enter in the address shown on the Excerpt from the commercial register showing French address.",
                                        "error_code": 22219
                                    }
                                ],
                                "requirement_friendly_name": "Business Address (Proof of Address)",
                                "requirement_name": "business_address_proof_info"
                            },
                            {
                                "friendly_name": "Excerpt from the commercial register (Extrait K-bis)",
                                "object_type": "commercial_registrar_excerpt",
                                "passed": false,
                                "failure_reason": "An Excerpt from the commercial register (Extrait K-bis) is missing. Please add one to the regulatory bundle.",
                                "error_code": 22216,
                                "valid": [],
                                "invalid": [
                                    {
                                        "friendly_name": "Document Number",
                                        "object_field": "document_number",
                                        "failure_reason": "The Document Number is missing. Please enter in the Document Number shown on the Excerpt from the commercial register (Extrait K-bis).",
                                        "error_code": 22217
                                    }
                                ],
                                "requirement_friendly_name": "Business Registration Number",
                                "requirement_name": "business_reg_no_info"
                            },
                            {
                                "friendly_name": "Government-issued ID",
                                "object_type": "government_issued_document",
                                "passed": false,
                                "failure_reason": "A Government-issued ID is missing. Please add one to the regulatory bundle.",
                                "error_code": 22216,
                                "valid": [],
                                "invalid": [
                                    {
                                        "friendly_name": "First Name",
                                        "object_field": "first_name",
                                        "failure_reason": "The First Name is missing. Or, it does not match the First Name you entered within Business information. Please enter in the First Name shown on the Government-issued ID or make sure both First Name fields use the same exact inputs.",
                                        "error_code": 22217
                                    },
                                    {
                                        "friendly_name": "Last Name",
                                        "object_field": "last_name",
                                        "failure_reason": "The Last Name is missing. Or, it does not match the Last Name you entered within Business information. Please enter in the Last Name shown on the Government-issued ID or make sure both Last Name fields use the same exact inputs.",
                                        "error_code": 22217
                                    }
                                ],
                                "requirement_friendly_name": "Name of Authorized Representative",
                                "requirement_name": "name_of_auth_rep_info"
                            },
                            {
                                "friendly_name": "Executed Copy of Power of Attorney",
                                "object_type": "power_of_attorney",
                                "passed": false,
                                "failure_reason": "An Executed Copy of Power of Attorney is missing. Please add one to the regulatory bundle.",
                                "error_code": 22216,
                                "valid": [],
                                "invalid": [],
                                "requirement_friendly_name": "Power of Attorney",
                                "requirement_name": "power_of_attorney_info"
                            },
                            {
                                "friendly_name": "Government-issued ID",
                                "object_type": "government_issued_document",
                                "passed": false,
                                "failure_reason": "A Government-issued ID is missing. Please add one to the regulatory bundle.",
                                "error_code": 22216,
                                "valid": [],
                                "invalid": [
                                    {
                                        "friendly_name": "First Name",
                                        "object_field": "first_name",
                                        "failure_reason": "The First Name is missing on the Governnment-Issued ID.",
                                        "error_code": 22217
                                    },
                                    {
                                        "friendly_name": "Last Name",
                                        "object_field": "last_name",
                                        "failure_reason": "The Last Name is missing on the Government-issued ID",
                                        "error_code": 22217
                                    }
                                ],
                                "requirement_friendly_name": "Name of Person granted the Power of Attorney",
                                "requirement_name": "name_in_power_of_attorney_info"
                            }
                        ]
                    }
                ],
                "meta": {
                    "page": 0,
                    "page_size": 50,
                    "first_page_url": "https://trusthub.twilio.com/v1/TrustProducts/BUaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Evaluations?PageSize=50&Page=0",
                    "previous_page_url": null,
                    "url": "https://trusthub.twilio.com/v1/TrustProducts/BUaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Evaluations?PageSize=50&Page=0",
                    "next_page_url": null,
                    "key": "results"
                }
            }
            '''
        ))

        actual = self.client.trusthub.v1.trust_products("BUXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                        .trust_products_evaluations.list()

        self.assertIsNotNone(actual)

    def test_fetch_request(self):
        self.holodeck.mock(Response(500, ''))

        with self.assertRaises(TwilioException):
            self.client.trusthub.v1.trust_products("BUXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                   .trust_products_evaluations("ELXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX").fetch()

        self.holodeck.assert_has_request(Request(
            'get',
            'https://trusthub.twilio.com/v1/TrustProducts/BUXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/Evaluations/ELXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
        ))

    def test_fetch_response(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "sid": "ELaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "policy_sid": "RNaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "trust_product_sid": "BUaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "status": "noncompliant",
                "date_created": "2020-04-28T18:14:01Z",
                "url": "https://trusthub.twilio.com/v1/TrustProducts/BUaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Evaluations/ELaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "results": [
                    {
                        "friendly_name": "Business",
                        "object_type": "business",
                        "passed": false,
                        "failure_reason": "A Business End-User is missing. Please add one to the regulatory bundle.",
                        "error_code": 22214,
                        "valid": [],
                        "invalid": [
                            {
                                "friendly_name": "Business Name",
                                "object_field": "business_name",
                                "failure_reason": "The Business Name is missing. Please enter in a Business Name on the Business information.",
                                "error_code": 22215
                            },
                            {
                                "friendly_name": "Business Registration Number",
                                "object_field": "business_registration_number",
                                "failure_reason": "The Business Registration Number is missing. Please enter in a Business Registration Number on the Business information.",
                                "error_code": 22215
                            },
                            {
                                "friendly_name": "First Name",
                                "object_field": "first_name",
                                "failure_reason": "The First Name is missing. Please enter in a First Name on the Business information.",
                                "error_code": 22215
                            },
                            {
                                "friendly_name": "Last Name",
                                "object_field": "last_name",
                                "failure_reason": "The Last Name is missing. Please enter in a Last Name on the Business information.",
                                "error_code": 22215
                            }
                        ],
                        "requirement_friendly_name": "Business",
                        "requirement_name": "business_info"
                    },
                    {
                        "friendly_name": "Excerpt from the commercial register (Extrait K-bis) showing name of Authorized Representative",
                        "object_type": "commercial_registrar_excerpt",
                        "passed": false,
                        "failure_reason": "An Excerpt from the commercial register (Extrait K-bis) showing name of Authorized Representative is missing. Please add one to the regulatory bundle.",
                        "error_code": 22216,
                        "valid": [],
                        "invalid": [
                            {
                                "friendly_name": "Business Name",
                                "object_field": "business_name",
                                "failure_reason": "The Business Name is missing. Or, it does not match the Business Name you entered within Business information. Please enter in the Business Name shown on the Excerpt from the commercial register (Extrait K-bis) showing name of Authorized Representative or make sure both Business Name fields use the same exact inputs.",
                                "error_code": 22217
                            }
                        ],
                        "requirement_friendly_name": "Business Name",
                        "requirement_name": "business_name_info"
                    },
                    {
                        "friendly_name": "Excerpt from the commercial register showing French address",
                        "object_type": "commercial_registrar_excerpt",
                        "passed": false,
                        "failure_reason": "An Excerpt from the commercial register showing French address is missing. Please add one to the regulatory bundle.",
                        "error_code": 22216,
                        "valid": [],
                        "invalid": [
                            {
                                "friendly_name": "Address sid(s)",
                                "object_field": "address_sids",
                                "failure_reason": "The Address is missing. Please enter in the address shown on the Excerpt from the commercial register showing French address.",
                                "error_code": 22219
                            }
                        ],
                        "requirement_friendly_name": "Business Address (Proof of Address)",
                        "requirement_name": "business_address_proof_info"
                    },
                    {
                        "friendly_name": "Excerpt from the commercial register (Extrait K-bis)",
                        "object_type": "commercial_registrar_excerpt",
                        "passed": false,
                        "failure_reason": "An Excerpt from the commercial register (Extrait K-bis) is missing. Please add one to the regulatory bundle.",
                        "error_code": 22216,
                        "valid": [],
                        "invalid": [
                            {
                                "friendly_name": "Document Number",
                                "object_field": "document_number",
                                "failure_reason": "The Document Number is missing. Please enter in the Document Number shown on the Excerpt from the commercial register (Extrait K-bis).",
                                "error_code": 22217
                            }
                        ],
                        "requirement_friendly_name": "Business Registration Number",
                        "requirement_name": "business_reg_no_info"
                    },
                    {
                        "friendly_name": "Government-issued ID",
                        "object_type": "government_issued_document",
                        "passed": false,
                        "failure_reason": "A Government-issued ID is missing. Please add one to the regulatory bundle.",
                        "error_code": 22216,
                        "valid": [],
                        "invalid": [
                            {
                                "friendly_name": "First Name",
                                "object_field": "first_name",
                                "failure_reason": "The First Name is missing. Or, it does not match the First Name you entered within Business information. Please enter in the First Name shown on the Government-issued ID or make sure both First Name fields use the same exact inputs.",
                                "error_code": 22217
                            },
                            {
                                "friendly_name": "Last Name",
                                "object_field": "last_name",
                                "failure_reason": "The Last Name is missing. Or, it does not match the Last Name you entered within Business information. Please enter in the Last Name shown on the Government-issued ID or make sure both Last Name fields use the same exact inputs.",
                                "error_code": 22217
                            }
                        ],
                        "requirement_friendly_name": "Name of Authorized Representative",
                        "requirement_name": "name_of_auth_rep_info"
                    },
                    {
                        "friendly_name": "Executed Copy of Power of Attorney",
                        "object_type": "power_of_attorney",
                        "passed": false,
                        "failure_reason": "An Executed Copy of Power of Attorney is missing. Please add one to the regulatory bundle.",
                        "error_code": 22216,
                        "valid": [],
                        "invalid": [],
                        "requirement_friendly_name": "Power of Attorney",
                        "requirement_name": "power_of_attorney_info"
                    },
                    {
                        "friendly_name": "Government-issued ID",
                        "object_type": "government_issued_document",
                        "passed": false,
                        "failure_reason": "A Government-issued ID is missing. Please add one to the regulatory bundle.",
                        "error_code": 22216,
                        "valid": [],
                        "invalid": [
                            {
                                "friendly_name": "First Name",
                                "object_field": "first_name",
                                "failure_reason": "The First Name is missing on the Governnment-Issued ID.",
                                "error_code": 22217
                            },
                            {
                                "friendly_name": "Last Name",
                                "object_field": "last_name",
                                "failure_reason": "The Last Name is missing on the Government-issued ID",
                                "error_code": 22217
                            }
                        ],
                        "requirement_friendly_name": "Name of Person granted the Power of Attorney",
                        "requirement_name": "name_in_power_of_attorney_info"
                    }
                ]
            }
            '''
        ))

        actual = self.client.trusthub.v1.trust_products("BUXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                        .trust_products_evaluations("ELXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX").fetch()

        self.assertIsNotNone(actual)
