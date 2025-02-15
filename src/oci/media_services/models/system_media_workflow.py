# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class SystemMediaWorkflow(object):
    """
    A named list of tasks to be used to run a job or as a template to create a MediaWorkflow.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new SystemMediaWorkflow object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param name:
            The value to assign to the name property of this SystemMediaWorkflow.
        :type name: str

        :param description:
            The value to assign to the description property of this SystemMediaWorkflow.
        :type description: str

        :param parameters:
            The value to assign to the parameters property of this SystemMediaWorkflow.
        :type parameters: dict(str, str)

        :param tasks:
            The value to assign to the tasks property of this SystemMediaWorkflow.
        :type tasks: list[oci.media_services.models.MediaWorkflowTask]

        """
        self.swagger_types = {
            'name': 'str',
            'description': 'str',
            'parameters': 'dict(str, str)',
            'tasks': 'list[MediaWorkflowTask]'
        }

        self.attribute_map = {
            'name': 'name',
            'description': 'description',
            'parameters': 'parameters',
            'tasks': 'tasks'
        }

        self._name = None
        self._description = None
        self._parameters = None
        self._tasks = None

    @property
    def name(self):
        """
        **[Required]** Gets the name of this SystemMediaWorkflow.
        System provided unique identifier for this static media workflow.


        :return: The name of this SystemMediaWorkflow.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this SystemMediaWorkflow.
        System provided unique identifier for this static media workflow.


        :param name: The name of this SystemMediaWorkflow.
        :type: str
        """
        self._name = name

    @property
    def description(self):
        """
        Gets the description of this SystemMediaWorkflow.
        Description of this workflow's processing and how that processing can be customized by
        specifying parameter values.


        :return: The description of this SystemMediaWorkflow.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this SystemMediaWorkflow.
        Description of this workflow's processing and how that processing can be customized by
        specifying parameter values.


        :param description: The description of this SystemMediaWorkflow.
        :type: str
        """
        self._description = description

    @property
    def parameters(self):
        """
        Gets the parameters of this SystemMediaWorkflow.
        JSON object representing named parameters and their default values that can be referenced throughout this workflow.
        The values declared here can be overridden by the MediaWorkflowConfigurations or parameters supplied when creating
        MediaWorkflowJobs from this MediaWorkflow.


        :return: The parameters of this SystemMediaWorkflow.
        :rtype: dict(str, str)
        """
        return self._parameters

    @parameters.setter
    def parameters(self, parameters):
        """
        Sets the parameters of this SystemMediaWorkflow.
        JSON object representing named parameters and their default values that can be referenced throughout this workflow.
        The values declared here can be overridden by the MediaWorkflowConfigurations or parameters supplied when creating
        MediaWorkflowJobs from this MediaWorkflow.


        :param parameters: The parameters of this SystemMediaWorkflow.
        :type: dict(str, str)
        """
        self._parameters = parameters

    @property
    def tasks(self):
        """
        **[Required]** Gets the tasks of this SystemMediaWorkflow.
        The processing to be done in this workflow. Each key of the MediaWorkflowTasks in this array is unique
        within the array. The order of the items is preserved from the order of the tasks array in
        CreateMediaWorkflowDetails or UpdateMediaWorkflowDetails.


        :return: The tasks of this SystemMediaWorkflow.
        :rtype: list[oci.media_services.models.MediaWorkflowTask]
        """
        return self._tasks

    @tasks.setter
    def tasks(self, tasks):
        """
        Sets the tasks of this SystemMediaWorkflow.
        The processing to be done in this workflow. Each key of the MediaWorkflowTasks in this array is unique
        within the array. The order of the items is preserved from the order of the tasks array in
        CreateMediaWorkflowDetails or UpdateMediaWorkflowDetails.


        :param tasks: The tasks of this SystemMediaWorkflow.
        :type: list[oci.media_services.models.MediaWorkflowTask]
        """
        self._tasks = tasks

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
