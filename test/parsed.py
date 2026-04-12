from ctypes import *

# file /usr/include/bits/types.h, line 31, column 23
__u_char = c_ubyte

# file /usr/include/bits/types.h, line 32, column 28
__u_short = c_ushort

# file /usr/include/bits/types.h, line 33, column 22
__u_int = c_uint

# file /usr/include/bits/types.h, line 34, column 27
__u_long = c_ulong

# file /usr/include/bits/types.h, line 37, column 21
__int8_t = c_byte

# file /usr/include/bits/types.h, line 38, column 23
__uint8_t = c_ubyte

# file /usr/include/bits/types.h, line 39, column 26
__int16_t = c_short

# file /usr/include/bits/types.h, line 40, column 28
__uint16_t = c_ushort

# file /usr/include/bits/types.h, line 41, column 20
__int32_t = c_int

# file /usr/include/bits/types.h, line 42, column 22
__uint32_t = c_uint

# file /usr/include/bits/types.h, line 44, column 25
__int64_t = c_long

# file /usr/include/bits/types.h, line 45, column 27
__uint64_t = c_ulong

# file /usr/include/bits/types.h, line 52, column 18
__int_least8_t = c_byte

# file /usr/include/bits/types.h, line 53, column 19
__uint_least8_t = c_ubyte

# file /usr/include/bits/types.h, line 54, column 19
__int_least16_t = c_short

# file /usr/include/bits/types.h, line 55, column 20
__uint_least16_t = c_ushort

# file /usr/include/bits/types.h, line 56, column 19
__int_least32_t = c_int

# file /usr/include/bits/types.h, line 57, column 20
__uint_least32_t = c_uint

# file /usr/include/bits/types.h, line 58, column 19
__int_least64_t = c_long

# file /usr/include/bits/types.h, line 59, column 20
__uint_least64_t = c_ulong

# file /usr/include/bits/types.h, line 63, column 18
__quad_t = c_long

# file /usr/include/bits/types.h, line 64, column 27
__u_quad_t = c_ulong

# file /usr/include/bits/types.h, line 72, column 18
__intmax_t = c_long

# file /usr/include/bits/types.h, line 73, column 27
__uintmax_t = c_ulong

# file /usr/include/bits/types.h, line 145, column 25
__dev_t = c_ulong

# file /usr/include/bits/types.h, line 146, column 25
__uid_t = c_uint

# file /usr/include/bits/types.h, line 147, column 25
__gid_t = c_uint

# file /usr/include/bits/types.h, line 148, column 25
__ino_t = c_ulong

# file /usr/include/bits/types.h, line 149, column 27
__ino64_t = c_ulong

# file /usr/include/bits/types.h, line 150, column 26
__mode_t = c_uint

# file /usr/include/bits/types.h, line 151, column 27
__nlink_t = c_ulong

# file /usr/include/bits/types.h, line 152, column 25
__off_t = c_long

# file /usr/include/bits/types.h, line 153, column 27
__off64_t = c_long

# file /usr/include/bits/types.h, line 154, column 25
__pid_t = c_int

# file /usr/include/bits/types.h, line 155, column 12

class __fsid_t(Structure):
    pass
__fsid_t._align_ = 4
__fsid_t._fields_ = [('__val', c_int * 2)]

# file /usr/include/bits/types.h, line 155, column 26
__fsid_t = __fsid_t

# file /usr/include/bits/types.h, line 156, column 27
__clock_t = c_long

# file /usr/include/bits/types.h, line 157, column 26
__rlim_t = c_ulong

# file /usr/include/bits/types.h, line 158, column 28
__rlim64_t = c_ulong

# file /usr/include/bits/types.h, line 159, column 24
__id_t = c_uint

# file /usr/include/bits/types.h, line 160, column 26
__time_t = c_long

# file /usr/include/bits/types.h, line 161, column 30
__useconds_t = c_uint

# file /usr/include/bits/types.h, line 162, column 31
__suseconds_t = c_long

# file /usr/include/bits/types.h, line 163, column 33
__suseconds64_t = c_long

# file /usr/include/bits/types.h, line 165, column 27
__daddr_t = c_int

# file /usr/include/bits/types.h, line 166, column 25
__key_t = c_int

# file /usr/include/bits/types.h, line 169, column 29
__clockid_t = c_int

# file /usr/include/bits/types.h, line 172, column 27
__timer_t = POINTER(None)

# file /usr/include/bits/types.h, line 175, column 29
__blksize_t = c_long

# file /usr/include/bits/types.h, line 180, column 28
__blkcnt_t = c_long

# file /usr/include/bits/types.h, line 181, column 30
__blkcnt64_t = c_long

# file /usr/include/bits/types.h, line 184, column 30
__fsblkcnt_t = c_ulong

# file /usr/include/bits/types.h, line 185, column 32
__fsblkcnt64_t = c_ulong

# file /usr/include/bits/types.h, line 188, column 30
__fsfilcnt_t = c_ulong

# file /usr/include/bits/types.h, line 189, column 32
__fsfilcnt64_t = c_ulong

# file /usr/include/bits/types.h, line 192, column 28
__fsword_t = c_long

# file /usr/include/bits/types.h, line 194, column 27
__ssize_t = c_long

# file /usr/include/bits/types.h, line 197, column 33
__syscall_slong_t = c_long

# file /usr/include/bits/types.h, line 199, column 33
__syscall_ulong_t = c_ulong

# file /usr/include/bits/types.h, line 203, column 19
__loff_t = c_long

# file /usr/include/bits/types.h, line 204, column 15
__caddr_t = c_char_p

# file /usr/include/bits/types.h, line 207, column 25
__intptr_t = c_long

# file /usr/include/bits/types.h, line 210, column 23
__socklen_t = c_uint

# file /usr/include/bits/types.h, line 215, column 13
__sig_atomic_t = c_int

# file /usr/include/bits/types/time_t.h, line 10, column 18
time_t = c_long

# file /usr/include/bits/types/struct_timeval.h, line 8, column 8

class timeval(Structure):
    pass
timeval._align_ = 8
timeval._fields_ = [('tv_sec', c_long), ('tv_usec', c_long)]

# file /usr/include/sys/time.h, line 28, column 23
suseconds_t = c_long

# file /usr/include/bits/types/__sigset_t.h, line 5, column 9

class __sigset_t(Structure):
    pass
__sigset_t._align_ = 8
__sigset_t._fields_ = [('__val', c_ulong * 16)]

# file /usr/include/bits/types/__sigset_t.h, line 8, column 3
__sigset_t = __sigset_t

# file /usr/include/bits/types/sigset_t.h, line 7, column 20
sigset_t = __sigset_t

# file /usr/include/bits/types/struct_timespec.h, line 11, column 8

class timespec(Structure):
    pass
timespec._align_ = 8
timespec._fields_ = [('tv_sec', c_long), ('tv_nsec', c_long)]

# file /usr/include/sys/select.h, line 49, column 18
__fd_mask = c_long

# file /usr/include/sys/select.h, line 59, column 9

class fd_set(Structure):
    pass
fd_set._align_ = 8
fd_set._fields_ = [('__fds_bits', c_long * 16)]

# file /usr/include/sys/select.h, line 70, column 5
fd_set = fd_set

# file /usr/include/sys/select.h, line 77, column 19
fd_mask = c_long

# file /usr/include/sys/select.h, line 102, column 12
DUMMYLIB_so.select.argtypes = [c_int, POINTER(fd_set), POINTER(fd_set), POINTER(fd_set), POINTER(timeval)]
DUMMYLIB_so.select.restype = c_int

# file /usr/include/sys/select.h, line 127, column 12
DUMMYLIB_so.pselect.argtypes = [c_int, POINTER(fd_set), POINTER(fd_set), POINTER(fd_set), POINTER(timespec), POINTER(__sigset_t)]
DUMMYLIB_so.pselect.restype = c_int

# file /usr/include/sys/time.h, line 52, column 8

class timezone(Structure):
    pass
timezone._align_ = 4
timezone._fields_ = [('tz_minuteswest', c_int), ('tz_dsttime', c_int)]

# file /usr/include/sys/time.h, line 67, column 12
DUMMYLIB_so.gettimeofday.argtypes = [POINTER(timeval), POINTER(None)]
DUMMYLIB_so.gettimeofday.restype = c_int

# file /usr/include/sys/time.h, line 86, column 12
DUMMYLIB_so.settimeofday.argtypes = [POINTER(timeval), POINTER(timezone)]
DUMMYLIB_so.settimeofday.restype = c_int

# file /usr/include/sys/time.h, line 94, column 12
DUMMYLIB_so.adjtime.argtypes = [POINTER(timeval), POINTER(timeval)]
DUMMYLIB_so.adjtime.restype = c_int

# file /usr/include/sys/time.h, line 130, column 8

class itimerval(Structure):

    class timeval(Structure):
        pass
    timeval._fields_ = [('tv_sec', c_long), ('tv_usec', c_long)]

    class timeval(Structure):
        pass
    timeval._fields_ = [('tv_sec', c_long), ('tv_usec', c_long)]
itimerval._align_ = 8
itimerval._fields_ = [('it_interval', timeval), ('it_value', timeval)]

# file /usr/include/sys/time.h, line 143, column 13
__itimer_which_t = c_int

# file /usr/include/sys/time.h, line 149, column 12
DUMMYLIB_so.getitimer.argtypes = [c_int, POINTER(itimerval)]
DUMMYLIB_so.getitimer.restype = c_int

# file /usr/include/sys/time.h, line 155, column 12
DUMMYLIB_so.setitimer.argtypes = [c_int, POINTER(itimerval), POINTER(itimerval)]
DUMMYLIB_so.setitimer.restype = c_int

# file /usr/include/sys/time.h, line 162, column 12
DUMMYLIB_so.utimes.argtypes = [c_char_p, timeval * 2]
DUMMYLIB_so.utimes.restype = c_int

# file /usr/include/sys/time.h, line 189, column 12
DUMMYLIB_so.lutimes.argtypes = [c_char_p, timeval * 2]
DUMMYLIB_so.lutimes.restype = c_int

# file /usr/include/sys/time.h, line 193, column 12
DUMMYLIB_so.futimes.argtypes = [c_int, timeval * 2]
DUMMYLIB_so.futimes.restype = c_int

# file /usr/include/asm-generic/int-ll64.h, line 20, column 25
__s8 = c_byte

# file /usr/include/asm-generic/int-ll64.h, line 21, column 23
__u8 = c_ubyte

# file /usr/include/asm-generic/int-ll64.h, line 23, column 26
__s16 = c_short

# file /usr/include/asm-generic/int-ll64.h, line 24, column 24
__u16 = c_ushort

# file /usr/include/asm-generic/int-ll64.h, line 26, column 24
__s32 = c_int

# file /usr/include/asm-generic/int-ll64.h, line 27, column 22
__u32 = c_uint

# file /usr/include/asm-generic/int-ll64.h, line 30, column 44
__s64 = c_long

# file /usr/include/asm-generic/int-ll64.h, line 31, column 42
__u64 = c_ulong

# file /usr/include/linux/posix_types.h, line 25, column 9

class __kernel_fd_set(Structure):
    pass
__kernel_fd_set._align_ = 8
__kernel_fd_set._fields_ = [('fds_bits', c_ulong * 16)]

# file /usr/include/linux/posix_types.h, line 27, column 3
__kernel_fd_set = __kernel_fd_set

# file /usr/include/linux/posix_types.h, line 30, column 16
__kernel_sighandler_t = CFUNCTYPE(None, c_int)

# file /usr/include/linux/posix_types.h, line 33, column 13
__kernel_key_t = c_int

# file /usr/include/linux/posix_types.h, line 34, column 13
__kernel_mqd_t = c_int

# file /usr/include/asm/posix_types_64.h, line 11, column 24
__kernel_old_uid_t = c_ushort

# file /usr/include/asm/posix_types_64.h, line 12, column 24
__kernel_old_gid_t = c_ushort

# file /usr/include/asm/posix_types_64.h, line 15, column 23
__kernel_old_dev_t = c_ulong

# file /usr/include/asm-generic/posix_types.h, line 15, column 15
__kernel_long_t = c_long

# file /usr/include/asm-generic/posix_types.h, line 16, column 23
__kernel_ulong_t = c_ulong

# file /usr/include/asm-generic/posix_types.h, line 20, column 26
__kernel_ino_t = c_ulong

# file /usr/include/asm-generic/posix_types.h, line 24, column 22
__kernel_mode_t = c_uint

