import os
import numpy as np
import pydicom
from skimage import measure
from stl import mesh


def load_dicom_series(dataset_path):
    slices = []

    # Walk through all folders and subfolders
    for root, dirs, files in os.walk(dataset_path):
        for file in files:
            file_path = os.path.join(root, file)

            try:
                dicom = pydicom.dcmread(file_path)

                if hasattr(dicom, "pixel_array"):
                    slices.append(dicom)

            except:
                continue

    print("Total DICOM slices found:", len(slices))

    if len(slices) == 0:
        raise RuntimeError("No DICOM files found in dataset.")

    # Sort slices by slice position
    try:
        slices.sort(key=lambda x: float(x.ImagePositionPatient[2]))
    except:
        print("Slice sorting skipped.")

    # Stack slices into 3D array
    image_volume = np.stack([s.pixel_array for s in slices])

    return image_volume


def generate_stl(volume, output_name="hip_model.stl"):

    # Extract surface using marching cubes
    verts, faces, normals, values = measure.marching_cubes(volume, level=300)

    # Create STL mesh
    hip_mesh = mesh.Mesh(np.zeros(faces.shape[0], dtype=mesh.Mesh.dtype))

    for i, face in enumerate(faces):
        for j in range(3):
            hip_mesh.vectors[i][j] = verts[face[j], :]

    hip_mesh.save(output_name)

    print("STL file created:", output_name)


def main():

    dataset_folder = "dataset"

    print("Loading DICOM files...")

    volume = load_dicom_series(dataset_folder)

    print("Volume shape:", volume.shape)

    print("Generating 3D model...")

    generate_stl(volume)


if __name__ == "__main__":
    main()
