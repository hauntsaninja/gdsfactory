"""Each component factory component returns a component.
Make sure new components get imported / registered
registered components get tested and are available
"""

import sys

from gdsfactory.components.add_fidutials import add_fidutials, add_fidutials_offsets
from gdsfactory.components.align import add_frame, align_wafer
from gdsfactory.components.array_component import array
from gdsfactory.components.array_with_fanout import (
    array_with_fanout,
    array_with_fanout_2d,
)
from gdsfactory.components.array_with_via import array_with_via, array_with_via_2d
from gdsfactory.components.awg import awg
from gdsfactory.components.bbox import bbox
from gdsfactory.components.bend_circular import bend_circular, bend_circular180
from gdsfactory.components.bend_circular_heater import bend_circular_heater
from gdsfactory.components.bend_euler import (
    bend_euler,
    bend_euler180,
    bend_euler_s,
    bend_straight_bend,
)
from gdsfactory.components.bend_port import bend_port
from gdsfactory.components.bend_s import bend_s
from gdsfactory.components.C import C
from gdsfactory.components.cavity import cavity
from gdsfactory.components.cdc import cdc
from gdsfactory.components.cdsem_all import cdsem_all
from gdsfactory.components.circle import circle
from gdsfactory.components.compass import compass
from gdsfactory.components.component_lattice import component_lattice
from gdsfactory.components.component_sequence import component_sequence
from gdsfactory.components.copy_layers import copy_layers
from gdsfactory.components.coupler import coupler
from gdsfactory.components.coupler90 import coupler90, coupler90circular
from gdsfactory.components.coupler90bend import coupler90bend
from gdsfactory.components.coupler_adiabatic import coupler_adiabatic
from gdsfactory.components.coupler_asymmetric import coupler_asymmetric
from gdsfactory.components.coupler_full import coupler_full
from gdsfactory.components.coupler_ring import coupler_ring
from gdsfactory.components.coupler_straight import coupler_straight
from gdsfactory.components.coupler_symmetric import coupler_symmetric
from gdsfactory.components.cross import cross
from gdsfactory.components.crossing_waveguide import (
    compensation_path,
    crossing,
    crossing45,
    crossing_arm,
    crossing_etched,
    crossing_from_taper,
)
from gdsfactory.components.cutback_bend import (
    cutback_bend,
    cutback_bend90,
    cutback_bend90circular,
    cutback_bend180,
    cutback_bend180circular,
    staircase,
)
from gdsfactory.components.cutback_component import (
    cutback_component,
    cutback_component_mirror,
)
from gdsfactory.components.dbr import dbr
from gdsfactory.components.dbr_tapered import dbr_tapered
from gdsfactory.components.delay_snake import delay_snake
from gdsfactory.components.delay_snake2 import delay_snake2
from gdsfactory.components.delay_snake3 import delay_snake3
from gdsfactory.components.delay_snake_sbend import delay_snake_sbend
from gdsfactory.components.dicing_lane import dicing_lane
from gdsfactory.components.die import die
from gdsfactory.components.die_bbox import die_bbox
from gdsfactory.components.die_bbox_frame import die_bbox_frame
from gdsfactory.components.disk import disk
from gdsfactory.components.ellipse import ellipse
from gdsfactory.components.extend_ports_list import extend_ports_list
from gdsfactory.components.extension import extend_port, extend_ports
from gdsfactory.components.fiber import fiber
from gdsfactory.components.fiber_array import fiber_array
from gdsfactory.components.grating_coupler_array import grating_coupler_array
from gdsfactory.components.grating_coupler_circular import grating_coupler_circular
from gdsfactory.components.grating_coupler_elliptical import (
    ellipse_arc,
    grating_coupler_elliptical,
    grating_coupler_elliptical_te,
    grating_coupler_elliptical_tm,
    grating_taper_points,
    grating_tooth_points,
)
from gdsfactory.components.grating_coupler_elliptical_arbitrary import (
    grating_coupler_elliptical_arbitrary,
)
from gdsfactory.components.grating_coupler_elliptical_lumerical import (
    grating_coupler_elliptical_lumerical,
)
from gdsfactory.components.grating_coupler_elliptical_trenches import (
    grating_coupler_elliptical_trenches,
    grating_coupler_te,
    grating_coupler_tm,
)
from gdsfactory.components.grating_coupler_loss import (
    grating_coupler_loss_fiber_array,
    grating_coupler_loss_fiber_array4,
    loss_deembedding_ch12_34,
    loss_deembedding_ch13_24,
    loss_deembedding_ch14_23,
)
from gdsfactory.components.grating_coupler_loss_fiber_single import (
    grating_coupler_loss_fiber_single,
)
from gdsfactory.components.grating_coupler_rectangular import (
    grating_coupler_rectangular,
)
from gdsfactory.components.grating_coupler_rectangular_arbitrary import (
    grating_coupler_rectangular_arbitrary,
)
from gdsfactory.components.grating_coupler_rectangular_arbitrary_slab import (
    grating_coupler_rectangular_arbitrary_slab,
)
from gdsfactory.components.grating_coupler_tree import grating_coupler_tree
from gdsfactory.components.hline import hline
from gdsfactory.components.L import L
from gdsfactory.components.litho_calipers import litho_calipers
from gdsfactory.components.litho_ruler import litho_ruler
from gdsfactory.components.litho_steps import litho_steps
from gdsfactory.components.logo import logo
from gdsfactory.components.loop_mirror import loop_mirror
from gdsfactory.components.mmi1x2 import mmi1x2
from gdsfactory.components.mmi2x2 import mmi2x2
from gdsfactory.components.mzi import mzi, mzi1x2_2x2, mzi2x2_2x2, mzi_coupler
from gdsfactory.components.mzi_arm import mzi_arm
from gdsfactory.components.mzi_arms import mzi_arms
from gdsfactory.components.mzi_lattice import mzi_lattice
from gdsfactory.components.mzi_pads_center import mzi_pads_center
from gdsfactory.components.mzi_phase_shifter import (
    mzi_phase_shifter,
    mzi_phase_shifter_top_heater_metal,
)
from gdsfactory.components.mzit import mzit
from gdsfactory.components.mzit_lattice import mzit_lattice
from gdsfactory.components.nxn import nxn
from gdsfactory.components.pack_doe import pack_doe, pack_doe_grid
from gdsfactory.components.pad import (
    pad,
    pad_array,
    pad_array0,
    pad_array90,
    pad_array180,
    pad_array270,
)
from gdsfactory.components.pad_gsg import pad_gsg_open, pad_gsg_short
from gdsfactory.components.pads_shorted import pads_shorted
from gdsfactory.components.ramp import ramp
from gdsfactory.components.rectangle import rectangle
from gdsfactory.components.rectangle_with_slits import rectangle_with_slits
from gdsfactory.components.resistance_meander import resistance_meander
from gdsfactory.components.resistance_sheet import resistance_sheet
from gdsfactory.components.ring import ring
from gdsfactory.components.ring_double import ring_double
from gdsfactory.components.ring_double_heater import ring_double_heater
from gdsfactory.components.ring_single import ring_single
from gdsfactory.components.ring_single_array import ring_single_array
from gdsfactory.components.ring_single_dut import ring_single_dut, taper2
from gdsfactory.components.ring_single_heater import ring_single_heater
from gdsfactory.components.seal_ring import seal_ring
from gdsfactory.components.spiral import spiral
from gdsfactory.components.spiral_circular import spiral_circular
from gdsfactory.components.spiral_external_io import spiral_external_io
from gdsfactory.components.spiral_inner_io import (
    spiral_inner_io,
    spiral_inner_io_fiber_single,
)
from gdsfactory.components.splitter_chain import splitter_chain
from gdsfactory.components.splitter_tree import splitter_tree
from gdsfactory.components.straight import straight
from gdsfactory.components.straight_array import straight_array
from gdsfactory.components.straight_heater_doped_rib import straight_heater_doped_rib
from gdsfactory.components.straight_heater_doped_strip import (
    straight_heater_doped_strip,
)
from gdsfactory.components.straight_heater_meander import straight_heater_meander
from gdsfactory.components.straight_heater_metal import (
    straight_heater_metal,
    straight_heater_metal_90_90,
    straight_heater_metal_undercut,
    straight_heater_metal_undercut_90_90,
)
from gdsfactory.components.straight_pin import straight_pin, straight_pn
from gdsfactory.components.straight_pin_slot import straight_pin_slot
from gdsfactory.components.straight_rib import straight_rib, straight_rib_tapered
from gdsfactory.components.switch_tree import switch_tree
from gdsfactory.components.taper import (
    taper,
    taper_strip_to_ridge,
    taper_strip_to_ridge_trenches,
)
from gdsfactory.components.taper_cross_section import (
    taper_cross_section_linear,
    taper_cross_section_sine,
)
from gdsfactory.components.taper_from_csv import (
    taper_0p5_to_3_l36,
    taper_from_csv,
    taper_w10_l100,
    taper_w10_l150,
    taper_w10_l200,
    taper_w11_l200,
    taper_w12_l200,
)
from gdsfactory.components.taper_parabolic import taper_parabolic
from gdsfactory.components.text import text, text_lines
from gdsfactory.components.text_rectangular import (
    text_rectangular,
    text_rectangular_multi_layer,
)
from gdsfactory.components.triangle import triangle, triangle2, triangle4
from gdsfactory.components.verniers import verniers
from gdsfactory.components.version_stamp import pixel, qrcode, version_stamp
from gdsfactory.components.via import via, via1, via2, viac
from gdsfactory.components.via_cutback import via_cutback
from gdsfactory.components.via_stack import (
    via_stack,
    via_stack_heater_m3,
    via_stack_slab_m3,
)
from gdsfactory.components.via_stack_slot import via_stack_slot, via_stack_slot_m1_m2
from gdsfactory.components.via_stack_with_offset import via_stack_with_offset
from gdsfactory.components.waveguide_template import strip
from gdsfactory.components.wire import wire_corner, wire_straight
from gdsfactory.components.wire_sbend import wire_sbend
from gdsfactory.get_factories import get_cells

