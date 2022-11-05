from .materials import Material

class Config:
    """Configuration class defining common object attributes"""
    LOWERS_DEPTH: float = 24.
    LOWERS_CASE_MATERIAL = Material.PLY_3_4
    FACE_FRAME_MEMBER_WIDTH = 1.5
    FACE_FRAME_MATERIAL = Material.HARDWOOD_3_4
    OVERLAY_GAP: float = 1/4
    MAX_DRAWER_BOX_HEIGHT: float = 5.
    DRAWER_FACE_INSET_MATERIAL = Material.PLY_1_4
    DRAWER_FACE_INSET_COLOR: str = '#e6cd83'
    DRAWER_BOX_COLOR: str = '#e6cd83'
    FACE_FRAME_COLOR: str = '#6e583b'
    CABINET_CASE_COLOR: str = '#e6cd83'
    
    
