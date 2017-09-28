# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: request.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import attach_network_interface_request_pb2 as attach__network__interface__request__pb2
import clone_vm_request_pb2 as clone__vm__request__pb2
import create_ipv4_subnet_request_pb2 as create__ipv4__subnet__request__pb2
import create_network_request_pb2 as create__network__request__pb2
import create_vm_request_pb2 as create__vm__request__pb2
import create_vm_snapshot_request_pb2 as create__vm__snapshot__request__pb2
import create_volume_request_pb2 as create__volume__request__pb2
import delete_ipv4_subnet_request_pb2 as delete__ipv4__subnet__request__pb2
import delete_network_request_pb2 as delete__network__request__pb2
import delete_vm_request_pb2 as delete__vm__request__pb2
import delete_vm_snapshot_request_pb2 as delete__vm__snapshot__request__pb2
import delete_volume_request_pb2 as delete__volume__request__pb2
import detach_network_interface_request_pb2 as detach__network__interface__request__pb2
import migrate_vm_request_pb2 as migrate__vm__request__pb2
import update_ipv4_subnet_request_pb2 as update__ipv4__subnet__request__pb2
import update_network_interface_request_pb2 as update__network__interface__request__pb2
import update_network_request_pb2 as update__network__request__pb2
import update_vm_power_state_request_pb2 as update__vm__power__state__request__pb2
import update_vm_request_pb2 as update__vm__request__pb2
import network_type_pb2 as network__type__pb2
import vm_power_state_pb2 as vm__power__state__pb2
import vlan_network_setting_pb2 as vlan__network__setting__pb2

from attach_network_interface_request_pb2 import *
from clone_vm_request_pb2 import *
from create_ipv4_subnet_request_pb2 import *
from create_network_request_pb2 import *
from create_vm_request_pb2 import *
from create_vm_snapshot_request_pb2 import *
from create_volume_request_pb2 import *
from delete_ipv4_subnet_request_pb2 import *
from delete_network_request_pb2 import *
from delete_vm_request_pb2 import *
from delete_vm_snapshot_request_pb2 import *
from delete_volume_request_pb2 import *
from detach_network_interface_request_pb2 import *
from migrate_vm_request_pb2 import *
from update_ipv4_subnet_request_pb2 import *
from update_network_interface_request_pb2 import *
from update_network_request_pb2 import *
from update_vm_power_state_request_pb2 import *
from update_vm_request_pb2 import *
from network_type_pb2 import *
from vm_power_state_pb2 import *
from vlan_network_setting_pb2 import *

