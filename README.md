# dockertags
List all tags for a Docker image on a remote registry

## install
`make install`

## uninstall
`make uninstall`

## usage
`dockertags <image_name>`

## example output

### non-offical images
```
$ dockertags cemdrk/merhabapy
fetching from https://registry.hub.docker.com/v2/repositories/cemdrk/merhabapy/tags
cemdrk/merhabapy:latest
```

### official images
```
$ dockertags python
fetching from https://registry.hub.docker.com/v2/repositories/library/python/tags
fetching from https://registry.hub.docker.com/v2/repositories/library/python/tags?page=2
...
```
