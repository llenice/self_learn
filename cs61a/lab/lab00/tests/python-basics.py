test = {
  'name': 'Python Basics',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> x = 20
          >>> x + 2
          22
          # locked
          >>> x
          22
          # locked
          >>> y = 5
          >>> y = y + 3
          >>> y * 2
          16
          # locked
          >>> y + x
          38
          # locked
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        }
      ],
      'scored': False,
      'type': 'wwpp'
    }
  ]
}
