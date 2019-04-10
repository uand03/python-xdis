# (C) Copyright 2019 by Rocky Bernstein
#
#  This program is free software; you can redistribute it and/or
#  modify it under the terms of the GNU General Public License
#  as published by the Free Software Foundation; either version 2
#  of the License, or (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.
"""
CPython 3.8 bytecode opcodes with the removed 3.7 and earlier opcodes reinstated

This is useful say in decompilation where a preprocessing step will fill in the
removed opcodes
"""

from xdis.opcodes.base import(
    def_op, finalize_opcodes,
    format_extended_arg36,
    init_opdata, jabs_op,
    jrel_op, update_pj3
    )

import xdis.opcodes.opcode_38 as opcode_38

version = 3.8

l = locals()

init_opdata(l, opcode_38, version)

# Reinstate these which are not strictly in 3.8...
def_op(l, 'BREAK_LOOP',           80,  0,  0)
jabs_op(l, 'CONTINUE_LOOP',      119,  0,  0)  # Target address
jrel_op(l, 'SETUP_LOOP',         120,  0,  0, conditional=True) # Distance to target address
jrel_op(l, 'SETUP_EXCEPT',       121,  0,  6, conditional=True)  #

format_MAKE_FUNCTION_arg = opcode_38.format_MAKE_FUNCTION_arg
format_value_flags = opcode_38.format_value_flags

opcode_arg_fmt = {
    'MAKE_FUNCTION': format_MAKE_FUNCTION_arg,
    'FORMAT_VALUE': format_value_flags,
    'EXTENDED_ARG': format_extended_arg36
}

update_pj3(globals(), l)

finalize_opcodes(l)
