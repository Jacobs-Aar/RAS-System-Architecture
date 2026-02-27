from setuptools import find_packages, setup

package_name = 'vision_perception'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools', 'opencv-python', 'numpy'],
    zip_safe=True,
    maintainer='Your Name',
    maintainer_email='your_email@example.com',
    description='ZED2i line detection and 2D mapping node',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            # This links the executable name 'line_mapper' to the main() function 
            # inside your src/vision_perception/vision_perception/line_mapper.py file
            'line_mapper = vision_perception.line_mapper:main'
        ],
    },
)