
from .nodes.comfy_nodes import EasyControlLoadFlux, EasyControlLoadLora, EasyControlLoadMultiLora, EasyControlGenerate, EasyControlLoadStyleLora, EasyControlLoadStyleLoraFromCivitai, EasyControlLoadFluxImg2Img, EasyControlGenerateImg2Img


# 注册节点
NODE_CLASS_MAPPINGS = {
    "EasyControlLoadFlux": EasyControlLoadFlux,
    "EasyControlLoadFlux_Img2Img": EasyControlLoadFluxImg2Img,  # Alias for compatibility
    "EasyControlLoadLora": EasyControlLoadLora,
    "EasyControlLoadMultiLora": EasyControlLoadMultiLora,
    "EasyControlGenerate": EasyControlGenerate,
    "EasyControlGenerate_Img2Img": EasyControlGenerateImg2Img,  # Alias for compatibility
    "EasyControlLoadStyleLora": EasyControlLoadStyleLora,
    "EasyControlLoadStyleLoraFromCivitai": EasyControlLoadStyleLoraFromCivitai,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "EasyControlLoadFlux": "Load EasyControl Flux Model",
    "EasyControlLoadFlux_Img2Img": "Load EasyControl Flux Model for Img2Img",
    "EasyControlLoadLora": "Load EasyControl Lora",
    "EasyControlLoadMultiLora": "Load Multiple EasyControl Loras",
    "EasyControlGenerate": "EasyControl Generate",
    "EasyControlGenerate_Img2Img": "EasyControl Generate for Img2Img",
    "EasyControlLoadStyleLora": "Load EasyControl Style Lora",
    "EasyControlLoadStyleLoraFromCivitai": "Load EasyControl Style Lora from Civitai",
} 
WEB_DIRECTORY = "./web"

__all__ = ['NODE_CLASS_MAPPINGS', 'NODE_DISPLAY_NAME_MAPPINGS', "WEB_DIRECTORY"]