# file /usr/include/asm-generic/posix_types.h, line 28, column 14
__kernel_pid_t = c_int

# file /usr/include/asm-generic/posix_types.h, line 32, column 14
__kernel_ipc_pid_t = c_int

# file /usr/include/asm-generic/posix_types.h, line 36, column 22
__kernel_uid_t = c_uint

# file /usr/include/asm-generic/posix_types.h, line 37, column 22
__kernel_gid_t = c_uint

# file /usr/include/asm-generic/posix_types.h, line 41, column 26
__kernel_suseconds_t = c_long

# file /usr/include/asm-generic/posix_types.h, line 45, column 14
__kernel_daddr_t = c_int

# file /usr/include/asm-generic/posix_types.h, line 49, column 22
__kernel_uid32_t = c_uint

# file /usr/include/asm-generic/posix_types.h, line 50, column 22
__kernel_gid32_t = c_uint

# file /usr/include/asm-generic/posix_types.h, line 72, column 26
__kernel_size_t = c_ulong

# file /usr/include/asm-generic/posix_types.h, line 73, column 25
__kernel_ssize_t = c_long

# file /usr/include/asm-generic/posix_types.h, line 74, column 25
__kernel_ptrdiff_t = c_long

# file /usr/include/asm-generic/posix_types.h, line 79, column 9

class __kernel_fsid_t(Structure):
    pass
__kernel_fsid_t._align_ = 4
__kernel_fsid_t._fields_ = [('val', c_int * 2)]

# file /usr/include/asm-generic/posix_types.h, line 81, column 3
__kernel_fsid_t = __kernel_fsid_t

# file /usr/include/asm-generic/posix_types.h, line 87, column 25
__kernel_off_t = c_long

# file /usr/include/asm-generic/posix_types.h, line 88, column 19
__kernel_loff_t = c_long

# file /usr/include/asm-generic/posix_types.h, line 89, column 28
__kernel_uoff_t = c_ulong

# file /usr/include/asm-generic/posix_types.h, line 90, column 25
__kernel_old_time_t = c_long

# file /usr/include/asm-generic/posix_types.h, line 91, column 25
__kernel_time_t = c_long

# file /usr/include/asm-generic/posix_types.h, line 92, column 19
__kernel_time64_t = c_long

# file /usr/include/asm-generic/posix_types.h, line 93, column 25
__kernel_clock_t = c_long

# file /usr/include/asm-generic/posix_types.h, line 94, column 14
__kernel_timer_t = c_int

# file /usr/include/asm-generic/posix_types.h, line 95, column 14
__kernel_clockid_t = c_int

# file /usr/include/asm-generic/posix_types.h, line 96, column 17
__kernel_caddr_t = c_char_p

# file /usr/include/asm-generic/posix_types.h, line 97, column 24
__kernel_uid16_t = c_ushort

# file /usr/include/asm-generic/posix_types.h, line 98, column 24
__kernel_gid16_t = c_ushort

# file /usr/include/linux/types.h, line 12, column 29
__s128 = c_int128

# file /usr/include/linux/types.h, line 13, column 27
__u128 = c_uint128

# file /usr/include/linux/types.h, line 31, column 25
__le16 = c_ushort

# file /usr/include/linux/types.h, line 32, column 25
__be16 = c_ushort

# file /usr/include/linux/types.h, line 33, column 25
__le32 = c_uint

# file /usr/include/linux/types.h, line 34, column 25
__be32 = c_uint

# file /usr/include/linux/types.h, line 35, column 25
__le64 = c_ulong

# file /usr/include/linux/types.h, line 36, column 25
__be64 = c_ulong

# file /usr/include/linux/types.h, line 38, column 25
__sum16 = c_ushort

# file /usr/include/linux/types.h, line 39, column 25
__wsum = c_uint

# file /usr/include/linux/types.h, line 55, column 28
__poll_t = c_uint

# file /usr/include/linux/v4l2-common.h, line 48, column 8

class v4l2_edid(Structure):
    pass
v4l2_edid._align_ = 8
v4l2_edid._fields_ = [('pad', c_uint), ('start_block', c_uint), ('blocks', c_uint), ('reserved', c_uint * 5), ('edid', POINTER(c_ubyte))]

# file /usr/include/linux/v4l2-controls.h, line 1418, column 8

class v4l2_ctrl_h264_sps(Structure):
    pass
v4l2_ctrl_h264_sps._align_ = 4
v4l2_ctrl_h264_sps._fields_ = [('profile_idc', c_ubyte), ('constraint_set_flags', c_ubyte), ('level_idc', c_ubyte), ('seq_parameter_set_id', c_ubyte), ('chroma_format_idc', c_ubyte), ('bit_depth_luma_minus8', c_ubyte), ('bit_depth_chroma_minus8', c_ubyte), ('log2_max_frame_num_minus4', c_ubyte), ('pic_order_cnt_type', c_ubyte), ('log2_max_pic_order_cnt_lsb_minus4', c_ubyte), ('max_num_ref_frames', c_ubyte), ('num_ref_frames_in_pic_order_cnt_cycle', c_ubyte), ('offset_for_ref_frame', c_int * 255), ('offset_for_non_ref_pic', c_int), ('offset_for_top_to_bottom_field', c_int), ('pic_width_in_mbs_minus1', c_ushort), ('pic_height_in_map_units_minus1', c_ushort), ('flags', c_uint)]

# file /usr/include/linux/v4l2-controls.h, line 1474, column 8

class v4l2_ctrl_h264_pps(Structure):
    pass
v4l2_ctrl_h264_pps._align_ = 2
v4l2_ctrl_h264_pps._fields_ = [('pic_parameter_set_id', c_ubyte), ('seq_parameter_set_id', c_ubyte), ('num_slice_groups_minus1', c_ubyte), ('num_ref_idx_l0_default_active_minus1', c_ubyte), ('num_ref_idx_l1_default_active_minus1', c_ubyte), ('weighted_bipred_idc', c_ubyte), ('pic_init_qp_minus26', c_byte), ('pic_init_qs_minus26', c_byte), ('chroma_qp_index_offset', c_byte), ('second_chroma_qp_index_offset', c_byte), ('flags', c_ushort)]

# file /usr/include/linux/v4l2-controls.h, line 1506, column 8

class v4l2_ctrl_h264_scaling_matrix(Structure):
    pass
v4l2_ctrl_h264_scaling_matrix._align_ = 1
v4l2_ctrl_h264_scaling_matrix._fields_ = [('scaling_list_4x4', c_ubyte * 16 * 6), ('scaling_list_8x8', c_ubyte * 64 * 6)]

# file /usr/include/linux/v4l2-controls.h, line 1511, column 8

class v4l2_h264_weight_factors(Structure):
    pass
v4l2_h264_weight_factors._align_ = 2
v4l2_h264_weight_factors._fields_ = [('luma_weight', c_short * 32), ('luma_offset', c_short * 32), ('chroma_weight', c_short * 2 * 32), ('chroma_offset', c_short * 2 * 32)]

# file /usr/include/linux/v4l2-controls.h, line 1536, column 8

class v4l2_ctrl_h264_pred_weights(Structure):
    pass
v4l2_ctrl_h264_pred_weights._align_ = 2
v4l2_ctrl_h264_pred_weights._fields_ = [('luma_log2_weight_denom', c_ushort), ('chroma_log2_weight_denom', c_ushort), ('weight_factors', v4l2_h264_weight_factors * 2)]

# file /usr/include/linux/v4l2-controls.h, line 1553, column 8

class v4l2_h264_reference(Structure):
    pass
v4l2_h264_reference._align_ = 1
v4l2_h264_reference._fields_ = [('fields', c_ubyte), ('index', c_ubyte)]

# file /usr/include/linux/v4l2-controls.h, line 1609, column 8

class v4l2_ctrl_h264_slice_params(Structure):
    pass
v4l2_ctrl_h264_slice_params._align_ = 4
v4l2_ctrl_h264_slice_params._fields_ = [('header_bit_size', c_uint), ('first_mb_in_slice', c_uint), ('slice_type', c_ubyte), ('colour_plane_id', c_ubyte), ('redundant_pic_cnt', c_ubyte), ('cabac_init_idc', c_ubyte), ('slice_qp_delta', c_byte), ('slice_qs_delta', c_byte), ('disable_deblocking_filter_idc', c_ubyte), ('slice_alpha_c0_offset_div2', c_byte), ('slice_beta_offset_div2', c_byte), ('num_ref_idx_l0_active_minus1', c_ubyte), ('num_ref_idx_l1_active_minus1', c_ubyte), ('reserved', c_ubyte), ('ref_pic_list0', v4l2_h264_reference * 32), ('ref_pic_list1', v4l2_h264_reference * 32), ('flags', c_uint)]

# file /usr/include/linux/v4l2-controls.h, line 1654, column 8

class v4l2_h264_dpb_entry(Structure):
    pass
v4l2_h264_dpb_entry._align_ = 8
v4l2_h264_dpb_entry._fields_ = [('reference_ts', c_ulong), ('pic_num', c_uint), ('frame_num', c_ushort), ('fields', c_ubyte), ('reserved', c_ubyte * 5), ('top_field_order_cnt', c_int), ('bottom_field_order_cnt', c_int), ('flags', c_uint)]

# file /usr/include/linux/v4l2-controls.h, line 1693, column 8

class v4l2_ctrl_h264_decode_params(Structure):
    pass
v4l2_ctrl_h264_decode_params._align_ = 8
v4l2_ctrl_h264_decode_params._fields_ = [('dpb', v4l2_h264_dpb_entry * 16), ('nal_ref_idc', c_ushort), ('frame_num', c_ushort), ('top_field_order_cnt', c_int), ('bottom_field_order_cnt', c_int), ('idr_pic_id', c_ushort), ('pic_order_cnt_lsb', c_ushort), ('delta_pic_order_cnt_bottom', c_int), ('delta_pic_order_cnt0', c_int), ('delta_pic_order_cnt1', c_int), ('dec_ref_pic_marking_bit_size', c_uint), ('pic_order_cnt_bit_size', c_uint), ('slice_group_change_cycle', c_uint), ('reserved', c_uint), ('flags', c_uint)]

# file /usr/include/linux/v4l2-controls.h, line 1770, column 8

class v4l2_ctrl_fwht_params(Structure):
    pass
v4l2_ctrl_fwht_params._align_ = 8
v4l2_ctrl_fwht_params._fields_ = [('backward_ref_ts', c_ulong), ('version', c_uint), ('width', c_uint), ('height', c_uint), ('flags', c_uint), ('colorspace', c_uint), ('xfer_func', c_uint), ('ycbcr_enc', c_uint), ('quantization', c_uint)]

# file /usr/include/linux/v4l2-controls.h, line 1803, column 8

class v4l2_vp8_segment(Structure):
    pass
v4l2_vp8_segment._align_ = 4
v4l2_vp8_segment._fields_ = [('quant_update', c_byte * 4), ('lf_update', c_byte * 4), ('segment_probs', c_ubyte * 3), ('padding', c_ubyte), ('flags', c_uint)]

# file /usr/include/linux/v4l2-controls.h, line 1830, column 8

class v4l2_vp8_loop_filter(Structure):
    pass
v4l2_vp8_loop_filter._align_ = 4
v4l2_vp8_loop_filter._fields_ = [('ref_frm_delta', c_byte * 4), ('mb_mode_delta', c_byte * 4), ('sharpness_level', c_ubyte), ('level', c_ubyte), ('padding', c_ushort), ('flags', c_uint)]

# file /usr/include/linux/v4l2-controls.h, line 1855, column 8

class v4l2_vp8_quantization(Structure):
    pass
v4l2_vp8_quantization._align_ = 2
v4l2_vp8_quantization._fields_ = [('y_ac_qi', c_ubyte), ('y_dc_delta', c_byte), ('y2_dc_delta', c_byte), ('y2_ac_delta', c_byte), ('uv_dc_delta', c_byte), ('uv_ac_delta', c_byte), ('padding', c_ushort)]

# file /usr/include/linux/v4l2-controls.h, line 1882, column 8

class v4l2_vp8_entropy(Structure):
    pass
v4l2_vp8_entropy._align_ = 1
v4l2_vp8_entropy._fields_ = [('coeff_probs', c_ubyte * 11 * 3 * 8 * 4), ('y_mode_probs', c_ubyte * 4), ('uv_mode_probs', c_ubyte * 3), ('mv_probs', c_ubyte * 19 * 2), ('padding', c_ubyte * 3)]

