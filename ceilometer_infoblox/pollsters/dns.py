#
# Copyright 2015 Infoblox, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

from ceilometer_infoblox import pollsters


class DNSPollster(pollsters.BaseNIOSPollster):

    def __init__(self):
        super(DNSPollster, self).__init__()

    IDENTIFIER = 'nios.dns.invalid'

    @property
    def meter_name(self):
        return self.IDENTIFIER

    @property
    def meter_type(self):
        return 'gauge'

    @property
    def meter_unit(self):
        return 'queries/s'


class QPSPollster(DNSPollster):

    def __init__(self):
        super(QPSPollster, self).__init__()

    IDENTIFIER = 'nios.dns.qps'


class CHRPollster(DNSPollster):

    def __init__(self):
        super(CHRPollster, self).__init__()

    IDENTIFIER = 'nios.dns.chr'

    @property
    def meter_unit(self):
        return '%'