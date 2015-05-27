Issues
======

- Click on Windows should run and show the state.

- Explain the data structure of YAML file.

  generating customized data::

      osbp
          $name:
              attr: ...
              desc: ...
              type: ...
              steps:
                  - name: ...
                    type: ...
                    para: ...
      script
          $name:
              desc: ...
              cont: ...
              type: ...
              sudo: ...
      config
          $name:
              desc: ...
              cont: ...

- Explain the requirements:
    + Python
    + Git

- Include Packages:
    + Requists
    + PyYAML

- Clean and import all OSBPs every time is expensive.

- Service temporarily unavailable error handling.

- Clean customized OSBPs could be force and fast.

  issues:

      #. using `api._list_index({'category': '...'})` is faster,
         but no `isCustomerContent` field,
         needs to know where is the end index of builtins

      #. delete methods are the same when using uri but id

- Export OSBP recipe can be more simple

- Let settings and customized OSBPs data as .txt file so that even notepad can open it.

- Verification:
  Given `A` is the exported.
  Import `A` to another Altair and export from the Altair as `B`.
  Check if `A` is the same with `B`.

- Remove data is not necessary; consider update just necessary part with diff feature (not implement yet)

- Need modulization.


After discussion
==============================

[v] Merge export cust feature to API class
[v] Use methods that fetching index and then retrieving one by one
[v] Use imperative to rewrite fetching
[v] Only export scripts and config files of customized OSBPs
[v] Use index data to fast distinguish customized data
[ ] Update usage to wiki
