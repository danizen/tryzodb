# tryzodb

## Summary

Working towards developing a cache for Django that lives in an mmap memory region from a file.

## Why

Dissatisfaction with the standard way of managing cache memory in Django. To
use these caches, I need to have redis installed.   Redis is great, but my
DevOps team sucks wind and we are steered away from Elasticache on AWS.

## what's the fastest way

Having tried zodb, I can see that struct pack/unpack is 1000 times faster than
pickle dumps/loads, and a bit faster than ctypes.Structure with ctypes.memmove.

In particular, struct.Structure(format), builds a packer/unpacker that is
already parsed.


