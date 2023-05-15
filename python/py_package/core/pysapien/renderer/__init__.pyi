from __future__ import annotations
import sapien.core.pysapien.renderer
import typing
import numpy
_Shape = typing.Tuple[int, ...]

__all__ = [
    "Context",
    "Cubemap",
    "LineSetObject",
    "Material",
    "Mesh",
    "Model",
    "Node",
    "Object",
    "PointSetObject",
    "PrimitiveSet",
    "Renderer",
    "Scene",
    "Shape",
    "Texture",
    "UIButton",
    "UICheckbox",
    "UIDisplayText",
    "UIGizmo",
    "UIInputFloat",
    "UIInputFloat2",
    "UIInputFloat3",
    "UIInputFloat4",
    "UIInputInt",
    "UIInputInt2",
    "UIInputInt3",
    "UIInputInt4",
    "UIInputText",
    "UIKeyFrame",
    "UIKeyFrameEditor",
    "UIOptions",
    "UISameLine",
    "UISection",
    "UISelectable",
    "UISliderAngle",
    "UISliderFloat",
    "UITreeNode",
    "UIWidget",
    "UIWindow"
]


class Context():
    def create_box_mesh(self) -> Mesh: ...
    def create_brdf_lut(self, size: int = 128) -> Texture: 
        """
        Generate BRDF LUT texture, see https://learnopengl.com/PBR/IBL/Specular-IBL
        """
    def create_capsule_mesh(self, radius: float, half_length: float, segments: int = 32, half_rings: int = 8) -> Mesh: ...
    def create_cone_mesh(self, segments: int = 32) -> Mesh: ...
    def create_cubemap_from_files(self, filenames: typing.List[str[6]], mipmap_levels: int) -> Cubemap: 
        """
        Load cube map, its mipmaps are generated based on roughness, details see https://learnopengl.com/PBR/IBL/Specular-IBL
        """
    def create_line_set(self, vertices: numpy.ndarray[numpy.float32], colors: numpy.ndarray[numpy.float32]) -> PrimitiveSet: ...
    def create_material(self, emission: numpy.ndarray[numpy.float32], base_color: numpy.ndarray[numpy.float32], specular: float, roughness: float, metallic: float, transmission: float = 0.0, ior: float = 1.0099999904632568) -> Material: ...
    def create_mesh_from_array(self, vertices: numpy.ndarray[numpy.float32], indices: numpy.ndarray[numpy.uint32], normals: numpy.ndarray[numpy.float32] = array([], dtype=float32), uvs: numpy.ndarray[numpy.float32] = array([], dtype=float32)) -> Mesh: ...
    def create_model(self, meshes: typing.List[Mesh], materials: typing.List[Material]) -> Model: ...
    def create_model_from_file(self, filename: str) -> Model: ...
    def create_point_set(self, vertices: numpy.ndarray[numpy.float32], colors: numpy.ndarray[numpy.float32]) -> PrimitiveSet: ...
    def create_texture_from_file(self, filename: str, mipmap_levels: int, filter: str = 'linear', address_mode: str = 'repeat') -> Texture: ...
    def create_uvsphere_mesh(self, segments: int = 32, half_rings: int = 16) -> Mesh: ...
    pass
class Cubemap():
    pass
class Node():
    def set_position(self, position: numpy.ndarray[numpy.float32]) -> None: ...
    def set_rotation(self, quat: numpy.ndarray[numpy.float32]) -> None: ...
    def set_scale(self, scale: numpy.ndarray[numpy.float32]) -> None: ...
    @property
    def children(self) -> typing.List[Node]:
        """
        :type: typing.List[Node]
        """
    @property
    def position(self) -> numpy.ndarray[numpy.float32]:
        """
        :type: numpy.ndarray[numpy.float32]
        """
    @property
    def rotation(self) -> numpy.ndarray[numpy.float32]:
        """
        :type: numpy.ndarray[numpy.float32]
        """
    @property
    def scale(self) -> numpy.ndarray[numpy.float32]:
        """
        :type: numpy.ndarray[numpy.float32]
        """
    pass