DESCRIPTOR = _descriptor.FileDescriptor(
  name='request.proto',
  package='',
  syntax='proto3',
  serialized_pb=_b('\n\rrequest.proto\x1a&attach_network_interface_request.proto\x1a\x16\x63lone_vm_request.proto\x1a create_ipv4_subnet_request.proto\x1a\x1c\x63reate_network_request.proto\x1a\x17\x63reate_vm_request.proto\x1a create_vm_snapshot_request.proto\x1a\x1b\x63reate_volume_request.proto\x1a delete_ipv4_subnet_request.proto\x1a\x1c\x64\x65lete_network_request.proto\x1a\x17\x64\x65lete_vm_request.proto\x1a delete_vm_snapshot_request.proto\x1a\x1b\x64\x65lete_volume_request.proto\x1a&detach_network_interface_request.proto\x1a\x18migrate_vm_request.proto\x1a update_ipv4_subnet_request.proto\x1a&update_network_interface_request.proto\x1a\x1cupdate_network_request.proto\x1a#update_vm_power_state_request.proto\x1a\x17update_vm_request.proto\x1a\x12network_type.proto\x1a\x14vm_power_state.proto\x1a\x1avlan_network_setting.proto\"\x8f\t\n\x07Request\x12\x0c\n\x04type\x18\x01 \x01(\t\x12-\n\x11\x63reate_vm_request\x18\x02 \x01(\x0b\x32\x10.CreateVMRequestH\x00\x12-\n\x11update_vm_request\x18\x03 \x01(\x0b\x32\x10.UpdateVMRequestH\x00\x12-\n\x11\x64\x65lete_vm_request\x18\x04 \x01(\x0b\x32\x10.DeleteVMRequestH\x00\x12>\n\x1a\x63reate_vm_snapshot_request\x18\x05 \x01(\x0b\x32\x18.CreateVMSnapshotRequestH\x00\x12>\n\x1a\x64\x65lete_vm_snapshot_request\x18\x06 \x01(\x0b\x32\x18.DeleteVMSnapshotRequestH\x00\x12+\n\x10\x63lone_vm_request\x18\x07 \x01(\x0b\x32\x0f.CloneVMRequestH\x00\x12/\n\x12migrate_vm_request\x18\x08 \x01(\x0b\x32\x11.MigrateVMRequestH\x00\x12\x43\n\x1dupdate_vm_power_state_request\x18\t \x01(\x0b\x32\x1a.UpdateVMPowerStateRequestH\x00\x12\x35\n\x15\x63reate_volume_request\x18\n \x01(\x0b\x32\x14.CreateVolumeRequestH\x00\x12\x35\n\x15\x64\x65lete_volume_request\x18\x0b \x01(\x0b\x32\x14.DeleteVolumeRequestH\x00\x12\x37\n\x16\x63reate_network_request\x18\x0c \x01(\x0b\x32\x15.CreateNetworkRequestH\x00\x12\x37\n\x16update_network_request\x18\r \x01(\x0b\x32\x15.UpdateNetworkRequestH\x00\x12\x37\n\x16\x64\x65lete_network_request\x18\x0e \x01(\x0b\x32\x15.DeleteNetworkRequestH\x00\x12J\n attach_network_interface_request\x18\x0f \x01(\x0b\x32\x1e.AttachNetworkInterfaceRequestH\x00\x12J\n update_network_interface_request\x18\x10 \x01(\x0b\x32\x1e.UpdateNetworkInterfaceRequestH\x00\x12J\n detach_network_interface_request\x18\x11 \x01(\x0b\x32\x1e.DetachNetworkInterfaceRequestH\x00\x12>\n\x1a\x63reate_ipv4_subnet_request\x18\x12 \x01(\x0b\x32\x18.CreateIPv4SubnetRequestH\x00\x12>\n\x1aupdate_ipv4_subnet_request\x18\x13 \x01(\x0b\x32\x18.UpdateIPv4SubnetRequestH\x00\x12>\n\x1a\x64\x65lete_ipv4_subnet_request\x18\x14 \x01(\x0b\x32\x18.DeleteIPv4SubnetRequestH\x00\x42\t\n\x07messageP\x00P\x01P\x02P\x03P\x04P\x05P\x06P\x07P\x08P\tP\nP\x0bP\x0cP\rP\x0eP\x0fP\x10P\x11P\x12P\x13P\x14P\x15\x62\x06proto3')
  ,
  dependencies=[attach__network__interface__request__pb2.DESCRIPTOR,clone__vm__request__pb2.DESCRIPTOR,create__ipv4__subnet__request__pb2.DESCRIPTOR,create__network__request__pb2.DESCRIPTOR,create__vm__request__pb2.DESCRIPTOR,create__vm__snapshot__request__pb2.DESCRIPTOR,create__volume__request__pb2.DESCRIPTOR,delete__ipv4__subnet__request__pb2.DESCRIPTOR,delete__network__request__pb2.DESCRIPTOR,delete__vm__request__pb2.DESCRIPTOR,delete__vm__snapshot__request__pb2.DESCRIPTOR,delete__volume__request__pb2.DESCRIPTOR,detach__network__interface__request__pb2.DESCRIPTOR,migrate__vm__request__pb2.DESCRIPTOR,update__ipv4__subnet__request__pb2.DESCRIPTOR,update__network__interface__request__pb2.DESCRIPTOR,update__network__request__pb2.DESCRIPTOR,update__vm__power__state__request__pb2.DESCRIPTOR,update__vm__request__pb2.DESCRIPTOR,network__type__pb2.DESCRIPTOR,vm__power__state__pb2.DESCRIPTOR,vlan__network__setting__pb2.DESCRIPTOR,],
  public_dependencies=[attach__network__interface__request__pb2.DESCRIPTOR,clone__vm__request__pb2.DESCRIPTOR,create__ipv4__subnet__request__pb2.DESCRIPTOR,create__network__request__pb2.DESCRIPTOR,create__vm__request__pb2.DESCRIPTOR,create__vm__snapshot__request__pb2.DESCRIPTOR,create__volume__request__pb2.DESCRIPTOR,delete__ipv4__subnet__request__pb2.DESCRIPTOR,delete__network__request__pb2.DESCRIPTOR,delete__vm__request__pb2.DESCRIPTOR,delete__vm__snapshot__request__pb2.DESCRIPTOR,delete__volume__request__pb2.DESCRIPTOR,detach__network__interface__request__pb2.DESCRIPTOR,migrate__vm__request__pb2.DESCRIPTOR,update__ipv4__subnet__request__pb2.DESCRIPTOR,update__network__interface__request__pb2.DESCRIPTOR,update__network__request__pb2.DESCRIPTOR,update__vm__power__state__request__pb2.DESCRIPTOR,update__vm__request__pb2.DESCRIPTOR,network__type__pb2.DESCRIPTOR,vm__power__state__pb2.DESCRIPTOR,vlan__network__setting__pb2.DESCRIPTOR,])




