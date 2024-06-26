from typing import List, Optional

from facefusion.typing import Angle, Score, LogLevel, ExecutionProviderKey, VideoMemoryStrategy, FaceSelectorMode, FaceSelectorOrder, FaceSelectorAge, FaceSelectorGender, FaceMaskType, FaceMaskRegion, OutputAudioEncoder, OutputVideoEncoder, OutputVideoPreset, FaceDetectorModel, FaceRecognizerModel, TempFrameFormat, Padding

# general
config_path : Optional[str] = None
source_paths : Optional[List[str]] = None
target_path : Optional[str] = None
output_path : Optional[str] = None
jobs_path : Optional[str] = None
# misc
force_download : Optional[bool] = None
skip_download : Optional[bool] = None
headless : Optional[bool] = None
log_level : Optional[LogLevel] = None
# execution
execution_device_id : Optional[str] = None
execution_providers : List[ExecutionProviderKey] = []
execution_thread_count : Optional[int] = None
execution_queue_count : Optional[int] = None
# memory
video_memory_strategy : Optional[VideoMemoryStrategy] = None
system_memory_limit : Optional[int] = None
# face analyser
face_detector_model : Optional[FaceDetectorModel] = None
face_detector_size : Optional[str] = None
face_detector_angles : Optional[List[Angle]] = None
face_detector_score : Optional[Score] = None
face_landmarker_score : Optional[Score] = None
face_recognizer_model : Optional[FaceRecognizerModel] = None
# face selector
face_selector_mode : Optional[FaceSelectorMode] = None
face_selector_order : Optional[FaceSelectorOrder] = None
face_selector_age : Optional[FaceSelectorAge] = None
face_selector_gender : Optional[FaceSelectorGender] = None
reference_face_position : Optional[int] = None
reference_face_distance : Optional[float] = None
reference_frame_number : Optional[int] = None
# face mask
face_mask_types : Optional[List[FaceMaskType]] = None
face_mask_blur : Optional[float] = None
face_mask_padding : Optional[Padding] = None
face_mask_regions : Optional[List[FaceMaskRegion]] = None
# frame extraction
trim_frame_start : Optional[int] = None
trim_frame_end : Optional[int] = None
temp_frame_format : Optional[TempFrameFormat] = None
keep_temp : Optional[bool] = None
# output creation
output_image_quality : Optional[int] = None
output_image_resolution : Optional[str] = None
output_audio_encoder : Optional[OutputAudioEncoder] = None
output_video_encoder : Optional[OutputVideoEncoder] = None
output_video_preset : Optional[OutputVideoPreset] = None
output_video_quality : Optional[int] = None
output_video_resolution : Optional[str] = None
output_video_fps : Optional[float] = None
skip_audio : Optional[bool] = None
# frame processors
frame_processors : List[str] = []
# uis
open_browser : Optional[bool] = None
ui_layouts : List[str] = []
