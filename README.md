# pylabrad


pylabrad is an interface to the LabRAD system in python with support for both clients and servers.
For general information about the LabRAD system/protocol see [the labrad repository](https://github.com/labrad/labrad) and associated [wiki](https://github.com/labrad/labrad/wiki).
For help getting started and understanding pylabrad take a look at the [wiki](https://github.com/labrad/pylabrad/wiki).



## Manager Compatibility

As of version 0.96.0, pylabrad is no longer compatible with the Delphi labrad manager available from Sourceforge.
Instead, use the new [scalabrad manager](https://github.com/labrad/scalabrad).



If we still want to use the old servers, like grapher and registry. 

- run [scalabrad manager](https://github.com/labrad/scalabrad)

  or according to https://github.com/ZeeUTao/scalabrad-web.

  A simple way is download a pre-built binary package from https://bintray.com/labrad/generic/scalabrad#files, and run a startup script `/bin/labrad.bat`. 

  > you may need to delete the environment variables defined for the old Delphi labrad manager

- run the Delphi labrad manager. 

  The host and port should be different from the scalabrad manager (localhost 7682), for example, you can use the port 7683. 
  
  ```
  Port: 7683
  Password: 
  Registry: D:\Labrad\Registry
  Auto-Run: yes
  
  + localhost
  ```



- import [pylabrad](https://github.com/ZeeUTao/pylabrad-zeeu), and test

  ```python
  import labrad
  cxn=labrad.connect()
  
  # add delphi manager, managers_add(host,port,password)
  cxn.auth.managers_add('localhost',7683,'')
  
  # this function show [(host,port,connected)]
  # If success, it gives [('localhost', 7683, True)]
  cxn.auth.managers()
  ```




- Then you can run the other server, for example, `0_data_vault.py`

  run in ipython3 or cmd

  ```
  # run 0_data_vault.py
  # or
  # ipython3 0_data_vault.py
  ```

  remember to type `Enter` and input password and directories

  

  and test it 

  ```
  import labrad
  cxn = labrad.connect()
  dv = cxn.data_vault
  ```

  
  
  load the old delphi registry in scalabrad, run the followings in `scalabrad-0.x.x\bin`
  
  ```cmd
  labrad --registry file:///D:/Labrad/Tao_Lab/Registry?format=delphi
  ```
  
  



  







The user interface for the manager and node along with the registry editor and grapher is now [web-based (scalabrad-web)](https://github.com/labrad/scalabrad-web).

## Node Server

In addition to the basic labrad client/server support, this package also includes a tool called the "node" server in the `labrad.node` package.
This server just runs other labrad servers, allowing you to start and stop them by sending labrad requests to the node.
By running node servers on one or more machines connected to labrad, you can remotely control which labrad servers are running on those machines.
This can be very useful in distributed setups.
For more information, including required configuration in the LabRAD registry (to, e.g., define directories containing servers),
see the [node docstring](https://github.com/labrad/pylabrad/blob/master/labrad/node/__init__.py).
The node module is executable, so you should launch it with `python -m labrad.node`.
To see documentation of the available command-line parameters run `python -m labrad.node --help`.

## Contributing

For instructions on how to contribute to pylabrad, see [contributing.md](https://github.com/labrad/labrad/blob/master/contributing.md).

## Tests

New code should have tests, and changes to existing code should not break existing tests.
To run the test suite, you'll need to have `pytest` installed, then run `py.test` from the command line when in the pylabrad directory.

## Building and Updating

Packages for pylabrad are distributed through [PyPI](https://pypi.python.org/pypi/pylabrad).
The best way to install pylabrad is using pip: `pip install pylabrad`.
If installing using git and including in `PYTHONPATH`, note that versions 0.95.0 or later require the `futures` python package.

For contributors who need to build and upload new packages, do the following:

* **Tag the release.** Create a git tag with the version number, e.g. `git tag 1.0.0`.
  You'll also want to push this tag to make it official: `git push origin 1.0.0`.
* **Build packages.** Make sure you have a clean local tree (no pending changes beyond the tag) and then build the packages: `source dist_build.sh`.
  Packages will be built in the `dist/` directory and you should take a look to make sure the version number was found properly.
* **Upload to PyPI.** Run the provided script to upload packages: `source dist_upload.sh`.
  This requires the `twine` package to ensure that the connection to PyPI is secure, so you may need to install it locally first: `pip install twine`.
  Of course, you'll need a PyPI account that has permissions to update the pylabrad package.

## Migration note

This repo was moved from the martinisgroup organization.
To tell git to pull updates from the new location, you'll
want to update the 'origin' remote in your local repository.
Use `git remote -v` to see the names and urls for all remotes
you have defined, then `git remote set-url` to update the url,
changing the organization to labrad:

```
$ git remote -v
origin	git@github.com:martinisgroup/pylabrad (fetch)
origin	git@github.com:martinisgroup/pylabrad (push)

$ git remote set-url origin git@github.com:labrad/pylabrad
```

## Credits

```
PyParsing Copyright (c) 2003-2007  Paul T. McGuire
```

```
unwrap.py from http://www.wave.co.nz/~glyn/
```
