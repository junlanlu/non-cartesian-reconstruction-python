"""Import and export util functions."""
import sys

sys.path.append("..")
from typing import Any, Dict, Optional

import nibabel as nib
import numpy as np
import scipy.io as sio


def import_mat(path: str) -> Dict[str, Any]:
    """Import  matlab file as dictionary.

    Args:
        path: str file path of matlab file
    Returns:
        dictionary loaded from matlab file
    """
    return sio.loadmat(path)


def export_nii(image: np.ndarray, path: str, fov: Optional[float] = None):
    """Export image as nifti file.

    Args:
        image: np.ndarray 3D image to be exporetd
        path: str file path of nifti file
        fov: float field of view
    """
    nii_imge = nib.Nifti1Image(image, np.eye(4))
    nib.save(nii_imge, path)