# file /usr/include/linux/v4l2-controls.h, line 1901, column 8

class v4l2_vp8_entropy_coder_state(Structure):
    pass
v4l2_vp8_entropy_coder_state._align_ = 1
v4l2_vp8_entropy_coder_state._fields_ = [('range', c_ubyte), ('value', c_ubyte), ('bit_count', c_ubyte), ('padding', c_ubyte)]

# file /usr/include/linux/v4l2-controls.h, line 1947, column 8

class v4l2_ctrl_vp8_frame(Structure):

    class v4l2_vp8_segment(Structure):
        pass
    v4l2_vp8_segment._fields_ = [('quant_update', c_byte * 4), ('lf_update', c_byte * 4), ('segment_probs', c_ubyte * 3), ('padding', c_ubyte), ('flags', c_uint)]

    class v4l2_vp8_loop_filter(Structure):
        pass
    v4l2_vp8_loop_filter._fields_ = [('ref_frm_delta', c_byte * 4), ('mb_mode_delta', c_byte * 4), ('sharpness_level', c_ubyte), ('level', c_ubyte), ('padding', c_ushort), ('flags', c_uint)]

    class v4l2_vp8_quantization(Structure):
        pass
    v4l2_vp8_quantization._fields_ = [('y_ac_qi', c_ubyte), ('y_dc_delta', c_byte), ('y2_dc_delta', c_byte), ('y2_ac_delta', c_byte), ('uv_dc_delta', c_byte), ('uv_ac_delta', c_byte), ('padding', c_ushort)]

    class v4l2_vp8_entropy(Structure):
        pass
    v4l2_vp8_entropy._fields_ = [('coeff_probs', c_ubyte * 11 * 3 * 8 * 4), ('y_mode_probs', c_ubyte * 4), ('uv_mode_probs', c_ubyte * 3), ('mv_probs', c_ubyte * 19 * 2), ('padding', c_ubyte * 3)]

    class v4l2_vp8_entropy_coder_state(Structure):
        pass
    v4l2_vp8_entropy_coder_state._fields_ = [('range', c_ubyte), ('value', c_ubyte), ('bit_count', c_ubyte), ('padding', c_ubyte)]
v4l2_ctrl_vp8_frame._align_ = 8
v4l2_ctrl_vp8_frame._fields_ = [('segment', v4l2_vp8_segment), ('lf', v4l2_vp8_loop_filter), ('quant', v4l2_vp8_quantization), ('entropy', v4l2_vp8_entropy), ('coder_state', v4l2_vp8_entropy_coder_state), ('width', c_ushort), ('height', c_ushort), ('horizontal_scale', c_ubyte), ('vertical_scale', c_ubyte), ('version', c_ubyte), ('prob_skip_false', c_ubyte), ('prob_intra', c_ubyte), ('prob_last', c_ubyte), ('prob_gf', c_ubyte), ('num_dct_parts', c_ubyte), ('first_part_size', c_uint), ('first_part_header_bits', c_uint), ('dct_part_sizes', c_uint * 8), ('last_frame_ts', c_ulong), ('golden_frame_ts', c_ulong), ('alt_frame_ts', c_ulong), ('flags', c_ulong)]

# file /usr/include/linux/v4l2-controls.h, line 2003, column 8

class v4l2_ctrl_mpeg2_sequence(Structure):
    pass
v4l2_ctrl_mpeg2_sequence._align_ = 4
v4l2_ctrl_mpeg2_sequence._fields_ = [('horizontal_size', c_ushort), ('vertical_size', c_ushort), ('vbv_buffer_size', c_uint), ('profile_and_level_indication', c_ushort), ('chroma_format', c_ubyte), ('flags', c_ubyte)]

# file /usr/include/linux/v4l2-controls.h, line 2050, column 8

class v4l2_ctrl_mpeg2_picture(Structure):
    pass
v4l2_ctrl_mpeg2_picture._align_ = 8
v4l2_ctrl_mpeg2_picture._fields_ = [('backward_ref_ts', c_ulong), ('forward_ref_ts', c_ulong), ('flags', c_uint), ('f_code', c_ubyte * 2 * 2), ('picture_coding_type', c_ubyte), ('picture_structure', c_ubyte), ('intra_dc_precision', c_ubyte), ('reserved', c_ubyte * 5)]

# file /usr/include/linux/v4l2-controls.h, line 2083, column 8

class v4l2_ctrl_mpeg2_quantisation(Structure):
    pass
v4l2_ctrl_mpeg2_quantisation._align_ = 1
v4l2_ctrl_mpeg2_quantisation._fields_ = [('intra_quantiser_matrix', c_ubyte * 64), ('non_intra_quantiser_matrix', c_ubyte * 64), ('chroma_intra_quantiser_matrix', c_ubyte * 64), ('chroma_non_intra_quantiser_matrix', c_ubyte * 64)]

# file /usr/include/linux/v4l2-controls.h, line 2185, column 8

class v4l2_ctrl_hevc_sps(Structure):
    pass
v4l2_ctrl_hevc_sps._align_ = 8
v4l2_ctrl_hevc_sps._fields_ = [('video_parameter_set_id', c_ubyte), ('seq_parameter_set_id', c_ubyte), ('pic_width_in_luma_samples', c_ushort), ('pic_height_in_luma_samples', c_ushort), ('bit_depth_luma_minus8', c_ubyte), ('bit_depth_chroma_minus8', c_ubyte), ('log2_max_pic_order_cnt_lsb_minus4', c_ubyte), ('sps_max_dec_pic_buffering_minus1', c_ubyte), ('sps_max_num_reorder_pics', c_ubyte), ('sps_max_latency_increase_plus1', c_ubyte), ('log2_min_luma_coding_block_size_minus3', c_ubyte), ('log2_diff_max_min_luma_coding_block_size', c_ubyte), ('log2_min_luma_transform_block_size_minus2', c_ubyte), ('log2_diff_max_min_luma_transform_block_size', c_ubyte), ('max_transform_hierarchy_depth_inter', c_ubyte), ('max_transform_hierarchy_depth_intra', c_ubyte), ('pcm_sample_bit_depth_luma_minus1', c_ubyte), ('pcm_sample_bit_depth_chroma_minus1', c_ubyte), ('log2_min_pcm_luma_coding_block_size_minus3', c_ubyte), ('log2_diff_max_min_pcm_luma_coding_block_size', c_ubyte), ('num_short_term_ref_pic_sets', c_ubyte), ('num_long_term_ref_pics_sps', c_ubyte), ('chroma_format_idc', c_ubyte), ('sps_max_sub_layers_minus1', c_ubyte), ('reserved', c_ubyte * 6), ('flags', c_ulong)]

# file /usr/include/linux/v4l2-controls.h, line 2274, column 8

class v4l2_ctrl_hevc_pps(Structure):
    pass
v4l2_ctrl_hevc_pps._align_ = 8
v4l2_ctrl_hevc_pps._fields_ = [('pic_parameter_set_id', c_ubyte), ('num_extra_slice_header_bits', c_ubyte), ('num_ref_idx_l0_default_active_minus1', c_ubyte), ('num_ref_idx_l1_default_active_minus1', c_ubyte), ('init_qp_minus26', c_byte), ('diff_cu_qp_delta_depth', c_ubyte), ('pps_cb_qp_offset', c_byte), ('pps_cr_qp_offset', c_byte), ('num_tile_columns_minus1', c_ubyte), ('num_tile_rows_minus1', c_ubyte), ('column_width_minus1', c_ubyte * 20), ('row_height_minus1', c_ubyte * 22), ('pps_beta_offset_div2', c_byte), ('pps_tc_offset_div2', c_byte), ('log2_parallel_merge_level_minus2', c_ubyte), ('reserved', c_ubyte), ('flags', c_ulong)]

# file /usr/include/linux/v4l2-controls.h, line 2321, column 8

class v4l2_hevc_dpb_entry(Structure):
    pass
v4l2_hevc_dpb_entry._align_ = 8
v4l2_hevc_dpb_entry._fields_ = [('timestamp', c_ulong), ('flags', c_ubyte), ('field_pic', c_ubyte), ('reserved', c_ushort), ('pic_order_cnt_val', c_int)]

# file /usr/include/linux/v4l2-controls.h, line 2354, column 8

class v4l2_hevc_pred_weight_table(Structure):
    pass
v4l2_hevc_pred_weight_table._align_ = 1
v4l2_hevc_pred_weight_table._fields_ = [('delta_luma_weight_l0', c_byte * 16), ('luma_offset_l0', c_byte * 16), ('delta_chroma_weight_l0', c_byte * 2 * 16), ('chroma_offset_l0', c_byte * 2 * 16), ('delta_luma_weight_l1', c_byte * 16), ('luma_offset_l1', c_byte * 16), ('delta_chroma_weight_l1', c_byte * 2 * 16), ('chroma_offset_l1', c_byte * 2 * 16), ('luma_log2_weight_denom', c_ubyte), ('delta_chroma_log2_weight_denom', c_byte)]

# file /usr/include/linux/v4l2-controls.h, line 2431, column 8

class v4l2_ctrl_hevc_slice_params(Structure):

    class v4l2_hevc_pred_weight_table(Structure):
        pass
    v4l2_hevc_pred_weight_table._fields_ = [('delta_luma_weight_l0', c_byte * 16), ('luma_offset_l0', c_byte * 16), ('delta_chroma_weight_l0', c_byte * 2 * 16), ('chroma_offset_l0', c_byte * 2 * 16), ('delta_luma_weight_l1', c_byte * 16), ('luma_offset_l1', c_byte * 16), ('delta_chroma_weight_l1', c_byte * 2 * 16), ('chroma_offset_l1', c_byte * 2 * 16), ('luma_log2_weight_denom', c_ubyte), ('delta_chroma_log2_weight_denom', c_byte)]
v4l2_ctrl_hevc_slice_params._align_ = 8
v4l2_ctrl_hevc_slice_params._fields_ = [('bit_size', c_uint), ('data_byte_offset', c_uint), ('num_entry_point_offsets', c_uint), ('nal_unit_type', c_ubyte), ('nuh_temporal_id_plus1', c_ubyte), ('slice_type', c_ubyte), ('colour_plane_id', c_ubyte), ('slice_pic_order_cnt', c_int), ('num_ref_idx_l0_active_minus1', c_ubyte), ('num_ref_idx_l1_active_minus1', c_ubyte), ('collocated_ref_idx', c_ubyte), ('five_minus_max_num_merge_cand', c_ubyte), ('slice_qp_delta', c_byte), ('slice_cb_qp_offset', c_byte), ('slice_cr_qp_offset', c_byte), ('slice_act_y_qp_offset', c_byte), ('slice_act_cb_qp_offset', c_byte), ('slice_act_cr_qp_offset', c_byte), ('slice_beta_offset_div2', c_byte), ('slice_tc_offset_div2', c_byte), ('pic_struct', c_ubyte), ('reserved0', c_ubyte * 3), ('slice_segment_addr', c_uint), ('ref_idx_l0', c_ubyte * 16), ('ref_idx_l1', c_ubyte * 16), ('short_term_ref_pic_set_size', c_ushort), ('long_term_ref_pic_set_size', c_ushort), ('pred_weight_table', v4l2_hevc_pred_weight_table), ('reserved1', c_ubyte * 2), ('flags', c_ulong)]

# file /usr/include/linux/v4l2-controls.h, line 2505, column 8

class v4l2_ctrl_hevc_decode_params(Structure):
    pass
v4l2_ctrl_hevc_decode_params._align_ = 8
v4l2_ctrl_hevc_decode_params._fields_ = [('pic_order_cnt_val', c_int), ('short_term_ref_pic_set_size', c_ushort), ('long_term_ref_pic_set_size', c_ushort), ('num_active_dpb_entries', c_ubyte), ('num_poc_st_curr_before', c_ubyte), ('num_poc_st_curr_after', c_ubyte), ('num_poc_lt_curr', c_ubyte), ('poc_st_curr_before', c_ubyte * 16), ('poc_st_curr_after', c_ubyte * 16), ('poc_lt_curr', c_ubyte * 16), ('num_delta_pocs_of_ref_rps_idx', c_ubyte), ('reserved', c_ubyte * 3), ('dpb', v4l2_hevc_dpb_entry * 16), ('flags', c_ulong)]

# file /usr/include/linux/v4l2-controls.h, line 2544, column 8

