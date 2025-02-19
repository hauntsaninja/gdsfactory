import numpy as np
import pytest

import gdsfactory as gf

DEMO_PORT_ANGLE = 10


@pytest.fixture
def shear_waveguide_symmetric():
    P = gf.path.straight(length=10)
    c = gf.path.extrude(
        P, "strip", shear_angle_start=DEMO_PORT_ANGLE, shear_angle_end=DEMO_PORT_ANGLE
    )
    return c


@pytest.fixture
def shear_waveguide_start():
    P = gf.path.straight(length=10)
    c = gf.path.extrude(
        P, "strip", shear_angle_start=DEMO_PORT_ANGLE, shear_angle_end=None
    )
    return c


@pytest.fixture
def shear_waveguide_end():
    P = gf.path.straight(length=10)
    c = gf.path.extrude(
        P, "strip", shear_angle_start=None, shear_angle_end=DEMO_PORT_ANGLE
    )
    return c


@pytest.fixture
def regular_waveguide():
    P = gf.path.straight(length=10)
    c = gf.path.extrude(P, "strip")
    return c


@pytest.fixture
def more_slanted_than_wide():
    P = gf.path.straight(length=0.1)
    c = gf.path.extrude(P, "strip", shear_angle_start=60, shear_angle_end=60)
    return c


@pytest.fixture
def skinny():
    P = gf.path.straight(length=0.1)
    c = gf.path.extrude(P, "strip")
    return c


@pytest.fixture
def linear_taper():
    P = gf.path.straight(length=10)

    s = gf.Section(width=3, offset=0, layer=gf.LAYER.SLAB90, name="slab")
    X1 = gf.CrossSection(
        width=1,
        offset=0,
        layer=gf.LAYER.WG,
        name="core",
        port_names=("o1", "o2"),
        sections=[s],
    )
    s2 = gf.Section(width=2, offset=0, layer=gf.LAYER.SLAB90, name="slab")
    X2 = gf.CrossSection(
        width=0.5,
        offset=0,
        layer=gf.LAYER.WG,
        name="core",
        port_names=("o1", "o2"),
        sections=[s2],
    )
    t = gf.path.transition(X1, X2, width_type="linear")
    c = gf.path.extrude(P, t)
    return c


@pytest.fixture
def linear_taper_sheared():
    P = gf.path.straight(length=10)

    s = gf.Section(width=3, offset=0, layer=gf.LAYER.SLAB90, name="slab")
    X1 = gf.CrossSection(
        width=1,
        offset=0,
        layer=gf.LAYER.WG,
        name="core",
        port_names=("o1", "o2"),
        sections=[s],
    )
    s2 = gf.Section(width=2, offset=0, layer=gf.LAYER.SLAB90, name="slab")
    X2 = gf.CrossSection(
        width=0.5,
        offset=0,
        layer=gf.LAYER.WG,
        name="core",
        port_names=("o1", "o2"),
        sections=[s2],
    )
    t = gf.path.transition(X1, X2, width_type="linear")
    c = gf.path.extrude(P, t, shear_angle_start=10, shear_angle_end=None)
    return c


@pytest.fixture
def curve():
    P = gf.path.euler()
    c = gf.path.extrude(P, "strip")
    return c


@pytest.fixture
def curve_sheared():
    angle = 15
    P = gf.path.euler()
    c = gf.path.extrude(P, "strip", shear_angle_start=angle, shear_angle_end=angle)
    return c


def test_mate_on_shear_xor_empty(
    regular_waveguide, shear_waveguide_start, shear_waveguide_end
):
    # two sheared components joined at the sheared port should appear the same as two straight component joined
    two_straights = gf.Component()
    c1 = two_straights << regular_waveguide
    c2 = two_straights << regular_waveguide
    c2.connect("o1", c1.ports["o2"])

    two_shears = gf.Component()
    c1 = two_shears << shear_waveguide_end
    c2 = two_shears << shear_waveguide_start
    c2.connect("o1", c1.ports["o2"])

    xor = gf.geometry.xor_diff(two_straights, two_shears)
    assert not xor.layers


