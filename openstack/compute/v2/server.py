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
#         Copyright 2018 Huawei Technologies Co., Ltd.
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

from openstack.compute import compute_service
from openstack.compute.v2 import metadata as _metadata
from openstack.compute.v2 import tag
from openstack import resource2
from openstack import utils


class Server(resource2.Resource, _metadata.MetadataMixin, tag.TagMixin):
    resource_key = 'server'
    resources_key = 'servers'
    base_path = '/servers'
    service = compute_service.ComputeService()

    # capabilities
    allow_create = True
    allow_get = True
    allow_update = True
    allow_delete = True
    allow_list = True

    _query_mapping = resource2.QueryParameters(
        "image", "flavor", "name",
        "status", "all_tenants",
        "sort_key", "sort_dir",
        "reservation_id", "tags",
        "project_id", "host",
        tags_any="tags-any",
        not_tags_any="not-tags-any",
        is_deleted="deleted",
        ipv4_address="ip",
        ipv6_address="ip6",
        changes_since="changes-since",
        not_tags="not-tags"
    )

    #: A list of dictionaries holding links relevant to this server.
    links = resource2.Body('links')

    access_ipv4 = resource2.Body('accessIPv4')
    access_ipv6 = resource2.Body('accessIPv6')
    #: A dictionary of addresses this server can be accessed through.
    #: The dictionary contains keys such as ``private`` and ``public``,
    #: each containing a list of dictionaries for addresses of that type.
    #: The addresses are contained in a dictionary with keys ``addr``
    #: and ``version``, which is either 4 or 6 depending on the protocol
    #: of the IP address. *Type: dict*
    addresses = resource2.Body('addresses', type=dict)
    #: Timestamp of when the server was created.
    created_at = resource2.Body('created')
    #: The reason about the server in ERROR status.
    fault = resource2.Body('fault', type=dict)
    #: The flavor reference, as a ID or full URL, for the flavor to use for
    #: this server.
    flavor_id = resource2.Body('flavorRef')
    #: The flavor property as returned from server.
    flavor = resource2.Body('flavor', type=dict)
    #: An ID representing the host of this server.
    host_id = resource2.Body('hostId')
    #: The hostname of the server. Since microversion 2.3.
    hostname = resource2.Body('OS-EXT-SRV-ATTR:hostname')
    #: The status of the compute service. The value can be UP,
    #: DOWN, UNKNOWN or an empty string. Since microversion 2.16.
    host_status = resource2.Body('host_status')
    #: The image reference, as a ID or full URL, for the image to use for
    #: this server.
    image_id = resource2.Body('imageRef')
    #: The image property as returned from server.
    image = resource2.Body('image', type=dict)
    #: Since microversion 2.3.
    reservation_id_ext = resource2.Body('OS-EXT-SRV-ATTR:reservation_id')
    #: The UUID of the kernel image when using AMI format image.
    #: Since microversion 2.3.
    kernel_id = resource2.Body('OS-EXT-SRV-ATTR:kernel_id')
    #: The launch order of the server created in batch. Since microversion 2.3.
    launch_index = resource2.Body('OS-EXT-SRV-ATTR:launch_index', type=int)
    #: The lock status of the server. Since microversion 2.9.
    is_locked = resource2.Body('locked')
    #: Metadata stored for this server. *Type: dict*
    metadata = resource2.Body('metadata', type=dict)
    #: A single metadata queried. *Type: dict*
    meta = resource2.Body('meta', type=dict)
    #: While the server is building, this value represents the percentage
    #: of completion. Once it is completed, it will be 100.  *Type: int*
    progress = resource2.Body('progress', type=int)
    #: The ID of the project this server is associated with.
    project_id = resource2.Body('tenant_id')
    #: The UUID of the ramdisk image when using AMI format image.
    #: Since microversion 2.3.
    ramdisk_id = resource2.Body('OS-EXT-SRV-ATTR:ramdisk_id')
    #: The device name of the system disk of the server.
    #: Since microversion 2.3.
    root_device_name = resource2.Body('OS-EXT-SRV-ATTR:root_device_name')
    #: The state this server is in. Valid values include ``ACTIVE``,
    #: ``BUILDING``, ``DELETED``, ``ERROR``, ``HARD_REBOOT``, ``PASSWORD``,
    #: ``PAUSED``, ``REBOOT``, ``REBUILD``, ``RESCUED``, ``RESIZED``,
    #: ``REVERT_RESIZE``, ``SHUTOFF``, ``SOFT_DELETED``, ``STOPPED``,
    #: ``SUSPENDED``, ``UNKNOWN``, or ``VERIFY_RESIZE``.
    status = resource2.Body('status')
    #: Timestamp of when this server was last updated.
    updated_at = resource2.Body('updated')
    #: The ID of the owners of this server.
    user_id = resource2.Body('user_id')
    #: The name of an associated keypair
    key_name = resource2.Body('key_name')
    #: The disk configuration. Either AUTO or MANUAL.
    disk_config = resource2.Body('OS-DCF:diskConfig')
    #: Indicates whether a configuration drive enables metadata injection.
    #: Not all cloud providers enable this feature.
    has_config_drive = resource2.Body('config_drive')
    #: The name of the availability zone this server is a part of.
    availability_zone = resource2.Body('OS-EXT-AZ:availability_zone')
    #: The power state of this server.
    power_state = resource2.Body('OS-EXT-STS:power_state')
    #: The task state of this server.
    task_state = resource2.Body('OS-EXT-STS:task_state')
    #: The VM state of this server.
    vm_state = resource2.Body('OS-EXT-STS:vm_state')
    #: A list of an attached volumes. Each item in the list contains at least
    #: an "id" key to identify the specific volumes.
    attached_volumes = resource2.Body(
        'os-extended-volumes:volumes_attached')
    #: The timestamp when the server was launched.
    launched_at = resource2.Body('OS-SRV-USG:launched_at')
    #: The timestamp when the server was terminated (if it has been).
    terminated_at = resource2.Body('OS-SRV-USG:terminated_at')
    #: A list of applicable security groups. Each group contains keys for
    #: description, name, id, and rules.
    security_groups = resource2.Body('security_groups')
    #: When a server is first created, it provides the administrator password.
    admin_password = resource2.Body('adminPass')
    #: The file path and contents, text only, to inject into the server at
    #: launch. The maximum size of the file path data is 255 bytes.
    #: The maximum limit is The number of allowed bytes in the decoded,
    #: rather than encoded, data.
    personality = resource2.Body('personality')
    #: Configuration information or scripts to use upon launch.
    #: Must be Base64 encoded.
    user_data = resource2.Body('OS-EXT-SRV-ATTR:user_data')
    #: Enables fine grained control of the block device mapping for an
    #: instance. This is typically used for booting servers from volumes.
    block_device_mapping = resource2.Body('block_device_mapping_v2')
    #: The dictionary of data to send to the scheduler.
    scheduler_hints = resource2.Body('os:scheduler_hints', type=dict)
    #: A networks object. Required parameter when there are multiple
    #: networks defined for the tenant. When you do not specify the
    #: networks parameter, the server attaches to the only network
    #: created for the current tenant.
    networks = resource2.Body('networks')
    #: The hypervisor host name. Appears in the response for administrative
    #: users only.
    hypervisor_hostname = resource2.Body('OS-EXT-SRV-ATTR:hypervisor_hostname')
    #: The instance name. The Compute API generates the instance name from the
    #: instance name template. Appears in the response for administrative users
    #: only.
    instance_name = resource2.Body('OS-EXT-SRV-ATTR:instance_name')
    min_count = resource2.Body("min_count")
    max_count = resource2.Body("max_count")
    description = resource2.Body("description")
    # reservation_id
    reservation_id = resource2.Body("reservation_id")
    # locked
    locked = resource2.Body("locked", type=bool)
    # tags
    tags = resource2.Body("tags", type=list)
    # reserved attribute
    evsOpts = resource2.Body("evsOpts")
    hyperThreadAffinity = resource2.Body("hyperThreadAffinity")
    numaOpts = resource2.Body("numaOpts")
    vcpuAffinity = resource2.Body("vcpuAffinity")
    # host
    host = resource2.Body("OS-EXT-SRV-ATTR:host")

    # only microversion
    # hostname = resource2.Body("OS-EXT-SRV-ATTR:hostname")
    # kernel_id = resource2.Body("OS-EXT-SRV-ATTR:kernel_id")
    # ramdisk_id = resource2.Body("OS-EXT-SRV-ATTR:ramdisk_id")
    # launch_index = resource2.Body("OS-EXT-SRV-ATTR:launch_index")
    # reservation_id_attr = resource2.Body("OS-EXT-SRV-ATTR:reservation_id")
    # root_device_name = resource2.Body("OS-EXT-SRV-ATTR:root_device_name")
    # host_status = resource2.Body("host_status")

    def _prepare_request(self, requires_id=True, prepend_key=True):
        request = super(Server, self)._prepare_request(requires_id=requires_id,
                                                       prepend_key=prepend_key)

        server_body = request.body[self.resource_key]

        # Some names exist without prefix on requests but with a prefix
        # on responses. If we find that we've populated one of these
        # attributes with something and then go to make a request, swap out
        # the name to the bare version.

        # Availability Zones exist with a prefix on response, but not request
        az_key = "OS-EXT-AZ:availability_zone"
        if az_key in server_body:
            server_body["availability_zone"] = server_body.pop(az_key)

        # User Data exists with a prefix on response, but not request
        ud_key = "OS-EXT-SRV-ATTR:user_data"
        if ud_key in server_body:
            server_body["user_data"] = server_body.pop(ud_key)

        # Scheduler hints are sent in a top-level scope, not within the
        # resource_key scope like everything else. If we try to send
        # scheduler_hints, pop them out of the resource_key scope and into
        # their own top-level scope.
        hint_key = "os:scheduler_hints"
        if hint_key in server_body:
            request.body[hint_key] = server_body.pop(hint_key)

        return request

    def _action(self, session, body):
        """Preform server actions given the message body."""
        # NOTE: This is using Server.base_path instead of self.base_path
        # as both Server and ServerDetail instances can be acted on, but
        # the URL used is sans any additional /detail/ part.
        url = utils.urljoin(Server.base_path, self.id, 'action')
        headers = {'Accept': ''}
        endpoint_override = self.service.get_endpoint_override()
        service = self.get_service_filter(self, session)
        return session.post(
            url, endpoint_filter=self.service, microversion=service.microversion, json=body, headers=headers,
            endpoint_override=endpoint_override)

    def change_password(self, session, new_password):
        """Change the administrator password to the given password."""
        body = {'changePassword': {'adminPass': new_password}}
        self._action(session, body)

    def reboot(self, session, reboot_type):
        """Reboot server where reboot_type might be 'SOFT' or 'HARD'."""
        body = {'reboot': {'type': reboot_type}}
        self._action(session, body)

    def force_delete(self, session):
        """Force delete a server."""
        body = {'forceDelete': None}
        self._action(session, body)

    def rebuild(self, session, name, admin_password,
                preserve_ephemeral=False, image=None,
                access_ipv4=None, access_ipv6=None,
                metadata=None, personality=None):
        """Rebuild the server with the given arguments."""
        action = {
            'name': name,
            'adminPass': admin_password,
            'preserve_ephemeral': preserve_ephemeral
        }
        if image is not None:
            action['imageRef'] = resource2.Resource._get_id(image)
        if access_ipv4 is not None:
            action['accessIPv4'] = access_ipv4
        if access_ipv6 is not None:
            action['accessIPv6'] = access_ipv6
        if metadata is not None:
            action['metadata'] = metadata
        if personality is not None:
            action['personality'] = personality

        body = {'rebuild': action}
        response = self._action(session, body)
        self._translate_response(response)
        return self

    def resize(self, session, flavor):
        """Resize server to flavor reference."""
        body = {'resize': {'flavorRef': flavor}}
        self._action(session, body)

    def confirm_resize(self, session):
        """Confirm the resize of the server."""
        body = {'confirmResize': None}
        self._action(session, body)

    def revert_resize(self, session):
        """Revert the resize of the server."""
        body = {'revertResize': None}
        self._action(session, body)

    def create_image(self, session, name, metadata=None):
        """Create image from server."""
        action = {'name': name}
        if metadata is not None:
            action['metadata'] = metadata
        body = {'createImage': action}
        self._action(session, body)

    def add_security_group(self, session, security_group):
        body = {"addSecurityGroup": {"name": security_group}}
        self._action(session, body)

    def remove_security_group(self, session, security_group):
        body = {"removeSecurityGroup": {"name": security_group}}
        self._action(session, body)

    def reset_state(self, session, state):
        body = {"os-resetState": {"state": state}}
        self._action(session, body)

    def add_fixed_ip(self, session, network_id):
        body = {"addFixedIp": {"networkId": network_id}}
        self._action(session, body)

    def remove_fixed_ip(self, session, address):
        body = {"removeFixedIp": {"address": address}}
        self._action(session, body)

    def add_floating_ip(self, session, address, fixed_address=None):
        body = {"addFloatingIp": {"address": address}}
        if fixed_address is not None:
            body['addFloatingIp']['fixed_address'] = fixed_address
        self._action(session, body)

    def remove_floating_ip(self, session, address):
        body = {"removeFloatingIp": {"address": address}}
        self._action(session, body)

    def pause(self, session):
        body = {"pause": None}
        self._action(session, body)

    def unpause(self, session):
        body = {"unpause": None}
        self._action(session, body)

    def suspend(self, session):
        body = {"suspend": None}
        self._action(session, body)

    def resume(self, session):
        body = {"resume": None}
        self._action(session, body)

    def lock(self, session):
        body = {"lock": None}
        self._action(session, body)

    def unlock(self, session):
        body = {"unlock": None}
        self._action(session, body)

    def rescue(self, session, admin_pass=None, image_ref=None):
        body = {"rescue": {}}
        if admin_pass is not None:
            body["rescue"]["adminPass"] = admin_pass
        if image_ref is not None:
            body["rescue"]["rescue_image_ref"] = image_ref
        self._action(session, body)

    def unrescue(self, session):
        body = {"unrescue": None}
        self._action(session, body)

    def evacuate(self, session, host=None, admin_pass=None, force=None):
        body = {"evacuate": {}}
        if host is not None:
            body["evacuate"]["host"] = host
        if admin_pass is not None:
            body["evacuate"]["adminPass"] = admin_pass
        if force is not None:
            body["evacuate"]["force"] = force
        self._action(session, body)

    def start(self, session):
        body = {"os-start": None}
        self._action(session, body)

    def stop(self, session, stop_type):
        body = {"os-stop": {"type": stop_type}}
        self._action(session, body)

    def shelve(self, session):
        body = {"shelve": None}
        self._action(session, body)

    def unshelve(self, session):
        body = {"unshelve": None}
        self._action(session, body)

    def console_output(self, session, lines):
        body = {"os-getConsoleOutput": {"length": lines}}
        return self._action(session, body).json()["output"]