class Material():
    def set_base_color(self, rgba: numpy.ndarray[numpy.float32]) -> None: ...
    def set_emission(self, emission: float) -> None: ...
    def set_metallic(self, metallic: float) -> None: ...
    def set_roughness(self, roughness: float) -> None: ...
    def set_specular(self, specular: float) -> None: ...
    def set_textures(self, base_color: Texture = None, roughness: Texture = None, normal: Texture = None, metallic: Texture = None, emission: Texture = None, transmission: Texture = None) -> None: ...
    def set_transmission(self, transmission: float) -> None: ...
    pass
class Mesh():
    pass
class Model():
    pass
class LineSetObject(Node):
    pass
class Object(Node):
    @property
    def cast_shadow(self) -> bool:
        """
        :type: bool
        """
    @cast_shadow.setter
    def cast_shadow(self, arg1: bool) -> None:
        pass
    @property
    def model(self) -> Model:
        """
        :type: Model
        """
    @property
    def shading_mode(self) -> int:
        """
        :type: int
        """
    @shading_mode.setter
    def shading_mode(self, arg1: int) -> None:
        pass
    @property
    def transparency(self) -> float:
        """
        :type: float
        """
    @transparency.setter
    def transparency(self, arg1: float) -> None:
        pass
    pass
class PointSetObject(Node):
    pass
class PrimitiveSet():
    pass
class Renderer():
    def set_custom_cubemap(self, name: str, texture: Cubemap) -> None: ...
    @typing.overload
    def set_custom_property(self, name: str, value: float) -> None: ...
    @typing.overload
    def set_custom_property(self, name: str, value: int) -> None: ...
    def set_custom_texture(self, name: str, texture: Texture) -> None: ...
    pass
class Scene():
    def add_line_set(self, line_set: PrimitiveSet, parent: Node = None) -> LineSetObject: ...
    def add_node(self, parent: Node = None) -> Node: ...
    def add_object(self, model: Model, parent: Node = None) -> Object: ...
    def add_point_set(self, point_set: PrimitiveSet, parent: Node = None) -> PointSetObject: ...
    def remove_node(self, node: Node) -> None: ...
    pass
class Shape():
    pass
class Texture():
    pass
class UIWidget():
    def get_children(self) -> typing.List[UIWidget]: ...
    def remove(self) -> None: ...
    def remove_children(self) -> None: ...
    pass
class UICheckbox(UIWidget):
    def Callback(self, func: typing.Callable[[UICheckbox], None]) -> UICheckbox: ...
    def Checked(self, checked: bool) -> UICheckbox: ...
    def Label(self, label: str) -> UICheckbox: ...
    def __init__(self) -> None: ...
    @property
    def checked(self) -> bool:
        """
        :type: bool
        """
    pass
class UIDisplayText(UIWidget):
    def Text(self, text: str) -> UIDisplayText: ...
    def __init__(self) -> None: ...
    pass
class UIGizmo(UIWidget):
    def CameraMatrices(self, arg0: numpy.ndarray[numpy.float32], arg1: numpy.ndarray[numpy.float32]) -> None: ...
    def Matrix(self, matrix: numpy.ndarray[numpy.float32]) -> UIGizmo: ...
    def __init__(self) -> None: ...
    @property
    def matrix(self) -> numpy.ndarray[numpy.float32]:
        """
        :type: numpy.ndarray[numpy.float32]
        """
    pass
class UIInputFloat(UIWidget):
    def Callback(self, func: typing.Callable[[UIInputFloat], None]) -> UIInputFloat: ...
    def Label(self, label: str) -> UIInputFloat: ...
    def ReadOnly(self, read_only: bool) -> UIInputFloat: ...
    def Value(self, value: float) -> UIInputFloat: ...
    def __init__(self) -> None: ...
    @property
    def value(self) -> float:
        """
        :type: float
        """
    pass
class UIInputFloat2(UIWidget):
    def Callback(self, func: typing.Callable[[UIInputFloat2], None]) -> UIInputFloat2: ...
    def Label(self, label: str) -> UIInputFloat2: ...
    def ReadOnly(self, read_only: bool) -> UIInputFloat2: ...
    def Value(self, value: numpy.ndarray[numpy.float32]) -> UIInputFloat2: ...
    def __init__(self) -> None: ...
    @property
    def value(self) -> numpy.ndarray[numpy.float32]:
        """
        :type: numpy.ndarray[numpy.float32]
        """
    pass
