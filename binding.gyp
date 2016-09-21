{
  'targets': [
    {
      'target_name': 'zmq',
      'sources': [ 'binding.cc' ],
      'include_dirs' : ["<!(node -e \"require('nan')\")", 'include'],
      'cflags!': ['-fno-exceptions'],
      'cflags_cc!': ['-fno-exceptions'],
      'conditions': [
        ['OS=="win"', {
          'msbuild_toolset': 'v120',
          'defines': ['ZMQ_STATIC'],
          'conditions': [
            ['target_arch=="ia32"', {
              'libraries': [
                '<(PRODUCT_DIR)/../../windows/lib/Win32/libzmq',
                'ws2_32.lib',
              ]
            },{
              'libraries': [
                '<(PRODUCT_DIR)/../../windows/lib/x64/libzmq',
                'ws2_32.lib',
              ]
            }]
          ],
        }],
        ['OS=="mac" or OS=="solaris"', {
          'xcode_settings': {
            'GCC_ENABLE_CPP_EXCEPTIONS': 'YES',
            'MACOSX_DEPLOYMENT_TARGET': '10.6',
          },
          'libraries': [ '<(PRODUCT_DIR)/../../unix/lib/libzmq.a' ],
        }],
        ['OS=="openbsd" or OS=="freebsd"', {
        }],
        ['OS=="linux"', {
          'cflags': ['-fPIC'],
          'cflags_cc': ['-fPIC'],
          'libraries': [ '<(PRODUCT_DIR)/../../unix/lib/libzmq.a' ],
        }],
      ]
    }
  ]
}
