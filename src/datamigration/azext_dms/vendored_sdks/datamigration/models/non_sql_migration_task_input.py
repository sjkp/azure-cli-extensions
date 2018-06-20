# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class NonSqlMigrationTaskInput(Model):
    """Base class for non sql migration task input.

    :param target_connection_info: Information for connecting to target
    :type target_connection_info:
     ~azure.mgmt.datamigration.models.SqlConnectionInfo
    :param target_database_name: Target database name
    :type target_database_name: str
    :param project_name: Name of the migration project
    :type project_name: str
    :param project_location: An URL that points to the drop location to access
     project artifacts
    :type project_location: str
    :param selected_tables: Metadata of the tables selected for migration
    :type selected_tables:
     list[~azure.mgmt.datamigration.models.NonSqlDataMigrationTable]
    """

    _validation = {
        'target_connection_info': {'required': True},
        'target_database_name': {'required': True},
        'project_name': {'required': True},
        'project_location': {'required': True},
        'selected_tables': {'required': True},
    }

    _attribute_map = {
        'target_connection_info': {'key': 'targetConnectionInfo', 'type': 'SqlConnectionInfo'},
        'target_database_name': {'key': 'targetDatabaseName', 'type': 'str'},
        'project_name': {'key': 'projectName', 'type': 'str'},
        'project_location': {'key': 'projectLocation', 'type': 'str'},
        'selected_tables': {'key': 'selectedTables', 'type': '[NonSqlDataMigrationTable]'},
    }

    def __init__(self, target_connection_info, target_database_name, project_name, project_location, selected_tables):
        super(NonSqlMigrationTaskInput, self).__init__()
        self.target_connection_info = target_connection_info
        self.target_database_name = target_database_name
        self.project_name = project_name
        self.project_location = project_location
        self.selected_tables = selected_tables