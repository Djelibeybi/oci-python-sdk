# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class MediaWorkflowJobFact(object):
    """
    One fact of a list of facts associated to a MediaWorkflowJob that presents a point-in-time
    snapshot of the resources, data and events that were composed to generate a runnable job.
    This information will be used internally to trouble-shoot problematic workflows or jobs.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new MediaWorkflowJobFact object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param media_workflow_job_id:
            The value to assign to the media_workflow_job_id property of this MediaWorkflowJobFact.
        :type media_workflow_job_id: str

        :param key:
            The value to assign to the key property of this MediaWorkflowJobFact.
        :type key: int

        :param name:
            The value to assign to the name property of this MediaWorkflowJobFact.
        :type name: str

        :param type:
            The value to assign to the type property of this MediaWorkflowJobFact.
        :type type: str

        :param detail:
            The value to assign to the detail property of this MediaWorkflowJobFact.
        :type detail: dict(str, str)

        """
        self.swagger_types = {
            'media_workflow_job_id': 'str',
            'key': 'int',
            'name': 'str',
            'type': 'str',
            'detail': 'dict(str, str)'
        }

        self.attribute_map = {
            'media_workflow_job_id': 'mediaWorkflowJobId',
            'key': 'key',
            'name': 'name',
            'type': 'type',
            'detail': 'detail'
        }

        self._media_workflow_job_id = None
        self._key = None
        self._name = None
        self._type = None
        self._detail = None

    @property
    def media_workflow_job_id(self):
        """
        **[Required]** Gets the media_workflow_job_id of this MediaWorkflowJobFact.
        Reference to the parent job.


        :return: The media_workflow_job_id of this MediaWorkflowJobFact.
        :rtype: str
        """
        return self._media_workflow_job_id

    @media_workflow_job_id.setter
    def media_workflow_job_id(self, media_workflow_job_id):
        """
        Sets the media_workflow_job_id of this MediaWorkflowJobFact.
        Reference to the parent job.


        :param media_workflow_job_id: The media_workflow_job_id of this MediaWorkflowJobFact.
        :type: str
        """
        self._media_workflow_job_id = media_workflow_job_id

    @property
    def key(self):
        """
        **[Required]** Gets the key of this MediaWorkflowJobFact.
        System generated serial number to uniquely identify a detail in order within a MediaWorkflowJob.


        :return: The key of this MediaWorkflowJobFact.
        :rtype: int
        """
        return self._key

    @key.setter
    def key(self, key):
        """
        Sets the key of this MediaWorkflowJobFact.
        System generated serial number to uniquely identify a detail in order within a MediaWorkflowJob.


        :param key: The key of this MediaWorkflowJobFact.
        :type: int
        """
        self._key = key

    @property
    def name(self):
        """
        **[Required]** Gets the name of this MediaWorkflowJobFact.
        Unique name. It is read-only and generated for the fact.


        :return: The name of this MediaWorkflowJobFact.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this MediaWorkflowJobFact.
        Unique name. It is read-only and generated for the fact.


        :param name: The name of this MediaWorkflowJobFact.
        :type: str
        """
        self._name = name

    @property
    def type(self):
        """
        **[Required]** Gets the type of this MediaWorkflowJobFact.
        The type of information contained in this detail.


        :return: The type of this MediaWorkflowJobFact.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this MediaWorkflowJobFact.
        The type of information contained in this detail.


        :param type: The type of this MediaWorkflowJobFact.
        :type: str
        """
        self._type = type

    @property
    def detail(self):
        """
        **[Required]** Gets the detail of this MediaWorkflowJobFact.
        The body of the detail captured as JSON.


        :return: The detail of this MediaWorkflowJobFact.
        :rtype: dict(str, str)
        """
        return self._detail

    @detail.setter
    def detail(self, detail):
        """
        Sets the detail of this MediaWorkflowJobFact.
        The body of the detail captured as JSON.


        :param detail: The detail of this MediaWorkflowJobFact.
        :type: dict(str, str)
        """
        self._detail = detail

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