class v4l2_ctrl_hevc_scaling_matrix(Structure):
    pass
v4l2_ctrl_hevc_scaling_matrix._align_ = 1
v4l2_ctrl_hevc_scaling_matrix._fields_ = [('scaling_list_4x4', c_ubyte * 16 * 6), ('scaling_list_8x8', c_ubyte * 64 * 6), ('scaling_list_16x16', c_ubyte * 64 * 6), ('scaling_list_32x32', c_ubyte * 64 * 2), ('scaling_list_dc_coef_16x16', c_ubyte * 6), ('scaling_list_dc_coef_32x32', c_ubyte * 2)]

# file /usr/include/linux/v4l2-controls.h, line 2575, column 8

class v4l2_vp9_loop_filter(Structure):
    pass
v4l2_vp9_loop_filter._align_ = 1
v4l2_vp9_loop_filter._fields_ = [('ref_deltas', c_byte * 4), ('mode_deltas', c_byte * 2), ('level', c_ubyte), ('sharpness', c_ubyte), ('flags', c_ubyte), ('reserved', c_ubyte * 7)]

# file /usr/include/linux/v4l2-controls.h, line 2596, column 8

class v4l2_vp9_quantization(Structure):
    pass
v4l2_vp9_quantization._align_ = 1
v4l2_vp9_quantization._fields_ = [('base_q_idx', c_ubyte), ('delta_q_y_dc', c_byte), ('delta_q_uv_dc', c_byte), ('delta_q_uv_ac', c_byte), ('reserved', c_ubyte * 4)]

# file /usr/include/linux/v4l2-controls.h, line 2640, column 8

class v4l2_vp9_segmentation(Structure):
    pass
v4l2_vp9_segmentation._align_ = 2
v4l2_vp9_segmentation._fields_ = [('feature_data', c_short * 4 * 8), ('feature_enabled', c_ubyte * 8), ('tree_probs', c_ubyte * 7), ('pred_probs', c_ubyte * 3), ('flags', c_ubyte), ('reserved', c_ubyte * 5)]

# file /usr/include/linux/v4l2-controls.h, line 2725, column 8

class v4l2_ctrl_vp9_frame(Structure):

    class v4l2_vp9_loop_filter(Structure):
        pass
    v4l2_vp9_loop_filter._fields_ = [('ref_deltas', c_byte * 4), ('mode_deltas', c_byte * 2), ('level', c_ubyte), ('sharpness', c_ubyte), ('flags', c_ubyte), ('reserved', c_ubyte * 7)]

    class v4l2_vp9_quantization(Structure):
        pass
    v4l2_vp9_quantization._fields_ = [('base_q_idx', c_ubyte), ('delta_q_y_dc', c_byte), ('delta_q_uv_dc', c_byte), ('delta_q_uv_ac', c_byte), ('reserved', c_ubyte * 4)]

    class v4l2_vp9_segmentation(Structure):
        pass
    v4l2_vp9_segmentation._fields_ = [('feature_data', c_short * 4 * 8), ('feature_enabled', c_ubyte * 8), ('tree_probs', c_ubyte * 7), ('pred_probs', c_ubyte * 3), ('flags', c_ubyte), ('reserved', c_ubyte * 5)]
v4l2_ctrl_vp9_frame._align_ = 8
v4l2_ctrl_vp9_frame._fields_ = [('lf', v4l2_vp9_loop_filter), ('quant', v4l2_vp9_quantization), ('seg', v4l2_vp9_segmentation), ('flags', c_uint), ('compressed_header_size', c_ushort), ('uncompressed_header_size', c_ushort), ('frame_width_minus_1', c_ushort), ('frame_height_minus_1', c_ushort), ('render_width_minus_1', c_ushort), ('render_height_minus_1', c_ushort), ('last_frame_ts', c_ulong), ('golden_frame_ts', c_ulong), ('alt_frame_ts', c_ulong), ('ref_frame_sign_bias', c_ubyte), ('reset_frame_context', c_ubyte), ('frame_context_idx', c_ubyte), ('profile', c_ubyte), ('bit_depth', c_ubyte), ('interpolation_filter', c_ubyte), ('tile_cols_log2', c_ubyte), ('tile_rows_log2', c_ubyte), ('reference_mode', c_ubyte), ('reserved', c_ubyte * 7)]

# file /usr/include/linux/v4l2-controls.h, line 2769, column 8

class v4l2_vp9_mv_probs(Structure):
    pass
v4l2_vp9_mv_probs._align_ = 1
v4l2_vp9_mv_probs._fields_ = [('joint', c_ubyte * 3), ('sign', c_ubyte * 2), ('classes', c_ubyte * 10 * 2), ('class0_bit', c_ubyte * 2), ('bits', c_ubyte * 10 * 2), ('class0_fr', c_ubyte * 3 * 2 * 2), ('fr', c_ubyte * 3 * 2), ('class0_hp', c_ubyte * 2), ('hp', c_ubyte * 2)]

# file /usr/include/linux/v4l2-controls.h, line 2817, column 8

class v4l2_ctrl_vp9_compressed_hdr(Structure):

    class v4l2_vp9_mv_probs(Structure):
        pass
    v4l2_vp9_mv_probs._fields_ = [('joint', c_ubyte * 3), ('sign', c_ubyte * 2), ('classes', c_ubyte * 10 * 2), ('class0_bit', c_ubyte * 2), ('bits', c_ubyte * 10 * 2), ('class0_fr', c_ubyte * 3 * 2 * 2), ('fr', c_ubyte * 3 * 2), ('class0_hp', c_ubyte * 2), ('hp', c_ubyte * 2)]
v4l2_ctrl_vp9_compressed_hdr._align_ = 1
v4l2_ctrl_vp9_compressed_hdr._fields_ = [('tx_mode', c_ubyte), ('tx8', c_ubyte * 1 * 2), ('tx16', c_ubyte * 2 * 2), ('tx32', c_ubyte * 3 * 2), ('coef', c_ubyte * 3 * 6 * 6 * 2 * 2 * 4), ('skip', c_ubyte * 3), ('inter_mode', c_ubyte * 3 * 7), ('interp_filter', c_ubyte * 2 * 4), ('is_inter', c_ubyte * 4), ('comp_mode', c_ubyte * 5), ('single_ref', c_ubyte * 2 * 5), ('comp_ref', c_ubyte * 5), ('y_mode', c_ubyte * 9 * 4), ('uv_mode', c_ubyte * 9 * 10), ('partition', c_ubyte * 3 * 16), ('mv', v4l2_vp9_mv_probs)]

# file /usr/include/linux/v4l2-controls.h, line 2895, column 8

class v4l2_ctrl_av1_sequence(Structure):
    pass
v4l2_ctrl_av1_sequence._align_ = 4
v4l2_ctrl_av1_sequence._fields_ = [('flags', c_uint), ('seq_profile', c_ubyte), ('order_hint_bits', c_ubyte), ('bit_depth', c_ubyte), ('reserved', c_ubyte), ('max_frame_width_minus_1', c_ushort), ('max_frame_height_minus_1', c_ushort)]

# file /usr/include/linux/v4l2-controls.h, line 2924, column 8

class v4l2_ctrl_av1_tile_group_entry(Structure):
    pass
v4l2_ctrl_av1_tile_group_entry._align_ = 4
v4l2_ctrl_av1_tile_group_entry._fields_ = [('tile_offset', c_uint), ('tile_size', c_uint), ('tile_row', c_uint), ('tile_col', c_uint)]

# file /usr/include/linux/v4l2-controls.h, line 2992, column 8

class v4l2_av1_global_motion(Structure):
    pass
v4l2_av1_global_motion._align_ = 4
v4l2_av1_global_motion._fields_ = [('flags', c_ubyte * 8), ('type', c_uint * 8), ('params', c_int * 6 * 8), ('invalid', c_ubyte), ('reserved', c_ubyte * 3)]

# file /usr/include/linux/v4l2-controls.h, line 3030, column 8

class v4l2_av1_loop_restoration(Structure):
    pass
v4l2_av1_loop_restoration._align_ = 4
v4l2_av1_loop_restoration._fields_ = [('flags', c_ubyte), ('lr_unit_shift', c_ubyte), ('lr_uv_shift', c_ubyte), ('reserved', c_ubyte), ('frame_restoration_type', c_uint * 3), ('loop_restoration_size', c_uint * 3)]

# file /usr/include/linux/v4l2-controls.h, line 3051, column 8

class v4l2_av1_cdef(Structure):
    pass
v4l2_av1_cdef._align_ = 1
v4l2_av1_cdef._fields_ = [('damping_minus_3', c_ubyte), ('bits', c_ubyte), ('y_pri_strength', c_ubyte * 8), ('y_sec_strength', c_ubyte * 8), ('uv_pri_strength', c_ubyte * 8), ('uv_sec_strength', c_ubyte * 8)]

# file /usr/include/linux/v4l2-controls.h, line 3102, column 8

class v4l2_av1_segmentation(Structure):
    pass
v4l2_av1_segmentation._align_ = 2
v4l2_av1_segmentation._fields_ = [('flags', c_ubyte), ('last_active_seg_id', c_ubyte), ('feature_enabled', c_ubyte * 8), ('feature_data', c_short * 8 * 8)]

# file /usr/include/linux/v4l2-controls.h, line 3137, column 8

class v4l2_av1_loop_filter(Structure):
    pass
v4l2_av1_loop_filter._align_ = 1
v4l2_av1_loop_filter._fields_ = [('flags', c_ubyte), ('level', c_ubyte * 4), ('sharpness', c_ubyte), ('ref_deltas', c_byte * 8), ('mode_deltas', c_byte * 2), ('delta_lf_res', c_ubyte)]

# file /usr/include/linux/v4l2-controls.h, line 3171, column 8

class v4l2_av1_quantization(Structure):
    pass
v4l2_av1_quantization._align_ = 1
v4l2_av1_quantization._fields_ = [('flags', c_ubyte), ('base_q_idx', c_ubyte), ('delta_q_y_dc', c_byte), ('delta_q_u_dc', c_byte), ('delta_q_u_ac', c_byte), ('delta_q_v_dc', c_byte), ('delta_q_v_ac', c_byte), ('qm_y', c_ubyte), ('qm_u', c_ubyte), ('qm_v', c_ubyte), ('delta_q_res', c_ubyte)]

# file /usr/include/linux/v4l2-controls.h, line 3207, column 8

class v4l2_av1_tile_info(Structure):
    pass
v4l2_av1_tile_info._align_ = 4
v4l2_av1_tile_info._fields_ = [('flags', c_ubyte), ('context_update_tile_id', c_ubyte), ('tile_cols', c_ubyte), ('tile_rows', c_ubyte), ('mi_col_starts', c_uint * 65), ('mi_row_starts', c_uint * 65), ('width_in_sbs_minus_1', c_uint * 64), ('height_in_sbs_minus_1', c_uint * 64), ('tile_size_bytes', c_ubyte), ('reserved', c_ubyte * 3)]

# file /usr/include/linux/v4l2-controls.h, line 3344, column 8

class v4l2_ctrl_av1_frame(Structure):

    class v4l2_av1_tile_info(Structure):
        pass
    v4l2_av1_tile_info._fields_ = [('flags', c_ubyte), ('context_update_tile_id', c_ubyte), ('tile_cols', c_ubyte), ('tile_rows', c_ubyte), ('mi_col_starts', c_uint * 65), ('mi_row_starts', c_uint * 65), ('width_in_sbs_minus_1', c_uint * 64), ('height_in_sbs_minus_1', c_uint * 64), ('tile_size_bytes', c_ubyte), ('reserved', c_ubyte * 3)]

    class v4l2_av1_quantization(Structure):
        pass
    v4l2_av1_quantization._fields_ = [('flags', c_ubyte), ('base_q_idx', c_ubyte), ('delta_q_y_dc', c_byte), ('delta_q_u_dc', c_byte), ('delta_q_u_ac', c_byte), ('delta_q_v_dc', c_byte), ('delta_q_v_ac', c_byte), ('qm_y', c_ubyte), ('qm_u', c_ubyte), ('qm_v', c_ubyte), ('delta_q_res', c_ubyte)]

    class v4l2_av1_segmentation(Structure):
        pass
    v4l2_av1_segmentation._fields_ = [('flags', c_ubyte), ('last_active_seg_id', c_ubyte), ('feature_enabled', c_ubyte * 8), ('feature_data', c_short * 8 * 8)]

    class v4l2_av1_loop_filter(Structure):
        pass
    v4l2_av1_loop_filter._fields_ = [('flags', c_ubyte), ('level', c_ubyte * 4), ('sharpness', c_ubyte), ('ref_deltas', c_byte * 8), ('mode_deltas', c_byte * 2), ('delta_lf_res', c_ubyte)]

    class v4l2_av1_cdef(Structure):
        pass
    v4l2_av1_cdef._fields_ = [('damping_minus_3', c_ubyte), ('bits', c_ubyte), ('y_pri_strength', c_ubyte * 8), ('y_sec_strength', c_ubyte * 8), ('uv_pri_strength', c_ubyte * 8), ('uv_sec_strength', c_ubyte * 8)]

    class v4l2_av1_loop_restoration(Structure):
        pass
    v4l2_av1_loop_restoration._fields_ = [('flags', c_ubyte), ('lr_unit_shift', c_ubyte), ('lr_uv_shift', c_ubyte), ('reserved', c_ubyte), ('frame_restoration_type', c_uint * 3), ('loop_restoration_size', c_uint * 3)]

    class v4l2_av1_global_motion(Structure):
        pass
    v4l2_av1_global_motion._fields_ = [('flags', c_ubyte * 8), ('type', c_uint * 8), ('params', c_int * 6 * 8), ('invalid', c_ubyte), ('reserved', c_ubyte * 3)]