class UIInputFloat3(UIWidget):
    def Callback(self, func: typing.Callable[[UIInputFloat3], None]) -> UIInputFloat3: ...
    def Label(self, label: str) -> UIInputFloat3: ...
    def ReadOnly(self, read_only: bool) -> UIInputFloat3: ...
    def Value(self, value: numpy.ndarray[numpy.float32]) -> UIInputFloat3: ...
    def __init__(self) -> None: ...
    @property
    def value(self) -> numpy.ndarray[numpy.float32]:
        """
        :type: numpy.ndarray[numpy.float32]
        """
    pass
class UIInputFloat4(UIWidget):
    def Callback(self, func: typing.Callable[[UIInputFloat4], None]) -> UIInputFloat4: ...
    def Label(self, label: str) -> UIInputFloat4: ...
    def ReadOnly(self, read_only: bool) -> UIInputFloat4: ...
    def Value(self, value: numpy.ndarray[numpy.float32]) -> UIInputFloat4: ...
    def __init__(self) -> None: ...
    @property
    def value(self) -> numpy.ndarray[numpy.float32]:
        """
        :type: numpy.ndarray[numpy.float32]
        """
    pass
class UIInputInt(UIWidget):
    def Callback(self, func: typing.Callable[[UIInputInt], None]) -> UIInputInt: ...
    def Label(self, label: str) -> UIInputInt: ...
    def ReadOnly(self, read_only: bool) -> UIInputInt: ...
    def Value(self, value: int) -> UIInputInt: ...
    def __init__(self) -> None: ...
    @property
    def value(self) -> int:
        """
        :type: int
        """
    pass
class UIInputInt2(UIWidget):
    def Callback(self, func: typing.Callable[[UIInputInt2], None]) -> UIInputInt2: ...
    def Label(self, label: str) -> UIInputInt2: ...
    def ReadOnly(self, read_only: bool) -> UIInputInt2: ...
    def Value(self, value: numpy.ndarray[numpy.int32]) -> UIInputInt2: ...
    def __init__(self) -> None: ...
    @property
    def value(self) -> numpy.ndarray[numpy.int32]:
        """
        :type: numpy.ndarray[numpy.int32]
        """
    pass
class UIInputInt3(UIWidget):
    def Callback(self, func: typing.Callable[[UIInputInt3], None]) -> UIInputInt3: ...
    def Label(self, label: str) -> UIInputInt3: ...
    def ReadOnly(self, read_only: bool) -> UIInputInt3: ...
    def Value(self, value: numpy.ndarray[numpy.int32]) -> UIInputInt3: ...
    def __init__(self) -> None: ...
    @property
    def value(self) -> numpy.ndarray[numpy.int32]:
        """
        :type: numpy.ndarray[numpy.int32]
        """
    pass
class UIInputInt4(UIWidget):
    def Callback(self, func: typing.Callable[[UIInputInt4], None]) -> UIInputInt4: ...
    def Label(self, label: str) -> UIInputInt4: ...
    def ReadOnly(self, read_only: bool) -> UIInputInt4: ...
    def Value(self, value: numpy.ndarray[numpy.int32]) -> UIInputInt4: ...
    def __init__(self) -> None: ...
    @property
    def value(self) -> numpy.ndarray[numpy.int32]:
        """
        :type: numpy.ndarray[numpy.int32]
        """
    pass
class UIInputText(UIWidget):
    def Callback(self, func: typing.Callable[[UIInputText], None]) -> UIInputText: ...
    def Label(self, label: str) -> UIInputText: ...
    def ReadOnly(self, read_only: bool) -> UIInputText: ...
    def Size(self, size: int) -> UIInputText: ...
    def Value(self, value: str) -> UIInputText: ...
    def __init__(self) -> None: ...
    @property
    def value(self) -> str:
        """
        :type: str
        """
    pass
class UIKeyFrame():
    def get_id(self) -> int: ...
    @property
    def frame(self) -> int:
        """
        :type: int
        """
    pass
