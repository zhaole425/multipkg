#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: zhaole

import time

MULTIPKG_VERSION = "1.1"

def whoami():
    return "root"

META={
    "ationlog": [{
        'actor': whoami(),
        'time': time.time(),
        'type': 'build',
        'actions': [{
            'summary': 'multipkg initialiation',
            'text': 'multipkg version' + MULTIPKG_VERSION
        }]
    }]
}


class Pkgbase(object):
    def __init__(self, directory, cleanup=False, force=False,
                 warn_on_error=False, verbose=False, overrides=False,
                 meta=""):
        self.directory = directory
        pass

    def __enter__(self):
        pass
#
#
# my $init_metadata = {
#   'actionlog' => [
#     { 'actor'   => whoami(),
#       'time'    => time(),
#       'type'    => 'build',
#       'actions' => [
#         { 'summary' => 'multipkg initialiation',
#           'text'    => "multipkg version: "
#             . MULTIPKG_VERSION . "\n"
#             . "invoked as: $0 "
#             . join( ' ', @ARGV ) . "\n",
#         },
#       ],
#     },
#   ],
# };
#
#
#
#
#
# sub
# new
# {
#     my $proto = shift;
# my % rest;
# if (@ _ == 0)
# {
# % rest = ();
# } elsif( @ _ == 1) {
#                    % rest = % {$_[0]} if (ref $_[0] eq 'HASH');
# } else {
# % rest = @ _;
# }
#
# my $
#
#
# class = ref $proto | | $proto;
#
#
# my % d = $
#
# class ->_defaults;
#
#
# my $nd = $
#
# class ->_dereference(\ % d);
#
#
# my $self = bless
# {(% $nd, % rest)}, $
#
# class ;
#
#
# my @ required;
# my @ bad = ();
# for ($self->_required_fields) {
#     push @ bad, $_ unless(defined $self->{$_});
# }
#
# if (@ bad) {
# warn "Error creating '$class': ".
# (join ',', @ bad)." not defined\n";
# return undef;
# }
#
# return undef
# unless $self->_init;
#
# return $self;
# # }