_REQUEST = _descriptor.Descriptor(
  name='Request',
  full_name='Request',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='Request.type', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='create_vm_request', full_name='Request.create_vm_request', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='update_vm_request', full_name='Request.update_vm_request', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='delete_vm_request', full_name='Request.delete_vm_request', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='create_vm_snapshot_request', full_name='Request.create_vm_snapshot_request', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='delete_vm_snapshot_request', full_name='Request.delete_vm_snapshot_request', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='clone_vm_request', full_name='Request.clone_vm_request', index=6,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='migrate_vm_request', full_name='Request.migrate_vm_request', index=7,
      number=8, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='update_vm_power_state_request', full_name='Request.update_vm_power_state_request', index=8,
      number=9, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='create_volume_request', full_name='Request.create_volume_request', index=9,
      number=10, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='delete_volume_request', full_name='Request.delete_volume_request', index=10,
      number=11, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='create_network_request', full_name='Request.create_network_request', index=11,
      number=12, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='update_network_request', full_name='Request.update_network_request', index=12,
      number=13, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='delete_network_request', full_name='Request.delete_network_request', index=13,
      number=14, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='attach_network_interface_request', full_name='Request.attach_network_interface_request', index=14,
      number=15, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='update_network_interface_request', full_name='Request.update_network_interface_request', index=15,
      number=16, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='detach_network_interface_request', full_name='Request.detach_network_interface_request', index=16,
      number=17, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='create_ipv4_subnet_request', full_name='Request.create_ipv4_subnet_request', index=17,
      number=18, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='update_ipv4_subnet_request', full_name='Request.update_ipv4_subnet_request', index=18,
      number=19, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='delete_ipv4_subnet_request', full_name='Request.delete_ipv4_subnet_request', index=19,
      number=20, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='message', full_name='Request.message',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=688,
  serialized_end=1855,
)

