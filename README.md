# batch-rename-files
Batch rename files by pattern

usage: `batch_rename_files.py [-h] -d DIR [-m MATCH] [-r RENAME] [-a]`

***********************************************
>In a directory rename files that match pattern
***********************************************
```
optional arguments:
  -h, --help            Show this help message and exit
  -d DIR, --dir DIR     Directory where to search files
  -m MATCH, --match MATCH
                        Filename regular expression match pattern
  -r RENAME, --rename RENAME
                        Renamed filename (can include matched groups {0},{1}, ...)
  -a, --approve         Approve file rename (by default script doesn't do any file operations)
```