def test_rotations_are_normal(
    regular_waveguide, shear_waveguide_start, shear_waveguide_end
):
    two_shears = gf.Component()
    c1 = two_shears << shear_waveguide_end
    c2 = two_shears << shear_waveguide_start
    c2.connect("o1", c1.ports["o2"])

    assert c2.rotation % 90 == 0


def test_area_stays_same(
    regular_waveguide,
    shear_waveguide_start,
    shear_waveguide_end,
    shear_waveguide_symmetric,
):
    components = [
        regular_waveguide,
        shear_waveguide_start,
        shear_waveguide_end,
        shear_waveguide_symmetric,
    ]
    areas = [c.area() for c in components]
    np.testing.assert_allclose(areas, desired=areas[0])


def test_area_stays_same_skinny(
    skinny,
    more_slanted_than_wide,
):
    components = [
        skinny,
        more_slanted_than_wide,
    ]
    areas = [c.area() for c in components]
    np.testing.assert_allclose(areas, desired=areas[0])


# def test_area_stays_same_curve(
#     curve,
#     curve_sheared,
# ):
#     components = [
#         curve,
#         curve_sheared,
#     ]
#     areas = [c.area() for c in components]
#     np.testing.assert_allclose(areas, desired=areas[0], atol=1e-5)


def test_mate_on_shear_xor_empty_transition(linear_taper, linear_taper_sheared):
    # two sheared components joined at the sheared port should appear the same as two straight component joined
    two_straights = gf.Component()
    c1 = two_straights << linear_taper
    c2 = two_straights << linear_taper
    c2.connect("o1", c1.ports["o2"])

    two_shears = gf.Component()
    c1 = two_shears << linear_taper_sheared
    c2 = two_shears << linear_taper_sheared
    c2.connect("o1", c1.ports["o1"])

    xor = gf.geometry.xor_diff(two_straights, two_shears)
    assert not xor.layers


def test_mate_on_shear_xor_empty_curve(curve, curve_sheared):
    # two sheared components joined at the sheared port should appear the same as two straight component joined
    two_straights = gf.Component()
    c1 = two_straights << curve
    c2 = two_straights << curve
    c2.connect("o1", c1.ports["o2"])

    two_shears = gf.Component()
    c1 = two_shears << curve_sheared
    c2 = two_shears << curve_sheared
    c2.connect("o1", c1.ports["o1"])

    xor = gf.geometry.xor_diff(two_straights, two_shears)
    assert not xor.layers


def test_shear_angle_annotated_on_ports(shear_waveguide_start, shear_waveguide_end):
    assert shear_waveguide_start.ports["o1"].shear_angle == DEMO_PORT_ANGLE
    assert shear_waveguide_start.ports["o2"].shear_angle is None

    assert shear_waveguide_end.ports["o2"].shear_angle == DEMO_PORT_ANGLE
    assert shear_waveguide_end.ports["o1"].shear_angle is None


def test_port_attributes(regular_waveguide, shear_waveguide_symmetric):
    regular_ports = [p.to_dict() for p in regular_waveguide.ports.values()]
    shear_ports = [p.to_dict() for p in shear_waveguide_symmetric.ports.values()]

    for p in shear_ports:
        shear_angle = p.pop("shear_angle")
        assert shear_angle == DEMO_PORT_ANGLE

    for p1, p2 in zip(regular_ports, shear_ports):
        for k in p.keys():
            assert p1[k] == p2[k], f"{k} differs! {p1[k]} != {p2[k]}"


if __name__ == "__main__":
    P = gf.path.straight(length=10)
    regular_waveguide1 = gf.path.extrude(P, "strip")
    P = gf.path.straight(length=10)
    shear_waveguide_symmetric1 = gf.path.extrude(
        P, "strip", shear_angle_start=DEMO_PORT_ANGLE, shear_angle_end=DEMO_PORT_ANGLE
    )
    c = test_port_attributes(
        regular_waveguide=regular_waveguide1,
        shear_waveguide_symmetric=shear_waveguide_symmetric1,
    )