v4l2_ctrl_av1_frame._align_ = 8
v4l2_ctrl_av1_frame._fields_ = [('tile_info', v4l2_av1_tile_info), ('quantization', v4l2_av1_quantization), ('superres_denom', c_ubyte), ('segmentation', v4l2_av1_segmentation), ('loop_filter', v4l2_av1_loop_filter), ('cdef', v4l2_av1_cdef), ('skip_mode_frame', c_ubyte * 2), ('primary_ref_frame', c_ubyte), ('loop_restoration', v4l2_av1_loop_restoration), ('global_motion', v4l2_av1_global_motion), ('flags', c_uint), ('frame_type', c_uint), ('order_hint', c_uint), ('upscaled_width', c_uint), ('interpolation_filter', c_uint), ('tx_mode', c_uint), ('frame_width_minus_1', c_uint), ('frame_height_minus_1', c_uint), ('render_width_minus_1', c_ushort), ('render_height_minus_1', c_ushort), ('current_frame_id', c_uint), ('buffer_removal_time', c_uint * 32), ('reserved', c_ubyte * 4), ('order_hints', c_uint * 8), ('reference_frame_ts', c_ulong * 8), ('ref_frame_idx', c_byte * 7), ('refresh_frame_flags', c_ubyte)]

# file /usr/include/linux/v4l2-controls.h, line 3447, column 8

class v4l2_ctrl_av1_film_grain(Structure):
    pass
v4l2_ctrl_av1_film_grain._align_ = 2
v4l2_ctrl_av1_film_grain._fields_ = [('flags', c_ubyte), ('cr_mult', c_ubyte), ('grain_seed', c_ushort), ('film_grain_params_ref_idx', c_ubyte), ('num_y_points', c_ubyte), ('point_y_value', c_ubyte * 16), ('point_y_scaling', c_ubyte * 16), ('num_cb_points', c_ubyte), ('point_cb_value', c_ubyte * 16), ('point_cb_scaling', c_ubyte * 16), ('num_cr_points', c_ubyte), ('point_cr_value', c_ubyte * 16), ('point_cr_scaling', c_ubyte * 16), ('grain_scaling_minus_8', c_ubyte), ('ar_coeff_lag', c_ubyte), ('ar_coeffs_y_plus_128', c_ubyte * 25), ('ar_coeffs_cb_plus_128', c_ubyte * 25), ('ar_coeffs_cr_plus_128', c_ubyte * 25), ('ar_coeff_shift_minus_6', c_ubyte), ('grain_scale_shift', c_ubyte), ('cb_mult', c_ubyte), ('cb_luma_mult', c_ubyte), ('cr_luma_mult', c_ubyte), ('cb_offset', c_ushort), ('cr_offset', c_ushort), ('reserved', c_ubyte * 4)]

# file /usr/include/linux/v4l2-controls.h, line 3488, column 8

class v4l2_ctrl_hdr10_cll_info(Structure):
    pass
v4l2_ctrl_hdr10_cll_info._align_ = 2
v4l2_ctrl_hdr10_cll_info._fields_ = [('max_content_light_level', c_ushort), ('max_pic_average_light_level', c_ushort)]

# file /usr/include/linux/v4l2-controls.h, line 3508, column 8

class v4l2_ctrl_hdr10_mastering_display(Structure):
    pass
v4l2_ctrl_hdr10_mastering_display._align_ = 4
v4l2_ctrl_hdr10_mastering_display._fields_ = [('display_primaries_x', c_ushort * 3), ('display_primaries_y', c_ushort * 3), ('white_point_x', c_ushort), ('white_point_y', c_ushort), ('max_display_mastering_luminance', c_uint), ('min_display_mastering_luminance', c_uint)]

# file /usr/include/linux/videodev2.h, line 415, column 8

class v4l2_rect(Structure):
    pass
v4l2_rect._align_ = 4
v4l2_rect._fields_ = [('left', c_int), ('top', c_int), ('width', c_uint), ('height', c_uint)]

# file /usr/include/linux/videodev2.h, line 422, column 8

class v4l2_fract(Structure):
    pass
v4l2_fract._align_ = 4
v4l2_fract._fields_ = [('numerator', c_uint), ('denominator', c_uint)]

# file /usr/include/linux/videodev2.h, line 427, column 8

class v4l2_area(Structure):
    pass
v4l2_area._align_ = 4
v4l2_area._fields_ = [('width', c_uint), ('height', c_uint)]

# file /usr/include/linux/videodev2.h, line 443, column 8

class v4l2_capability(Structure):
    pass
v4l2_capability._align_ = 4
v4l2_capability._fields_ = [('driver', c_ubyte * 16), ('card', c_ubyte * 32), ('bus_info', c_ubyte * 32), ('version', c_uint), ('capabilities', c_uint), ('device_caps', c_uint), ('reserved', c_uint * 3)]

# file /usr/include/linux/videodev2.h, line 499, column 8

class v4l2_pix_format(Structure):
    pass
v4l2_pix_format._align_ = 4
v4l2_pix_format._fields_ = [('width', c_uint), ('height', c_uint), ('pixelformat', c_uint), ('field', c_uint), ('bytesperline', c_uint), ('sizeimage', c_uint), ('colorspace', c_uint), ('priv', c_uint), ('flags', c_uint), ('quantization', c_uint), ('xfer_func', c_uint)]

# file /usr/include/linux/videodev2.h, line 875, column 8

class v4l2_fmtdesc(Structure):
    pass
v4l2_fmtdesc._align_ = 4
v4l2_fmtdesc._fields_ = [('index', c_uint), ('type', c_uint), ('flags', c_uint), ('description', c_ubyte * 32), ('pixelformat', c_uint), ('mbus_code', c_uint), ('reserved', c_uint * 3)]

# file /usr/include/linux/videodev2.h, line 910, column 8

class v4l2_frmsize_discrete(Structure):
    pass
v4l2_frmsize_discrete._align_ = 4
v4l2_frmsize_discrete._fields_ = [('width', c_uint), ('height', c_uint)]

# file /usr/include/linux/videodev2.h, line 915, column 8

class v4l2_frmsize_stepwise(Structure):
    pass
v4l2_frmsize_stepwise._align_ = 4
v4l2_frmsize_stepwise._fields_ = [('min_width', c_uint), ('max_width', c_uint), ('step_width', c_uint), ('min_height', c_uint), ('max_height', c_uint), ('step_height', c_uint)]

# file /usr/include/linux/videodev2.h, line 924, column 8

class v4l2_frmsizeenum(Structure):
    pass
v4l2_frmsizeenum._align_ = 4
v4l2_frmsizeenum._fields_ = [('index', c_uint), ('pixel_format', c_uint), ('type', c_uint), ('reserved', c_uint * 2)]

# file /usr/include/linux/videodev2.h, line 946, column 8

class v4l2_frmival_stepwise(Structure):

    class v4l2_fract(Structure):
        pass
    v4l2_fract._fields_ = [('numerator', c_uint), ('denominator', c_uint)]

    class v4l2_fract(Structure):
        pass
    v4l2_fract._fields_ = [('numerator', c_uint), ('denominator', c_uint)]

    class v4l2_fract(Structure):
        pass
    v4l2_fract._fields_ = [('numerator', c_uint), ('denominator', c_uint)]
v4l2_frmival_stepwise._align_ = 4
v4l2_frmival_stepwise._fields_ = [('min', v4l2_fract), ('max', v4l2_fract), ('step', v4l2_fract)]

# file /usr/include/linux/videodev2.h, line 952, column 8

class v4l2_frmivalenum(Structure):
    pass
v4l2_frmivalenum._align_ = 4
v4l2_frmivalenum._fields_ = [('index', c_uint), ('pixel_format', c_uint), ('width', c_uint), ('height', c_uint), ('type', c_uint), ('reserved', c_uint * 2)]

# file /usr/include/linux/videodev2.h, line 970, column 8

class v4l2_timecode(Structure):
    pass
v4l2_timecode._align_ = 4
v4l2_timecode._fields_ = [('type', c_uint), ('flags', c_uint), ('frames', c_ubyte), ('seconds', c_ubyte), ('minutes', c_ubyte), ('hours', c_ubyte), ('userbits', c_ubyte * 4)]

# file /usr/include/linux/videodev2.h, line 995, column 8

class v4l2_jpegcompression(Structure):
    pass
v4l2_jpegcompression._align_ = 4
v4l2_jpegcompression._fields_ = [('quality', c_int), ('APPn', c_int), ('APP_len', c_int), ('APP_data', c_char * 60), ('COM_len', c_int), ('COM_data', c_char * 60), ('jpeg_markers', c_uint)]

# file /usr/include/linux/videodev2.h, line 1029, column 8

class v4l2_requestbuffers(Structure):
    pass
v4l2_requestbuffers._align_ = 4
v4l2_requestbuffers._fields_ = [('count', c_uint), ('type', c_uint), ('memory', c_uint), ('capabilities', c_uint), ('flags', c_ubyte), ('reserved', c_ubyte * 3)]

# file /usr/include/linux/videodev2.h, line 1073, column 8

class v4l2_plane(Structure):

    class _usr_include_linux_videodev2_h_1076_2_(Union):
        pass
    _usr_include_linux_videodev2_h_1076_2_._fields_ = [('mem_offset', c_uint), ('userptr', c_ulong), ('fd', c_int)]
v4l2_plane._align_ = 8
v4l2_plane._fields_ = [('bytesused', c_uint), ('length', c_uint), ('m', _usr_include_linux_videodev2_h_1076_2_), ('data_offset', c_uint), ('reserved', c_uint * 11)]

# file /usr/include/linux/videodev2.h, line 1120, column 8

class v4l2_buffer(Structure):

    class timeval(Structure):
        pass
    timeval._fields_ = [('tv_sec', c_long), ('tv_usec', c_long)]

    class v4l2_timecode(Structure):
        pass
    v4l2_timecode._fields_ = [('type', c_uint), ('flags', c_uint), ('frames', c_ubyte), ('seconds', c_ubyte), ('minutes', c_ubyte), ('hours', c_ubyte), ('userbits', c_ubyte * 4)]

    class _usr_include_linux_videodev2_h_1132_2_(Union):

        class v4l2_plane(Structure):

            class _usr_include_linux_videodev2_h_1076_2_(Union):
                pass
            _usr_include_linux_videodev2_h_1076_2_._fields_ = [('mem_offset', c_uint), ('userptr', c_ulong), ('fd', c_int)]
        v4l2_plane._fields_ = [('bytesused', c_uint), ('length', c_uint), ('m', _usr_include_linux_videodev2_h_1076_2_), ('data_offset', c_uint), ('reserved', c_uint * 11)]
    _usr_include_linux_videodev2_h_1132_2_._fields_ = [('offset', c_uint), ('userptr', c_ulong), ('planes', POINTER(v4l2_plane)), ('fd', c_int)]
v4l2_buffer._align_ = 8
v4l2_buffer._fields_ = [('index', c_uint), ('type', c_uint), ('bytesused', c_uint), ('flags', c_uint), ('field', c_uint), ('timestamp', timeval), ('timecode', v4l2_timecode), ('sequence', c_uint), ('memory', c_uint), ('m', _usr_include_linux_videodev2_h_1132_2_), ('length', c_uint), ('reserved2', c_uint)]