class ServerDetail(Server):
    base_path = '/servers/detail'

    # capabilities
    allow_create = False
    allow_get = False
    allow_update = False
    allow_delete = False
    allow_list = True

class ServerListDetail(Server):
    base_path = '/servers/detail'
    allow_create = False
    allow_get = False
    allow_update = False
    allow_delete = False
    allow_list = True

    flavor = resource2.Body('flavor')
    image = resource2.Body('image')

    def list_ext(cls, session, paginated=False, headers=None, **params):
        more_data = True
        query_params = cls._query_mapping._transpose(params)
        uri = cls.get_list_uri(params)

        if headers:
            headers.update({"Accept": "application/json"})
        else:
            headers = {"Accept": "application/json"}

        service = cls.get_service_filter(cls, session)
        while more_data:
            endpoint_override = cls.service.get_endpoint_override()
            resp = session.get(uri, endpoint_filter=cls.service,
                               microversion=service.microversion,
                               endpoint_override=endpoint_override,
                               headers=headers,
                               params=query_params)
            response_json = resp.json()
            if cls.resources_key:
                resources = cls.find_value_by_accessor(response_json,
                                                       cls.resources_key)
            else:
                resources = response_json
            if not resources:
                more_data = False
            yielded = 0
            new_marker = None
            for data in resources:
                data.pop("self", None)
                value = cls.existing(**data)
                new_marker = value.id
                yielded += 1
                yield value
            query_params = dict(query_params)
            next_marker = cls.get_next_marker(response_json,
                                              yielded,
                                              query_params)
            if next_marker:
                new_marker = next_marker if next_marker != -1 else None
            if not new_marker:
                return
            if not paginated:
                return
            if cls.query_limit_key in query_params:
                if yielded < query_params["limit"]:
                    return
            query_params[cls.query_limit_key] = yielded
            query_params[cls.query_marker_key] = new_marker