class UIKeyFrameEditor(UIWidget):
    def DeleteKeyFrameCallback(self, func: typing.Callable[[UIKeyFrameEditor], None]) -> UIKeyFrameEditor: ...
    def InsertKeyFrameCallback(self, func: typing.Callable[[UIKeyFrameEditor], None]) -> UIKeyFrameEditor: ...
    def LoadKeyFrameCallback(self, func: typing.Callable[[UIKeyFrameEditor], None]) -> UIKeyFrameEditor: ...
    def UpdateKeyFrameCallback(self, func: typing.Callable[[UIKeyFrameEditor], None]) -> UIKeyFrameEditor: ...
    def __init__(self, arg0: float) -> None: ...
    def get_current_frame(self) -> int: ...
    def get_key_frame_to_modify(self) -> int: ...
    def get_key_frames_in_used(self) -> typing.List[UIKeyFrame]: ...
    pass
class UIOptions(UIWidget):
    def Callback(self, func: typing.Callable[[UIOptions], None]) -> UIOptions: ...
    def Index(self, index: int) -> UIOptions: ...
    def Items(self, items: typing.List[str]) -> UIOptions: ...
    def Label(self, label: str) -> UIOptions: ...
    def Style(self, style: str) -> UIOptions: ...
    def __init__(self) -> None: ...
    @property
    def index(self) -> int:
        """
        :type: int
        """
    @property
    def value(self) -> str:
        """
        :type: str
        """
    pass
class UISameLine(UIWidget):
    def Offset(self, offset: float) -> UISameLine: ...
    def Spacing(self, spacing: float) -> UISameLine: ...
    def __init__(self) -> None: ...
    def append(self, *args) -> UISameLine: ...
    pass
class UISection(UIWidget):
    def Expanded(self, expanded: bool) -> UISection: ...
    def Label(self, label: str) -> UISection: ...
    def __init__(self) -> None: ...
    def append(self, *args) -> UISection: ...
    pass
class UISelectable(UIWidget):
    def Callback(self, func: typing.Callable[[UISelectable], None]) -> UISelectable: ...
    def Label(self, label: str) -> UISelectable: ...
    def Selected(self, selected: bool) -> UISelectable: ...
    def __init__(self) -> None: ...
    @property
    def value(self) -> bool:
        """
        :type: bool
        """
    pass
class UISliderAngle(UIWidget):
    def Callback(self, func: typing.Callable[[UISliderAngle], None]) -> UISliderAngle: ...
    def Label(self, label: str) -> UISliderAngle: ...
    def Max(self, max: float) -> UISliderAngle: ...
    def Min(self, min: float) -> UISliderAngle: ...
    def Value(self, value: float) -> UISliderAngle: ...
    def Width(self, width: float) -> UISliderAngle: ...
    def __init__(self) -> None: ...
    @property
    def value(self) -> float:
        """
        :type: float
        """
    pass
class UISliderFloat(UIWidget):
    def Callback(self, func: typing.Callable[[UISliderFloat], None]) -> UISliderFloat: ...
    def Label(self, label: str) -> UISliderFloat: ...
    def Max(self, max: float) -> UISliderFloat: ...
    def Min(self, min: float) -> UISliderFloat: ...
    def Value(self, value: float) -> UISliderFloat: ...
    def Width(self, width: float) -> UISliderFloat: ...
    def __init__(self) -> None: ...
    @property
    def value(self) -> float:
        """
        :type: float
        """
    pass
class UITreeNode(UIWidget):
    def Label(self, label: str) -> UITreeNode: ...
    def __init__(self) -> None: ...
    def append(self, *args) -> UITreeNode: ...
    pass
class UIButton(UIWidget):
    def Callback(self, func: typing.Callable[[UIButton], None]) -> UIButton: ...
    def Label(self, label: str) -> UIButton: ...
    def __init__(self) -> None: ...
    pass
class UIWindow(UIWidget):
    def Label(self, label: str) -> UIWindow: ...
    def Pos(self, x: float, y: float) -> UIWindow: ...
    def Size(self, x: float, y: float) -> UIWindow: ...
    def __init__(self) -> None: ...
    def append(self, *args) -> UIWindow: ...
    pass