# file /usr/include/linux/videodev2.h, line 1153, column 25
DUMMYLIB_so.v4l2_timeval_to_ns.argtypes = [POINTER(timeval)]
DUMMYLIB_so.v4l2_timeval_to_ns.restype = c_ulong

# file /usr/include/linux/videodev2.h, line 1217, column 8

class v4l2_exportbuffer(Structure):
    pass
v4l2_exportbuffer._align_ = 4
v4l2_exportbuffer._fields_ = [('type', c_uint), ('index', c_uint), ('plane', c_uint), ('flags', c_uint), ('fd', c_int), ('reserved', c_uint * 11)]

# file /usr/include/linux/videodev2.h, line 1229, column 8

class v4l2_framebuffer(Structure):

    class _usr_include_linux_videodev2_h_1235_2_(Structure):
        pass
    _usr_include_linux_videodev2_h_1235_2_._fields_ = [('width', c_uint), ('height', c_uint), ('pixelformat', c_uint), ('field', c_uint), ('bytesperline', c_uint), ('sizeimage', c_uint), ('colorspace', c_uint), ('priv', c_uint)]
v4l2_framebuffer._align_ = 8
v4l2_framebuffer._fields_ = [('capability', c_uint), ('flags', c_uint), ('base', POINTER(None)), ('fmt', _usr_include_linux_videodev2_h_1235_2_)]

# file /usr/include/linux/videodev2.h, line 1264, column 8

class v4l2_clip(Structure):

    class v4l2_rect(Structure):
        pass
    v4l2_rect._fields_ = [('left', c_int), ('top', c_int), ('width', c_uint), ('height', c_uint)]
v4l2_clip._align_ = 8
v4l2_clip._fields_ = [('c', v4l2_rect), ('next', POINTER(v4l2_clip))]

# file /usr/include/linux/videodev2.h, line 1269, column 8

class v4l2_window(Structure):

    class v4l2_rect(Structure):
        pass
    v4l2_rect._fields_ = [('left', c_int), ('top', c_int), ('width', c_uint), ('height', c_uint)]

    class v4l2_clip(Structure):

        class v4l2_rect(Structure):
            pass
        v4l2_rect._fields_ = [('left', c_int), ('top', c_int), ('width', c_uint), ('height', c_uint)]
    v4l2_clip._fields_ = [('c', v4l2_rect), ('next', POINTER(v4l2_clip))]
v4l2_window._align_ = 8
v4l2_window._fields_ = [('w', v4l2_rect), ('field', c_uint), ('chromakey', c_uint), ('clips', POINTER(v4l2_clip)), ('clipcount', c_uint), ('bitmap', POINTER(None)), ('global_alpha', c_ubyte)]

# file /usr/include/linux/videodev2.h, line 1282, column 8

class v4l2_captureparm(Structure):

    class v4l2_fract(Structure):
        pass
    v4l2_fract._fields_ = [('numerator', c_uint), ('denominator', c_uint)]
v4l2_captureparm._align_ = 4
v4l2_captureparm._fields_ = [('capability', c_uint), ('capturemode', c_uint), ('timeperframe', v4l2_fract), ('extendedmode', c_uint), ('readbuffers', c_uint), ('reserved', c_uint * 4)]

# file /usr/include/linux/videodev2.h, line 1295, column 8

class v4l2_outputparm(Structure):

    class v4l2_fract(Structure):
        pass
    v4l2_fract._fields_ = [('numerator', c_uint), ('denominator', c_uint)]
v4l2_outputparm._align_ = 4
v4l2_outputparm._fields_ = [('capability', c_uint), ('outputmode', c_uint), ('timeperframe', v4l2_fract), ('extendedmode', c_uint), ('writebuffers', c_uint), ('reserved', c_uint * 4)]

# file /usr/include/linux/videodev2.h, line 1307, column 8

class v4l2_cropcap(Structure):

    class v4l2_rect(Structure):
        pass
    v4l2_rect._fields_ = [('left', c_int), ('top', c_int), ('width', c_uint), ('height', c_uint)]

    class v4l2_rect(Structure):
        pass
    v4l2_rect._fields_ = [('left', c_int), ('top', c_int), ('width', c_uint), ('height', c_uint)]

    class v4l2_fract(Structure):
        pass
    v4l2_fract._fields_ = [('numerator', c_uint), ('denominator', c_uint)]
v4l2_cropcap._align_ = 4
v4l2_cropcap._fields_ = [('type', c_uint), ('bounds', v4l2_rect), ('defrect', v4l2_rect), ('pixelaspect', v4l2_fract)]

# file /usr/include/linux/videodev2.h, line 1314, column 8

class v4l2_crop(Structure):

    class v4l2_rect(Structure):
        pass
    v4l2_rect._fields_ = [('left', c_int), ('top', c_int), ('width', c_uint), ('height', c_uint)]
v4l2_crop._align_ = 4
v4l2_crop._fields_ = [('type', c_uint), ('c', v4l2_rect)]

# file /usr/include/linux/videodev2.h, line 1332, column 8

class v4l2_selection(Structure):

    class v4l2_rect(Structure):
        pass
    v4l2_rect._fields_ = [('left', c_int), ('top', c_int), ('width', c_uint), ('height', c_uint)]
v4l2_selection._align_ = 4
v4l2_selection._fields_ = [('type', c_uint), ('target', c_uint), ('flags', c_uint), ('r', v4l2_rect), ('reserved', c_uint * 9)]

# file /usr/include/linux/videodev2.h, line 1345, column 15
v4l2_std_id = c_ulong

# file /usr/include/linux/videodev2.h, line 1477, column 8

class v4l2_standard(Structure):

    class v4l2_fract(Structure):
        pass
    v4l2_fract._fields_ = [('numerator', c_uint), ('denominator', c_uint)]
v4l2_standard._align_ = 8
v4l2_standard._fields_ = [('index', c_uint), ('id', c_ulong), ('name', c_ubyte * 24), ('frameperiod', v4l2_fract), ('framelines', c_uint), ('reserved', c_uint * 4)]

# file /usr/include/linux/videodev2.h, line 1525, column 8

class v4l2_bt_timings(Structure):

    class v4l2_fract(Structure):
        pass
    v4l2_fract._fields_ = [('numerator', c_uint), ('denominator', c_uint)]
v4l2_bt_timings._align_ = 1
v4l2_bt_timings._fields_ = [('width', c_uint), ('height', c_uint), ('interlaced', c_uint), ('polarities', c_uint), ('pixelclock', c_ulong), ('hfrontporch', c_uint), ('hsync', c_uint), ('hbackporch', c_uint), ('vfrontporch', c_uint), ('vsync', c_uint), ('vbackporch', c_uint), ('il_vfrontporch', c_uint), ('il_vsync', c_uint), ('il_vbackporch', c_uint), ('standards', c_uint), ('flags', c_uint), ('picture_aspect', v4l2_fract), ('cea861_vic', c_ubyte), ('hdmi_vic', c_ubyte), ('reserved', c_ubyte * 46)]

# file /usr/include/linux/videodev2.h, line 1649, column 8

class v4l2_dv_timings(Structure):
    pass
v4l2_dv_timings._align_ = 1
v4l2_dv_timings._fields_ = [('type', c_uint)]

# file /usr/include/linux/videodev2.h, line 1668, column 8

class v4l2_enum_dv_timings(Structure):

    class v4l2_dv_timings(Structure):

        class _usr_include_linux_videodev2_h_1651_2_(Union):
            pass
        _usr_include_linux_videodev2_h_1651_2_._align_ = 4
        _usr_include_linux_videodev2_h_1651_2_._fields_ = []
    v4l2_dv_timings._fields_ = [('type', c_uint), ('union v4l2_dv_timings::(anonymous at /usr/include/linux/videodev2.h:1651:2)', _usr_include_linux_videodev2_h_1651_2_)]
v4l2_enum_dv_timings._align_ = 4
v4l2_enum_dv_timings._fields_ = [('index', c_uint), ('pad', c_uint), ('reserved', c_uint * 2), ('timings', v4l2_dv_timings)]

# file /usr/include/linux/videodev2.h, line 1686, column 8

class v4l2_bt_timings_cap(Structure):
    pass
v4l2_bt_timings_cap._align_ = 1
v4l2_bt_timings_cap._fields_ = [('min_width', c_uint), ('max_width', c_uint), ('min_height', c_uint), ('max_height', c_uint), ('min_pixelclock', c_ulong), ('max_pixelclock', c_ulong), ('standards', c_uint), ('capabilities', c_uint), ('reserved', c_uint * 16)]

# file /usr/include/linux/videodev2.h, line 1713, column 8

class v4l2_dv_timings_cap(Structure):
    pass
v4l2_dv_timings_cap._align_ = 4
v4l2_dv_timings_cap._fields_ = [('type', c_uint), ('pad', c_uint), ('reserved', c_uint * 2)]

# file /usr/include/linux/videodev2.h, line 1727, column 8

class v4l2_input(Structure):
    pass
v4l2_input._align_ = 8
v4l2_input._fields_ = [('index', c_uint), ('name', c_ubyte * 32), ('type', c_uint), ('audioset', c_uint), ('tuner', c_uint), ('std', c_ulong), ('status', c_uint), ('capabilities', c_uint), ('reserved', c_uint * 3)]

# file /usr/include/linux/videodev2.h, line 1779, column 8

class v4l2_output(Structure):
    pass
v4l2_output._align_ = 8
v4l2_output._fields_ = [('index', c_uint), ('name', c_ubyte * 32), ('type', c_uint), ('audioset', c_uint), ('modulator', c_uint), ('std', c_ulong), ('capabilities', c_uint), ('reserved', c_uint * 3)]

# file /usr/include/linux/videodev2.h, line 1803, column 8

class v4l2_control(Structure):
    pass
v4l2_control._align_ = 4
v4l2_control._fields_ = [('id', c_uint), ('value', c_int)]

# file /usr/include/linux/videodev2.h, line 1808, column 8

class v4l2_ext_control(Structure):
    pass
v4l2_ext_control._align_ = 1
v4l2_ext_control._fields_ = [('id', c_uint), ('size', c_uint), ('reserved2', c_uint * 1)]

# file /usr/include/linux/videodev2.h, line 1851, column 8

class v4l2_ext_controls(Structure):

    class v4l2_ext_control(Structure):

        class _usr_include_linux_videodev2_h_1812_2_(Union):
            pass
        _usr_include_linux_videodev2_h_1812_2_._align_ = 1
        _usr_include_linux_videodev2_h_1812_2_._fields_ = []
    v4l2_ext_control._fields_ = [('id', c_uint), ('size', c_uint), ('reserved2', c_uint * 1), ('union v4l2_ext_control::(anonymous at /usr/include/linux/videodev2.h:1812:2)', _usr_include_linux_videodev2_h_1812_2_)]
v4l2_ext_controls._align_ = 8
v4l2_ext_controls._fields_ = [('count', c_uint), ('error_idx', c_uint), ('request_fd', c_int), ('reserved', c_uint * 1), ('controls', POINTER(v4l2_ext_control))]

# file /usr/include/linux/videodev2.h, line 1927, column 8

class v4l2_queryctrl(Structure):
    pass
v4l2_queryctrl._align_ = 4
v4l2_queryctrl._fields_ = [('id', c_uint), ('type', c_uint), ('name', c_ubyte * 32), ('minimum', c_int), ('maximum', c_int), ('step', c_int), ('default_value', c_int), ('flags', c_uint), ('reserved', c_uint * 2)]

# file /usr/include/linux/videodev2.h, line 1940, column 8

class v4l2_query_ext_ctrl(Structure):
    pass
v4l2_query_ext_ctrl._align_ = 8
v4l2_query_ext_ctrl._fields_ = [('id', c_uint), ('type', c_uint), ('name', c_char * 32), ('minimum', c_long), ('maximum', c_long), ('step', c_ulong), ('default_value', c_long), ('flags', c_uint), ('elem_size', c_uint), ('elems', c_uint), ('nr_of_dims', c_uint), ('dims', c_uint * 4), ('reserved', c_uint * 32)]

# file /usr/include/linux/videodev2.h, line 1957, column 8

class v4l2_querymenu(Structure):
    pass
v4l2_querymenu._align_ = 1
v4l2_querymenu._fields_ = [('id', c_uint), ('index', c_uint), ('reserved', c_uint)]

