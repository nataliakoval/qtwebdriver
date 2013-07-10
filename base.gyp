{
  'includes': [
    'wd.gypi',
    'wd_common.gypi',
  ],

  'targets': [
    {
      'target_name': 'chromium_base',
      'type': 'static_library',
      'standalone_static_library': 1,

      'include_dirs': [
        'inc/',
        'src/',
      ],

      'sources': [
        'src/base/at_exit.cc',
        'src/base/atomicops_internals_x86_gcc.cc',
        'src/base/base64.cc',
        'src/base/base_paths.cc',      
        'src/base/base_switches.cc',
        'src/base/callback_internal.cc',
        'src/base/command_line.cc',
        'src/base/debug/alias.cc',
        'src/base/debug/debugger.cc',        
        'src/base/environment.cc',
        'src/base/file_path.cc',
        'src/base/file_util.cc',
        'src/base/json/json_parser.cc',
        'src/base/json/json_reader.cc',
        'src/base/json/json_writer.cc',
        'src/base/json/string_escape.cc',
        'src/base/lazy_instance.cc',
        'src/base/location.cc',
        'src/base/logging.cc',
        'src/base/memory/ref_counted.cc',
        'src/base/memory/singleton.cc',
        'src/base/memory/weak_ptr.cc',
        'src/base/message_loop.cc',
        'src/base/message_loop_proxy.cc',
        'src/base/message_loop_proxy_impl.cc',
        'src/base/message_pump.cc',
        'src/base/message_pump_default.cc',
        'src/base/metrics/bucket_ranges.cc',
        'src/base/metrics/histogram_base.cc',
        'src/base/metrics/histogram.cc',
        'src/base/metrics/histogram_samples.cc',
        'src/base/metrics/sample_vector.cc',
        'src/base/metrics/statistics_recorder.cc',
        'src/base/path_service.cc',
        'src/base/pending_task.cc',
        'src/base/pickle.cc',
        'src/base/platform_file.cc',
        'src/base/profiler/alternate_timer.cc',
        'src/base/profiler/scoped_profile.cc',
        'src/base/profiler/tracked_time.cc',
        'src/base/rand_util.cc',
        'src/base/run_loop.cc',
        'src/base/scoped_temp_dir.cc',        
        'src/base/string_number_conversions.cc',
        'src/base/string_piece.cc',
        'src/base/stringprintf.cc',
        'src/base/string_split.cc',
        'src/base/string_util.cc',
        'src/base/synchronization/lock.cc',
        'src/base/task_runner.cc',
        'src/base/third_party/dmg_fp/dtoa.cc',
        'src/base/third_party/dmg_fp/g_fmt.cc',
        'src/base/third_party/dynamic_annotations/dynamic_annotations.c',
        'src/base/third_party/icu/icu_utf.cc',
        'src/base/third_party/nspr/prtime.cc',
        'src/base/third_party/xdg_user_dirs/xdg_user_dir_lookup.cc',
        'src/base/threading/post_task_and_reply_impl.cc',
        'src/base/threading/thread.cc',
        'src/base/threading/thread_checker_impl.cc',
        'src/base/threading/thread_collision_warner.cc',
        'src/base/threading/thread_restrictions.cc',
        'src/base/threading/worker_pool.cc',
        'src/base/thread_task_runner_handle.cc',
        'src/base/time.cc',    
        'src/base/timer.cc',
        'src/base/tracked_objects.cc',
        'src/base/tracking_info.cc',
        'src/base/utf_string_conversions.cc',
        'src/base/utf_string_conversion_utils.cc',
        'src/base/values.cc',
        'src/third_party/modp_b64/modp_b64.cc'
      ],

      'conditions': [

        ['OS=="linux"', {
          'defines': [
            '__STDC_FORMAT_MACROS',
            'OS_POSIX',
          ],
          'sources': [
            'src/base/string16.cc',
            'src/base/time_posix.cc',
            'src/base/base_paths_posix.cc',
            'src/base/debug/debugger_posix.cc',
            'src/base/file_util_posix.cc',
            'src/base/nix/xdg_util.cc',
            'src/base/platform_file_posix.cc',
            'src/base/rand_util_posix.cc',
            'src/base/safe_strerror_posix.cc',
            'src/base/synchronization/condition_variable_posix.cc',
            'src/base/synchronization/lock_impl_posix.cc',
            'src/base/synchronization/waitable_event_posix.cc',
            'src/base/sys_info_posix.cc',
            'src/base/sys_string_conversions_posix.cc',
            'src/base/threading/platform_thread_posix.cc',
            'src/base/threading/thread_local_posix.cc',
            'src/base/threading/thread_local_storage_posix.cc',
            'src/base/threading/worker_pool_posix.cc',
            'src/net/base/file_stream_metrics_posix.cc',
            'src/net/base/file_stream_posix.cc',
            'src/net/base/net_errors_posix.cc',
            'src/base/sys_info_linux.cc',
          ],
        } ],

        [ 'OS == "win"', {
          'defines': [
            '_WIN32',
            'OS_WIN',
            'NOMINMAX',
            '_CRT_RAND_S',
            'WIN32',
            '_WINSOCKAPI_',
          ],
          'msvs_configuration_attributes': {
            'CharacterSet': '1'
          },
          'sources': [
            'src/base/cpu.cc',
            'src/base/time_win.cc',
            'src/base/base_paths_win.cc',
            'src/base/debug/debugger_win.cc',
            'src/base/file_util_win.cc',
            'src/base/platform_file_win.cc',
            'src/base/rand_util_win.cc',
            'src/base/synchronization/condition_variable_win.cc',
            'src/base/synchronization/lock_impl_win.cc',
            'src/base/synchronization/waitable_event_win.cc',
            'src/base/sys_info_win.cc',
            'src/base/threading/platform_thread_win.cc',
            'src/base/threading/thread_local_win.cc',
            'src/base/threading/thread_local_storage_win.cc',
            'src/base/threading/worker_pool_win.cc',
            'src/net/base/file_stream_win.cc',
            'src/net/base/file_stream_metrics_win.cc',
            'src/net/base/net_errors_win.cc',
            'src/base/sys_info_win.cc',
            'src/base/win/windows_version.cc',
            'src/base/win/registry.cc',
            'src/base/win/scoped_handle.cc',
            'src/base/win/wrapped_window_proc.cc',
            'src/base/message_pump_win.cc',
            'src/base/process_util.cc',
            'src/base/process_util_win.cc',
          ],
        } ],
      ],
    }
  ],
}
