#!/bin/bash

ionic build
ionic cap add android
ionic cap copy
ionic cap sync
ionic cap open android
