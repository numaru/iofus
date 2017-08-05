# Iofus

A python 3 module to handle Dofus 2.0 network protocol.

## Getting started

**TODO**: see `test/test_integration` as a first example.

## Tests

Run `python -m unittest` to run the tests.

## Protocol builder

A script to convert the network messages from decompiled action script 3 to python.

To update the protocol to a new version follow these steps :
1. Copy the `ankamagames/dofus/network` folder into `protocol_builder/input`.
2. Run `python protocol_builder/app.py`.
3. Three output files must be generated in `protocol_builder/output`.
4. Copy these output files into the `iofus` folder.
5. Run `sudo python setup.py install` again.
