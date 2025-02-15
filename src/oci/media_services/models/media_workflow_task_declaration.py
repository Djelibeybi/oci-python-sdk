# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class MediaWorkflowTaskDeclaration(object):
    """
    The declaration of a type of task that can be used in a MediaWorkflow.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new MediaWorkflowTaskDeclaration object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param name:
            The value to assign to the name property of this MediaWorkflowTaskDeclaration.
        :type name: str

        :param version:
            The value to assign to the version property of this MediaWorkflowTaskDeclaration.
        :type version: int

        :param parameters_schema:
            The value to assign to the parameters_schema property of this MediaWorkflowTaskDeclaration.
        :type parameters_schema: dict(str, str)

        :param parameters_schema_allowing_references:
            The value to assign to the parameters_schema_allowing_references property of this MediaWorkflowTaskDeclaration.
        :type parameters_schema_allowing_references: dict(str, str)

        """
        self.swagger_types = {
            'name': 'str',
            'version': 'int',
            'parameters_schema': 'dict(str, str)',
            'parameters_schema_allowing_references': 'dict(str, str)'
        }

        self.attribute_map = {
            'name': 'name',
            'version': 'version',
            'parameters_schema': 'parametersSchema',
            'parameters_schema_allowing_references': 'parametersSchemaAllowingReferences'
        }

        self._name = None
        self._version = None
        self._parameters_schema = None
        self._parameters_schema_allowing_references = None

    @property
    def name(self):
        """
        **[Required]** Gets the name of this MediaWorkflowTaskDeclaration.
        MediaWorkflowTaskDeclaration identifier. The name and version should be unique among
        MediaWorkflowTaskDeclarations.


        :return: The name of this MediaWorkflowTaskDeclaration.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this MediaWorkflowTaskDeclaration.
        MediaWorkflowTaskDeclaration identifier. The name and version should be unique among
        MediaWorkflowTaskDeclarations.


        :param name: The name of this MediaWorkflowTaskDeclaration.
        :type: str
        """
        self._name = name

    @property
    def version(self):
        """
        **[Required]** Gets the version of this MediaWorkflowTaskDeclaration.
        The version of MediaWorkflowTaskDeclaration, incremented whenever the team implementing the task processor
        modifies the JSON schema of this declaration's definitions, parameters or list of required parameters.


        :return: The version of this MediaWorkflowTaskDeclaration.
        :rtype: int
        """
        return self._version

    @version.setter
    def version(self, version):
        """
        Sets the version of this MediaWorkflowTaskDeclaration.
        The version of MediaWorkflowTaskDeclaration, incremented whenever the team implementing the task processor
        modifies the JSON schema of this declaration's definitions, parameters or list of required parameters.


        :param version: The version of this MediaWorkflowTaskDeclaration.
        :type: int
        """
        self._version = version

    @property
    def parameters_schema(self):
        """
        **[Required]** Gets the parameters_schema of this MediaWorkflowTaskDeclaration.
        JSON schema specifying the parameters supported by this type of task. This is used to validate tasks'
        parameters when jobs are created.


        :return: The parameters_schema of this MediaWorkflowTaskDeclaration.
        :rtype: dict(str, str)
        """
        return self._parameters_schema

    @parameters_schema.setter
    def parameters_schema(self, parameters_schema):
        """
        Sets the parameters_schema of this MediaWorkflowTaskDeclaration.
        JSON schema specifying the parameters supported by this type of task. This is used to validate tasks'
        parameters when jobs are created.


        :param parameters_schema: The parameters_schema of this MediaWorkflowTaskDeclaration.
        :type: dict(str, str)
        """
        self._parameters_schema = parameters_schema

    @property
    def parameters_schema_allowing_references(self):
        """
        **[Required]** Gets the parameters_schema_allowing_references of this MediaWorkflowTaskDeclaration.
        JSON schema similar to the parameterSchema, but permits parameter values to refer to other parameters using the
        ${/path/to/another/parmeter} syntax.  This is used to validate task parameters when workflows are created.


        :return: The parameters_schema_allowing_references of this MediaWorkflowTaskDeclaration.
        :rtype: dict(str, str)
        """
        return self._parameters_schema_allowing_references

    @parameters_schema_allowing_references.setter
    def parameters_schema_allowing_references(self, parameters_schema_allowing_references):
        """
        Sets the parameters_schema_allowing_references of this MediaWorkflowTaskDeclaration.
        JSON schema similar to the parameterSchema, but permits parameter values to refer to other parameters using the
        ${/path/to/another/parmeter} syntax.  This is used to validate task parameters when workflows are created.


        :param parameters_schema_allowing_references: The parameters_schema_allowing_references of this MediaWorkflowTaskDeclaration.
        :type: dict(str, str)
        """
        self._parameters_schema_allowing_references = parameters_schema_allowing_references

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
