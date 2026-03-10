#3D Hip Joint Model from CT DICOM Images

Project Description:

This project reconstructs a 3D model from CT scan slices stored in DICOM format.
The program loads the CT images, combines them into a 3D volume, and extracts a surface mesh using the Marching Cubes algorithm. The final 3D model is exported in STL format.        

#Dataset

The CT dataset used for this project was obtained from an open-source repository.

Dataset link:
https://www.kaggle.com/datasets/phantomxdata/abdomen-pelvis-ct-collection-phantomx

The dataset contains multiple folders with DICOM slices.


#Dependencies
The following Python libraries are required:
numpy, 

pydicom,

scikit-image, 

numpy-stl, 

scipy and

matlpotlib

Install them using:
pip install -r requirements.txt


How to Run:

1>Place the dataset folder inside the project directory.

2>Open a terminal or command prompt.

3>Navigate to the project folder.

cd project_folder

Run the Python script:
python hip_model.py

Output:

After running the script, a 3D model file will be generated:

hip_model.stl

We can see the 3d constructed model through mesh.