_factory_passives = dict(
    bend_circular=bend_circular,
    bend_euler=bend_euler,
    bend_euler_s=bend_euler_s,
    bend_s=bend_s,
    cdc=cdc,
    coupler=coupler,
    coupler_adiabatic=coupler_adiabatic,
    coupler_asymmetric=coupler_asymmetric,
    coupler_full=coupler_full,
    coupler_ring=coupler_ring,
    coupler_symmetric=coupler_symmetric,
    crossing=crossing,
    crossing45=crossing45,
    taper_cross_section_linear=taper_cross_section_linear,
    taper_cross_section_sine=taper_cross_section_sine,
    taper=taper,
    taper2=taper2,
    taper_0p5_to_3_l36=taper_0p5_to_3_l36,
    taper_from_csv=taper_from_csv,
    taper_strip_to_ridge=taper_strip_to_ridge,
    taper_strip_to_ridge_trenches=taper_strip_to_ridge_trenches,
    taper_w10_l100=taper_w10_l100,
    taper_w10_l150=taper_w10_l150,
    taper_w10_l200=taper_w10_l200,
    taper_w11_l200=taper_w11_l200,
    taper_w12_l200=taper_w12_l200,
    mmi1x2=mmi1x2,
    mmi2x2=mmi2x2,
)
__all__ = [
    "C",
    "L",
    "add_fidutials",
    "add_fidutials_offsets",
    "add_frame",
    "align",
    "align_wafer",
    "array",
    "array_with_fanout",
    "array_with_fanout_2d",
    "array_with_via",
    "array_with_via_2d",
    "awg",
    "bbox",
    "bend_circular",
    "bend_circular180",
    "bend_circular_heater",
    "bend_euler",
    "bend_euler180",
    "bend_euler_s",
    "bend_port",
    "bend_s",
    "bend_straight_bend",
    "cavity",
    "cdsem_all",
    "circle",
    "compass",
    "compensation_path",
    "component_lattice",
    "component_sequence",
    "via_stack",
    "via_stack_heater_m3",
    "via_stack_slab_m3",
    "via_stack_slot",
    "via_stack_slot_m1_m2",
    "via_stack_with_offset",
    "copy_layers",
    "coupler",
    "coupler90",
    "coupler90bend",
    "coupler90circular",
    "coupler_adiabatic",
    "coupler_asymmetric",
    "coupler_full",
    "coupler_ring",
    "coupler_straight",
    "coupler_symmetric",
    "cross",
    "crossing",
    "crossing45",
    "crossing_arm",
    "crossing_etched",
    "crossing_from_taper",
    "crossing_waveguide",
    "cutback_bend",
    "cutback_bend180",
    "cutback_bend180circular",
    "cutback_bend90",
    "cutback_bend90circular",
    "cutback_component",
    "cutback_component_mirror",
    "dbr",
    "dbr_tapered",
    "delay_snake",
    "delay_snake2",
    "delay_snake3",
    "delay_snake_sbend",
    "die",
    "dicing_lane",
    "die_bbox",
    "die_bbox_frame",
    "disk",
    "ellipse",
    "ellipse_arc",
    "extend_port",
    "extend_ports",
    "extend_ports_list",
    "extension",
    "fiber",
    "fiber_array",
    "text_lines",
    "grating_coupler_array",
    "grating_coupler_circular",
    "grating_coupler_elliptical",
    "grating_coupler_elliptical_arbitrary",
    "grating_coupler_elliptical_lumerical",
    "grating_coupler_elliptical_te",
    "grating_coupler_elliptical_tm",
    "grating_coupler_elliptical_trenches",
    "grating_coupler_functions",
    "grating_coupler_loss",
    "grating_coupler_loss_fiber_array",
    "grating_coupler_loss_fiber_array4",
    "grating_coupler_loss_fiber_single",
    "grating_coupler_rectangular",
    "grating_coupler_rectangular_arbitrary",
    "grating_coupler_rectangular_arbitrary_slab",
    "grating_coupler_te",
    "grating_coupler_tm",
    "grating_coupler_tree",
    "grating_taper_points",
    "grating_tooth_points",
    "hline",
    "litho_calipers",
    "litho_ruler",
    "litho_steps",
    "logo",
    "loop_mirror",
    "loss_deembedding_ch12_34",
    "loss_deembedding_ch13_24",
    "loss_deembedding_ch14_23",
    "mmi1x2",
    "mmi2x2",
    "mzi",
    "mzi_arms",
    "mzi_pads_center",
    "mzi1x2_2x2",
    "mzi2x2_2x2",
    "mzi_coupler",
    "mzi_arm",
    "mzi_lattice",
    "mzi_phase_shifter",
    "mzi_phase_shifter_top_heater_metal",
    "mzit",
    "mzit_lattice",
    "nxn",
    "pack_doe_grid",
    "pack_doe",
    "pad",
    "pad_array",
    "pad_array0",
    "pad_array180",
    "pad_array270",
    "pad_array90",
    "pad_gsg",
    "pad_gsg_open",
    "pad_gsg_short",
    "pads_shorted",
    "pixel",
    "qrcode",
    "ramp",
    "rectangle",
    "rectangle_with_slits",
    "resistance_meander",
    "resistance_sheet",
    "ring",
    "ring_double",
    "ring_double_heater",
    "ring_single",
    "ring_single_heater",
    "ring_single_array",
    "ring_single_dut",
    "seal_ring",
    "spiral",
    "spiral_circular",
    "spiral_external_io",
    "spiral_inner_io",
    "spiral_inner_io_fiber_single",
    "splitter_chain",
    "splitter_tree",
    "staircase",
    "straight",
    "straight_array",
    "straight_heater_doped_rib",
    "straight_heater_doped_strip",
    "straight_heater_metal",
    "straight_heater_metal_90_90",
    "straight_heater_metal_undercut",
    "straight_heater_metal_undercut_90_90",
    "straight_heater_meander",
    "straight_pin",
    "straight_pin_slot",
    "straight_pn",
    "straight_rib",
    "straight_rib_tapered",
    "strip",
    "switch_tree",
    "taper",
    "taper2",
    "taper_0p5_to_3_l36",
    "taper_from_csv",
    "taper_parabolic",
    "taper_strip_to_ridge",
    "taper_strip_to_ridge_trenches",
    "taper_w10_l100",
    "taper_w10_l150",
    "taper_w10_l200",
    "taper_w11_l200",
    "taper_w12_l200",
    "text",
    "text_rectangular",
    "text_rectangular_multi_layer",
    "triangle",
    "triangle2",
    "triangle4",
    "verniers",
    "version_stamp",
    "via",
    "via1",
    "via2",
    "via_cutback",
    "viac",
    "waveguide_template",
    "wire",
    "wire_corner",
    "wire_sbend",
    "wire_straight",
]

cells = get_cells(sys.modules[__name__])


if __name__ == "__main__":
    from gdsfactory.cell import CELLS

    print(len(cells.keys()))
    print(len(CELLS.keys()))
    print(set(CELLS.keys()) - set(cells.keys()))

    print("cells")
    for i in cells.keys():
        print(i)

    print()
    print("CELLS")
    for i in CELLS.keys():
        print(i)
