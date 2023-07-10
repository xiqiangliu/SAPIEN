#!/bin/bash
docker run -v `pwd`:/workspace/SAPIEN -it --rm \
       fxiangucsd/sapien-build-env:3.0 bash -c "cd /workspace/SAPIEN && rm -rf build wheelhouse dist sapien.egg-info"