# file /usr/include/linux/videodev2.h, line 1995, column 8

class v4l2_tuner(Structure):
    pass
v4l2_tuner._align_ = 4
v4l2_tuner._fields_ = [('index', c_uint), ('name', c_ubyte * 32), ('type', c_uint), ('capability', c_uint), ('rangelow', c_uint), ('rangehigh', c_uint), ('rxsubchans', c_uint), ('audmode', c_uint), ('signal', c_int), ('afc', c_int), ('reserved', c_uint * 4)]

# file /usr/include/linux/videodev2.h, line 2009, column 8

class v4l2_modulator(Structure):
    pass
v4l2_modulator._align_ = 4
v4l2_modulator._fields_ = [('index', c_uint), ('name', c_ubyte * 32), ('capability', c_uint), ('rangelow', c_uint), ('rangehigh', c_uint), ('txsubchans', c_uint), ('type', c_uint), ('reserved', c_uint * 3)]

# file /usr/include/linux/videodev2.h, line 2052, column 8

class v4l2_frequency(Structure):
    pass
v4l2_frequency._align_ = 4
v4l2_frequency._fields_ = [('tuner', c_uint), ('type', c_uint), ('frequency', c_uint), ('reserved', c_uint * 8)]

# file /usr/include/linux/videodev2.h, line 2063, column 8

class v4l2_frequency_band(Structure):
    pass
v4l2_frequency_band._align_ = 4
v4l2_frequency_band._fields_ = [('tuner', c_uint), ('type', c_uint), ('index', c_uint), ('capability', c_uint), ('rangelow', c_uint), ('rangehigh', c_uint), ('modulation', c_uint), ('reserved', c_uint * 9)]

# file /usr/include/linux/videodev2.h, line 2074, column 8

class v4l2_hw_freq_seek(Structure):
    pass
v4l2_hw_freq_seek._align_ = 4
v4l2_hw_freq_seek._fields_ = [('tuner', c_uint), ('type', c_uint), ('seek_upward', c_uint), ('wrap_around', c_uint), ('spacing', c_uint), ('rangelow', c_uint), ('rangehigh', c_uint), ('reserved', c_uint * 5)]

# file /usr/include/linux/videodev2.h, line 2089, column 8

class v4l2_rds_data(Structure):
    pass
v4l2_rds_data._align_ = 1
v4l2_rds_data._fields_ = [('lsb', c_ubyte), ('msb', c_ubyte), ('block', c_ubyte)]

# file /usr/include/linux/videodev2.h, line 2109, column 8

class v4l2_audio(Structure):
    pass
v4l2_audio._align_ = 4
v4l2_audio._fields_ = [('index', c_uint), ('name', c_ubyte * 32), ('capability', c_uint), ('mode', c_uint), ('reserved', c_uint * 2)]

# file /usr/include/linux/videodev2.h, line 2124, column 8

class v4l2_audioout(Structure):
    pass
v4l2_audioout._align_ = 4
v4l2_audioout._fields_ = [('index', c_uint), ('name', c_ubyte * 32), ('capability', c_uint), ('mode', c_uint), ('reserved', c_uint * 2)]

# file /usr/include/linux/videodev2.h, line 2141, column 8

class v4l2_enc_idx_entry(Structure):
    pass
v4l2_enc_idx_entry._align_ = 8
v4l2_enc_idx_entry._fields_ = [('offset', c_ulong), ('pts', c_ulong), ('length', c_uint), ('flags', c_uint), ('reserved', c_uint * 2)]

# file /usr/include/linux/videodev2.h, line 2150, column 8

class v4l2_enc_idx(Structure):
    pass
v4l2_enc_idx._align_ = 8
v4l2_enc_idx._fields_ = [('entries', c_uint), ('entries_cap', c_uint), ('reserved', c_uint * 4), ('entry', v4l2_enc_idx_entry * 64)]

# file /usr/include/linux/videodev2.h, line 2166, column 8

class v4l2_encoder_cmd(Structure):
    pass
v4l2_encoder_cmd._align_ = 4
v4l2_encoder_cmd._fields_ = [('cmd', c_uint), ('flags', c_uint)]

# file /usr/include/linux/videodev2.h, line 2202, column 8

class v4l2_decoder_cmd(Structure):
    pass
v4l2_decoder_cmd._align_ = 8
v4l2_decoder_cmd._fields_ = [('cmd', c_uint), ('flags', c_uint)]

# file /usr/include/linux/videodev2.h, line 2235, column 8

class v4l2_vbi_format(Structure):
    pass
v4l2_vbi_format._align_ = 4
v4l2_vbi_format._fields_ = [('sampling_rate', c_uint), ('offset', c_uint), ('samples_per_line', c_uint), ('sample_format', c_uint), ('start', c_int * 2), ('count', c_uint * 2), ('flags', c_uint), ('reserved', c_uint * 2)]

# file /usr/include/linux/videodev2.h, line 2263, column 8

class v4l2_sliced_vbi_format(Structure):
    pass
v4l2_sliced_vbi_format._align_ = 4
v4l2_sliced_vbi_format._fields_ = [('service_set', c_ushort), ('service_lines', c_ushort * 24 * 2), ('io_size', c_uint), ('reserved', c_uint * 2)]

# file /usr/include/linux/videodev2.h, line 2287, column 8

class v4l2_sliced_vbi_cap(Structure):
    pass
v4l2_sliced_vbi_cap._align_ = 4
v4l2_sliced_vbi_cap._fields_ = [('service_set', c_ushort), ('service_lines', c_ushort * 24 * 2), ('type', c_uint), ('reserved', c_uint * 3)]

# file /usr/include/linux/videodev2.h, line 2298, column 8

class v4l2_sliced_vbi_data(Structure):
    pass
v4l2_sliced_vbi_data._align_ = 4
v4l2_sliced_vbi_data._fields_ = [('id', c_uint), ('field', c_uint), ('line', c_uint), ('reserved', c_uint), ('data', c_ubyte * 48)]

# file /usr/include/linux/videodev2.h, line 2328, column 8

class v4l2_mpeg_vbi_itv0_line(Structure):
    pass
v4l2_mpeg_vbi_itv0_line._align_ = 1
v4l2_mpeg_vbi_itv0_line._fields_ = [('id', c_ubyte), ('data', c_ubyte * 42)]

# file /usr/include/linux/videodev2.h, line 2333, column 8

class v4l2_mpeg_vbi_itv0(Structure):
    pass
v4l2_mpeg_vbi_itv0._align_ = 1
v4l2_mpeg_vbi_itv0._fields_ = [('linemask', c_uint * 2), ('line', v4l2_mpeg_vbi_itv0_line * 35)]

# file /usr/include/linux/videodev2.h, line 2338, column 8

class v4l2_mpeg_vbi_ITV0(Structure):
    pass
v4l2_mpeg_vbi_ITV0._align_ = 1
v4l2_mpeg_vbi_ITV0._fields_ = [('line', v4l2_mpeg_vbi_itv0_line * 36)]

# file /usr/include/linux/videodev2.h, line 2345, column 8

class v4l2_mpeg_vbi_fmt_ivtv(Structure):
    pass
v4l2_mpeg_vbi_fmt_ivtv._align_ = 1
v4l2_mpeg_vbi_fmt_ivtv._fields_ = [('magic', c_ubyte * 4)]

# file /usr/include/linux/videodev2.h, line 2365, column 8

class v4l2_plane_pix_format(Structure):
    pass
v4l2_plane_pix_format._align_ = 1
v4l2_plane_pix_format._fields_ = [('sizeimage', c_uint), ('bytesperline', c_uint), ('reserved', c_ushort * 6)]

# file /usr/include/linux/videodev2.h, line 2387, column 8

class v4l2_pix_format_mplane(Structure):
    pass
v4l2_pix_format_mplane._align_ = 1
v4l2_pix_format_mplane._fields_ = [('width', c_uint), ('height', c_uint), ('pixelformat', c_uint), ('field', c_uint), ('colorspace', c_uint), ('plane_fmt', v4l2_plane_pix_format * 8), ('num_planes', c_ubyte), ('flags', c_ubyte), ('quantization', c_ubyte), ('xfer_func', c_ubyte), ('reserved', c_ubyte * 7)]

# file /usr/include/linux/videodev2.h, line 2412, column 8

class v4l2_sdr_format(Structure):
    pass
v4l2_sdr_format._align_ = 1
v4l2_sdr_format._fields_ = [('pixelformat', c_uint), ('buffersize', c_uint), ('reserved', c_ubyte * 24)]

# file /usr/include/linux/videodev2.h, line 2429, column 8

class v4l2_meta_format(Structure):
    pass
v4l2_meta_format._align_ = 1
v4l2_meta_format._fields_ = [('dataformat', c_uint), ('buffersize', c_uint), ('width', c_uint), ('height', c_uint), ('bytesperline', c_uint)]

# file /usr/include/linux/videodev2.h, line 2449, column 8

class v4l2_format(Structure):

    class _usr_include_linux_videodev2_h_2451_2_(Union):

        class v4l2_pix_format(Structure):

            class _usr_include_linux_videodev2_h_509_2_(Union):
                pass
            _usr_include_linux_videodev2_h_509_2_._align_ = 4
            _usr_include_linux_videodev2_h_509_2_._fields_ = []
        v4l2_pix_format._fields_ = [('width', c_uint), ('height', c_uint), ('pixelformat', c_uint), ('field', c_uint), ('bytesperline', c_uint), ('sizeimage', c_uint), ('colorspace', c_uint), ('priv', c_uint), ('flags', c_uint), ('union v4l2_pix_format::(anonymous at /usr/include/linux/videodev2.h:509:2)', _usr_include_linux_videodev2_h_509_2_), ('quantization', c_uint), ('xfer_func', c_uint)]

        class v4l2_pix_format_mplane(Structure):

            class _usr_include_linux_videodev2_h_2397_3_(Union):
                pass
            _usr_include_linux_videodev2_h_2397_3_._align_ = 1
            _usr_include_linux_videodev2_h_2397_3_._fields_ = []
        v4l2_pix_format_mplane._fields_ = [('width', c_uint), ('height', c_uint), ('pixelformat', c_uint), ('field', c_uint), ('colorspace', c_uint), ('plane_fmt', v4l2_plane_pix_format * 8), ('num_planes', c_ubyte), ('flags', c_ubyte), ('union v4l2_pix_format_mplane::(anonymous at /usr/include/linux/videodev2.h:2397:3)', _usr_include_linux_videodev2_h_2397_3_), ('quantization', c_ubyte), ('xfer_func', c_ubyte), ('reserved', c_ubyte * 7)]

        class v4l2_window(Structure):

            class v4l2_rect(Structure):
                pass
            v4l2_rect._fields_ = [('left', c_int), ('top', c_int), ('width', c_uint), ('height', c_uint)]

            class v4l2_clip(Structure):

                class v4l2_rect(Structure):
                    pass
                v4l2_rect._fields_ = [('left', c_int), ('top', c_int), ('width', c_uint), ('height', c_uint)]
            v4l2_clip._fields_ = [('c', v4l2_rect), ('next', POINTER(v4l2_clip))]
        v4l2_window._fields_ = [('w', v4l2_rect), ('field', c_uint), ('chromakey', c_uint), ('clips', POINTER(v4l2_clip)), ('clipcount', c_uint), ('bitmap', POINTER(None)), ('global_alpha', c_ubyte)]

        class v4l2_vbi_format(Structure):
            pass
        v4l2_vbi_format._fields_ = [('sampling_rate', c_uint), ('offset', c_uint), ('samples_per_line', c_uint), ('sample_format', c_uint), ('start', c_int * 2), ('count', c_uint * 2), ('flags', c_uint), ('reserved', c_uint * 2)]

        class v4l2_sliced_vbi_format(Structure):
            pass
        v4l2_sliced_vbi_format._fields_ = [('service_set', c_ushort), ('service_lines', c_ushort * 24 * 2), ('io_size', c_uint), ('reserved', c_uint * 2)]

        class v4l2_sdr_format(Structure):
            pass
        v4l2_sdr_format._fields_ = [('pixelformat', c_uint), ('buffersize', c_uint), ('reserved', c_ubyte * 24)]

        class v4l2_meta_format(Structure):
            pass
        v4l2_meta_format._fields_ = [('dataformat', c_uint), ('buffersize', c_uint), ('width', c_uint), ('height', c_uint), ('bytesperline', c_uint)]
    _usr_include_linux_videodev2_h_2451_2_._fields_ = [('pix', v4l2_pix_format), ('pix_mp', v4l2_pix_format_mplane), ('win', v4l2_window), ('vbi', v4l2_vbi_format), ('sliced', v4l2_sliced_vbi_format), ('sdr', v4l2_sdr_format), ('meta', v4l2_meta_format), ('raw_data', c_ubyte * 200)]
