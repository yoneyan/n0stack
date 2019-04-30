// Code generated by protoc-gen-go. DO NOT EDIT.
// source: n0stack/budget/v0/network_interface.proto

package pbudget

import (
	fmt "fmt"
	proto "github.com/golang/protobuf/proto"
	math "math"
)

// Reference imports to suppress errors if they are not otherwise used.
var _ = proto.Marshal
var _ = fmt.Errorf
var _ = math.Inf

// This is a compile-time assertion to ensure that this generated file
// is compatible with the proto package it is being compiled against.
// A compilation error at this line likely means your copy of the
// proto package needs to be updated.
const _ = proto.ProtoPackageIsVersion3 // please upgrade the proto package

type NetworkInterface struct {
	Annotations          map[string]string `protobuf:"bytes,1,rep,name=annotations,proto3" json:"annotations,omitempty" protobuf_key:"bytes,1,opt,name=key,proto3" protobuf_val:"bytes,2,opt,name=value,proto3"`
	HardwareAddress      string            `protobuf:"bytes,2,opt,name=hardware_address,json=hardwareAddress,proto3" json:"hardware_address,omitempty"`
	Ipv4Address          string            `protobuf:"bytes,3,opt,name=ipv4_address,json=ipv4Address,proto3" json:"ipv4_address,omitempty"`
	Ipv6Address          string            `protobuf:"bytes,4,opt,name=ipv6_address,json=ipv6Address,proto3" json:"ipv6_address,omitempty"`
	XXX_NoUnkeyedLiteral struct{}          `json:"-"`
	XXX_unrecognized     []byte            `json:"-"`
	XXX_sizecache        int32             `json:"-"`
}

func (m *NetworkInterface) Reset()         { *m = NetworkInterface{} }
func (m *NetworkInterface) String() string { return proto.CompactTextString(m) }
func (*NetworkInterface) ProtoMessage()    {}
func (*NetworkInterface) Descriptor() ([]byte, []int) {
	return fileDescriptor_ad6189f6f4d6146a, []int{0}
}

func (m *NetworkInterface) XXX_Unmarshal(b []byte) error {
	return xxx_messageInfo_NetworkInterface.Unmarshal(m, b)
}
func (m *NetworkInterface) XXX_Marshal(b []byte, deterministic bool) ([]byte, error) {
	return xxx_messageInfo_NetworkInterface.Marshal(b, m, deterministic)
}
func (m *NetworkInterface) XXX_Merge(src proto.Message) {
	xxx_messageInfo_NetworkInterface.Merge(m, src)
}
func (m *NetworkInterface) XXX_Size() int {
	return xxx_messageInfo_NetworkInterface.Size(m)
}
func (m *NetworkInterface) XXX_DiscardUnknown() {
	xxx_messageInfo_NetworkInterface.DiscardUnknown(m)
}

var xxx_messageInfo_NetworkInterface proto.InternalMessageInfo

func (m *NetworkInterface) GetAnnotations() map[string]string {
	if m != nil {
		return m.Annotations
	}
	return nil
}

func (m *NetworkInterface) GetHardwareAddress() string {
	if m != nil {
		return m.HardwareAddress
	}
	return ""
}

func (m *NetworkInterface) GetIpv4Address() string {
	if m != nil {
		return m.Ipv4Address
	}
	return ""
}

func (m *NetworkInterface) GetIpv6Address() string {
	if m != nil {
		return m.Ipv6Address
	}
	return ""
}

func init() {
	proto.RegisterType((*NetworkInterface)(nil), "n0stack.budget.v0.NetworkInterface")
	proto.RegisterMapType((map[string]string)(nil), "n0stack.budget.v0.NetworkInterface.AnnotationsEntry")
}

func init() {
	proto.RegisterFile("n0stack/budget/v0/network_interface.proto", fileDescriptor_ad6189f6f4d6146a)
}

var fileDescriptor_ad6189f6f4d6146a = []byte{
	// 261 bytes of a gzipped FileDescriptorProto
	0x1f, 0x8b, 0x08, 0x00, 0x00, 0x00, 0x00, 0x00, 0x02, 0xff, 0xe2, 0xd2, 0xcc, 0x33, 0x28, 0x2e,
	0x49, 0x4c, 0xce, 0xd6, 0x4f, 0x2a, 0x4d, 0x49, 0x4f, 0x2d, 0xd1, 0x2f, 0x33, 0xd0, 0xcf, 0x4b,
	0x2d, 0x29, 0xcf, 0x2f, 0xca, 0x8e, 0xcf, 0xcc, 0x2b, 0x49, 0x2d, 0x4a, 0x4b, 0x4c, 0x4e, 0xd5,
	0x2b, 0x28, 0xca, 0x2f, 0xc9, 0x17, 0x12, 0x84, 0x2a, 0xd5, 0x83, 0x28, 0xd5, 0x2b, 0x33, 0x50,
	0x9a, 0xcd, 0xc4, 0x25, 0xe0, 0x07, 0x51, 0xee, 0x09, 0x53, 0x2d, 0x14, 0xc6, 0xc5, 0x9d, 0x98,
	0x97, 0x97, 0x5f, 0x92, 0x58, 0x92, 0x99, 0x9f, 0x57, 0x2c, 0xc1, 0xa8, 0xc0, 0xac, 0xc1, 0x6d,
	0x64, 0xa2, 0x87, 0xa1, 0x5b, 0x0f, 0x5d, 0xa7, 0x9e, 0x23, 0x42, 0x9b, 0x6b, 0x5e, 0x49, 0x51,
	0x65, 0x10, 0xb2, 0x41, 0x42, 0x9a, 0x5c, 0x02, 0x19, 0x89, 0x45, 0x29, 0xe5, 0x89, 0x45, 0xa9,
	0xf1, 0x89, 0x29, 0x29, 0x45, 0xa9, 0xc5, 0xc5, 0x12, 0x4c, 0x0a, 0x8c, 0x1a, 0x9c, 0x41, 0xfc,
	0x30, 0x71, 0x47, 0x88, 0xb0, 0x90, 0x22, 0x17, 0x4f, 0x66, 0x41, 0x99, 0x09, 0x5c, 0x19, 0x33,
	0x58, 0x19, 0x37, 0x48, 0x0c, 0x55, 0x89, 0x19, 0x5c, 0x09, 0x0b, 0x5c, 0x89, 0x19, 0x54, 0x89,
	0x94, 0x1d, 0x97, 0x00, 0xba, 0x8b, 0x84, 0x04, 0xb8, 0x98, 0xb3, 0x53, 0x2b, 0x25, 0x18, 0xc1,
	0xaa, 0x41, 0x4c, 0x21, 0x11, 0x2e, 0xd6, 0xb2, 0xc4, 0x9c, 0xd2, 0x54, 0xa8, 0x5b, 0x20, 0x1c,
	0x2b, 0x26, 0x0b, 0x46, 0x27, 0xcb, 0x28, 0xf3, 0xf4, 0xcc, 0x92, 0x8c, 0xd2, 0x24, 0xbd, 0xe4,
	0xfc, 0x5c, 0x7d, 0x58, 0x40, 0x23, 0x68, 0x70, 0xb0, 0xea, 0xa5, 0xe7, 0x23, 0xc2, 0xde, 0xba,
	0x00, 0xc2, 0x4c, 0x62, 0x03, 0xcb, 0x19, 0x03, 0x02, 0x00, 0x00, 0xff, 0xff, 0x30, 0xc5, 0xbc,
	0x76, 0x9f, 0x01, 0x00, 0x00,
}
