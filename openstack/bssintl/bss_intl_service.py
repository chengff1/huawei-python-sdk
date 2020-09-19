# -*- coding:utf-8 -*-
# Copyright 2019 Huawei Technologies Co.,Ltd.
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may not use
# this file except in compliance with the License.  You may obtain a copy of the
# License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software distributed
# under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR
# CONDITIONS OF ANY KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations under the License.

from openstack import service_filter


class BssIntlService(service_filter.ServiceFilter):
    valid_versions = [service_filter.ValidVersion('v1')]

    def __init__(self, version=None):
        """Create A Bss Service"""
        super(BssIntlService, self).__init__(
            service_type='bss-intlv1',
            version=version,
            requires_project_id=False
        )
