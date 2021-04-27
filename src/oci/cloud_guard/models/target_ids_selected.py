# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .target_selected import TargetSelected
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class TargetIdsSelected(TargetSelected):
    """
    Target selection on basis of TargetIds.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new TargetIdsSelected object with values from keyword arguments. The default value of the :py:attr:`~oci.cloud_guard.models.TargetIdsSelected.kind` attribute
        of this class is ``TARGETIDS`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param kind:
            The value to assign to the kind property of this TargetIdsSelected.
            Allowed values for this property are: "ALL", "TARGETTYPES", "TARGETIDS"
        :type kind: str

        :param values:
            The value to assign to the values property of this TargetIdsSelected.
        :type values: list[str]

        """
        self.swagger_types = {
            'kind': 'str',
            'values': 'list[str]'
        }

        self.attribute_map = {
            'kind': 'kind',
            'values': 'values'
        }

        self._kind = None
        self._values = None
        self._kind = 'TARGETIDS'

    @property
    def values(self):
        """
        Gets the values of this TargetIdsSelected.
        Ids of Target


        :return: The values of this TargetIdsSelected.
        :rtype: list[str]
        """
        return self._values

    @values.setter
    def values(self, values):
        """
        Sets the values of this TargetIdsSelected.
        Ids of Target


        :param values: The values of this TargetIdsSelected.
        :type: list[str]
        """
        self._values = values

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