_REQUEST.fields_by_name['create_vm_request'].message_type = create__vm__request__pb2._CREATEVMREQUEST
_REQUEST.fields_by_name['update_vm_request'].message_type = update__vm__request__pb2._UPDATEVMREQUEST
_REQUEST.fields_by_name['delete_vm_request'].message_type = delete__vm__request__pb2._DELETEVMREQUEST
_REQUEST.fields_by_name['create_vm_snapshot_request'].message_type = create__vm__snapshot__request__pb2._CREATEVMSNAPSHOTREQUEST
_REQUEST.fields_by_name['delete_vm_snapshot_request'].message_type = delete__vm__snapshot__request__pb2._DELETEVMSNAPSHOTREQUEST
_REQUEST.fields_by_name['clone_vm_request'].message_type = clone__vm__request__pb2._CLONEVMREQUEST
_REQUEST.fields_by_name['migrate_vm_request'].message_type = migrate__vm__request__pb2._MIGRATEVMREQUEST
_REQUEST.fields_by_name['update_vm_power_state_request'].message_type = update__vm__power__state__request__pb2._UPDATEVMPOWERSTATEREQUEST
_REQUEST.fields_by_name['create_volume_request'].message_type = create__volume__request__pb2._CREATEVOLUMEREQUEST
_REQUEST.fields_by_name['delete_volume_request'].message_type = delete__volume__request__pb2._DELETEVOLUMEREQUEST
_REQUEST.fields_by_name['create_network_request'].message_type = create__network__request__pb2._CREATENETWORKREQUEST
_REQUEST.fields_by_name['update_network_request'].message_type = update__network__request__pb2._UPDATENETWORKREQUEST
_REQUEST.fields_by_name['delete_network_request'].message_type = delete__network__request__pb2._DELETENETWORKREQUEST
_REQUEST.fields_by_name['attach_network_interface_request'].message_type = attach__network__interface__request__pb2._ATTACHNETWORKINTERFACEREQUEST
_REQUEST.fields_by_name['update_network_interface_request'].message_type = update__network__interface__request__pb2._UPDATENETWORKINTERFACEREQUEST
_REQUEST.fields_by_name['detach_network_interface_request'].message_type = detach__network__interface__request__pb2._DETACHNETWORKINTERFACEREQUEST
_REQUEST.fields_by_name['create_ipv4_subnet_request'].message_type = create__ipv4__subnet__request__pb2._CREATEIPV4SUBNETREQUEST
_REQUEST.fields_by_name['update_ipv4_subnet_request'].message_type = update__ipv4__subnet__request__pb2._UPDATEIPV4SUBNETREQUEST
_REQUEST.fields_by_name['delete_ipv4_subnet_request'].message_type = delete__ipv4__subnet__request__pb2._DELETEIPV4SUBNETREQUEST
_REQUEST.oneofs_by_name['message'].fields.append(
  _REQUEST.fields_by_name['create_vm_request'])
_REQUEST.fields_by_name['create_vm_request'].containing_oneof = _REQUEST.oneofs_by_name['message']
_REQUEST.oneofs_by_name['message'].fields.append(
  _REQUEST.fields_by_name['update_vm_request'])
_REQUEST.fields_by_name['update_vm_request'].containing_oneof = _REQUEST.oneofs_by_name['message']
_REQUEST.oneofs_by_name['message'].fields.append(
  _REQUEST.fields_by_name['delete_vm_request'])
_REQUEST.fields_by_name['delete_vm_request'].containing_oneof = _REQUEST.oneofs_by_name['message']
_REQUEST.oneofs_by_name['message'].fields.append(
  _REQUEST.fields_by_name['create_vm_snapshot_request'])
_REQUEST.fields_by_name['create_vm_snapshot_request'].containing_oneof = _REQUEST.oneofs_by_name['message']
_REQUEST.oneofs_by_name['message'].fields.append(
  _REQUEST.fields_by_name['delete_vm_snapshot_request'])
_REQUEST.fields_by_name['delete_vm_snapshot_request'].containing_oneof = _REQUEST.oneofs_by_name['message']
_REQUEST.oneofs_by_name['message'].fields.append(
  _REQUEST.fields_by_name['clone_vm_request'])
