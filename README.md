# pr-stats

## How to use
```
$ ./pr-stats --since=2023-12-11 --until=2024-12-18 --repo="{org}/{repo}"

[
  {
    "author": "xxx",
    "count": 31
  },
  {
    "author": "xxx",
    "count": 68
  },
  {
    "author": "xxx",
    "count": 39
  },
  {
    "author": "xxx",
    "count": 29
  }
]
```

```
$ ./pr-stats -v --since=2023-12-11 --until=2024-12-18 --repo="{org}/{repo}"

[
  {
    "author": "xxx",
    "count": 31,
    "prs": [...]
  },
  {
    "author": "xxx",
    "count": 68,
    "prs": [...]

  },
  {
    "author": "xxx",
    "count": 39,
    "prs": [...]
  },
  {
    "author": "xxx",
    "count": 29,
    "prs": [...]
  }
]
```
