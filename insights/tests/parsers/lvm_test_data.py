# flake8: noqa
LVMCONFIG = """
  WARNING: Running as a non-root user. Functionality may be unavailable.
devices {
	filter=["a|.*/|"]
	allow_changes_with_duplicate_pvs=0
	issue_discards=0
	pv_min_size=2048
	require_restorefile_with_uuid=1
	disable_after_error_count=0
	ignore_lvm_mirrors=1
	ignore_suspended_devices=0
	data_alignment_offset_detection=1
	data_alignment=0
	data_alignment_detection=1
	md_chunk_alignment=1
	fw_raid_component_detection=0
	md_component_detection=1
	multipath_component_detection=1
	sysfs_scan=1
	write_cache_state=1
	cache_file_prefix=""
	cache_dir="/etc/lvm/cache"
	preferred_names=["^/dev/mpath/","^/dev/mapper/mpath","^/dev/[hs]d"]
	external_device_info_source="none"
	obtain_device_list_from_udev=1
	scan="/dev"
	dir="/dev"
	global_filter=["a|.*/|"]
	cache="/etc/lvm/cache/.cache"
	default_data_alignment=1
}
backup {
	backup=1
	backup_dir="/etc/lvm/backup"
	archive=1
	archive_dir="/etc/lvm/archive"
	retain_min=10
	retain_days=30
}
shell {
	history_size=100
}
config {
	checks=1
	abort_on_errors=0
	profile_dir="/etc/lvm/profile"
}
allocation {
	thin_pool_metadata_require_separate_pvs=0
	cache_pool_metadata_require_separate_pvs=0
	mirror_logs_require_separate_pvs=0
	wipe_signatures_when_zeroing_new_lvs=1
	use_blkid_wiping=1
	maximise_cling=1
	raid_stripe_all_devices=0
	cache_pool_cachemode="writethrough"
	cache_metadata_format=0
	cache_mode="writethrough"
	thin_pool_zero=1
	thin_pool_discards="passdown"
	thin_pool_chunk_size_policy="generic"
	physical_extent_size=4096
}
log {
	report_command_log=0
	debug_classes=["memory","devices","io","activation","allocation","lvmetad","metadata","cache","locking","lvmpolld","dbus"]
	activation=0
	prefix="  "
	command_names=0
	indent=1
	level=0
	overwrite=0
	syslog=1
	silent=0
	verbose=0
	command_log_sort="log_seq_num"
	command_log_cols="log_seq_num,log_type,log_context,log_object_type,log_object_name,log_object_id,log_object_group,log_object_group_id,log_message,log_errno,log_ret_code"
	command_log_selection="!(log_type=status && message=success)"
}
global {
	fallback_to_lvm1=0
	notify_dbus=1
	use_lvmpolld=1
	system_id_source="none"
	use_lvmlockd=0
	use_lvmetad=1
	sparse_segtype_default="thin"
	raid10_segtype_default="raid10"
	mirror_segtype_default="raid1"
	metadata_read_only=0
	abort_on_internal_errors=0
	prioritise_write_locks=1
	locking_dir="/run/lock/lvm"
	fallback_to_local_locking=1
	fallback_to_clustered_locking=1
	wait_for_locks=1
	locking_type=1
	etc="/etc"
	proc="/proc"
	activation=1
	suffix=1
	si_unit_consistency=1
	units="r"
	test=0
	umask=63
	format="lvm2"
	locking_library="liblvm2clusterlock.so"
	detect_internal_vg_cache_corruption=0
	lvdisplay_shows_full_device_path=0
	use_aio=1
	lvmetad_update_wait_time=10
	lvmlockd_lock_retries=3
	sanlock_lv_extend=256
	thin_check_executable="/usr/sbin/thin_check"
	thin_dump_executable="/usr/sbin/thin_dump"
	thin_repair_executable="/usr/sbin/thin_repair"
	thin_check_options=["-q","--clear-needs-check-flag"]
	thin_repair_options=[""]
	cache_check_executable="/usr/sbin/cache_check"
	cache_dump_executable="/usr/sbin/cache_dump"
	cache_repair_executable="/usr/sbin/cache_repair"
	cache_check_options=["-q","--clear-needs-check-flag"]
	cache_repair_options=[""]
	fsadm_executable="/usr/sbin/fsadm"
}
activation {
	activation_mode="degraded"
	polling_interval=15
	monitoring=1
	use_mlockall=0
	thin_pool_autoextend_percent=20
	thin_pool_autoextend_threshold=100
	snapshot_autoextend_percent=20
	snapshot_autoextend_threshold=100
	mirror_log_fault_policy="allocate"
	mirror_image_fault_policy="remove"
	raid_fault_policy="warn"
	readahead="auto"
	raid_region_size=2048
	process_priority=-18
	reserved_memory=8192
	reserved_stack=64
	use_linear_target=1
	missing_stripe_filler="error"
	retry_deactivation=1
	verify_udev_operations=0
	udev_rules=1
	udev_sync=1
	checks=0
	mirror_region_size=2048
	error_when_full=0
	mirror_device_fault_policy="remove"
	auto_set_activation_skip=1
}
metadata {
	check_pv_device_sizes=1
	record_lvs_history=0
	lvs_history_retention_time=0
	pvmetadatacopies=1
	vgmetadatacopies=0
	pvmetadatasize=255
	pvmetadataignore=0
	stripesize=64
}
report {
	output_format="basic"
	compact_output=0
	compact_output_cols=""
	aligned=1
	buffered=1
	headings=1
	separator=" "
	list_item_separator=","
	prefixes=0
	quoted=1
	columns_as_rows=0
	binary_values_as_numeric=0
	time_format="%Y-%m-%d %T %z"
	devtypes_sort="devtype_name"
	devtypes_cols="devtype_name,devtype_max_partitions,devtype_description"
	devtypes_cols_verbose="devtype_name,devtype_max_partitions,devtype_description"
	lvs_sort="vg_name,lv_name"
	lvs_cols="lv_name,vg_name,lv_attr,lv_size,pool_lv,origin,data_percent,metadata_percent,move_pv,mirror_log,copy_percent,convert_lv"
	lvs_cols_verbose="lv_name,vg_name,seg_count,lv_attr,lv_size,lv_major,lv_minor,lv_kernel_major,lv_kernel_minor,pool_lv,origin,data_percent,metadata_percent,move_pv,copy_percent,mirror_log,convert_lv,lv_uuid,lv_profile"
	vgs_sort="vg_name"
	vgs_cols="vg_name,pv_count,lv_count,snap_count,vg_attr,vg_size,vg_free"
	vgs_cols_verbose="vg_name,vg_attr,vg_extent_size,pv_count,lv_count,snap_count,vg_size,vg_free,vg_uuid,vg_profile"
	pvs_sort="pv_name"
	pvs_cols="pv_name,vg_name,pv_fmt,pv_attr,pv_size,pv_free"
	pvs_cols_verbose="pv_name,vg_name,pv_fmt,pv_attr,pv_size,pv_free,dev_size,pv_uuid"
	segs_sort="vg_name,lv_name,seg_start"
	segs_cols="lv_name,vg_name,lv_attr,stripes,segtype,seg_size"
	segs_cols_verbose="lv_name,vg_name,lv_attr,seg_start,seg_size,stripes,segtype,stripesize,chunksize"
	pvsegs_sort="pv_name,pvseg_start"
	pvsegs_cols="pv_name,vg_name,pv_fmt,pv_attr,pv_size,pv_free,pvseg_start,pvseg_size"
	pvsegs_cols_verbose="pv_name,vg_name,pv_fmt,pv_attr,pv_size,pv_free,pvseg_start,pvseg_size,lv_name,seg_start_pe,segtype,seg_pe_ranges"
	vgs_cols_full="vg_all"
	pvs_cols_full="pv_all"
	lvs_cols_full="lv_all"
	pvsegs_cols_full="pvseg_all,pv_uuid,lv_uuid"
	segs_cols_full="seg_all,lv_uuid"
	vgs_sort_full="vg_name"
	pvs_sort_full="pv_name"
	lvs_sort_full="vg_name,lv_name"
	pvsegs_sort_full="pv_uuid,pvseg_start"
	segs_sort_full="lv_uuid,seg_start"
	mark_hidden_devices=1
	two_word_unknown_device=0
}
dmeventd {
	raid_library="libdevmapper-event-lvm2raid.so"
	thin_library="libdevmapper-event-lvm2thin.so"
	snapshot_library="libdevmapper-event-lvm2snapshot.so"
	mirror_library="libdevmapper-event-lvm2mirror.so"
	thin_command="lvm lvextend --use-policies"
	executable="/usr/sbin/dmeventd"
}
tags {
	hosttags=0
}
local {
	system_id=""
	host_id=0
}""".strip()

LVMCONFIG2 = """
global {
	umask=077
	test=0
	units="r"
	si_unit_consistency=1
	suffix=1
	activation=1
	fallback_to_lvm1=0
}
""".strip()

LVMCONFIG3 = """
global {
	test=077
	test=0
	units="r"
	si_unit_consistency=1
	suffix=1
	activation=1
	fallback_to_lvm1=0
}
""".strip()