v4l2_format._align_ = 8
v4l2_format._fields_ = [('type', c_uint), ('fmt', _usr_include_linux_videodev2_h_2451_2_)]

# file /usr/include/linux/videodev2.h, line 2465, column 8

class v4l2_streamparm(Structure):

    class _usr_include_linux_videodev2_h_2467_2_(Union):

        class v4l2_captureparm(Structure):

            class v4l2_fract(Structure):
                pass
            v4l2_fract._fields_ = [('numerator', c_uint), ('denominator', c_uint)]
        v4l2_captureparm._fields_ = [('capability', c_uint), ('capturemode', c_uint), ('timeperframe', v4l2_fract), ('extendedmode', c_uint), ('readbuffers', c_uint), ('reserved', c_uint * 4)]

        class v4l2_outputparm(Structure):

            class v4l2_fract(Structure):
                pass
            v4l2_fract._fields_ = [('numerator', c_uint), ('denominator', c_uint)]
        v4l2_outputparm._fields_ = [('capability', c_uint), ('outputmode', c_uint), ('timeperframe', v4l2_fract), ('extendedmode', c_uint), ('writebuffers', c_uint), ('reserved', c_uint * 4)]
    _usr_include_linux_videodev2_h_2467_2_._fields_ = [('capture', v4l2_captureparm), ('output', v4l2_outputparm), ('raw_data', c_ubyte * 200)]
v4l2_streamparm._align_ = 4
v4l2_streamparm._fields_ = [('type', c_uint), ('parm', _usr_include_linux_videodev2_h_2467_2_)]

# file /usr/include/linux/videodev2.h, line 2488, column 8

class v4l2_event_vsync(Structure):
    pass
v4l2_event_vsync._align_ = 1
v4l2_event_vsync._fields_ = [('field', c_ubyte)]

# file /usr/include/linux/videodev2.h, line 2499, column 8

class v4l2_event_ctrl(Structure):
    pass
v4l2_event_ctrl._align_ = 8
v4l2_event_ctrl._fields_ = [('changes', c_uint), ('type', c_uint), ('flags', c_uint), ('minimum', c_int), ('maximum', c_int), ('step', c_int), ('default_value', c_int)]

# file /usr/include/linux/videodev2.h, line 2513, column 8

class v4l2_event_frame_sync(Structure):
    pass
v4l2_event_frame_sync._align_ = 4
v4l2_event_frame_sync._fields_ = [('frame_sequence', c_uint)]

# file /usr/include/linux/videodev2.h, line 2519, column 8

class v4l2_event_src_change(Structure):
    pass
v4l2_event_src_change._align_ = 4
v4l2_event_src_change._fields_ = [('changes', c_uint)]

# file /usr/include/linux/videodev2.h, line 2532, column 8

class v4l2_event_motion_det(Structure):
    pass
v4l2_event_motion_det._align_ = 4
v4l2_event_motion_det._fields_ = [('flags', c_uint), ('frame_sequence', c_uint), ('region_mask', c_uint)]

# file /usr/include/linux/videodev2.h, line 2538, column 8

class v4l2_event(Structure):

    class _usr_include_linux_videodev2_h_2540_2_(Union):

        class v4l2_event_vsync(Structure):
            pass
        v4l2_event_vsync._fields_ = [('field', c_ubyte)]

        class v4l2_event_ctrl(Structure):

            class _usr_include_linux_videodev2_h_2502_2_(Union):
                pass
            _usr_include_linux_videodev2_h_2502_2_._align_ = 8
            _usr_include_linux_videodev2_h_2502_2_._fields_ = []
        v4l2_event_ctrl._fields_ = [('changes', c_uint), ('type', c_uint), ('union v4l2_event_ctrl::(anonymous at /usr/include/linux/videodev2.h:2502:2)', _usr_include_linux_videodev2_h_2502_2_), ('flags', c_uint), ('minimum', c_int), ('maximum', c_int), ('step', c_int), ('default_value', c_int)]

        class v4l2_event_frame_sync(Structure):
            pass
        v4l2_event_frame_sync._fields_ = [('frame_sequence', c_uint)]

        class v4l2_event_src_change(Structure):
            pass
        v4l2_event_src_change._fields_ = [('changes', c_uint)]

        class v4l2_event_motion_det(Structure):
            pass
        v4l2_event_motion_det._fields_ = [('flags', c_uint), ('frame_sequence', c_uint), ('region_mask', c_uint)]
    _usr_include_linux_videodev2_h_2540_2_._fields_ = [('vsync', v4l2_event_vsync), ('ctrl', v4l2_event_ctrl), ('frame_sync', v4l2_event_frame_sync), ('src_change', v4l2_event_src_change), ('motion_det', v4l2_event_motion_det), ('data', c_ubyte * 64)]

    class timespec(Structure):
        pass
    timespec._fields_ = [('tv_sec', c_long), ('tv_nsec', c_long)]
v4l2_event._align_ = 8
v4l2_event._fields_ = [('type', c_uint), ('u', _usr_include_linux_videodev2_h_2540_2_), ('pending', c_uint), ('sequence', c_uint), ('timestamp', timespec), ('id', c_uint), ('reserved', c_uint * 8)]

# file /usr/include/linux/videodev2.h, line 2558, column 8

class v4l2_event_subscription(Structure):
    pass
v4l2_event_subscription._align_ = 4
v4l2_event_subscription._fields_ = [('type', c_uint), ('id', c_uint), ('flags', c_uint), ('reserved', c_uint * 5)]

# file /usr/include/linux/videodev2.h, line 2583, column 8

class v4l2_dbg_match(Structure):
    pass
v4l2_dbg_match._align_ = 1
v4l2_dbg_match._fields_ = [('type', c_uint)]

# file /usr/include/linux/videodev2.h, line 2591, column 8

class v4l2_dbg_register(Structure):

    class v4l2_dbg_match(Structure):

        class _usr_include_linux_videodev2_h_2585_2_(Union):
            pass
        _usr_include_linux_videodev2_h_2585_2_._align_ = 4
        _usr_include_linux_videodev2_h_2585_2_._fields_ = []
    v4l2_dbg_match._fields_ = [('type', c_uint), ('union v4l2_dbg_match::(anonymous at /usr/include/linux/videodev2.h:2585:2)', _usr_include_linux_videodev2_h_2585_2_)]
v4l2_dbg_register._align_ = 1
v4l2_dbg_register._fields_ = [('match', v4l2_dbg_match), ('size', c_uint), ('reg', c_ulong), ('val', c_ulong)]

# file /usr/include/linux/videodev2.h, line 2602, column 8

class v4l2_dbg_chip_info(Structure):

    class v4l2_dbg_match(Structure):

        class _usr_include_linux_videodev2_h_2585_2_(Union):
            pass
        _usr_include_linux_videodev2_h_2585_2_._align_ = 4
        _usr_include_linux_videodev2_h_2585_2_._fields_ = []
    v4l2_dbg_match._fields_ = [('type', c_uint), ('union v4l2_dbg_match::(anonymous at /usr/include/linux/videodev2.h:2585:2)', _usr_include_linux_videodev2_h_2585_2_)]
v4l2_dbg_chip_info._align_ = 1
v4l2_dbg_chip_info._fields_ = [('match', v4l2_dbg_match), ('name', c_char * 32), ('flags', c_uint), ('reserved', c_uint * 32)]

# file /usr/include/linux/videodev2.h, line 2625, column 8

class v4l2_create_buffers(Structure):

    class v4l2_format(Structure):

        class _usr_include_linux_videodev2_h_2451_2_(Union):

            class v4l2_pix_format(Structure):

                class _usr_include_linux_videodev2_h_509_2_(Union):
                    pass
                _usr_include_linux_videodev2_h_509_2_._align_ = 4
                _usr_include_linux_videodev2_h_509_2_._fields_ = []
            v4l2_pix_format._fields_ = [('width', c_uint), ('height', c_uint), ('pixelformat', c_uint), ('field', c_uint), ('bytesperline', c_uint), ('sizeimage', c_uint), ('colorspace', c_uint), ('priv', c_uint), ('flags', c_uint), ('union v4l2_pix_format::(anonymous at /usr/include/linux/videodev2.h:509:2)', _usr_include_linux_videodev2_h_509_2_), ('quantization', c_uint), ('xfer_func', c_uint)]

            class v4l2_pix_format_mplane(Structure):

                class _usr_include_linux_videodev2_h_2397_3_(Union):
                    pass
                _usr_include_linux_videodev2_h_2397_3_._align_ = 1
                _usr_include_linux_videodev2_h_2397_3_._fields_ = []
            v4l2_pix_format_mplane._fields_ = [('width', c_uint), ('height', c_uint), ('pixelformat', c_uint), ('field', c_uint), ('colorspace', c_uint), ('plane_fmt', v4l2_plane_pix_format * 8), ('num_planes', c_ubyte), ('flags', c_ubyte), ('union v4l2_pix_format_mplane::(anonymous at /usr/include/linux/videodev2.h:2397:3)', _usr_include_linux_videodev2_h_2397_3_), ('quantization', c_ubyte), ('xfer_func', c_ubyte), ('reserved', c_ubyte * 7)]

            class v4l2_window(Structure):

                class v4l2_rect(Structure):
                    pass
                v4l2_rect._fields_ = [('left', c_int), ('top', c_int), ('width', c_uint), ('height', c_uint)]

                class v4l2_clip(Structure):

                    class v4l2_rect(Structure):
                        pass
                    v4l2_rect._fields_ = [('left', c_int), ('top', c_int), ('width', c_uint), ('height', c_uint)]
                v4l2_clip._fields_ = [('c', v4l2_rect), ('next', POINTER(v4l2_clip))]
            v4l2_window._fields_ = [('w', v4l2_rect), ('field', c_uint), ('chromakey', c_uint), ('clips', POINTER(v4l2_clip)), ('clipcount', c_uint), ('bitmap', POINTER(None)), ('global_alpha', c_ubyte)]

            class v4l2_vbi_format(Structure):
                pass
            v4l2_vbi_format._fields_ = [('sampling_rate', c_uint), ('offset', c_uint), ('samples_per_line', c_uint), ('sample_format', c_uint), ('start', c_int * 2), ('count', c_uint * 2), ('flags', c_uint), ('reserved', c_uint * 2)]

            class v4l2_sliced_vbi_format(Structure):
                pass
            v4l2_sliced_vbi_format._fields_ = [('service_set', c_ushort), ('service_lines', c_ushort * 24 * 2), ('io_size', c_uint), ('reserved', c_uint * 2)]

            class v4l2_sdr_format(Structure):
                pass
            v4l2_sdr_format._fields_ = [('pixelformat', c_uint), ('buffersize', c_uint), ('reserved', c_ubyte * 24)]

            class v4l2_meta_format(Structure):
                pass
            v4l2_meta_format._fields_ = [('dataformat', c_uint), ('buffersize', c_uint), ('width', c_uint), ('height', c_uint), ('bytesperline', c_uint)]
        _usr_include_linux_videodev2_h_2451_2_._fields_ = [('pix', v4l2_pix_format), ('pix_mp', v4l2_pix_format_mplane), ('win', v4l2_window), ('vbi', v4l2_vbi_format), ('sliced', v4l2_sliced_vbi_format), ('sdr', v4l2_sdr_format), ('meta', v4l2_meta_format), ('raw_data', c_ubyte * 200)]
    v4l2_format._fields_ = [('type', c_uint), ('fmt', _usr_include_linux_videodev2_h_2451_2_)]
v4l2_create_buffers._align_ = 8
v4l2_create_buffers._fields_ = [('index', c_uint), ('count', c_uint), ('memory', c_uint), ('format', v4l2_format), ('capabilities', c_uint), ('flags', c_uint), ('max_num_buffers', c_uint), ('reserved', c_uint * 5)]

# file /usr/include/linux/videodev2.h, line 2643, column 8

class v4l2_remove_buffers(Structure):
    pass
v4l2_remove_buffers._align_ = 4
v4l2_remove_buffers._fields_ = [('index', c_uint), ('count', c_uint), ('type', c_uint), ('reserved', c_uint * 13)]
