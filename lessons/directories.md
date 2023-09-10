# Directories

## os module

### .chdir()

Changes the current working directory path.

Examples:

```python
import os
os.chdir("/etc")
```

### .getcwd()

Return the current directory.

Examples:

```python
import os
print(os.getcwd())
```

### .listdir()

Display all subfolders and files inside the given directory in a list separated by commas.

Examples:

```python
import os
os.listdir("folder")
```

### .mkdir()

Create a directory in the current path working directory

Examples:

```python
import os
os.mkdir("folder")
```

### .rmdir()

Deletes the directory **only** if it empty.

Examples:

```python
import os
os.rmdir("folder")
```

## os.path module

### .isdir()

Check if its a directory or not and return a boolean.

Examples:

```python
import os
os.path.isdir("folder")
```

### .join()

Join one or more path segments intelligently. The return value is the concatenation of path and all members of \*paths, with exactly one directory separator following each non-empty part, except the last. That is, the result will only end in a separator if the last part is either empty or ends in a separator. If a segment is an absolute path (which on Windows requires both a drive and a root), then all previous segments are ignored and joining continues from the absolute path segment.

Examples:

```python
import os
os.path.join("folder", files)
```