class ServerAction(resource2.Resource):
    base_path = "/servers/%(server_id)s/os-instance-actions"
    allow_list = True
    resources_key = 'instanceActions'
    service = compute_service.ComputeService()

    # Behavioral action
    # Ranges:
    # Create , delete , evacuate , restore , stop ,
    # Start , reboot , rebuild , revertResize ,
    # confirmResize , detach_volume ,
    # Attach_volume , attach_interface ,
    # Detach_interface , lock , unlock , resize ,
    # Migrate , pause , unpause , suspend , resume ,
    # Rescue , unrescue , changePassword ,
    # Shelve , unshelve , live-migration ,
    # Live_migration_cancel ,
    # Live_migration_force_complete ,
    # Trigger_crash_dump, extend_volume
    action = resource2.Body("action")
    # ecs id
    instance_uuid = resource2.Body("instance_uuid")
    # Behavior completion status information
    message = resource2.Body("message")
    # project id
    project_id = resource2.Body("project_id")
    # request id
    request_id = resource2.Body("request_id")
    # update at
    updated_at = resource2.Body("updated_at")
    # start time
    start_time = resource2.Body("start_time")
    # user id
    user_id = resource2.Body("user_id")
    # server id
    server_id = resource2.URI("server_id")


class ServerActionReqID(resource2.Resource):
    base_path = "/servers/%(server_id)s/os-instance-actions"
    allow_get = True
    resource_key = 'instanceAction'
    service = compute_service.ComputeService()

    # Behavioral action
    # Ranges:
    # Create , delete , evacuate , restore , stop ,
    # Start , reboot , rebuild , revertResize ,
    # confirmResize , detach_volume ,
    # Attach_volume , attach_interface ,
    # Detach_interface , lock , unlock , resize ,
    # Migrate , pause , unpause , suspend , resume ,
    # Rescue , unrescue , changePassword ,
    # Shelve , unshelve , live-migration ,
    # Live_migration_cancel ,
    # Live_migration_force_complete ,
    # Trigger_crash_dump, extend_volume
    action = resource2.Body("action")
    # ecs id
    instance_uuid = resource2.Body("instance_uuid")
    # Behavior completion status information
    message = resource2.Body("message")
    # project id
    project_id = resource2.Body("project_id")
    # request id
    id = resource2.Body("request_id")
    # start time
    start_time = resource2.Body("start_time")
    # user id
    user_id = resource2.Body("user_id")
    # events
    events = resource2.Body("events", type=list)
    # server id
    server_id = resource2.URI("server_id")


class ServerOS(resource2.Resource):
    base_path = "/cloudservers"
    allow_create = True

    service = compute_service.ComputeService()

    # admin password
    adminpass = resource2.Body("adminpass")
    # key name
    keyname = resource2.Body("keyname")
    # user id
    userid = resource2.Body("userid")
    # metadata
    metadata = resource2.Body("metadata", type=dict)

    def reinstall(self, session, server_id):
        url = utils.urljoin(self.base_path, server_id, 'reinstallos')
        headers = {'Accept': ''}
        endpoint_override = self.service.get_endpoint_override()
        service = self.get_service_filter(self, session)
        body = {"os-reinstall": self._body.dirty}
        return session.post(
            url, endpoint_filter=self.service, microversion=service.microversion, json=body, headers=headers,
            endpoint_override=endpoint_override).json()


class VncAddress(resource2.Resource):
    base_path = '/servers/%(server_id)s/remote-consoles'

    service = compute_service.ComputeService()

    allow_create = True

    server_id = resource2.URI('server_id')

    # The total number of lists of elastic cloud servers.
    remote_console = resource2.Body('remote_console')
    # Elastic cloud server details list.
    type = resource2.Body('type')
    protocol = resource2.Body('protocol')
    url = resource2.Body('url')
