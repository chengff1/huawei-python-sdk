# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.
#
#      Huawei has modified this source file.
#     
#         Copyright 2020 Huawei Technologies Co., Ltd.
#         
#         Licensed under the Apache License, Version 2.0 (the "License"); you may not
#         use this file except in compliance with the License. You may obtain a copy of
#         the License at
#         
#             http://www.apache.org/licenses/LICENSE-2.0
#         
#         Unless required by applicable law or agreed to in writing, software
#         distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#         WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#         License for the specific language governing permissions and limitations under
#         the License.

from openstack.identity import identity_service
from openstack import resource2 as resource


class Service(resource.Resource):
    resource_key = 'service'
    resources_key = 'services'
    base_path = '/services'
    service = identity_service.IdentityService()

    # capabilities
    allow_create = True
    allow_get = True
    allow_update = True
    allow_delete = True
    allow_list = True
    patch_update = True

    _query_mapping = resource.QueryParameters('type')

    # Properties
    #: User-facing description of the service. *Type: string*
    description = resource.Body('description')
    #: Setting this value to ``False`` prevents the service and
    #: its endpoints from appearing in the service catalog. *Type: bool*
    is_enabled = resource.Body('enabled', type=bool)
    #: The links for the service resource.
    links = resource.Body('links')
    #: User-facing name of the service. *Type: string*
    name = resource.Body('name')
    #: Describes the API implemented by the service. The following values are
    #: recognized within the OpenStack ecosystem: ``compute``, ``image``,
    #: ``ec2``, ``identity``, ``volume``, ``network``. To support non-core and
    #: future projects, the value should not be validated against this list.
    #: *Type: string*
    type = resource.Body('type')
    #: The id of the service. *Type: string*
    id = resource.Body('id')


class Catalog(resource.Resource):
    base_path = '/auth/catalog'
    service = identity_service.IdentityService()

    # capabilities
    allow_create = True
    allow_get = True
    allow_update = True
    allow_delete = True
    allow_list = True
    patch_update = True

    # Properties
    catalog = resource.Body('catalog', type=list)

    def get_service_catalog(self, session):
        endpoint_override = self.service.get_endpoint_override()
        uri = self.base_path
        response = session.get(uri, endpoint_filter=self.service, endpoint_override=endpoint_override)
        self._translate_response(response)
        return self
