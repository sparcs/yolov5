import setuptools

with open('README.md', 'r', encoding='utf-8') as f:
	long_description = f.read()

setuptools.setup(
	name='yolov5',
	version='0.0.1',
	description='yolov5',
	long_description=long_description,
	long_description_content_type='text/markdown',
	url='https://www.ultralytics.com',
	packages=['models', 'utils'],
	classifiers=[
		'Programming Language :: Python :: 3',
		'Environment :: GPU :: NVIDIA CUDA'
		],
	python_requires='>=3.8',
)
