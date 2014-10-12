# Copyright 2014 The Android Open Source Project
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import unittest

def full(props):
    """Returns whether a device is a FULL capability camera2 device.

    Args:
        props: Camera properties object.

    Returns:
        Boolean.
    """
    return props.has_key("android.info.supportedHardwareLevel") and \
           props["android.info.supportedHardwareLevel"] == 1

def limited(props):
    """Returns whether a device is a LIMITED capability camera2 device.

    Args:
        props: Camera properties object.

    Returns:
        Boolean.
    """
    return props.has_key("android.info.supportedHardwareLevel") and \
           props["android.info.supportedHardwareLevel"] == 0

def legacy(props):
    """Returns whether a device is a LEGACY capability camera2 device.

    Args:
        props: Camera properties object.

    Returns:
        Boolean.
    """
    return props.has_key("android.info.supportedHardwareLevel") and \
           props["android.info.supportedHardwareLevel"] == 2

def manual_sensor(props):
    """Returns whether a device supports MANUAL_SENSOR capabilities.

    Args:
        props: Camera properties object.

    Returns:
        Boolean.
    """
    return    props.has_key("android.request.availableCapabilities") and \
              1 in props["android.request.availableCapabilities"] \
           or full(props)

def manual_post_proc(props):
    """Returns whether a device supports MANUAL_POST_PROCESSING capabilities.

    Args:
        props: Camera properties object.

    Returns:
        Boolean.
    """
    return    props.has_key("android.request.availableCapabilities") and \
              2 in props["android.request.availableCapabilities"] \
           or full(props)

def raw(props):
    """Returns whether a device supports RAW capabilities.

    Args:
        props: Camera properties object.

    Returns:
        Boolean.
    """
    return props.has_key("android.request.availableCapabilities") and \
           3 in props["android.request.availableCapabilities"]

def sensor_fusion(props):
    """Returns whether the camera and motion sensor timestamps for the device
    are in the same time domain and can be compared direcctly.

    Args:
        props: Camera properties object.

    Returns:
        Boolean.
    """
    return props.has_key("android.sensor.info.timestampSource") and \
           props["android.sensor.info.timestampSource"] == 1

class __UnitTest(unittest.TestCase):
    """Run a suite of unit tests on this module.
    """
    # TODO: Add more unit tests.

if __name__ == '__main__':
    unittest.main()