_REQUEST.fields_by_name['clone_vm_request'].containing_oneof = _REQUEST.oneofs_by_name['message']
_REQUEST.oneofs_by_name['message'].fields.append(
  _REQUEST.fields_by_name['migrate_vm_request'])
_REQUEST.fields_by_name['migrate_vm_request'].containing_oneof = _REQUEST.oneofs_by_name['message']
_REQUEST.oneofs_by_name['message'].fields.append(
  _REQUEST.fields_by_name['update_vm_power_state_request'])
_REQUEST.fields_by_name['update_vm_power_state_request'].containing_oneof = _REQUEST.oneofs_by_name['message']
_REQUEST.oneofs_by_name['message'].fields.append(
  _REQUEST.fields_by_name['create_volume_request'])
_REQUEST.fields_by_name['create_volume_request'].containing_oneof = _REQUEST.oneofs_by_name['message']
_REQUEST.oneofs_by_name['message'].fields.append(
  _REQUEST.fields_by_name['delete_volume_request'])
_REQUEST.fields_by_name['delete_volume_request'].containing_oneof = _REQUEST.oneofs_by_name['message']
_REQUEST.oneofs_by_name['message'].fields.append(
  _REQUEST.fields_by_name['create_network_request'])
_REQUEST.fields_by_name['create_network_request'].containing_oneof = _REQUEST.oneofs_by_name['message']
_REQUEST.oneofs_by_name['message'].fields.append(
  _REQUEST.fields_by_name['update_network_request'])
_REQUEST.fields_by_name['update_network_request'].containing_oneof = _REQUEST.oneofs_by_name['message']
_REQUEST.oneofs_by_name['message'].fields.append(
  _REQUEST.fields_by_name['delete_network_request'])
_REQUEST.fields_by_name['delete_network_request'].containing_oneof = _REQUEST.oneofs_by_name['message']
_REQUEST.oneofs_by_name['message'].fields.append(
  _REQUEST.fields_by_name['attach_network_interface_request'])
_REQUEST.fields_by_name['attach_network_interface_request'].containing_oneof = _REQUEST.oneofs_by_name['message']
_REQUEST.oneofs_by_name['message'].fields.append(
  _REQUEST.fields_by_name['update_network_interface_request'])
_REQUEST.fields_by_name['update_network_interface_request'].containing_oneof = _REQUEST.oneofs_by_name['message']
_REQUEST.oneofs_by_name['message'].fields.append(
  _REQUEST.fields_by_name['detach_network_interface_request'])
_REQUEST.fields_by_name['detach_network_interface_request'].containing_oneof = _REQUEST.oneofs_by_name['message']
_REQUEST.oneofs_by_name['message'].fields.append(
  _REQUEST.fields_by_name['create_ipv4_subnet_request'])
_REQUEST.fields_by_name['create_ipv4_subnet_request'].containing_oneof = _REQUEST.oneofs_by_name['message']
_REQUEST.oneofs_by_name['message'].fields.append(
  _REQUEST.fields_by_name['update_ipv4_subnet_request'])
_REQUEST.fields_by_name['update_ipv4_subnet_request'].containing_oneof = _REQUEST.oneofs_by_name['message']
_REQUEST.oneofs_by_name['message'].fields.append(
  _REQUEST.fields_by_name['delete_ipv4_subnet_request'])
_REQUEST.fields_by_name['delete_ipv4_subnet_request'].containing_oneof = _REQUEST.oneofs_by_name['message']
DESCRIPTOR.message_types_by_name['Request'] = _REQUEST
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Request = _reflection.GeneratedProtocolMessageType('Request', (_message.Message,), dict(
  DESCRIPTOR = _REQUEST,
  __module__ = 'request_pb2'
  # @@protoc_insertion_point(class_scope:Request)
  ))
_sym_db.RegisterMessage(Request)


# @@protoc_insertion_point(module_scope)
