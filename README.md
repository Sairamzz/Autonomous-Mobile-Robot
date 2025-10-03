# Autonomous Mobile Robot

This project focuses on the design and implementation of an Autonomous Mobile Robot (AMR) capable of navigating in an indoor environment using ROS 2, SLAM, and path planning algorithms. The work integrates hardware, perception, control, and planning into a single robotic system.

* [Objective](#Objective)
* [Features](#Features)
* [RobotDesign](#RobotDesign)
* [Implementation](#Implementation)
* [Results](#Results)
* [Contributors](#Contributors)
* [Credits](#Credits)

## Objective:

The objective of this project was to design a mobile robot that can map an environment, localize itself, and autonomously navigate from a start to a goal location while avoiding obstacles. The system leverages modern robotic middleware and integrates multiple subsystems, including perception, motion planning, and control.

## Features:

- ROS 2 Humble framework for modular and scalable system integration.
- SLAM (Simultaneous Localization and Mapping) using Cartographer for real-time map generation.
- Localization with AMCL for robust pose estimation on a known map.
- Navigation2 stack for global and local path planning.
- Obstacle avoidance through integrated sensor feedback.
- Waypoints navigation for multi-goal task execution.
- Custom robot design with CAD/SolidWorks models included in this repository.

### Flowchart of the System

<img width="961" height="460" alt="image" src="https://github.com/user-attachments/assets/38d0d95f-7cc0-408d-8647-b004f5624859" />

## Robot Design:

The robot used in this project was custom-designed to support onboard sensors, computation, and locomotion requirements.
All CAD models and SolidWorks design files can be found in the Robot_Design folder of this repository.

The design emphasizes modularity, sensor mounting flexibility, and robust structural support for indoor navigation tasks.

### CAD MODEL

<img width="710" height="619" alt="image" src="https://github.com/user-attachments/assets/98c34a2d-0b01-4cc2-a45a-ff2c65761e69" />

## Implementation:

The implementation followed a stepwise approach:
1. Simulation in Gazebo
    - Built an indoor environment with obstacles.
    - Deployed the custom robot model in simulation to test SLAM and navigation pipelines.

2. Mapping & Localization
    - Used Cartographer for online SLAM to build occupancy grid maps.
    - Implemented AMCL for probabilistic localization when using a pre-built map.

3. Path Planning
    - Global planner: A* and NavFn to generate optimal paths on the occupancy grid.
    - Local planner: DWB (Dynamic Window Approach) for real-time obstacle avoidance.

4. Navigation
    - ROS 2 Navigation2 stack configured for goal-driven and waypoint-based navigation.
    - Tuned parameters for costmaps, inflation radius, and controller gains.

5. Hardware Deployment
    - Implemented the system on a custom-built robot platform.
    - Integrated onboard sensors including LiDAR, IMU, and wheel encoders.
    - Performed real-world navigation tasks in a closed environment, validating SLAM, localization, and navigation performance.

### Power Connections

<img width="864" height="333" alt="image" src="https://github.com/user-attachments/assets/2f6ea976-c046-4d15-b070-7dd0b9597c39" />

### Mapping Using Slam toolbox

<img width="1410" height="902" alt="image" src="https://github.com/user-attachments/assets/6be27810-43f0-4c93-abc5-54245c2f6453" />

## Results:

- The AMR successfully performed online mapping, localization, and autonomous navigation in structured environments.

- Demonstrated obstacle avoidance and recovery behaviors in both simulation and hardware tests.

- Performance depended heavily on sensor accuracy and tuned parameters for costmaps and planners.

- Future improvements could include multi-robot exploration, improved sensor fusion, and integration of learning-based planners for more dynamic environments.

### Simulation

<img width="769" height="846" alt="image" src="https://github.com/user-attachments/assets/8f917c03-5f9b-4f3e-a894-56e8b5c9e039" />

[simulation_video.webm](https://github.com/user-attachments/assets/b1c2e12c-e722-4c7b-94d0-ccb61e67912d)

### Real-time

<img width="689" height="834" alt="image" src="https://github.com/user-attachments/assets/131775ec-677f-499b-941b-836db6296151" />

## Contributors:

Sairam Sridharan
Sevya Jai Aniss J
Shandhoosh V

## Credits:

This project integrates several existing ROS 2 packages alongside our own code:

- ```serial_motor_demo``` → Demonstration package for serial motor control (sourced from the ROS 2 community).

- ```joy_tester``` → Utility package for joystick teleoperation and testing.

- ```sllidar_ros2``` → Official ROS 2 driver for Slamtec RPLIDAR sensors.

These were included in the workspace for convenience, and all rights remain with their original authors.
Our main contribution is the custom ```my_bot``` package, which defines the robot description, launch files, and navigation configurations, and integrates the above packages into a working AMR system.
