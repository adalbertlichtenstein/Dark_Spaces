project(
  'Dark_Spaces',
  'c',
  meson_version : '>= 1.3.0',
  version : '0.1',
  default_options : ['warning_level=3'],
)

dependencies = [
]

sources = [
  'dark_spaces.c',
]

exe = executable(
  'Dark_Spaces',
  sources,
  dependencies : dependencies,
  install : true,
)

test('basic', exe)
