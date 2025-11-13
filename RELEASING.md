# Releasing the ea


```shell
cldfbench makecldf cldfbench_modis.py --with-zenodo --with-cldfreadme --glottolog-version v5.2
pytest
```

```shell
cldfbench readme cldfbench_modis.py
cldfbench zenodo --communities dplace cldfbench_modis.py
dplace check cldfbench_modis.py
```

```shell
git status
git tag
```

Adapt CHANGELOG.md.
Add, commit and push all changes.

```shell
dplace release cldfbench_modis.py vX.Y
```